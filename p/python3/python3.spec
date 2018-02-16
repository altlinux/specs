# ======================================================
# Conditionals and other variables controlling the build
# ======================================================

# Below the same shorthands as in Redhat's spec are definied,
# but mostly through ALT Sisyphus rpm-build-python3's macros
# (to make the picture more clear and less error-prone).

%global pybasever 3.5

%global with_rewheel 0

# pybasever without the dot:
%global pyshortver 35

%global pyabi m

%global pynameabi python%pybasever%pyabi

# Here, we re-use the machinery of rpm-build-python3 definitions
# to generate the paths etc. in the way they are usually determined
# for the build system. (The input to this machinery is:
# %%__python3_version and %%__python3_abiflags;

%global __python3_version %pybasever
# the above also affects %%_python3_abi_version the way we need indeed.
%global __python3_abiflags %pyabi
# the above also affects %%_python3_abiflags

# they normally refer to Python3 installed in the build system,
# but we are building a new one, and not going to use the old one).

%global pylibdir %__python3_libdir
%global dynload_dir %__python3_dynlibdir
%global include_dir %__python3_includedir
%global tool_dir %__python3_tooldir
%global pylibdir_noarch %__python3_libdir_noarch

# All bytecode files are now in a __pycache__ subdirectory, with a name
# reflecting the version of the bytecode (to permit sharing of python libraries
# between different runtimes)
# See http://www.python.org/dev/peps/pep-3147/
# For example,
#   foo/bar.py
# now has bytecode at:
#   foo/__pycache__/bar.cpython-35.pyc
#   foo/__pycache__/bar.cpython-35.pyo
%global bytecode_suffixes .cpython-%{pyshortver}*.py?

# Python's configure script defines SOVERSION, and this is used in the Makefile
# to determine INSTSONAME, the name of the libpython DSO:
#   LDLIBRARY='libpython$(VERSION).so'
#   INSTSONAME="$LDLIBRARY".$SOVERSION
# We mirror this here in order to make it easier to add the -gdb.py hooks.
# (if these get out of sync, the payload of the libs subpackage will fail
# and halt the build)
%global py_SOVERSION 1.0

# some arches don't have valgrind so we need to disable its support on them
%ifnarch s390
%global with_valgrind 1
%else
%global with_valgrind 0
%endif

%global with_gdbm 1

# Change from yes to no to turn this off
%global with_computed_gotos yes

%global _optlevel 3

%def_disable test_posix_fadvise

Summary: Version 3 of the Python programming language aka Python 3000
Name: python3
Version: %{pybasever}.4
Release: alt3
License: Python
Group: Development/Python3

# New common location for site-packages is supported since 0.1.9.
# %%python3_ABI_dep is defined since 0.1.9.1.
# The path macros brought in sync in 0.1.9.2.
# %%__libpython3 macro is defined and used for the verify_elf trick
# since 0.1.9.3.
BuildRequires(pre): rpm-build-python3 >= 0.1.9.3
BuildPreReq: liblzma-devel
# For Bluetooth support
# see https://bugzilla.redhat.com/show_bug.cgi?id=879720
BuildPreReq: libbluez-devel
BuildRequires: bzip2-devel db4-devel libexpat-devel gcc-c++ libgmp-devel libffi-devel libGL-devel libX11-devel libncursesw-devel libssl-devel libreadline-devel libsqlite3-devel tcl-devel tk-devel zlib-devel

%if %with_gdbm
BuildRequires: gdbm-devel
%endif

%if 0%{?with_valgrind}
BuildRequires: valgrind-devel
%endif

%if 0%{?with_rewheel}
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pip
%endif

%{?!_without_check:%{?!_disable_check:BuildRequires: /dev/pts}}

# Fix find-requires
%global __python3 %buildroot%_bindir/python3
%add_python3_path %pylibdir
#Do not recompile .py files with old python3
%add_python3_compile_exclude %pylibdir
# Help verify_elf:
%global __libpython3 %buildroot%__libpython3

Source: %name-%version.tar

#RH Patches

# Fixup distutils/unixccompiler.py to remove standard library path from rpath:
# Was Patch0 in ivazquez' python3000 specfile:
Patch1:         Python-3.1.1-rpath.patch

# 00055 #
# Systemtap support: add statically-defined probe points
# Patch sent upstream as http://bugs.python.org/issue14776
# with some subsequent reworking to cope with LANG=C in an rpmbuild
# (where sys.getfilesystemencoding() == 'ascii')
Patch55: 00055-systemtap.patch

# The lib64 patch
# on top of ALT's python3-site-packages.patch (Patch1005)
Patch102: python3-site-packages-lib64.patch

# 00104 #
# Only used when "%_lib" == "lib64"
# Another lib64 fix, for distutils/tests/test_install.py; not upstream:
Patch104: 00104-lib64-fix-for-test_install.patch

# 00131 #
# The four tests in test_io built on top of check_interrupted_write_retry
# fail when built in Koji, for ppc and ppc64; for some reason, the SIGALRM
# handlers are never called, and the call to write runs to completion
# (rhbz#732998)
Patch131: 00131-disable-tests-in-test_io.patch

# 00132 #
# Add non-standard hooks to unittest for use in the "check" phase below, when
# running selftests within the build:
#   @unittest._skipInRpmBuild(reason)
# for tests that hang or fail intermittently within the build environment, and:
#   @unittest._expectedFailureInRpmBuild
# for tests that always fail within the build environment
#
# The hooks only take effect if WITHIN_PYTHON_RPM_BUILD is set in the
# environment, which we set manually in the appropriate portion of the "check"
# phase below (and which potentially other python-* rpms could set, to reuse
# these unittest hooks in their own "check" phases)
Patch132: 00132-add-rpmbuild-hooks-to-unittest.patch


# 00137 #
# Some tests within distutils fail when run in an rpmbuild:
Patch137: 00137-skip-distutils-tests-that-fail-in-rpmbuild.patch

# 00139 #
# ARM-specific: skip known failure in test_float:
#  http://bugs.python.org/issue8265 (rhbz#706253)
Patch139: 00139-skip-test_float-known-failure-on-arm.patch

# ideally short lived patch disabling a test thats fragile on different arches
Patch140: python3-arm-skip-failing-fragile-test.patch

# 00143 #
# Fix the --with-tsc option on ppc64, and rework it on 32-bit ppc to avoid
# aliasing violations (rhbz#698726)
# Sent upstream as http://bugs.python.org/issue12872
Patch143: 00143-tsc-on-ppc.patch

# 00146 #
# Support OpenSSL FIPS mode (e.g. when OPENSSL_FORCE_FIPS_MODE=1 is set)
# - handle failures from OpenSSL (e.g. on attempts to use MD5 in a
#   FIPS-enforcing environment)
# - add a new "usedforsecurity" keyword argument to the various digest
#   algorithms in hashlib so that you can whitelist a callsite with
#   "usedforsecurity=False"
# (sent upstream for python 3 as http://bugs.python.org/issue9216 ; see RHEL6
# python patch 119)
# - enforce usage of the _hashlib implementation: don't fall back to the _md5
#   and _sha* modules (leading to clearer error messages if fips selftests
#   fail)
# - don't build the _md5 and _sha* modules; rely on the _hashlib implementation
#   of hashlib
# (rhbz#563986)
# Note: Up to Python 3.4.0.b1, upstream had their own implementation of what
# they assumed would become sha3. This patch was adapted to give it the
# usedforsecurity argument, even though it did nothing (OpenSSL didn't have
# sha3 implementation at that time).In 3.4.0.b2, sha3 implementation was reverted
# (see http://bugs.python.org/issue16113), but the alterations were left in the
# patch, since they may be useful again if upstream decides to rerevert sha3
# implementation and OpenSSL still doesn't support it. For now, they're harmless.
Patch146: 00146-hashlib-fips.patch

# 00150 #
# temporarily disable rAssertAlmostEqual in test_cmath on PPC (bz #750811)
# caused by a glibc bug. This patch can be removed when we have a glibc with
# the patch mentioned here:
#   http://sourceware.org/bugzilla/show_bug.cgi?id=13472
Patch150: 00150-disable-rAssertAlmostEqual-cmath-on-ppc.patch

# 00155 #
# Avoid allocating thunks in ctypes unless absolutely necessary, to avoid
# generating SELinux denials on "import ctypes" and "import uuid" when
# embedding Python within httpd (rhbz#814391)
Patch155: 00155-avoid-ctypes-thunks.patch

# 00157 #
# Update uid/gid handling throughout the standard library: uid_t and gid_t are
# unsigned 32-bit values, but existing code often passed them through C long
# values, which are signed 32-bit values on 32-bit architectures, leading to
# negative int objects for uid/gid values >= 2^31 on 32-bit architectures.
#
# Introduce _PyObject_FromUid/Gid to convert uid_t/gid_t values to python
# objects, using int objects where the value will fit (long objects otherwise),
# and _PyArg_ParseUid/Gid to convert int/long to uid_t/gid_t, with -1 allowed
# as a special case (since this is given special meaning by the chown syscall)
#
# Update standard library to use this throughout for uid/gid values, so that
# very large uid/gid values are round-trippable, and -1 remains usable.
# (rhbz#697470)
Patch157: 00157-uid-gid-overflows.patch

# 00160 #
# Python 3.3 added os.SEEK_DATA and os.SEEK_HOLE, which may be present in the
# header files in the build chroot, but may not be supported in the running
# kernel, hence we disable this test in an rpm build.
# Adding these was upstream issue http://bugs.python.org/issue10142
# Not yet sent upstream
Patch160: 00160-disable-test_fs_holes-in-rpm-build.patch

# 00163 #
# Some tests within test_socket fail intermittently when run inside Koji;
# disable them using unittest._skipInRpmBuild
# Not yet sent upstream
Patch163: 00163-disable-parts-of-test_socket-in-rpm-build.patch


# 00170 #                                                                                           
# In debug builds, try to print repr() when a C-level assert fails in the                           
# garbage collector (typically indicating a reference-counting error                                
# somewhere else e.g in an extension module)                                                        
# Backported to 2.7 from a patch I sent upstream for py3k                                           
#   http://bugs.python.org/issue9263  (rhbz#614680)                                                 
# hiding the proposed new macros/functions within gcmodule.c to avoid exposing                      
# them within the extension API.                                                                    
# (rhbz#850013
Patch170: 00170-gc-assertions.patch


# 00178 #
# Don't duplicate various FLAGS in sysconfig values
# http://bugs.python.org/issue17679
# Does not affect python2 AFAICS (different sysconfig values initialization)
Patch178: 00178-dont-duplicate-flags-in-sysconfig.patch

# 00179 #
# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=951802
# Reported upstream in http://bugs.python.org/issue17737
# This patch basically looks at every frame and if it is somehow corrupted,
# it just stops printing the traceback - it doesn't fix the actual bug.
# This bug seems to only affect ARM.
# Doesn't seem to affect Python 2 AFAICS.
Patch179: 00179-dont-raise-error-on-gdb-corrupted-frames-in-backtrace.patch

# 00180 #
# Enable building on ppc64p7
# Not appropriate for upstream, Fedora-specific naming
Patch180: 00180-python-add-support-for-ppc64p7.patch

# 00184 #
# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=979696
# Fixes build of ctypes against libffi with multilib wrapper
# Python recognizes ffi.h only if it contains "#define LIBFFI_H",
# but the wrapper doesn't contain that, which makes the build fail
# We patch this by also accepting "#define ffi_wrapper_h"
Patch184: 00184-ctypes-should-build-with-libffi-multilib-wrapper.patch

# 00186 #
# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=1023607
# Previously, this fixed a problem where some *.py files were not being
# bytecompiled properly during build. This was result of py_compile.compile
# raising exception when trying to convert test file with bad encoding, and
# thus not continuing bytecompilation for other files.
# This was fixed upstream, but the test hasn't been merged yet, so we keep it
Patch186: 00186-dont-raise-from-py_compile.patch

# 00188 #
# Downstream only patch that should be removed when we compile all guaranteed
# hashlib algorithms properly. The problem is this:
# - during tests, test_hashlib is imported and executed before test_lib2to3
# - if at least one hash function has failed, trying to import it triggers an
#   exception that is being caught and exception is logged:
#   http://hg.python.org/cpython/file/2de806c8b070/Lib/hashlib.py#l217
# - logging the exception makes logging module run basicConfig
# - when lib2to3 tests are run again, lib2to3 runs basicConfig again, which
#   doesn't do anything, because it was run previously
#   (logging.root.handlers != []), which means that the default setup
#   (most importantly logging level) is not overriden. That means that a test
#   relying on this will fail (test_filename_changing_on_output_single_dir)
Patch188: 00188-fix-lib2to3-tests-when-hashlib-doesnt-compile-properly.patch

# 00189 #
#
# Add the rewheel module, allowing to recreate wheels from already installed
# ones
# https://github.com/bkabrda/rewheel
%if 0%{with_rewheel}
Patch189: 00189-add-rewheel-module.patch
%endif

# Tests requiring SIGHUP to work don't work in Koji
# see rhbz#1088233
Patch194: temporarily-disable-tests-requiring-SIGHUP.patch

# 00196
#
#  Fix test_gdb failure on ppc64le
Patch196: 00196-test-gdb-match-addr-before-builtin.patch

# 00200 #                                                                                           
# Fix for gettext plural form headers (lines that begin with "#")                                   
# Note: Backported from scl
Patch200: 00200-gettext-plural-fix.patch

# 00201 #                                                                                           
# Fixes memory leak in gdbm module (rhbz#977308)                                                    
# This was upstreamed as a part of bigger patch, but for our purposes                               
# this is ok: http://bugs.python.org/issue18404                                                     
# Note: Backported from scl
Patch201: 00201-fix-memory-leak-in-gdbm.patch 

# test_threading fails in koji dues to it's handling of signals
Patch203: 00203-disable-threading-test-koji.patch

# LIBPL variable in makefile takes LIBPL from configure.ac
# but the LIBPL variable defined there doesn't respect libdir macro
Patch205: 00205-make-libpl-respect-lib64.patch

# Remove hf flag from arm triplet which is used
# by debian but fedora infra uses only eabi without hf
Patch206: 00206-remove-hf-from-arm-triplet.patch

# Avoid truncated _math.o files caused by parallel builds
# modified version of https://bugs.python.org/issue24421
# rhbz#1292461
Patch207: 00207-math-once.patch

# 00243 #
# Fix the triplet used on 64-bit MIPS
# rhbz#1322526: https://bugzilla.redhat.com/show_bug.cgi?id=1322526
# Upstream uses Debian-like style mips64-linux-gnuabi64
# Fedora needs the default mips64-linux-gnu
Patch243: 00243-fix-mips64-triplet.patch


# (New patches go here ^^^)
#
# When adding new patches to "python" and "python3" in Fedora 17 onwards,
# please try to keep the patch numbers in-sync between the two specfiles:
#
#   - use the same patch number across both specfiles for conceptually-equivalent
#     fixes, ideally with the same name
#
#   - when a patch is relevant to both specfiles, use the same introductory
#     comment in both specfiles where possible (to improve "diff" output when
#     comparing them)
#
#   - when a patch is only relevant for one of the two specfiles, leave a gap
#     in the patch numbering in the other specfile, adding a comment when
#     omitting a patch, both in the manifest section here, and in the "prep"
#     phase below
#
# Hopefully this will make it easier to ensure that all relevant fixes are
# applied to both versions.

#ALT Linux patches

# Under some kernels not working on tmpfs,
# see http://comments.gmane.org/gmane.linux.suse.kernel/3182
%if_enabled test_posix_fadvise
Patch1002: python-3.3.0-skip-test_posix_fadvise-alt.patch
%endif

# RLIMIT 1000000 unavailable in hasher
Patch1003: python-3.3.1-skip-test_setrusage_refcount-alt.patch

# Disable "-i386-linux-gnu"-like suffixes for lib-dynload/*.so modules.
# Disables test for those suffixes.
Patch1004: python-3.5.1-alt-disable-build-PLATFORM_TRIPLET.patch

# Use a common /usr/lib/python3/site-packages (without the minor version)
Patch1005: python3-site-packages.patch
# %%python3_sitelibdir{,_noarch} from rpm-build-python3 >= 0.1.9
# are consistent with this.
# (TODO: Perhaps, we should consider substituting the value of the macros into the patch,
# so that we have a single point of control and a guarantee of consistency.)

Patch1006: python-3.5.1-glibc-2.25-getentropy.patch

Patch1007: python-3.5.1-upstream-expat-compat.patch

# add correct arch for ppc64/ppc64le
# it should be ppc64le-linux-gnu/ppc64-linux-gnu instead powerpc64le-linux-gnu/powerpc64-linux-gnu
Patch5001: python3-powerppc-arch.patch

# Fix locale issues with new glibc.
# Based on: https://github.com/python/cpython/pull/4174
Patch5010: python-glibc-alt.patch

# ======================================================
# Additional metadata, and subpackages
# ======================================================

Url: http://www.python.org/

# Like in Fedora:
Provides: python(abi) = %pybasever

# ALT's special name (looking like: python3.3-ABI(64bit)):
#
# (BTW, %%ABI_suffix is computed in a new-arch-ABI-proof way:
# if a new weird arch-ABI arises, at least, we'll have
# a weird suffix here, not coinciding with another existing one.)
Provides: %python3_ABI_dep

Requires: %name-base = %EVR

%if 0%{with_rewheel}
Requires: python3-setuptools
Requires: python3-pip
%endif

# ALT Sisyphus RPM Macros Packaging Policy
# makes sure that the RPM support for building
# the language-specific modules comes together with
# the compiler/-devel pkgs:
Requires: rpm-build-python3 >= 0.1.9

%description
Python 3 is a new version of the language that is incompatible with the 2.x
line of releases. The language is mostly the same, but many details, especially
how built-in objects like dictionaries and strings work, have changed
considerably, and a lot of deprecated features have finally been removed.

%package base
Summary: Python 3 runtime libraries
Group: Development/Python3
Provides: %name-libs = %EVR
Obsoletes: %name-libs < %EVR
%py3_provides builtins
# Prepare for the future default method (to test the result earlier):
%python3_req_hier
# It's an OS-independent alias (which other modules might want to import)
# leading to an OS-specific path module.
%py3_provides os.path

# Things which have become internal in 3.5
# (we do not use %%py3_provides here, because the autoreqs generated
# with this new version of python3 must not include these ones;
# they are only needed to run non-recompiled modules):
Provides: python3.3(time)
Provides: python3.3(atexit)

%filter_from_requires /^%name[[:space:]]/d
%filter_from_requires /^\/usr\/bin\/%name/d

# The package that may have provided the common
# /usr/lib{,64}/python3/site-packages
# before we patched python3 itself for supporting this path.
%define python3_sitebasename %(basename %(dirname %python3_sitelibdir))
Obsoletes: %python3_sitebasename-site-packages

%description base
This package contains files used to embed Python 3 into applications.

%package dev
Summary: Libraries and header files needed for Python 3 development
Group: Development/Python3
Requires: %name = %EVR
Requires: lib%name = %EVR
Conflicts: %name < %EVR
Provides: %name-devel = %pybasever
Provides: lib%name-devel = %EVR

# ALT Sisyphus RPM Macros Packaging Policy
# makes sure that the RPM support for building
# the language-specific modules comes together with
# the compiler/-devel pkgs:
Requires: rpm-build-python3 >= 0.1.9

%description dev
This package contains libraries and header files used to build applications
with and native libraries for Python 3

%package -n libpython3
Summary: Python3 shared library
Group: Development/Python3
Requires: %name-base = %EVR

%description -n libpython3
This package contains Python3 shared library

%package tools
Summary: A collection of tools included with Python 3
Group: Development/Python3
Requires: %name = %EVR
Requires: %name-modules-tkinter = %EVR
Requires: %name-modules-curses = %EVR

%description tools
This package contains several tools included with Python 3

%package modules-tkinter
Summary: A GUI toolkit for Python 3
Group: Development/Python3
Provides: %name-modules-idlelib = %EVR
Obsoletes: %name-modules-idlelib < 3.3.1-alt4
Requires: tk

%description modules-tkinter
The Tkinter (Tk interface) program is an graphical user interface for
the Python scripting language.

%package modules-sqlite3
Summary: DB-API 2.0 interface for SQLite databases
Group: Development/Python3

%description modules-sqlite3
SQLite is a C library that provides a lightweight disk-based database
that doesn't require a separate server process and allows accessing
the database using a nonstandard variant of the SQL query language.
Some applications can use SQLite for internal data storage.  It's also
possible to prototype an application using SQLite and then port the
code to a larger database such as PostgreSQL or Oracle.

%package modules-curses
Summary: Python3 "curses" module
Group: Development/Python3

%description modules-curses
An interface to the curses library, providing portable terminal
handling. The Curses module provides an interface to the curses library, the
de-facto standard for portable advanced terminal handling.
This extension module is designed to match the API of ncurses, an
open-source curses library hosted on Linux and the BSD variants of UNIX.

%package test
Summary: The test modules from the main python 3 package
Group: Development/Python3
Requires: %name = %EVR
Requires: %name-modules-tkinter = %EVR
Requires: %name-modules-curses = %EVR
Requires: %name-modules-sqlite3 = %EVR
Requires: %name-tools = %EVR
%add_python3_req_skip test.test_warnings.data

%description test
The test modules from the main %name package.
These are in a separate package to save space, as they are almost never used
in production.

You might want to install the python3-test package if you're developing
python 3 code that uses more than just unittest and/or test_support.py.

%prep
%setup

# Ensure that we're using the system copy of various libraries, rather than
# copies shipped by upstream in the tarball:
#   Remove embedded copy of expat:
rm -r Modules/expat || exit 1

#   Remove embedded copy of libffi:
for SUBDIR in darwin libffi libffi_arm_wince libffi_msvc libffi_osx ; do
  rm -r Modules/_ctypes/$SUBDIR || exit 1 ;
done

#   Remove embedded copy of zlib:
rm -r Modules/zlib || exit 1

# Don't build upstream Python's implementation of these crypto algorithms;
# instead rely on _hashlib and OpenSSL.
#
# For example, in our builds hashlib.md5 is implemented within _hashlib via
# OpenSSL (and thus respects FIPS mode), and does not fall back to _md5
# TODO: there seems to be no OpenSSL support in Python for sha3 so far
# when it is there, also remove _sha3/ dir
for f in md5module.c sha1module.c sha256module.c sha512module.c; do
    rm Modules/$f
done

%if 0%{with_rewheel}
%global pip_version 7.1.0
sed -r -i s/'_PIP_VERSION = "[0-9.]+"'/'_PIP_VERSION = "%{pip_version}"'/ Lib/ensurepip/__init__.py
%endif

#
# Apply patches:
#
%patch1 -p1
%patch1005 -p1

%if "%_lib" != "lib"
< %PATCH102 sed -e 's:lib64:%_lib:g' | patch -p1
< %PATCH104 sed -e 's:lib64:%_lib:g' | patch -p1
%endif
%ifarch ppc ppc64
%patch131 -p1
%endif
%patch132 -p1
%patch137 -p1
%ifarch %{arm}
%patch139 -p1
%patch140 -p1
%endif
%patch143 -p1 -b .tsc-on-ppc
%patch146 -p1
%ifarch ppc ppc64
%patch150 -p1
%endif
%patch155 -p1
%patch157 -p1
%patch160 -p1
%patch163 -p1
%patch178 -p1
%patch179 -p1
%patch180 -p1
##patch184 -p1
%patch186 -p1
%patch188 -p1

%if 0%{with_rewheel}
%patch189 -p1
%endif

%patch194 -p1
%patch196 -p1
%patch203 -p1
%patch205 -p1
%patch206 -p1
##patch207 -p1
%patch243 -p1

# ALT Linux patches
%if_enabled test_posix_fadvise
%patch1002 -p2
%endif
%patch1003 -p2
%patch1004 -p1

##patch1006 -p1
##patch1007 -p1

# Currently (2010-01-15), http://docs.python.org/library is for 2.6, and there
# are many differences between 2.6 and the Python 3 library.
#
# Fix up the URLs within pydoc to point at the documentation for this
# MAJOR.MINOR version:
#
sed --in-place \
    --expression="s|http://docs.python.org/library|http://docs.python.org/%pybasever/library|g" \
    Lib/pydoc.py || exit 1

%patch5001 -p1
%patch5010 -p2

rm -fr ../build-shared
mkdir ../build-shared
%autoreconf
cp -rl * ../build-shared/

# ======================================================
# Configuring and building the code:
# ======================================================

%build
topdir=$(pwd)

build() {
%configure \
  --enable-ipv6 \
  --with-system-ffi \
  --enable-loadable-sqlite-extensions \
%if 0%{?with_systemtap}
  --with-systemtap \
%endif
%if 0%{?with_valgrind}
  --with-valgrind \
%endif
  --with-system-expat \
  --with-dbmliborder=gdbm:ndbm:bdb \
  --with-computed-gotos=%with_computed_gotos \
  --without-ensurepip \
  $*

%make_build CFLAGS=
}

pushd ../build-shared
build  --enable-shared
popd

build

# ======================================================
# Installing the built code:
# ======================================================

%install

pushd ../build-shared
make install DESTDIR=%buildroot INSTALL="install -p"
popd

find build -exec touch {} \;
make install DESTDIR=%buildroot INSTALL="install -p"

mv $RPM_BUILD_ROOT%_bindir/2to3 $RPM_BUILD_ROOT%_bindir/python3-2to3

# Development tools
install -m755 -d $RPM_BUILD_ROOT%tool_dir
install Tools/README $RPM_BUILD_ROOT%tool_dir/
cp -ar Tools/freeze $RPM_BUILD_ROOT%tool_dir/
cp -ar Tools/i18n $RPM_BUILD_ROOT%tool_dir/
cp -ar Tools/pynche $RPM_BUILD_ROOT%tool_dir/
cp -ar Tools/scripts $RPM_BUILD_ROOT%tool_dir/

# Documentation tools
install -m755 -d %buildroot%pylibdir/Doc
cp -ar Doc/tools %buildroot%pylibdir/Doc/

# Demo scripts
cp -ar Tools/demo %buildroot%tool_dir/

install -d -m 0755 %buildroot%python3_sitelibdir/__pycache__
%if "%_lib" != "lib"
install -d -m 0755 %buildroot%python3_sitelibdir_noarch/__pycache__
%endif
# The install scripts put a README in the old-style %pylibdir/site-packages
# (actually, they copy the tree from the sources).
# So, we move it by force (like in rpm-build-python for other python3 packages,
# but in a more controlled way: we make sure that we know exactly what we copy,
# otherwise rmdir would fail):
mv -t %buildroot%python3_sitelibdir/ %buildroot%pylibdir/site-packages/README
rmdir %buildroot%pylibdir/site-packages

# Make python3-devel multilib-ready (bug #192747, #139911)
%global _pyconfig32_h pyconfig-32.h
%global _pyconfig64_h pyconfig-64.h

%ifarch aarch64 e2k ppc64 x86_64
%global _pyconfig_h %_pyconfig64_h
%else
%global _pyconfig_h %_pyconfig32_h
%endif

mv %buildroot%include_dir/pyconfig.h  %buildroot%include_dir/%_pyconfig_h
cat > %buildroot%include_dir/pyconfig.h << EOF
#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "%_pyconfig32_h"
#elif __WORDSIZE == 64
#include "%_pyconfig64_h"
#else
#error "Unknown word size"
#endif
EOF

# Fix for bug 201434: make sure distutils looks at the right pyconfig.h file
# Similar for sysconfig: sysconfig.get_config_h_filename tries to locate
# pyconfig.h so it can be parsed, and needs to do this at runtime in site.py
# when python starts up (bug 653058)
#
# Split this out so it goes directly to the pyconfig-32.h/pyconfig-64.h
# variants:
sed -i -e "s/'pyconfig.h'/'%_pyconfig_h'/" \
  %buildroot%pylibdir/distutils/sysconfig.py \
  %buildroot%pylibdir/sysconfig.py

## Switch all shebangs to refer to the specific Python version.
#LD_LIBRARY_PATH=./build/optimized ./build/optimized/python \
#  Tools/scripts/pathfix.py \
#  -i "%_bindir/python%pybasever" \
#  %buildroot

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
find %buildroot -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

# .xpm and .xbm files should not be executable:
find %buildroot \
  \( -name \*.xbm -o -name \*.xpm -o -name \*.xpm.1 \) \
  -exec chmod a-x {} \;

# Remove executable flag from files that shouldn't have it:
chmod a-x \
  %buildroot%pylibdir/distutils/tests/Setup.sample \
  %buildroot%tool_dir/README

# Get rid of DOS batch files:
find %buildroot -name \*.bat -exec rm {} \;

# Get rid of backup files:
find %buildroot/ -name "*~" -exec rm {} \;
find . -name "*~" -exec rm {} \;
rm %buildroot%pylibdir/LICENSE.txt

# Get rid of crappy code:
rm %buildroot%tool_dir/scripts/abitype.py
rm %buildroot%tool_dir/scripts/fixcid.py
rm %buildroot%pylibdir/encodings/{,__pycache__/}rot_13*.py*

# Skip the 2to3 test data (which might contain Python2 code)
%global lib2to3_tests %pylibdir/lib2to3/tests
%add_python3_compile_exclude %lib2to3_tests/data
%add_findreq_skiplist %lib2to3_tests/data/*
%add_findprov_skiplist %lib2to3_tests/data/*
# http://bugs.python.org/issue26911 :
# remove a seemingly unused source file with broken code (a broken import):
rm %buildroot%lib2to3_tests/{,__pycache__/}pytree_idempotency*.py*

# http://bugs.python.org/issue26912 :
# rm another seemingly unused source file with a broken import:
rm %buildroot%pylibdir/test/test_email/{,__pycache__/}torture_test*.py*

# Get rid of win tests
rm %buildroot%pylibdir/test/{,__pycache__/}test_winreg*.py*
rm %buildroot%pylibdir/test/{,__pycache__/}test_winsound*.py*
rm %buildroot%pylibdir/test/{,__pycache__/}win_console_handler*.py*
rm %buildroot%pylibdir/distutils/tests/{,__pycache__/}test_msvc{9,}compiler*.py*
rm %buildroot%pylibdir/test/test_importlib/{,__pycache__/}test_windows*.py*
# The libs which are being tested below have been excluded in %%files (long ago):
rm %buildroot%pylibdir/test/test_asyncio/{,__pycache__/}test_windows_events*.py*
rm %buildroot%pylibdir/test/test_asyncio/{,__pycache__/}test_windows_utils*.py*

# Get rid of bad* tests -- just skip them:
%add_findreq_skiplist %pylibdir/test/bad*.py
%add_findprov_skiplist %pylibdir/test/bad*.py

# Get rid of windows-related stuff
%add_findreq_skiplist %pylibdir/distutils/*msvc*compiler*.py*
%add_findprov_skiplist %pylibdir/distutils/*msvc*compiler*.py*
rm %buildroot%pylibdir/distutils/command/{,__pycache__/}bdist_msi*.py*
rm %buildroot%pylibdir/distutils/command/*.exe
rm %buildroot%tool_dir/scripts/win_add2path.py

# Get rid of crap
rm -r %buildroot%pylibdir/ctypes/macholib/fetch_macholib
rm %buildroot%tool_dir/scripts/md5sum.py
rm %buildroot%tool_dir/scripts/parseentities.py

# Remove sphinxext (temporary)
rm -r %buildroot%pylibdir/Doc/tools/{extensions,pydoctheme,static,templates}
rm %buildroot%pylibdir/Doc/tools/susp-ignored.csv

# Fix end-of-line encodings:
find %buildroot/ -name \*.py -exec sed -i 's/\r//' {} \;

# Note that
#  %pylibdir/Demo/distutils/test2to3/setup.py
# is in iso-8859-1 encoding, and that this is deliberate; this is test data
# for the 2to3 tool, and one of the functions of the 2to3 tool is to fixup
# character encodings within python source code


# Fixup permissions for shared libraries from non-standard 555 to standard 755:
find %buildroot \
    -perm 555 -exec chmod 755 {} \;

# Ensure that the curses module was linked against libncursesw.so, rather than
# libncurses.so (bug 539917)
ldd %buildroot/%dynload_dir/_curses*.so \
    | grep curses \
    | grep libncurses.so && { echo "_curses.so linked against libncurses.so" ; exit 1; }

export LD_LIBRARY_PATH=%buildroot%_libdir
find %buildroot -type f -a -name "*.py" -a -not -wholename "*/test/*" -a -not -wholename "*/tests/*" -a -not -wholename "*/scripts/*" -print0 | xargs -0 %buildroot%_bindir/%name -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%buildroot")[2]) for f in sys.argv[1:]]'
find %buildroot -type f -a -name "*.py" -a -not -wholename "*/test/*" -a -not -wholename "*/tests/*" -a -not -wholename "*/scripts/*" -print0 | xargs -0 %buildroot%_bindir/%name -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%buildroot")[2]) for f in sys.argv[1:]]'

sed -i 's,/usr/local/bin/python,/usr/bin/python3,' %buildroot%_libdir/python%pybasever/cgi.py

# Replace the shell implementation with the more correct .py one
# (BTW, the .py one used to be packaged in python3-3.3):
ln -sfv \
   "$(relative \
	%pylibdir/config-%pybasever%pyabi/python-config.py \
   	%_bindir/python%pybasever%pyabi-config)" \
   %buildroot%_bindir/python%pybasever%pyabi-config

%global python_ignored_files site-packages(/.+\.(pth|egg-info/(entry_points|namespace_packages)\.txt))?$
mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
cat > %buildroot%_sysconfdir/buildreqs/files/ignore.d/%name << EOF
^%_libdir/python3[^/]*/%python_ignored_files
%if "lib" != "%_lib"
^%prefix/lib/python3[^/]*/%python_ignored_files
%endif
EOF

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/%name-base-files.req.list
# %name dirlist for %_rpmlibdir/files.req
%dynload_dir/	%name-base
%tool_dir/	%name-tools
EOF
# rpm-build-python3 has a dep on exactly this file with the list
# (for modularity: there used to be a separate package
# with these directories and the corresponding site customization):
cat <<\EOF >%buildroot%_rpmlibdir/%python3_sitebasename-site-packages-files.req.list
%(dirname %python3_sitelibdir)	%name-base
%python3_sitelibdir/	%name-base
%if "%_lib" != "lib"
%(dirname %python3_sitelibdir_noarch)/	%name-base
%python3_sitelibdir_noarch/	%name-base
%endif
EOF

%check
# ALT#32008:
if head -1 %buildroot%_bindir/python3-config | fgrep -q python; then
configdir="$(WITHIN_PYTHON_RPM_BUILD= LD_LIBRARY_PATH=`pwd` ./python %buildroot%_bindir/python3-config --configdir)"
else
configdir="$(%buildroot%_bindir/python3-config --configdir)"
fi
[ -d %buildroot"$configdir" ]

WITHIN_PYTHON_RPM_BUILD= LD_LIBRARY_PATH=`pwd` ./python -m test.regrtest --verbose --findleaks

%files
%doc LICENSE README
%_bindir/pydoc*
%_bindir/python3
%_bindir/python%pybasever
%_bindir/%pynameabi
%_bindir/pyvenv
%_bindir/pyvenv-%pybasever
%_mandir/*/*

%files base
%doc LICENSE README
%config %_sysconfdir/buildreqs/files/ignore.d/%name
%_rpmlibdir/%name-base-files.req.list
%_rpmlibdir/%python3_sitebasename-site-packages-files.req.list

%dir %(dirname %python3_sitelibdir)
%dir %python3_sitelibdir/
%dir %python3_sitelibdir/__pycache__/
%python3_sitelibdir/README

%if "%_lib" != "lib"
%dir %(dirname %python3_sitelibdir_noarch)
%dir %python3_sitelibdir_noarch/
%dir %python3_sitelibdir_noarch/__pycache__/
%endif

%dir %pylibdir
%dir %dynload_dir
%dynload_dir/_bisect.cpython-%pyshortver%pyabi.so
%dynload_dir/_bz2.cpython-%pyshortver%pyabi.so
%dynload_dir/_codecs_cn.cpython-%pyshortver%pyabi.so
%dynload_dir/_codecs_hk.cpython-%pyshortver%pyabi.so
%dynload_dir/_codecs_iso2022.cpython-%pyshortver%pyabi.so
%dynload_dir/_codecs_jp.cpython-%pyshortver%pyabi.so
%dynload_dir/_codecs_kr.cpython-%pyshortver%pyabi.so
%dynload_dir/_codecs_tw.cpython-%pyshortver%pyabi.so
%dynload_dir/_crypt.cpython-%pyshortver%pyabi.so
%dynload_dir/_csv.cpython-%pyshortver%pyabi.so
%dynload_dir/_ctypes.cpython-%pyshortver%pyabi.so
%dynload_dir/_datetime.cpython-%pyshortver%pyabi.so
%dynload_dir/_dbm.cpython-%pyshortver%pyabi.so
%dynload_dir/_decimal.cpython-%pyshortver%pyabi.so
%dynload_dir/_elementtree.cpython-%pyshortver%pyabi.so
%if %with_gdbm
%dynload_dir/_gdbm.cpython-%pyshortver%pyabi.so
%endif
%dynload_dir/_hashlib.cpython-%pyshortver%pyabi.so
%dynload_dir/_heapq.cpython-%pyshortver%pyabi.so
%dynload_dir/_json.cpython-%pyshortver%pyabi.so
%dynload_dir/_lsprof.cpython-%pyshortver%pyabi.so
%dynload_dir/_lzma.cpython-%pyshortver%pyabi.so
%dynload_dir/_multibytecodec.cpython-%pyshortver%pyabi.so
%dynload_dir/_multiprocessing.cpython-%pyshortver%pyabi.so
%dynload_dir/_opcode.cpython-%pyshortver%pyabi.so
%dynload_dir/_pickle.cpython-%pyshortver%pyabi.so
%dynload_dir/_posixsubprocess.cpython-%pyshortver%pyabi.so
%dynload_dir/_random.cpython-%pyshortver%pyabi.so
%dynload_dir/_socket.cpython-%pyshortver%pyabi.so
%dynload_dir/_ssl.cpython-%pyshortver%pyabi.so
%dynload_dir/_struct.cpython-%pyshortver%pyabi.so
%dynload_dir/_testmultiphase.cpython-%pyshortver%pyabi.so
%dynload_dir/array.cpython-%pyshortver%pyabi.so
%dynload_dir/audioop.cpython-%pyshortver%pyabi.so
%dynload_dir/binascii.cpython-%pyshortver%pyabi.so
%dynload_dir/cmath.cpython-%pyshortver%pyabi.so
%dynload_dir/fcntl.cpython-%pyshortver%pyabi.so
%dynload_dir/grp.cpython-%pyshortver%pyabi.so
%dynload_dir/math.cpython-%pyshortver%pyabi.so
%dynload_dir/mmap.cpython-%pyshortver%pyabi.so
%dynload_dir/ossaudiodev.cpython-%pyshortver%pyabi.so
%dynload_dir/parser.cpython-%pyshortver%pyabi.so
%dynload_dir/pyexpat.cpython-%pyshortver%pyabi.so
%dynload_dir/readline.cpython-%pyshortver%pyabi.so
%dynload_dir/resource.cpython-%pyshortver%pyabi.so
%dynload_dir/select.cpython-%pyshortver%pyabi.so
%dynload_dir/spwd.cpython-%pyshortver%pyabi.so
%dynload_dir/syslog.cpython-%pyshortver%pyabi.so
%dynload_dir/termios.cpython-%pyshortver%pyabi.so
%dynload_dir/unicodedata.cpython-%pyshortver%pyabi.so
%dynload_dir/xxlimited.cpython-%pyshortver%pyabi.so
%dynload_dir/zlib.cpython-%pyshortver%pyabi.so

%pylibdir/*.py
%dir %pylibdir/__pycache__/
%pylibdir/__pycache__/*%bytecode_suffixes

%dir %pylibdir/asyncio/
%dir %pylibdir/asyncio/__pycache__/
%pylibdir/asyncio/*.py
%exclude %pylibdir/asyncio/windows_events.py
%exclude %pylibdir/asyncio/windows_utils.py
%pylibdir/asyncio/__pycache__/*%bytecode_suffixes

%dir %pylibdir/collections/
%dir %pylibdir/collections/__pycache__/
%pylibdir/collections/*.py
%pylibdir/collections/__pycache__/*%bytecode_suffixes

%dir %pylibdir/concurrent/
%dir %pylibdir/concurrent/__pycache__/
%pylibdir/concurrent/*.py
%pylibdir/concurrent/__pycache__/*%bytecode_suffixes

%dir %pylibdir/concurrent/futures/
%dir %pylibdir/concurrent/futures/__pycache__/
%pylibdir/concurrent/futures/*.py
%pylibdir/concurrent/futures/__pycache__/*%bytecode_suffixes

%dir %pylibdir/ctypes/
%dir %pylibdir/ctypes/__pycache__/
%pylibdir/ctypes/*.py
%pylibdir/ctypes/__pycache__/*%bytecode_suffixes
%pylibdir/ctypes/macholib

%dir %pylibdir/dbm/
%dir %pylibdir/dbm/__pycache__/
%pylibdir/dbm/*.py
%pylibdir/dbm/__pycache__/*%bytecode_suffixes

%dir %pylibdir/distutils/
%dir %pylibdir/distutils/__pycache__/
%pylibdir/distutils/*.py
%pylibdir/distutils/__pycache__/*%bytecode_suffixes
%pylibdir/distutils/README
%pylibdir/distutils/command

%dir %pylibdir/email/
%dir %pylibdir/email/__pycache__/
%pylibdir/email/*.py
%pylibdir/email/__pycache__/*%bytecode_suffixes
%pylibdir/email/mime
%doc %pylibdir/email/architecture.rst

%pylibdir/encodings

%dir %pylibdir/ensurepip/
%dir %pylibdir/ensurepip/__pycache__/
%pylibdir/ensurepip/*.py
%pylibdir/ensurepip/__pycache__/*%bytecode_suffixes
%exclude %pylibdir/ensurepip/_bundled

%if 0%{?with_rewheel}
%dir %pylibdir/ensurepip/rewheel/
%dir %pylibdir/ensurepip/rewheel/__pycache__/
%pylibdir/ensurepip/rewheel/*.py
%pylibdir/ensurepip/rewheel/__pycache__/*%bytecode_suffixes
%endif

%pylibdir/html
%pylibdir/http

%dir %pylibdir/importlib/
%dir %pylibdir/importlib/__pycache__/
%pylibdir/importlib/*.py
%pylibdir/importlib/__pycache__/*%bytecode_suffixes

%dir %pylibdir/json/
%dir %pylibdir/json/__pycache__/
%pylibdir/json/*.py
%pylibdir/json/__pycache__/*%bytecode_suffixes

%pylibdir/lib2to3
%exclude %lib2to3_tests
%pylibdir/logging
%pylibdir/multiprocessing
%exclude %pylibdir/multiprocessing/popen_spawn_win32.py
%pylibdir/plat-linux
%pylibdir/pydoc_data

%exclude %pylibdir/turtle.py
%exclude %pylibdir/__pycache__/turtle*%bytecode_suffixes

%dir %pylibdir/unittest/
%dir %pylibdir/unittest/__pycache__/
%pylibdir/unittest/*.py
%pylibdir/unittest/__pycache__/*%bytecode_suffixes

%pylibdir/urllib

%dir %pylibdir/venv/
%dir %pylibdir/venv/__pycache__/
%pylibdir/venv/*.py
%pylibdir/venv/__pycache__/*%bytecode_suffixes
%pylibdir/venv/scripts

%pylibdir/wsgiref
%pylibdir/xml
%pylibdir/xmlrpc

# "Makefile" and the config-32/64.h file are needed by
# distutils/sysconfig.py:_init_posix(), so we include them in the core
# package, along with their parent directories (bug 531901):
%dir %pylibdir/config-%pybasever%pyabi/
%pylibdir/config-%pybasever%pyabi/Makefile
%dir %include_dir/
%include_dir/%_pyconfig_h

%files -n libpython3
%_libdir/libpython%pybasever%pyabi.so.*

%files dev
%pylibdir/config-%pybasever%pyabi/*
%exclude %pylibdir/config-%pybasever%pyabi/Makefile
%include_dir/*.h
%exclude %include_dir/%_pyconfig_h
%doc Misc/README.valgrind Misc/valgrind-python.supp Misc/gdbinit
%_bindir/python3-config
%_bindir/python%pybasever-config
%_bindir/python%pybasever%pyabi-config
%_libdir/libpython3.so
%_libdir/libpython%pybasever%pyabi.so
%_libdir/pkgconfig/python3.pc
%_libdir/pkgconfig/python-%pybasever.pc
%_libdir/pkgconfig/python-%pybasever%pyabi.pc

%files tools
%_bindir/python3-2to3
%_bindir/2to3-%pybasever
%_bindir/idle*
%tool_dir
%exclude %tool_dir/scripts/run_tests.py
%doc %pylibdir/Doc

%files modules-tkinter
%pylibdir/idlelib
%pylibdir/tkinter
%exclude %pylibdir/tkinter/test
%dynload_dir/_tkinter.cpython-%pyshortver%pyabi.so
%pylibdir/turtle.py
%pylibdir/__pycache__/turtle*%bytecode_suffixes
%dir %pylibdir/turtledemo
%pylibdir/turtledemo/*.py
%pylibdir/turtledemo/*.cfg
%dir %pylibdir/turtledemo/__pycache__/
%pylibdir/turtledemo/__pycache__/*%bytecode_suffixes

%files modules-sqlite3
%dir %pylibdir/sqlite3/
%dir %pylibdir/sqlite3/__pycache__/
%pylibdir/sqlite3/*.py
%pylibdir/sqlite3/__pycache__/*%bytecode_suffixes
%dynload_dir/_sqlite3.cpython-%pyshortver%pyabi.so

%files modules-curses
%pylibdir/curses
%dynload_dir/_curses.cpython-%pyshortver%pyabi.so
%dynload_dir/_curses_panel.cpython-%pyshortver%pyabi.so

%files test
%pylibdir/ctypes/test
%pylibdir/distutils/tests
%lib2to3_tests
%pylibdir/sqlite3/test
%pylibdir/test
%dynload_dir/_ctypes_test.cpython-%pyshortver%pyabi.so
%dynload_dir/_testbuffer.cpython-%pyshortver%pyabi.so
%dynload_dir/_testcapi.cpython-%pyshortver%pyabi.so
%dynload_dir/_testimportmultiple.cpython-%pyshortver%pyabi.so
%pylibdir/tkinter/test
%pylibdir/unittest/test
%tool_dir/scripts/run_tests.py

%changelog
* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.4-alt3
- Fixed build with new glibc.

* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.4-alt2
- Packed audiotest.au files required by tests.
- Returned some distutils submodules required by setup scripts of numpy.
- Nis module no longer builds with new glibc.

* Sun Oct 29 2017 Anton Midyukov <antohami@altlinux.org> 3.5.4-alt1
- New version 3.5.4

* Mon Sep 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.1-alt10
- Fixed tests with new libexpat.

* Mon Jul 10 2017 Fr. Br. George <george@altlinux.ru> 3.5.1-alt9
- Add PLATFORM_TRIPLET suffix for binary module search

* Tue Apr 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.1-alt8
- Fixed interpreter breakage caused by rebuild with glibc >= 2.25
  (closes: #33356).

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.5.1-alt7.qa1
- NMU: rebuilt against Tcl/Tk 8.6.

* Thu May  5 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.1-alt7
- python3-modules-tkinter: Requires: tk (ALT#29206)

* Wed May  4 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.1-alt6
- (.spec) Adapted for other 64bit archs (thx sbolshakov@).

* Fri Apr 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.1-alt5
- %%py3_provides os.path (an OS-independent alias, which other modules
  might want to import).
- test: Some good code in lib2to3/tests restored (and some bad code removed).

* Wed Apr 20 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.1-alt4.1
- Rebuild with rpm-build-python3-0.1.10.2 (more autoreqs/provs will
  be found, and their default format has been tweaked slightly).

* Wed Apr 20 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.1-alt4
- put the Python implementation of python3-config back (as in 3.3)
  because it prints more correct values for --configdir (ALT#32008).

* Thu Apr 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.1-alt3
- I was wrong in letting __pycache__/ be handled by files.req:
  must be invisible. (Other pkgs gave this crazy Provides as a result.)

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.1-alt2
- Merged the major switch to a common /usr/lib{,64}/python3/site-packages
  done in 3.3:
  + Switch to a common /usr/lib{,64}/python3/site-packages
    (without the minor version).
  + Provide python3.3-ABI: compatible .so in Python modules rely on it.
  + Require rpm-build-python3 (as per ALT Sisyphus RPM Macros Packaging Policy).
  + This package does not "strictly" own /usr/lib{,64}/python3.3 anymore
    (for convenience of the transition and because it makes little sense).

* Wed Mar 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.1-alt1
- Updated to 3.5.1.
- Synced with Fedora python3-3.5.1-1.

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt8
- added ignored python3 files pattern for buildreq.
- (.spec) Help verify_elf by pointing %%__libpython3 to our newly
  built library.

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt7
- Unicode problem with ncurses fixed (RH#539917).
- Unpackage garbage __pycache__/* left-over from unwanted files.
- (.spec) Clean up to fail if the maintainer's intentions get not
  fulfilled because the sources or the build environment have changed.

* Sun Mar  6 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt6
- Switch to a common /usr/lib{,64}/python3/site-packages
  (without the minor version).
- Provide python3.3-ABI: compatible .so in Python modules rely on it.
- Require rpm-build-python3 (as per ALT Sisyphus RPM Macros Packaging Policy).
- This package does not "strictly" own /usr/lib{,64}/python3.3 anymore
  (for convenience of the transition and because it makes little sense).

* Sat Mar  5 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt5
- do not test SSL (this is currently broken in Sisyphus anyway, but we
  need to be able to rebuild; the SSL-bugs haven't gone away and need
  a fix; but we are moving to 3.5 very soon)

* Tue Apr 16 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.1-alt4
- remove subpackage %%name-modules-idlelib (moved to
  %%name-modules-tkinter)
- move %%_libdir/python*/Tools/scripts/run_tests.py to subpackage
  %%name-test

* Fri Apr 12 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.1-alt3
- add subpackage %%name-modules-idlelib

* Fri Apr 12 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.1-alt2
- fix gcc 4.8 incompatibility (rhbz#927358); regenerate autotool
  intermediates
- fix error in platform.platform() when non-ascii byte strings are
  decoded to unicode (rhbz#922149)

* Fri Apr 12 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.1-alt1
- version up to 3.3.1
- skip test_posix_fadvise: RLIMIT_CPU 1000000 unavailable in hasher

* Fri Mar 29 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.0-alt1
- version up to 3.3.0
- add support for Bluetooth

* Wed May 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.3-alt3
- base: add python3.x(builtins) to Provides

* Thu Apr 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.3-alt2
- python-3.2.3-autoconf-sem_open_check-alt.patch

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Mon Mar 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.2-alt4
- build python3 binary with static libpython3
- split up independent libpython3 subpackage with shared library
- change optimization to -O3

* Thu Jan 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.2-alt3
- repair build with fresh rpm-build-python3
- enable check

* Wed Dec 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.2-alt2
- rebuild with rpm-build-python3
- split up, rename subpackages

* Tue Dec 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.2-alt1
- initial Python3 port from Fedora
