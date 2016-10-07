%def_disable openswan

Name: kde4-plasma-nm
Version: 0.9.3.6
Release: alt2

Group: Graphical desktop/KDE
Summary: Plasma applet written in QML for managing network connections
Url: https://projects.kde.org/projects/playground/network/plasma-nm
License: LGPLv2+ and GPLv2+

Requires: NetworkManager-daemon >= 0.9.8
Requires: NetworkManager-adsl NetworkManager-wifi

Source: plasma-nm-%version.tar
Source10: 01-plasma-nm.js

# Automatically added by buildreq on Wed Feb 19 2014 (-bi)
# optimized out: ModemManager-devel automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libmm-qt libnm-qt libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir ruby ruby-stdlibs xdg-utils xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: NetworkManager-devel gcc-c++ glib2-devel kde4libs-devel libicu50 libmm-qt-devel libnm-qt-devel libopenconnect-devel qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel libmm-qt-devel libnm-qt-devel libopenconnect-devel kde-common-devel
BuildRequires: pkgconfig(ModemManager) pkgconfig(NetworkManager) pkgconfig(libnm-glib) pkgconfig(libnm-util)

%description
Plasma applet and editor for managing your network connections in KDE 4 using
the default NetworkManager service.

%package maxi
Group: Graphical desktop/KDE
Summary: Mobile support for %name
BuildArch: noarch
Provides: plasma-applet-networkmanager
Obsoletes: plasma-applet-networkmanager
Requires: %name = %EVR
Requires: %name-connect-mobile
Requires: %name-connect-openvpn
Requires: %name-connect-vpnc
Requires: %name-connect-openconnect
Requires: %name-connect-openswan
Requires: %name-connect-strongswan
Requires: %name-connect-l2tp
Requires: %name-connect-pptp
%description maxi
%summary.

%package connect-mobile
Group: Graphical desktop/KDE
Summary: Mobile support for %name
Requires: %name = %EVR
Requires: ModemManager NetworkManager-bluetooth NetworkManager-wwan mobile-broadband-provider-info
%description connect-mobile
%summary.

%package connect-openvpn
Group: Graphical desktop/KDE
Summary: OpenVPN support for %name
Requires: %name = %EVR
Requires: NetworkManager-openvpn
%description connect-openvpn
%summary.

%package connect-vpnc
Group: Graphical desktop/KDE
Summary: Vpnc support for %name
Requires: %name = %EVR
Requires: NetworkManager-vpnc
%description connect-vpnc
%summary.

%package connect-openconnect
Group: Graphical desktop/KDE
Summary: OpenConnect support for %name
Requires: %name = %EVR
Requires: NetworkManager-openconnect
%description connect-openconnect
%summary.

%package connect-openswan
Group: Graphical desktop/KDE
Summary: Openswan support for %name
Requires: %name = %EVR
%if_enabled openswan
Requires: NetworkManager-openswan
%endif
%description connect-openswan
%summary.

%package connect-strongswan
Group: Graphical desktop/KDE
Summary: Strongswan support for %name
Requires: %name = %EVR
Requires: strongswan
%description connect-strongswan
%summary.

%package connect-l2tp
Group: Graphical desktop/KDE
Summary: L2TP support for %name
Requires: %name = %EVR
Requires: NetworkManager-l2tp
%description connect-l2tp
%summary.

%package connect-pptp
Group: Graphical desktop/KDE
Summary: PPTP support for %name
Requires: %name = %EVR
Requires: NetworkManager-pptp
%description connect-pptp
%summary.

%prep
%setup -n plasma-nm-%version

%build
%K4build


%install
%K4install

# migrate to nm plasmoid
install -m644 -p -D %SOURCE10 %buildroot/%_K4apps/plasma-desktop/updates/01-plasma-nm.js

%K4find_lang --with-kde --output=%name.lang plasma_applet_org.kde.networkmanagement
%K4find_lang --with-kde --append --output=%name.lang plasmanetworkmanagement-kded
%K4find_lang --with-kde --append --output=%name.lang kde-nm-connection-editor
%K4find_lang --with-kde --append --output=%name.lang libplasmanetworkmanagement-editor
%K4find_lang --with-kde plasmanetworkmanagement_vpncui
%K4find_lang --with-kde plasmanetworkmanagement_openvpnui
%K4find_lang --with-kde plasmanetworkmanagement_openconnectui
%K4find_lang --with-kde plasmanetworkmanagement_openswanui
%K4find_lang --with-kde plasmanetworkmanagement_strongswanui
%K4find_lang --with-kde plasmanetworkmanagement_l2tpui
%K4find_lang --with-kde plasmanetworkmanagement_pptpui


%files maxi

%files -f %name.lang
# kde-nm-connection-editor
%_K4bindir/kde-nm-connection-editor
%_K4libdir/libplasmanetworkmanagement-editor.so
%_K4apps/kde-nm-connection-editor/kde-nm-connection-editorui.rc
%_K4xdg_apps/kde-nm-connection-editor.desktop
# plasma-nm applet
%_K4lib/imports/org/kde/networkmanagement/
%dir %_K4apps/plasma/plasmoids/org.kde.networkmanagement/
%_K4apps/plasma/plasmoids/org.kde.networkmanagement/contents
%_K4apps/plasma/plasmoids/org.kde.networkmanagement/metadata.desktop
%_K4srv/plasma-applet-networkmanagement.desktop
%_K4lib/plugins/designer/plasmanetworkmanagementwidgets.so
%_K4apps/desktoptheme/default/icons/plasma-networkmanagement*.svgz
%_K4iconsdir/oxygen/*/*/*
%_K4apps/plasma-desktop/updates/*.js
# plasma-nm notifications
%_K4srv/networkmanagement_notifications.desktop
%_K4lib/networkmanagement_notifications.so
%_K4apps/networkmanagement/networkmanagement.notifyrc
# plasma-nm kded
%_K4lib/kded_networkmanagement.so
%_K4srv/kded/networkmanagement.desktop
# plasma-nm other
%_K4libdir/libplasmanetworkmanagement-internal.so
%_K4srvtyp/plasma-networkmanagement-vpnuiplugin.desktop

%files connect-mobile

%files connect-openvpn -f plasmanetworkmanagement_openvpnui.lang
%_K4lib/plasmanetworkmanagement_openvpnui.so
%_K4srv/plasmanetworkmanagement_openvpnui.desktop

%files connect-vpnc -f plasmanetworkmanagement_vpncui.lang
%_K4lib/plasmanetworkmanagement_vpncui.so
%_K4srv/plasmanetworkmanagement_vpncui.desktop

%files connect-openconnect -f plasmanetworkmanagement_openconnectui.lang
%_K4lib/plasmanetworkmanagement_openconnectui.so
%_K4srv/plasmanetworkmanagement_openconnectui.desktop

%files connect-openswan -f plasmanetworkmanagement_openswanui.lang
%_K4lib/plasmanetworkmanagement_openswanui.so
%_K4srv/plasmanetworkmanagement_openswanui.desktop

%files connect-strongswan -f plasmanetworkmanagement_strongswanui.lang
%_K4lib/plasmanetworkmanagement_strongswanui.so
%_K4srv/plasmanetworkmanagement_strongswanui.desktop

%files connect-l2tp -f plasmanetworkmanagement_l2tpui.lang
%_K4lib/plasmanetworkmanagement_l2tpui.so
%_K4srv/plasmanetworkmanagement_l2tpui.desktop

%files connect-pptp -f plasmanetworkmanagement_pptpui.lang
%_K4lib/plasmanetworkmanagement_pptpui.so
%_K4srv/plasmanetworkmanagement_pptpui.desktop

%changelog
* Mon Oct 10 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.3.6-alt2
- rebuild with new openconnect

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.3.6-alt1
- new version

* Wed Mar 25 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.3.5-alt1
- new version (ALT#30861)

* Tue Aug 26 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.3.4-alt1
- new version

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.3.3-alt7
- update requires

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.3.3-alt6
- rebuild with new NM

* Mon May 12 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.3.3-alt5
- rebuild with new libnm-qt

* Thu Mar 20 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.3.3-alt4
- fix maxi subpackage

* Wed Mar 19 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.3.3-alt3
- add maxi subpackage
- obsolete plasma-applet-networkmanager

* Tue Mar 18 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.3.3-alt2
- add fix for new openconnect

* Tue Mar 18 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.3.3-alt1
- new version

* Tue Mar 18 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.3.2-alt3
- rebuild

* Wed Feb 19 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.3.2-alt2
- add some upstream fixes

* Tue Feb 18 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.3.2-alt1
- initial build
