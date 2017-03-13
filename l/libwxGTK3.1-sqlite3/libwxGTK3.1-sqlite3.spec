%global wxversion 3.1
%global wxincdir %_includedir/wx-%wxversion
%define oname wxsqlite3

Name: libwxGTK%wxversion-sqlite3
Version: 3.5.1
Release: alt1

Summary: C++ wrapper around the SQLite 3.x database

Group: System/Libraries
License: wxWidgets
Url: http://wxcode.sourceforge.net/components/wxsqlite3/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/utelle/wxsqlite3/archive/v%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Sun Sep 29 2013
# optimized out: fontconfig gnu-config libgdk-pixbuf libstdc++-devel libwayland-client libwayland-server python3-base
BuildRequires: gcc-c++ libwxGTK%wxversion-devel

# 3.5.0 - January 2017 SQLite3 library now integrated part of wxSQLite3
# libsqlite3-devel

%description
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database and is
specifically designed for use in programs based on the wxWidgets library.
wxSQLite3 does not try to hide the underlying database, in contrary almost all
special features of the current SQLite3 version 3.6.22 are supported, like for
example the creation of user defined scalar or aggregate functions. Since
SQLite stores strings in UTF-8 encoding, the wxSQLite3 methods provide
automatic conversion between wxStrings and UTF-8 strings. This works best for
the Unicode builds of wxWidgets.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: libwxGTK%wxversion-devel

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains html documentation
that use %name.

%prep
%setup

# delete bundled sqlite3 files
#rm -rfv sqlite3

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

# move headers from %_includedir/wx to %_includedir/wx-?.?/wx
mkdir %buildroot%wxincdir
mv %buildroot%_includedir/wx %buildroot%wxincdir

#find %buildroot -name '*.la' -exec rm -f {} ';'

# install own Debian-compatible pkgconfig file
mkdir -p %buildroot%_pkgconfigdir
sed -e "s!@VERSION@!%version!" \
	-e "s!@LIBDIR@!%_lib!" \
	-e "s!@WXVERSION@!%wxversion!g" \
wxsqlite3.pc.in > %buildroot%_pkgconfigdir/%oname-%wxversion.pc

%files
%doc LICENCE.txt readme.md
%_libdir/*.so.*

%files devel
%wxincdir/wx/*
%_pkgconfigdir/%oname-%wxversion.pc
%_libdir/*.so

#files doc
#doc docs/html

%changelog
* Mon Mar 13 2017 Vitaly Lipatov <lav@altlinux.ru> 3.5.1-alt1
- initial build to ALT Linux Sisyphus
