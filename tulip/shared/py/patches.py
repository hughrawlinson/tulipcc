# patches.py
# maybe one day automated list of patches in AMY

# Drumkit is [base_midi_note, name]
drumkit = [ 
    (89, "Maraca"),
    (39, "Kick"),
    (45, "Snare"),
    (52, "Snare2"),
    (51, "Snare3"),
    (41, "Snare4"),
    (53, "Closed Hat"),
    (56, "Open Hat"),
    (61, "Low Tom"),
    (94, "Clap"),
    (69, "Cowbell"),
    (74, "Congo Low"),
    (82, "Clave"),
    (60, "Block"),
    (60, "Roll"),
    (60, "Hit"),
    (60, "Crash"),
    (60, "Shell"),
    (60, "Chimes"),
    (60, "Seashore"),
    (60, "Pwr Snare"),
    (60, "Hi Tom"),
    (66, "Shamisen"),
    (66, "Koto"),
    (72, "Steel"),
    (60, "Pwr Kick"),
    (66, "Marimba"),
    (60, "Frets"),
    (60, "Std Kick")
    ]

patches =  [
"A11 Brass Set 1",
"A12 Brass Swell",
"A13 Trumpet",
"A14 Flutes",
"A15 Moving Strings",
"A16 Brass & Strings",
"A17 Choir",
"A18 Piano I",
"A21 Organ I",
"A22 Organ II",
"A23 Combo Organ",
"A24 Calliope",
"A25 Donald Pluck",
"A26 Celeste* (1 oct.up)",
"A27 Elect. Piano I",
"A28 Elect. Piano II",
"A31 Clock Chimes* (1 oct. up)",
"A32 Steel Drums",
"A33 Xylophone",
"A34 Brass III",
"A35 Fanfare",
"A36 String III ",
"A37 Pizzicato",
"A38 High Strings ",
"A41 Bass clarinet",
"A42 English Horn",
"A43 Brass Ensemble",
"A44 Guitar",
"A45 Koto",
"A46 Dark Pluck",
"A47 Funky I",
"A48 Synth Bass I (unison)",
"A51 Lead I",
"A52 Lead II",
"A53 Lead III ",
"A54 Funky II",
"A55 Synth Bass II",
"A56 Funky III",
"A57 Thud Wah",
"A58 Going Up",
"A61 Piano II",
"A62 Clav",
"A63 Frontier Organ ",
"A64 Snare Drum (unison)",
"A65 Tom Toms (unison)",
"A66 Timpani (unison)",
"A67 Shaker",
"A68 Synth Pad ",
"A71 Sweep I",
"A72 Pluck Sweep",
"A73 Repeater ",
"A74 Sweep II ",
"A75 Pluck Bell",
"A76 Dark Synth Piano",
"A77 Sustainer",
"A78 Wah Release",
"A81 Gong (play low chords)",
"A82 Resonance Funk",
"A83 Drum Booms* (1 oct. down)",
"A84 Dust Storm",
"A85 Rocket Men ",
"A86 Hand Claps",
"A87 FX Sweep",
"A88 Caverns ",
"B11 Strings ",
"B12 Violin ",
"B13 Chorus Vibes ",
"B14 Organ 1 ",
"B15 Harpsichord 1 ",
"B16 Recorder",
"B17 Perc. Pluck",
"B18 Noise Sweep",
"B21 Space Chimes ",
"B22 Nylon Guitar ",
"B23 Orchestral Pad ",
"B24 Bright Pluck ",
"B25 Organ Bell",
"B26 Accordion ",
"B27 FX Rise 1 ",
"B28 FX Rise 2",
"B31 Brass ",
"B32 Helicopter",
"B33 Lute ",
"B34 Chorus Funk ",
"B35 Tomita ",
"B36 FX Sweep 1",
"B37 Sharp Reed",
"B38 Bass Pluck",
"B41 Resonant Rise",
"B42 Harpsichord 2",
"B43 Dark Ensemble",
"B44 Contact Wah ",
"B45 Noise Sweep 2 ",
"B46 Glassy Wah",
"B47 Phase Ensemble",
"B48 Chorused Bell",
"B51 Clav",
"B52 Organ 2 ",
"B53 Bassoon ",
"B54 Auto Release Noise Sweep ",
"B55 Brass Ensemble ",
"B56 Ethereal",
"B57 Chorus Bell 2",
"B58 Blizzard ",
"B61 E. Piano with Tremolo",
"B62 Clarinet",
"B63 Thunder",
"B64 Reedy Organ",
"B65 Flute / Horn ",
"B66 Toy Rhodes",
"B67 Surf's Up",
"B68 OW Bass",
"B71 Piccolo",
"B72 Melodic Taps",
"B73 Meow Brass",
"B74 Violin (high)",
"B75 High Bells",
"B76 Rolling Wah ",
"B77 Ping Bell",
"B78 Brassy Organ",
"B81 Low Dark Strings",
"B82 Piccolo Trumpet",
"B83 Cello",
"B84 High Strings",
"B85 Rocket Men",
"B86 Forbidden Planet",
"B87 Froggy ",
"B88 Owgan",
"BRASS   1 ", 
"BRASS   2 ", 
"BRASS   3 ", 
"STRINGS 1 ", 
"STRINGS 2 ", 
"STRINGS 3 ", 
"ORCHESTRA ", 
"PIANO   1 ", 
"PIANO   2 ", 
"PIANO   3 ", 
"E.PIANO 1 ", 
"GUITAR  1 ", 
"GUITAR  2 ", 
"SYN-LEAD 1", 
"BASS    1 ", 
"BASS    2 ", 
"E.ORGAN 1 ", 
"PIPES   1 ", 
"HARPSICH 1", 
"CLAV    1 ", 
"VIBE    1 ", 
"MARIMBA   ", 
"KOTO      ", 
"FLUTE   1 ", 
"ORCH-CHIME", 
"TUB BELLS ", 
"STEEL DRUM", 
"TIMPANI   ", 
"REFS WHISL", 
"VOICE   1 ", 
"TRAIN     ", 
"TAKE OFF  ", 
"PIANO   4 ", 
"PIANO   5 ", 
"E.PIANO 2 ", 
"E.PIANO 3 ", 
"E.PIANO 4 ", 
"PIANO 5THS", 
"CELESTE   ", 
"TOY PIANO ", 
"HARPSICH 2", 
"HARPSICH 3", 
"CLAV    2 ", 
"CLAV    3 ", 
"E.ORGAN 2 ", 
"E.ORGAN 3 ", 
"E.ORGAN 4 ", 
"E.ORGAN 5 ", 
"PIPES   2 ", 
"PIPES   3 ", 
"PIPES   4 ", 
"CALIOPE   ", 
"ACCORDION ", 
"SITAR     ", 
"GUITAR  3 ", 
"GUITAR  4 ", 
"GUITAR  5 ", 
"GUITAR  6 ", 
"LUTE      ", 
"BANJO     ", 
"HARP    1 ", 
"HARP    2 ", 
"BASS    3 ", 
"BASS    4 ", 
"PICCOLO   ", 
"FLUTE   2 ", 
"OBOE      ", 
"CLARINET  ", 
"SAX BC    ", 
"BASSOON   ", 
"STRINGS 4 ", 
"STRINGS 5 ", 
"STRINGS 6 ", 
"STRINGS 7 ", 
"STRINGS 8 ", 
"BRASS   4 ", 
"BRASS   5 ", 
"BRASS 6 BC", 
"BRASS   7 ", 
"BRASS   8 ", 
"RECORDER  ", 
"HARMONICA1", 
"HRMNCA2 BC", 
"VOICE   2 ", 
"VOICE   3 ", 
"GLOKENSPL ", 
"VIBE    2 ", 
"XYLOPHONE ", 
"CHIMES    ", 
"GONG    1 ", 
"GONG    2 ", 
"BELLS     ", 
"COW BELL  ", 
"BLOCK     ", 
"FLEXATONE ", 
"LOG DRUM  ", 
"SYN-LEAD 2", 
"SYN-LEAD 3", 
"SYN-LEAD 4", 
"SYN-LEAD 5", 
"SYN-CLAV 1", 
"SYN-CLAV 2", 
"SYN-CLAV 3", 
"SYN-PIANO ", 
"SYNBRASS 1", 
"SYNBRASS 2", 
"SYNORGAN 1", 
"SYNORGAN 2", 
"SYN-VOX   ", 
"SYN-ORCH  ", 
"SYN-BASS 1", 
"SYN-BASS 2", 
"HARP-FLUTE", 
"BELL-FLUTE", 
"E.P-BRS BC", 
"T.BL-EXPA ", 
"CHIME-STRG", 
"B.DRM-SNAR", 
"SHIMMER   ", 
"EVOLUTION ", 
"WATER GDN ", 
"WASP STING", 
"LASER GUN ", 
"DESCENT   ", 
"OCTAVE WAR", 
"GRAND PRIX", 
"ST.HELENS ", 
"EXPLOSION "


]