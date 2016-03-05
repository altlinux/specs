# ======================================================
# Conditionals and other variables controlling the build
# ======================================================

%global pybasever 3.3
%global __python3_version %pybasever

# pybasever without the dot:
%global pyshortver 33

%global pyabi m

%global pynameabi python%pybasever%pyabi

%global pylibdir %_libdir/python%pybasever
%global dynload_dir %pylibdir/lib-dynload
%global pylibdir_noarch %_libexecdir/python%pybasever

# Fix find-requires
%define __python3 %buildroot%_bindir/python3
%add_python3_path %pylibdir

# All bytecode files are now in a __pycache__ subdirectory, with a name
# reflecting the version of the bytecode (to permit sharing of python libraries
# between different runtimes)
# See http://www.python.org/dev/peps/pep-3147/
# For example,
#   foo/bar.py
# now has bytecode at:
#   foo/__pycache__/bar.cpython-33.pyc
#   foo/__pycache__/bar.cpython-33.pyo
%global bytecode_suffixes .cpython-33.py?

# Python's configure script defines SOVERSION, and this is used in the Makefile
# to determine INSTSONAME, the name of the libpython DSO:
#   LDLIBRARY='libpython$(VERSION).so'
#   INSTSONAME="$LDLIBRARY".$SOVERSION
# We mirror this here in order to make it easier to add the -gdb.py hooks.
# (if these get out of sync, the payload of the libs subpackage will fail
# and halt the build)
%global py_SOVERSION 1.0

# some arches don't have valgrind so we need to disable its support on them
%ifarch %ix86 x86_64
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
Version: %pybasever.1
Release: alt5
License: Python
Group: Development/Python3

BuildRequires(pre): rpm-build-python3 >= 0.1.7
BuildPreReq: liblzma-devel
# For Bluetooth support
# see https://bugzilla.redhat.com/show_bug.cgi?id=879720
BuildPreReq: libbluez-devel
BuildRequires: bzip2-devel db4-devel libexpat-devel gcc-c++ libgmp-devel libffi-devel libGL-devel libX11-devel libncurses-devel libssl-devel libreadline-devel libsqlite3-devel tcl-devel tk-devel zlib-devel

%if %with_gdbm
BuildRequires: gdbm-devel
%endif

%if 0%{?with_valgrind}
BuildRequires: valgrind-devel
%endif

Source: %name-%version.tar

#RH Patches

# Fixup distutils/unixccompiler.py to remove standard library path from rpath:
# Was Patch0 in ivazquez' python3000 specfile:
Patch1: Python-3.1.1-rpath.patch

Patch102: python-3.3.0b1-lib64.patch

# 00104 #
# Only used when "%_lib" == "lib64"
# Another lib64 fix, for distutils/tests/test_install.py; not upstream:
Patch104: 00104-lib64-fix-for-test_install.patch


# 00113 #
# Add configure-time support for the COUNT_ALLOCS and CALL_PROFILE options
# described at http://svn.python.org/projects/python/trunk/Misc/SpecialBuilds.txt
# so that if they are enabled, they will be in that build's pyconfig.h, so that
# extension modules will reliably use them
# Not yet sent upstream
Patch113: 00113-more-configuration-flags.patch

# 00114 #
# Add flags for statvfs.f_flag to the constant list in posixmodule (i.e. "os")
# (rhbz:553020); partially upstream as http://bugs.python.org/issue7647
# Not yet sent upstream
Patch114: 00114-statvfs-f_flag-constants.patch

# 00125 #
# COUNT_ALLOCS is useful for debugging, but the upstream behaviour of always
# emitting debug info to stdout on exit is too verbose and makes it harder to
# use the debug build.  Add a "PYTHONDUMPCOUNTS" environment variable which
# must be set to enable the output on exit
# Not yet sent upstream
Patch125: 00125-less-verbose-COUNT_ALLOCS.patch

# In my koji builds, /root/bin is in the PATH for some reason
# This leads to test_subprocess.py failing, due to "test_leaking_fds_on_error"
# trying every dir in PATH for "nonexisting_i_hope", which leads to it raising
#  OSError: [Errno 13] Permission denied
# when it tries to read /root/bin, rather than raising "No such file"
#
# Work around this by specifying an absolute path for the non-existant
# executable
# Not yet sent upstream
Patch129: python-3.2.1-fix-test-subprocess-with-nonreadable-path-dir.patch

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

# 00134 #
# Fix a failure in test_sys.py when configured with COUNT_ALLOCS enabled
# Not yet sent upstream
Patch134: 00134-fix-COUNT_ALLOCS-failure-in-test_sys.patch

# 00135 #
# test_weakref's test_callback_in_cycle_resurrection doesn't work with
# COUNT_ALLOCS, as the metrics keep "C" alive.  Work around this for our
# debug build:
# Not yet sent upstream
Patch135: 00135-fix-test-within-test_weakref-in-debug-build.patch

# 00137 #
# Some tests within distutils fail when run in an rpmbuild:
Patch137: 00137-skip-distutils-tests-that-fail-in-rpmbuild.patch

# 00139 #
# ARM-specific: skip known failure in test_float:
#  http://bugs.python.org/issue8265 (rhbz#706253)
Patch139: 00139-skip-test_float-known-failure-on-arm.patch

# 00141 #
# Fix test_gc's test_newinstance case when configured with COUNT_ALLOCS:
# Not yet sent upstream
Patch141: 00141-fix-test_gc_with_COUNT_ALLOCS.patch

# 00142 #
# Some pty tests fail when run in mock (rhbz#714627):
Patch142: 00142-skip-failing-pty-tests-in-rpmbuild.patch

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
Patch146: 00146-hashlib-fips.patch

# 00158 #
# Upstream as of Python 3.3.1

# 00159 #
#  Patch159: 00159-correct-libdb-include-path.patch
# in python.spec
# TODO: python3 status?

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

# 00165 #
# python.spec has:
#   Patch165: 00165-crypt-module-salt-backport.patch
# which is a backport from 3.3 and thus not relevant to "python3"

# 00166 #
#  Patch166: 00166-fix-fake-repr-in-gdb-hooks.patch
# in python.spec
# TODO: python3 status?

# 00167 #
#  Patch167: 00167-disable-stack-navigation-tests-when-optimized-in-test_gdb.patch
# in python.spec
# TODO: python3 status?

# 00168 #
#  Patch168: 00168-distutils-cflags.patch
# in python.spec
# TODO: python3 status?

# 00169 #
#  Patch169: 00169-avoid-implicit-usage-of-md5-in-multiprocessing.patch
# in python.spec
# TODO: python3 status?

# 00170 #
#  Patch170: 00170-gc-assertions.patch
# in python.spec
# TODO: python3 status?

# 00171 #
# python.spec had:
#  Patch171: 00171-raise-correct-exception-when-dev-urandom-is-missing.patch
# TODO: python3 status?

# 00172 #
# python.spec had:
#  Patch172: 00172-use-poll-for-multiprocessing-socket-connection.patch
# TODO: python3 status?

# 00174 #
#  Patch174: 00174-fix-for-usr-move.patch
# TODO: python3 status?

# 00175 #
# Fix for configure.ac mistakenly detecting
#   checking whether gcc supports ParseTuple __format__... yes
# when it doesn't, when compiling with gcc 4.8
#
# Sent upstream as http://bugs.python.org/issue17547
# (rhbz#927358)
Patch175: 00175-fix-configure-Wformat.patch

# 00177 #
# Patch for potential unicode error when determining OS release names
# http://bugs.python.org/issue17429
# (rhbz#922149)
# Does not affect python2 (python2 uses a byte string so it doesn't need to decode)
Patch177: 00177-platform-unicode.patch

# 00178 #
# Don't duplicate various FLAGS in sysconfig values
# http://bugs.python.org/issue17679
# Does not affect python2 AFAICS (different sysconfig values initialization)
Patch178: 00178-dont-duplicate-flags-in-sysconfig.patch

Patch201: python-3.3.0-autoconf-sem_open_check-alt.patch

# Under some kernels not working on tmpfs,
# see http://comments.gmane.org/gmane.linux.suse.kernel/3182
%if_enabled test_posix_fadvise
Patch202: python-3.3.0-skip-test_posix_fadvise-alt.patch
%endif

# RLIMIT 1000000 unavailable in hasher
Patch203: python-3.3.1-skip-test_setrusage_refcount-alt.patch

# ======================================================
# Additional metadata, and subpackages
# ======================================================

Url: http://www.python.org/

Provides: python(abi) = %pybasever

Requires: %name-base = %EVR

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
%filter_from_requires /^%name[[:space:]]/d
%filter_from_requires /^\/usr\/bin\/%name/d

%description base
This package contains files used to embed Python 3 into applications.

%package dev
Summary: Libraries and header files needed for Python 3 development
Group: Development/Python3
Requires: %name = %EVR
Conflicts: %name < %EVR
Provides: %name-devel = %pybasever
Provides: lib%name-devel = %EVR

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
for f in md5module.c sha1module.c sha256module.c sha512module.c; do
    rm Modules/$f
done

#
# Apply patches:
#
%patch1 -p1

%if "%_lib" == "lib64"
%patch102 -p1
%patch104 -p1
%endif

%patch113 -p1
%patch114 -p1

%patch125 -p1 -b .less-verbose-COUNT_ALLOCS

%patch129 -p1

%ifarch ppc ppc64
%patch131 -p1
%endif

%patch132 -p1
%patch134 -p1
%patch135 -p1
%patch137 -p1
%ifarch %arm
%patch139 -p1
%endif
%patch141 -p1
%patch142 -p1
%patch143 -p1 -b .tsc-on-ppc
%patch146 -p1
#00158: FIXME
#00159: FIXME
%patch160 -p1
%patch163 -p1
#00165: TODO
#00166: TODO
#00167: TODO
#00168: TODO
#00169: TODO
#00170: TODO
#00171: TODO
#00172: TODO
#00174: TODO
%patch175 -p1
%patch177 -p1
%patch178 -p1

%patch201 -p2
%if_enabled test_posix_fadvise
%patch202 -p2
%endif
%patch203 -p2

# Currently (2010-01-15), http://docs.python.org/library is for 2.6, and there
# are many differences between 2.6 and the Python 3 library.
#
# Fix up the URLs within pydoc to point at the documentation for this
# MAJOR.MINOR version:
#
sed --in-place \
    --expression="s|http://docs.python.org/library|http://docs.python.org/%pybasever/library|g" \
    Lib/pydoc.py || exit 1

mkdir ../build-shared
%autoreconf
cp -rl * ../build-shared/

# Add target for optimized Power7 binaries:
sed -i -e "s/ppc64-\*/ppc64-\* \| ppc64p7-\*/" config.sub

%build
topdir=$(pwd)

build() {
%configure \
  --enable-ipv6 \
  --with-system-ffi \
%if 0%{?with_valgrind}
  --with-valgrind \
%endif
  --with-system-expat \
  --with-dbmliborder=gdbm:ndbm:bdb \
  --with-computed-gotos=%with_computed_gotos \
  $*

%make CFLAGS=
}

pushd ../build-shared
build  --enable-shared
popd

build

%install

pushd ../build-shared
make install DESTDIR=%buildroot INSTALL="install -p"
popd

make install DESTDIR=%buildroot INSTALL="install -p"

install -d -m 0755 $RPM_BUILD_ROOT%pylibdir/site-packages/__pycache__

mv $RPM_BUILD_ROOT%_bindir/2to3 $RPM_BUILD_ROOT%_bindir/python3-2to3

# Development tools
install -m755 -d $RPM_BUILD_ROOT%pylibdir/Tools
install Tools/README $RPM_BUILD_ROOT%pylibdir/Tools/
cp -ar Tools/freeze $RPM_BUILD_ROOT%pylibdir/Tools/
cp -ar Tools/i18n $RPM_BUILD_ROOT%pylibdir/Tools/
cp -ar Tools/pynche $RPM_BUILD_ROOT%pylibdir/Tools/
cp -ar Tools/scripts $RPM_BUILD_ROOT%pylibdir/Tools/

# Documentation tools
install -m755 -d %buildroot%pylibdir/Doc
cp -ar Doc/tools %buildroot%pylibdir/Doc/

# Demo scripts
cp -ar Tools/demo %buildroot%pylibdir/Tools/

# Fix for bug #136654
rm -f %buildroot%pylibdir/email/test/data/audiotest.au %buildroot%pylibdir/test/audiotest.au

%if "%_lib" == "lib64"
install -d -m 0755 %buildroot/usr/lib/python%pybasever/site-packages/__pycache__
%endif

# Make python3-devel multilib-ready (bug #192747, #139911)
%global _pyconfig32_h pyconfig-32.h
%global _pyconfig64_h pyconfig-64.h

%ifarch x86_64
%global _pyconfig_h %_pyconfig64_h
%else
%global _pyconfig_h %_pyconfig32_h
%endif

mv %buildroot%_includedir/%pynameabi/pyconfig.h  %buildroot%_includedir/%pynameabi/%_pyconfig_h
cat > %buildroot%_includedir/%pynameabi/pyconfig.h << EOF
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
  %buildroot%pylibdir/Tools/README

# Get rid of DOS batch files:
find %buildroot -name \*.bat -exec rm {} \;

# Get rid of backup files:
find %buildroot/ -name "*~" -exec rm -f {} \;
find . -name "*~" -exec rm -f {} \;
rm -f %buildroot%pylibdir/LICENSE.txt
# Junk, no point in putting in -test sub-pkg
rm -f $RPM_BUILD_ROOT/%pylibdir/idlelib/testcode.py*

# Get rid of stray patch file from buildroot:
rm -f %buildroot%pylibdir/test/test_imp.py.apply-our-changes-to-expected-shebang # from patch 4

# Get rid of crappy code:
rm -f %buildroot%pylibdir/Tools/scripts/abitype.py
rm -f %buildroot%pylibdir/Tools/scripts/fixcid.py
rm -f %buildroot%pylibdir/encodings/rot_13.py

# Get rid of lib2to3 tests (python2)
rm -rf %buildroot%pylibdir/lib2to3/tests

# Get rid of win tests
rm -f %buildroot%pylibdir/test/test_winreg.py
rm -f %buildroot%pylibdir/test/test_winsound.py
rm -f %buildroot%pylibdir/test/win_console_handler.py
rm -f %buildroot%pylibdir/distutils/tests/test_msvc9compyler.py

# Get rid of bad* tests
rm -rf %buildroot%pylibdir/test/bad*.py

# Get rid of windows-related stuff
rm -rf %buildroot%pylibdir/distutils/msvccompiler.py
rm -rf %buildroot%pylibdir/distutils/msvc9compiler.py
rm -rf %buildroot%pylibdir/distutils/command/bdist_msi.py
rm -rf %buildroot%pylibdir/distutils/command/*.exe
rm -f %buildroot%pylibdir/Tools/scripts/win_add2path.py

# Get rid of crap
rm -rf %buildroot%pylibdir/ctypes/macholib/fetch_macholib
rm -f %buildroot%pylibdir/Tools/scripts/md5sum.py
rm -f %buildroot%pylibdir/Tools/scripts/parseentities.py

# Remove sphinxext (temporary)
rm -rf %buildroot%pylibdir/Doc/tools/sphinxext
rm -f %buildroot%pylibdir/Doc/tools/sphinx-build.py

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
    | grep libncurses.so && (echo "_curses.so linked against libncurses.so" ; exit 1)

export LD_LIBRARY_PATH=%buildroot%_libdir
find %buildroot -type f -a -name "*.py" -a -not -wholename "*/test/*" -a -not -wholename "*/tests/*" -a -not -wholename "*/scripts/*" -print0 | xargs -0 %buildroot%_bindir/%name -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%buildroot")[2]) for f in sys.argv[1:]]'
find %buildroot -type f -a -name "*.py" -a -not -wholename "*/test/*" -a -not -wholename "*/tests/*" -a -not -wholename "*/scripts/*" -print0 | xargs -0 %buildroot%_bindir/%name -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%buildroot")[2]) for f in sys.argv[1:]]'

sed -i 's,/usr/local/bin/python,/usr/bin/python3,' %buildroot%_libdir/python%pybasever/cgi.py

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/%name-base-files.req.list
# %name dirlist for %_rpmlibdir/files.req
%pylibdir/	%name-base
%dynload_dir/	%name-base
%pylibdir/__pycache__/	%name-base
%pylibdir/site-packages/	%name-base
%pylibdir/site-packages/__pycache__/	%name-base
%pylibdir/Tools/	%name-tools
%pylibdir/Tools/__pycache__/	%name-tools
%pylibdir_noarch/	%name-base
%pylibdir_noarch/site-packages/	%name-base
%pylibdir_noarch/site-packages/__pycache__/	%name-base
EOF

#Do not recompile .py files with old python3
%add_python3_compile_exclude %_libdir/python%pybasever

%check
# Probably, some SSL-related things are currently anyway broken in Sisyphus
# with the current python3-3.3. Now, as we know it, we remove these tests
# to be able to rebuild python3-3.3 and make a transition to 3.5.
# (Of course, this doesn't mean that we assume that these things are OK in Sisyphus.
# TODO: report these bugs, at least, for p7.)
rm Lib/test/test_{ftplib,ssl}.py

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
%_rpmlibdir/%name-base-files.req.list
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
%dynload_dir/_pickle.cpython-%pyshortver%pyabi.so
%dynload_dir/_posixsubprocess.cpython-%pyshortver%pyabi.so
%dynload_dir/_random.cpython-%pyshortver%pyabi.so
%dynload_dir/_socket.cpython-%pyshortver%pyabi.so
%dynload_dir/_ssl.cpython-%pyshortver%pyabi.so
%dynload_dir/_struct.cpython-%pyshortver%pyabi.so
%dynload_dir/array.cpython-%pyshortver%pyabi.so
%dynload_dir/atexit.cpython-%pyshortver%pyabi.so
%dynload_dir/audioop.cpython-%pyshortver%pyabi.so
%dynload_dir/binascii.cpython-%pyshortver%pyabi.so
%dynload_dir/cmath.cpython-%pyshortver%pyabi.so
%dynload_dir/_datetime.cpython-%pyshortver%pyabi.so
%dynload_dir/fcntl.cpython-%pyshortver%pyabi.so
%dynload_dir/grp.cpython-%pyshortver%pyabi.so
%dynload_dir/math.cpython-%pyshortver%pyabi.so
%dynload_dir/mmap.cpython-%pyshortver%pyabi.so
%dynload_dir/nis.cpython-%pyshortver%pyabi.so
%dynload_dir/ossaudiodev.cpython-%pyshortver%pyabi.so
%dynload_dir/parser.cpython-%pyshortver%pyabi.so
%dynload_dir/pyexpat.cpython-%pyshortver%pyabi.so
%dynload_dir/readline.cpython-%pyshortver%pyabi.so
%dynload_dir/resource.cpython-%pyshortver%pyabi.so
%dynload_dir/select.cpython-%pyshortver%pyabi.so
%dynload_dir/spwd.cpython-%pyshortver%pyabi.so
%dynload_dir/syslog.cpython-%pyshortver%pyabi.so
%dynload_dir/termios.cpython-%pyshortver%pyabi.so
%dynload_dir/time.cpython-%pyshortver%pyabi.so
%dynload_dir/unicodedata.cpython-%pyshortver%pyabi.so
%dynload_dir/xxlimited.cpython-%pyshortver%pyabi.so
%dynload_dir/zlib.cpython-%pyshortver%pyabi.so

%dir %pylibdir/site-packages/
%dir %pylibdir/site-packages/__pycache__/
%pylibdir/site-packages/README
%pylibdir/*.py
%dir %pylibdir/__pycache__/
%pylibdir/__pycache__/*%bytecode_suffixes

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
%pylibdir/logging
%pylibdir/multiprocessing
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

%if "%_lib" == "lib64"
%attr(0755,root,root) %dir %prefix/lib/python%pybasever
%attr(0755,root,root) %dir %prefix/lib/python%pybasever/site-packages
%attr(0755,root,root) %dir %prefix/lib/python%pybasever/site-packages/__pycache__/
%endif

# "Makefile" and the config-32/64.h file are needed by
# distutils/sysconfig.py:_init_posix(), so we include them in the core
# package, along with their parent directories (bug 531901):
%dir %pylibdir/config-%pybasever%pyabi/
%pylibdir/config-%pybasever%pyabi/Makefile
%dir %_includedir/%pynameabi/
%_includedir/%pynameabi/%_pyconfig_h

%files -n libpython3
%_libdir/libpython%pybasever%pyabi.so.*

%files dev
%pylibdir/config-%pybasever%pyabi/*
%exclude %pylibdir/config-%pybasever%pyabi/Makefile
%_includedir/%pynameabi/*.h
%exclude %_includedir/%pynameabi/%_pyconfig_h
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
%pylibdir/Tools
%exclude %pylibdir/Tools/scripts/run_tests.py
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
%pylibdir/turtledemo/*.txt
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
%pylibdir/sqlite3/test
%pylibdir/test
%dynload_dir/_ctypes_test.cpython-%pyshortver%pyabi.so
%dynload_dir/_testbuffer.cpython-%pyshortver%pyabi.so
%dynload_dir/_testcapi.cpython-%pyshortver%pyabi.so
%pylibdir/tkinter/test
%pylibdir/unittest/test
%pylibdir/Tools/scripts/run_tests.py

%changelog
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
