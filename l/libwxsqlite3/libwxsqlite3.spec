%global wxversion %(wx-config --release)
%global wxincdir %_includedir/wx-%wxversion
%define oname wxsqlite3

Name: libwxsqlite3
Version: 3.0.5
Release: alt2

Summary: C++ wrapper around the SQLite 3.x database

Group: System/Libraries
License: wxWidgets
Url: http://wxcode.sourceforge.net/components/wxsqlite3/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://prdownloads.sourceforge.net/wxcode/%oname-%version.tar.gz
Source: %name-%version.tar
Source1: %oname-3.0.5.pc.in
Source44: import.info

# Automatically added by buildreq on Sun Sep 29 2013
# optimized out: fontconfig gnu-config libgdk-pixbuf libstdc++-devel libwayland-client libwayland-server python3-base
BuildRequires: gcc-c++ libsqlite3-devel libwxGTK-devel

Provides: %oname = %version-%release
Obsoletes: %oname = %version-%release

%description
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database and is
specifically designed for use in programs based on the wxWidgets library.
wxSQLite3 does not try to hide the underlying database, in contrary almost all
special features of the current SQLite3 version 3.6.22 are supported, like for
example the creation of user defined scalar or aggregate functions. Since
SQLite stores strings in UTF-8 encoding, the wxSQLite3 methods provide
automatic conversion between wxStrings and UTF-8 strings. This works best for
the Unicode builds of wxWidgets. In ANSI builds the current locale conversion
object (wxConvCurrent) is used for conversion to/from UTF-8. Special care has
to be taken if external administration tools are used to modify the database
contents, since not all of these tools operate in Unicode resp. UTF-8 mode.
wxSQLite3 includes an optional extension for SQLite supporting key based
database file encryption using 128 bit AES encryption. Starting with version
1.9.6 of wxSQLite3 the encryption extension is compatible with the SQLite
amalgamation source. Experimental support for 256 bit AES encryption has been
added in version 1.9.8.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: libwxGTK-devel

Provides: %oname-devel = %version-%release
Obsoletes: %oname-devel = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

Provides: %oname-doc = %version-%release
Obsoletes: %oname-doc = %version-%release

%description doc
The %name-doc package contains html documentation
that use %name.

%prep
%setup

# delete bundled sqlite3 files
find -name sqlite3 -type d | xargs rm -rfv

# copy correct configure file and set permission
chmod a+x configure29 configure
cp configure29 configure
cp %SOURCE1 %name.pc.in

%build
%configure
%make_build

%install
%makeinstall_std

# move headers from %_includedir/wx to %_includedir/wx-?.?/wx
mkdir %buildroot%wxincdir
mv %buildroot%_includedir/wx %buildroot%wxincdir

find %buildroot -name '*.la' -exec rm -f {} ';'

# install own Debian-compatible pkgconfig file
mkdir -p %buildroot%_pkgconfigdir
sed -e "s!@VERSION@!%version!" \
	-e "s!@LIBDIR@!%_lib!" \
	-e "s!@WXVERSION@!%wxversion!g" \
%SOURCE1 > %buildroot%_pkgconfigdir/%oname-%wxversion.pc

%files
%doc LICENCE.txt Readme.txt
%_libdir/*.so.*

%files devel
%wxincdir/wx/*
%_pkgconfigdir/%oname-%wxversion.pc
%_libdir/*.so

%files doc
%doc docs/html

%changelog
* Sun Sep 29 2013 Vitaly Lipatov <lav@altlinux.ru> 3.0.5-alt2
- initial build to ALT Linux Sisyphus

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.5-alt1_1
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_2
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_1
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_1
- initial fc import

