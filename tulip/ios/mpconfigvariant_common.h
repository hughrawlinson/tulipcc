/*
 * This file is part of the MicroPython project, http://micropython.org/
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2022 Jim Mussared
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

// This file enables and configures features common to all variants
// other than "minimal".

// Send raise KeyboardInterrupt directly from the signal handler rather than
// scheduling it into the VM.
#define MICROPY_ASYNC_KBD_INTR         (1)

// Enable helpers for printing debugging information.
#ifndef MICROPY_DEBUG_PRINTERS
#define MICROPY_DEBUG_PRINTERS         (1)
#endif

// Enable floating point by default.
#ifndef MICROPY_FLOAT_IMPL
#define MICROPY_FLOAT_IMPL             (MICROPY_FLOAT_IMPL_DOUBLE)
#endif

// Enable arbitrary precision long-int by default.
#ifndef MICROPY_LONGINT_IMPL
#define MICROPY_LONGINT_IMPL           (MICROPY_LONGINT_IMPL_MPZ)
#endif

// Enable use of C libraries that need read/write/lseek/fsync, e.g. axtls.
#define MICROPY_STREAMS_POSIX_API      (1)

// REPL conveniences.
#define MICROPY_REPL_EMACS_WORDS_MOVE  (1)
#define MICROPY_REPL_EMACS_EXTRA_WORDS_MOVE (1)
#define MICROPY_USE_READLINE_HISTORY   (1)
#ifndef MICROPY_READLINE_HISTORY_SIZE
#define MICROPY_READLINE_HISTORY_SIZE  (50)
#endif

// Seed random on import.
#define MICROPY_PY_RANDOM_SEED_INIT_FUNC (mp_random_seed_init())

// Allow exception details in low-memory conditions.
#define MICROPY_ENABLE_EMERGENCY_EXCEPTION_BUF (1)
#define MICROPY_EMERGENCY_EXCEPTION_BUF_SIZE (256)

// Allow loading of .mpy files.
#define MICROPY_PERSISTENT_CODE_LOAD   (1)

// Extra memory debugging.
#define MICROPY_MALLOC_USES_ALLOCATED_SIZE (0)
#define MICROPY_MEM_STATS              (0)

// Enable a small performance boost for the VM.
#define MICROPY_OPT_COMPUTED_GOTO      (1)

// Return number of collected objects from gc.collect().
#define MICROPY_PY_GC_COLLECT_RETVAL   (1)

// Enable detailed error messages and warnings.
#define MICROPY_ERROR_REPORTING     (MICROPY_ERROR_REPORTING_DETAILED)
#define MICROPY_WARNINGS               (1)
#define MICROPY_PY_STR_BYTES_CMP_WARN  (1)

// Configure the "sys" module with features not usually enabled on bare-metal.
#define MICROPY_PY_SYS_ATEXIT          (1)
#define MICROPY_PY_SYS_EXC_INFO        (1)

// Configure the "os" module with extra unix features.
#define MICROPY_PY_OS_INCLUDEFILE      "../tulip/ios/modos.c"
#define MICROPY_PY_OS_ERRNO            (1)
#define MICROPY_PY_OS_GETENV_PUTENV_UNSETENV (0)
#define MICROPY_PY_OS_SEP              (1)
#define MICROPY_PY_OS_SYSTEM           (0)
#define MICROPY_PY_OS_URANDOM          (1)

// Enable the unix-specific "time" module.
#define MICROPY_PY_TIME                (1)
#define MICROPY_PY_TIME_TIME_TIME_NS   (1)
#define MICROPY_PY_TIME_CUSTOM_SLEEP   (1)
#define MICROPY_PY_TIME_INCLUDEFILE    "ports/unix/modtime.c"

#if MICROPY_PY_SSL
#define MICROPY_PY_HASHLIB_MD5         (1)
#define MICROPY_PY_HASHLIB_SHA1        (1)
#define MICROPY_PY_CRYPTOLIB           (1)
#endif

// Use the posix implementation of the "select" module (unless the variant
// specifically asks for the MicroPython version).
#ifndef MICROPY_PY_SELECT
#define MICROPY_PY_SELECT              (0)
#endif
#ifndef MICROPY_PY_SELECT_POSIX
#define MICROPY_PY_SELECT_POSIX        (!MICROPY_PY_SELECT)
#endif

// Enable the "websocket" module.
#define MICROPY_PY_WEBSOCKET           (1)

// Enable the "machine" module, mostly for machine.mem*.
#define MICROPY_PY_MACHINE             (1)
#define MICROPY_PY_MACHINE_PULSE       (1)
