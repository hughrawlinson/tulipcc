# world_matrix.py

import os
import ubinascii as ub
import urequests
import json
import time 
import tulip
import world

# TODO: i should verify Tulip-ness some other way . I can revoke this token easily enough but why not do it per user?
world_token = "syt_dHVsaXA_lPADiXCwKdCJvreALSul_0ody9J"
host = "duraflame.rosaline.org"
room_id = "!rGPkdYQOECXDlTVoGe:%s" % (host)
files_room_id = "!MuceoboBAfueEttdFw:%s" % (host)
firmware_room_id = "!eMmMZLncsdKrMOFTMM:%s" % (host)
last_message = None

# micropython version of uuid from micropython-lib
class UUID:
    def __init__(self, bytes):
        if len(bytes) != 16:
            raise ValueError('bytes arg must be 16 bytes long')
        self._bytes = bytes

    @property
    def hex(self):
        return ub.hexlify(self._bytes).decode()

    def __str__(self):
        h = self.hex
        return '-'.join((h[0:8], h[8:12], h[12:16], h[16:20], h[20:32]))

    def __repr__(self):
        return "<UUID: %s>" % str(self)

def uuid4():
    """Generates a random UUID compliant to RFC 4122 pg.14"""
    random = bytearray(os.urandom(16))
    random[6] = (random[6] & 0x0F) | 0x40
    random[8] = (random[8] & 0x3F) | 0x80
    return UUID(bytes=random)



# PUT call to matrix CS api using auth
def matrix_put(url, data):
    return urequests.put(url, data=bytes(json.dumps(data).encode('utf-8')), headers={"Authorization":"Bearer %s" %(world_token)})

# GET call to matrix CS api using auth
def matrix_get(url):
    return urequests.get(url, headers={"Authorization":"Bearer %s" %(world_token)})

def matrix_post(url, data, content_type="application/octet-stream"):
    return urequests.post(url, data=data, headers={"Authorization":"Bearer %s" %(world_token), "Content-Type":content_type})



# Uploads a file or folder from Tulip to Tulip World
def upload(filename, content_type="application/octet-stream", room_id=files_room_id):
    tar = False
    url = "https://%s/_matrix/media/v3/upload?filename=%s" % (host, filename)

    if(world._isdir(filename)):
        tar = True
        print("Packing %s" % (filename))
        tulip.tar_create(filename)
        filename += ".tar"

    file = open(filename, "rb")
    uri = matrix_post(url, read_in_chunks(file), content_type=content_type).json()["content_uri"]

    # Now make an event / message
    data={"info":{"mimetype":content_type},"msgtype":"m.file","body":filename,"url":uri}
    url="https://%s/_matrix/client/v3/rooms/%s/send/%s/%s" % (host, room_id, "m.room.message", str(uuid4()))
    matrix_put(url, data)
    print("Uploaded %s to Tulip World." % (filename))
    if(tar):
        os.remove(filename)

# returns all the files within limit
def files(limit=5000, room_id=files_room_id): 
    f = []
    url = "https://%s/_matrix/client/r0/rooms/%s/initialSync?limit=%d" % (host,room_id,limit)
    data = matrix_get(url)
    grab_url = None
    for e in data.json()['messages']['chunk']:
        if(e['type']=='m.room.message'):
            if('url' in e['content']):
                f.append({'url':e["content"]["url"], 'age_ms':e['age'], 'filename':e['content']['body']})
    return f

def ls(count=10): # lists latest count files
    already = {}
    i = 0
    all_files = files()
    all_files.reverse()
    for f in all_files:
        fn = f["filename"]
        if(not fn in already):
            already[fn] = True
            if(fn.endswith(".tar")):
                fn = "< %s >" % (fn[:-4])
            print("\t% 40s %s" % (fn, world.nice_time(f["age_ms"]/1000)))
            i+=1
        if(i==count): break 


# Convenience function that just grabs the __last__ file named filename from Tulip World. Does full initial sync to find it
# Or, you can give it an item from files(), if you want a specific file and not look it up by filename
def download(filename, limit=5000, chunk_size=4096):
    grab_url = None
    if(type(filename)==dict): # this is a item in the files() list
        grab_url = filename["url"]
        age_nice = world.nice_time(filename["age_ms"]/1000)
        filename = filename["filename"]
    else: # was a filename search 
        # Check for an extension
        if('.' not in filename[-5:]):
            filename = filename + ".tar"
        for file in files(limit=limit):
            if(file["filename"] == filename):
                age_nice = world.nice_time(file["age_ms"]/1000)
                grab_url = file["url"] # Will get the latest (most recent) file with that name

    if(grab_url is not None):
        mxc_id = grab_url[6:]
        url = "https://%s/_matrix/media/r0/download/%s" % (host, mxc_id)

        #tulip.display_stop()
        r = matrix_get(url)
        b = r.save(filename, chunk_size=chunk_size)
        #tulip.display_start()

        print("Downloaded %s [%d bytes, last updated %s] from Tulip World." % (filename, b, age_nice.lstrip()))
        if(filename.endswith('.tar')):
            print("Unpacking %s. Run it with run('%s')" % (filename, filename[:-4]))
            tulip.tar_extract(filename, show_progress=False)
            os.remove(filename)

    else:
        print("Could not find %s on Tulip World" % (filename))



def downloadall():
    already = {}
    i = 0
    all_files = files()
    all_files.reverse()
    for f in all_files:
        fn = f["filename"]
        if(not fn in already):
            already[fn] = True
            if(fn.endswith(".tar")):
                fn = fn[:-4]
            print(fn)
            download(fn)
            print("\t% 40s %s" % (fn, world.nice_time(f["age_ms"]/1000)))
            
# Send a m.room.message to the tulip room
def send(message):
    data={"msgtype":"m.text","body":message}
    url="https://%s/_matrix/client/v3/rooms/%s/send/%s/%s" % (host, room_id, "m.room.message", str(uuid4()))
    matrix_put(url, data)

# Return new messages since the last check
def check(limit=1000):
    global last_message
    if(last_message is None):
        url = "https://%s/_matrix/client/r0/rooms/%s/initialSync?limit=%d" % (host,room_id,limit)
    else:
        url = "https://%s/_matrix/client/r0/rooms/%s/messages?from=%s&dir=f&limit=%d" % (host, room_id, last_message, limit)
    data = matrix_get(url)
    m = []
    if 'messages' in data.json():
        last_message = data.json()['messages']['end']
        for e in data.json()['messages']['chunk']:
            if(e['type']=='m.room.message'):
                if('body' in e['content']):
                    m.append({"body":e['content']['body'], "age_s":int(e['age']/1000)})
    return m


