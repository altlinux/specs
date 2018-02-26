Name: mrsync
Version: 20081028
Release: alt1.1.1

Summary: Transfers a bunch of files to multiple target simultaneously

License: GPL
Group: File tools
Url: http://sourceforge.net/projects/mrsync/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%{name}.%version.tar.bz2

%description
mrsync a tool to transfer files from master to many remote LAN machines
using Unix socket's multicast. It dynamically adjusts its speed of
transfering to ease on the network and to leave no one behind. 4 hours
for 140GB to 100 targets in 1Gbit LAN.

%prep
%setup -q -c %name
ln -sf Makefile.linux Makefile

%build
%make_build CC=gcc LIBS=

%install
mkdir -p %buildroot%_bindir
%make_install bindir=%buildroot%_bindir install

%files
%doc README
%_bindir/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20081028-alt1.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20081028-alt1.1
- Rebuilt with python 2.6

* Sat Nov 15 2008 Vitaly Lipatov <lav@altlinux.ru> 20081028-alt1
- new version 20081028 (with rpmrb script)

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 3.2.7-alt0.1
- new version 3.2.7 (with rpmrb script)
- remove libmrsync require :)

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt0.1
- initial build for ALT Linux Sisyphus

