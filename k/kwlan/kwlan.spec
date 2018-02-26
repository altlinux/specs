%define _22iconsdir %_iconsdir/hicolor/22x22/apps
Summary: Network manager for kde
Name: kwlan
Version: 0.6.3
Release: alt3
License: GPL
Group: Networking/Other
Packager: Boris Savelev <boris@altlinux.org>
Url: http://sourceforge.net/projects/kwlan/
Source: %name-%version.tar.gz

# Automatically added by buildreq on Mon Sep 22 2008
BuildRequires: doxygen gcc-c++ gcc-fortran graphviz imake kdelibs-devel libXt-devel libjpeg-devel libwireless-devel qt3-designer qt3-doc-html xml-utils xorg-cf-files

%description
Allows you to configure different network profiles using all encryptions wpa_supplicant provides (wep, wpa, wpa2 etc) for wireless networks.
Since version 0.4.5 kwlan can connect to unencrypted networks if wpa_supplicant is not available.
Kwlan can also store profiles for wired networks.
Dialup networks can be edited and connected to as well.
Systray icons show connection statistics per interface (can be disabled).

%prep
%setup

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure
%make_build

%install
%K3install
%K3find_lang %name

%files -f %name.lang
%doc README NEWS ChangeLog AUTHORS COPYING
%_K3bindir/%name
/usr/share/kde/applications/%name.desktop
%_K3datadir/apps/%name/*
/usr/share/kde/icons/hicolor/*/*/*.png
/usr/share/kde/icons/hicolor/*/*/*/*.png

%changelog
* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.6.3-alt3
- Build for TDE 3.5.13 release

* Fri Mar 04 2011 Timur Aitov <timonbl4@altlinux.org> 0.6.3-alt2
- move to alternate place

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for kwlan
  * postclean-05-filetriggers for spec file

* Mon Sep 22 2008 Boris Savelev <boris@altlinux.org> 0.6.3-alt1
- initial build

