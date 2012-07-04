%define _kde_alternate_placement 1

Name: plasma-applet-networkmanager
Version: 0.9.0.3
Release: alt1
Serial: 1

Group: Graphical desktop/KDE
Summary: NetworkManager frontend for KDE4 and Plasma
License: GPLv2
Url: http://www.kde.org

Provides: kde4-knetworkmanager = %version-%release

Requires: NetworkManager >= 0.7
Requires: kde4base-workspace-core
Requires: mobile-broadband-provider-info

Source: %name-%version.tar
Source1: po-ru.tar
Source10: libknetworkmanager_ru.po
# SuSE
Patch3: build-fix.diff
# ALT
Patch101: knetworkmanager-0.9-alt-i18n-workaround.patch
Patch102: knetworkmanager-0.9-alt-no-autostart.patch
Patch103: knetworkmanager-0.9.0.2-alt-fix-linking.patch

BuildRequires: NetworkManager-glib-devel gcc-c++ kde4base-workspace-devel mobile-broadband-provider-info libopenconnect-devel libssl-devel

%description
This package provides the NetworkManager plasma applet which aims to provide a
fully featured GUI frontend to NetworkManager daemon v0.7 including support
for wired, wireless, GSM and VPN networks.  It is exclusively written for
Plasma and KDE4 and it is not supposed to work in other environments. The
package provides Plasma based interface to NetworkManager daemon and KDE4
Control Module (kcm) for changing NetworkManager settings.

This applet needs Plasma shell to be usable. Main KDE 4 Plasma shell is
available in the kdebase-workspace-bin package. The user friendly name of the
applet is "Networks" (in e.g. "Add Widgets" dialog).

%prep
%setup -q -a1
%patch3 -p0
%patch101 -p1
%patch102 -p1
%patch103 -p1

subst 's/^.*tests/#&/' CMakeLists.txt
if ! grep -qe 'add_subdirectory([[:space:]]*po[[:space:]]*)' CMakeLists.txt
then
cat >> CMakeLists.txt <<__EOF__
find_package(Msgfmt REQUIRED)
find_package(Gettext REQUIRED)
add_subdirectory( po )
__EOF__
fi

if ! [ -d po/ru ]; then
    mv po-ru po/ru
    #install -m 0644 %SOURCE10 po/ru/libknetworkmanager.po
    echo "add_subdirectory(ru)" >> po/CMakeLists.txt
fi


%build
%K4cmake -DDBUS_SYSTEM_POLICY_DIR=%_K4dbus_system
%K4make


%install
%K4install
%K4find_lang --output=%name.lang kcm_networkmanagement
%K4find_lang --output=%name.lang --append kded_knetworkmanager
%K4find_lang --output=%name.lang --append libknmui
%K4find_lang --output=%name.lang --append plasma_applet_networkmanagement
%K4find_lang --output=%name.lang --append networkmanagement_openvpnui
%K4find_lang --output=%name.lang --append networkmanagement_pptpui
%K4find_lang --output=%name.lang --append networkmanagement_vpncui
%K4find_lang --output=%name.lang --append knetworkmanager
%K4find_lang --output=%name.lang --append solidcontrolnm09


%files -f %name.lang
#%_sysconfdir/dbus-1/system.d/NetworkManager-kde4.conf
#%_kde4_bindir/knetworkmanager
%_K4libdir/lib*.so.*
%_K4libdir/libknm_nm.so
%_K4libdir/libsolidcontrolfuture.so
%_K4lib/*.so
%_K4exec/*
%_K4iconsdir/oxygen/*/devices/network-wire*-*.*
#%_kde4_iconsdir/hicolor/*/apps/knetworkmanager.*
%_K4iconsdir/oxygen/*/devices/network-defaultroute.*
#%_kde4_xdg_apps/knetworkmanager.desktop
%_K4apps/networkmanagement
%_K4apps/desktoptheme/default/icons/network2.svgz
%_K4srv/kded/*.desktop
%_K4srv/*.desktop
%_K4srv/solidbackends/solid_networkmanager*.desktop
%_K4srvtyp/*.desktop


%changelog
* Mon Jul 02 2012 Sergey V Turchin <zerg@altlinux.org> 1:0.9.0.3-alt1
- new version

* Thu May 31 2012 Sergey V Turchin <zerg@altlinux.org> 1:0.9.0.2-alt1
- new version

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt0.3
- update to git20111027

* Wed Oct 12 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt0.2
- update to git20110925

* Wed Jun 01 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt0.1
- udpate to git20110503

* Thu Apr 07 2011 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.20
- add patch from to fix handling of BSSID

* Fri Mar 25 2011 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.19
- rebuilt

* Fri Jan 14 2011 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.18
- require mobile-broadband-provider-info (ALT#24909)

* Mon Nov 22 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.17
- update to svn r1192577

* Mon Nov 22 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.16
- disable dbus menu (patch from SuSE)

* Tue Oct 12 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.15
- update russian translation

* Mon Sep 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.14
- update to svn r1161677

* Mon Aug 16 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.13
- update to svn r1128615

* Tue Jul 13 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.11.M51.1
- built for M51

* Tue Jul 13 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.12
- don't autostart by default

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.10.M51.1
- build for M51

* Thu Apr 08 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.11
- fix russian translation

* Tue Jan 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.10
- update to svn r1057339

* Mon Jan 11 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.8.M51.1
- built for M51

* Mon Jan 11 2010 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.9
- add some fixes from svn

* Wed Dec 02 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.7.M51.1
- built for M51

* Wed Dec 02 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.8
- update russian translation; thanks cas@alt

* Thu Nov 26 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.5.M51.2
- built for M51

* Thu Nov 26 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.7
- update russian translation
- translate hal info.product strings

* Wed Nov 25 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.5.M51.1
- built for M51

* Tue Nov 24 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.6
- update russian translation

* Mon Nov 23 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.5
- update russian translation

* Wed Nov 18 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.4.M51.1
- built for M51

* Wed Nov 18 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.5
- update russian translation; thanks cas@alt

* Wed Nov 18 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.4
- update russian translation; thanks cas@alt

* Fri Nov 06 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.2.M51.1
- built for M51

* Fri Nov 06 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.3
- update to svn r1043876

* Tue Sep 29 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.2.1028043
- update to svn r1028043

* Mon Sep 07 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt0.1.svn1017841
- svn r1017841

* Thu Aug 20 2009 Sergey V Turchin <zerg@altlinux.org> 0.1-alt9.svn1012598
- svn r1012598

* Thu Aug 13 2009 Sergey V Turchin <zerg@altlinux.org> 0.1-alt8.svn1010399
- svn r1010399

* Wed Aug 12 2009 Sergey V Turchin <zerg@altlinux.org> 0.1-alt7.svn1007025
- svn r1007025

* Thu Aug 06 2009 Sergey V Turchin <zerg@altlinux.org> 0.1-alt6.svn1004062
- svn r1004062

* Tue Jul 14 2009 Sergey V Turchin <zerg@altlinux.org> 0.1-alt5.svn977685
- svn r977685

* Tue May 12 2009 Sergey V Turchin <zerg@altlinux.org> 0.1-alt4.svn958040
- svn r958040
- add translations

* Thu Mar 12 2009 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt3.svn923695
- fix requires

* Mon Feb 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2.svn923695
- svn923695

* Thu Feb 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2.svn918249
- rebuild with kde 4.2.0 

* Thu Jan 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt1.svn918249
- initial release

