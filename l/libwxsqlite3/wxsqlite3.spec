%global wxversion 3.2
%global wxincdir %_includedir/wx-%wxversion
%define oname wxsqlite3

Name: libwxsqlite3
Version: 4.8.1
Release: alt1
Epoch: 1

Summary: C++ wrapper around the SQLite 3.x database

Group: System/Libraries
License: wxWidgets
Url: http://wxcode.sourceforge.net/components/wxsqlite3/

# Source-url: https://github.com/utelle/wxsqlite3/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++ libwxGTK%wxversion-devel
BuildRequires: libsqlite3-devel
BuildRequires: doxygen

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
Requires: libsqlite3-devel

Obsoletes: libwxGTK3.0-sqlite3-devel
Obsoletes: libwxGTK3.1-sqlite3-devel
Obsoletes: libwxsqlite3-wx3.0-devel

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

%build
%autoreconf
%configure --enable-shared=yes --enable-static=no --enable-codec=chacha20 \
           --enable-codec=sqlcipher --enable-codec=rc4 --enable-codec=aes256 \
           --enable-codec=aes128
%make_build

# build docs
pushd docs
doxygen
popd

%install
%makeinstall_std

# move headers from %_includedir/wx to %_includedir/wx-?.?/wx
mkdir %buildroot%wxincdir
mv %buildroot%_includedir/wx %buildroot%wxincdir

find %buildroot -name '*.la' -exec rm -f {} ';'

%files
%doc LICENCE.txt readme.md
%_libdir/*.so.*

%files devel
%wxincdir/wx/*
%_pkgconfigdir/wxsqlite3.pc
%_libdir/*.so

%files doc
%doc docs/html

%changelog
* Mon Mar 06 2022 Anton Midyukov <antohami@altlinux.org> 1:4.8.1-alt1
- Initial build from libwxGTK3.0-sqlite3
- Build with wxGTK3.2
- Obsoletes old devel subpackages of previous versions
- build documentation
