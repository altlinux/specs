# TODO: rename package
%define oname autoscan-network
%define _subver	.bin

Name: AutoScan
Version: 1.50
Release: alt1.1

Summary: AutoScan - a utility for network exploration

License: GPL
Group: Networking/Other
Url: http://autoscan.fr/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://autoscan.fr/download_files/%oname-%version.tar
Patch: autoscan-network-1.10-ppc.patch
Patch1: autoscan-network-fixcurl.patch

# Automatically added by buildreq on Mon Oct 25 2010
BuildRequires: libao-devel libcurl-devel libelf-devel libgnomeui-devel libvorbis-devel libvte-devel libxml2-devel

BuildPreReq: libgnome-keyring-devel

%description
The objective of the program is to post the list of all equipment
connected to the network. A list of ports preset is scanned for each
equipment.

%prep
%setup -n %oname-%version
%patch -p1
%patch1 -p2

%build
%__subst "s|export GCONF|-export GCONF|" configure
./configure --distrib-fedora --without-daemon
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_docdir/%oname
rm -rf %buildroot%_menudir
mkdir -p %buildroot%_niconsdir
mv %buildroot%_iconsdir/%oname.png %buildroot%_niconsdir

%files
%doc AUTHORS copyright
%_bindir/*
#%_sbindir/*
%_datadir/apps/%oname/
%_datadir/sounds/%oname/
%_desktopdir/%oname.desktop
%_pixmapsdir/%oname/
%_niconsdir/%oname.png

%changelog
* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.50-alt1.1
- Rebuilt with curl 7.21.7

* Mon Oct 25 2010 Vitaly Lipatov <lav@altlinux.ru> 1.50-alt1
- new version 1.50 (with rpmrb script)
- update buildreqs

* Sun Nov 29 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.41-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for AutoScan
  * postclean-05-filetriggers for spec file

* Fri Feb 27 2009 Vitaly Lipatov <lav@altlinux.ru> 1.41-alt1
- new version 1.41 (with rpmrb script)
- fix build on PPC (thanks, Sergey Bolshakov)

* Mon Oct 29 2007 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt1
- new version 1.10 (with rpmrb script)
- cleanup spec, update buildreq, enable smp-build
- build without autoscan-agent (nessus, snmp support)

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 1.01-alt1
- new version 1.01 (with rpmrb script)

* Sat Mar 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.99-alt0.1
- new version 0.99
- remove using obsoletes gnome-config, gdk
- remove desktopdir; use pixmapsdir

* Thu Dec 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.97.2b-eter1alt0.1
- new version

* Mon Sep 19 2005 Vitaly Lipatov <lav@altlinux.ru> 0.97.2b-alt0.1
- first build for ALT Linux Sisyphus
- spec from PLD Team <feedback@pld-linux.org> (thanks)
