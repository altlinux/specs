Name: mingw32-sqlite
Version: 3.6.6.2
Release: alt1

Summary: MinGW Windows port of sqlite embeddable SQL database engine

License: Public Domain
Group: Development/Databases
Url: http://www.sqlite.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.sqlite.org/sqlite-%version.tar

BuildArch: noarch

# Patches from Fedora native package.
Patch1: sqlite-3.6.6.2-libdl.patch
Patch2: sqlite-3.6.6.2-lemon-snprintf.patch

# Patches for MinGW port.
Patch1000: mingw32-sqlite-3.6.6.2-no-undefined.patch


BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-runtime >= 3.15.1

BuildRequires: mingw32-filesystem >= 26
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils

#BuildRequires: mingw32-pdcurses
BuildRequires: mingw32-readline
BuildRequires: mingw32-termcap >= 1.3.1-3

BuildRequires: autoconf
BuildRequires: libtool

#Requires: pkgconfig

%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

This package contains cross-compiled libraries and development tools
for Windows.

%prep
%setup -n sqlite-%version
%patch1 -p1 -b .libdl
%patch2 -p1 -b .lemon-sprintf
%patch1000 -p1

# Ships with an old/broken version of libtool which cannot create
# Windows libraries properly.  So pull in the current version.
autoreconf
libtoolize --force

%build
# I think there's a bug in the configure script where, if
# cross-compiling, it cannot correctly determine the target executable
# extension (ie. .exe).  As a result it doesn't correctly detect that
# the target is Windows and so tries to use Unix-specific functions
# which don't exist.  In any case we can work around this by forcing
# the extension via this export.
#   - RWMJ 2008-09-30
export config_TARGET_EXEEXT=.exe

%_mingw32_configure --disable-tcl
%make_build

%install
%makeinstall_std

# Remove static libraries but DON'T remove *.dll.a files.
#rm %buildroot%_mingw32_libdir/libsqlite3.a
rm %buildroot%_mingw32_libdir/libsqlite3.la

#chmod 0644 %buildroot%_mingw32_libdir/libsqlite3.dll.a

%files
%doc README VERSION
%_mingw32_bindir/sqlite3.exe
#%_mingw32_bindir/libsqlite3-0.dll
#%_mingw32_libdir/libsqlite3.dll.a
%_mingw32_libdir/libsqlite3.a
%_mingw32_includedir/sqlite3.h
%_mingw32_includedir/sqlite3ext.h
%_mingw32_libdir/pkgconfig/sqlite3.pc

%changelog
* Fri Mar 25 2011 Vitaly Lipatov <lav@altlinux.ru> 3.6.6.2-alt1
- initial build for ALT Linux Sisyphus

* Tue Dec 16 2008 Richard Jones <rjones@redhat.com> - 3.6.6.2-1
- New upstream release (to match Fedora native), 3.6.6.2.
- Replace patches with ones from native.
- Rebase -no-undefined patch.
- Remove spurious +x permissions on libsqlite3.dll.a.
- Requires pkgconfig.

* Sat Nov 22 2008 Richard Jones <rjones@redhat.com> - 3.5.9-3
- Rebuild against new readline.

* Fri Oct 31 2008 Richard Jones <rjones@redhat.com> - 3.5.9-2
- Rebuild against latest termcap.

* Thu Sep 25 2008 Richard Jones <rjones@redhat.com> - 3.5.9-1
- Initial RPM release.
