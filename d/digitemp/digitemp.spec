Name: digitemp
Version: 3.6.0
Release: alt1.2.1
License: GPL
Group: Monitoring
Source: digitemp.tar
Patch: digitemp-alt-misc_fixes.patch
URL: http://www.digitemp.com
Packager: Denis Klimov <zver@altlinux.ru>
Summary: DigiTemp, a one-wire LAN temperature sensor reader
BuildRequires: libusb-compat-devel perl-DBI perl-GD2 perl-libnet rrd-perl perl-CGI

%description
DigiTemp is a console application for reading Dallas Semiconductor 1-wire
network temperature sensors. It supports the DS18S20, DS18B20, DS1822.
This version requires a DS2490 USB to 1-wire adapter.

It includes perl scripts for logging using RRDB and MySQL, as well as a 
NetSaint/Nagios plugin and graph generating scripts using RRDB.

%package ds2490
Summary: Digitemp for the DS2490 1-wire adapter
Group: Monitoring
%description ds2490
Digitemp for the DS2490 1-wire adapter

%package ds9097
Summary: Digitemp for the DS9097 1-wire adapter
Group: Monitoring
%description ds9097
Digitemp for the DS9097 1-wire adapter

%package ds9097u
Summary: Digitemp for the DS9097U 1-wire adapter
Group: Monitoring
%description ds9097u
Digitemp for the DS9097U 1-wire adapter

%package doc
Summary: Digitemp documentation
Group: Documentation
%description doc
Digitemp documentation

%package utils
Summary: Perl and python scripts for logging using RRDB and MySQL
Group: Monitoring
%description utils
Perl and python scripts for logging using RRDB and MySQL

%package full
Summary: All subpackages digitemp
Group: Monitoring
Requires: %name-ds2490 = %version-%release 
Requires: %name-ds9097 = %version-%release
Requires: %name-ds9097u = %version-%release
Requires: %name-doc = %version-%release
Requires: %name-utils = %version-%release
%description full
Virtual package. It's digitemp subpackages:
%name-ds2490
%name-ds9097
%name-ds9097u
%name-doc
%name-utils

%prep
%setup -n %name
%patch -p2

sed -i 's|^\(CC.*\)|\1 -g|' Makefile

%build
%make_build ds2490
%make_build ds9097
%make_build ds9097u

%install
install -D -m 2755 digitemp_DS2490 %buildroot%_bindir/digitemp_DS2490
install -D -m 2755 digitemp_DS9097 %buildroot%_bindir/digitemp_DS9097
install -D -m 2755 digitemp_DS9097U %buildroot%_bindir/digitemp_DS9097U
install -D -m 644 digitemp.1 %buildroot/%_man1dir/digitemp.1

install -D -d %buildroot%_datadir/%name
cp -R perl %buildroot%_datadir/%name
cp -R python %buildroot%_datadir/%name
cp -R rrdb %buildroot%_datadir/%name

%files full

%files doc
%doc COPYRIGHT COPYING FAQ README ChangeLog CREDITS TODO
%_man1dir/*

%files ds2490
%_bindir/digitemp_DS2490

%files ds9097
%_bindir/digitemp_DS9097

%files ds9097u
%_bindir/digitemp_DS9097U

%files utils
%_datadir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt1.2.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1.2
- Rebuilt for debuginfo

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1.1
- Rebuilt with python 2.6

* Fri May 08 2009 Slava Semushin <php-coder@altlinux.ru> 3.6.0-alt1
- NMU
- Updated to 3.6.0

* Tue Nov 20 2007 Denis Klimov <zver@altlinux.ru> 3.5.0-alt4
- fix invalid syntax in python/gui/dttest.py

* Mon Aug 13 2007 Denis Klimov <zver@altlinux.ru> 3.5.0-alt3
- add shield for macros in changelog

* Thu May 24 2007 Denis Klimov <zver@altlinux.ru> 3.5.0-alt2
- add %%make_build
- change %description for digitemp-full
- %%_datadir/%%name/* change to %%_datadir/%name

* Tue May 15 2007 Denis Klimov <zver@altlinux.ru> 3.5.0-alt1
- Initial build for Sisyphus

