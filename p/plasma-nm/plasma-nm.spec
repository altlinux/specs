%define rname plasma-nm
%def_enable libreswan

%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: %rname
Version: 6.7.2
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 Plasma applet written in QML for managing network connections
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: NetworkManager-daemon
Requires: NetworkManager-adsl NetworkManager-wifi
Requires: mobile-broadband-provider-info
Requires: qca-qt6-ossl
# prison qml
Requires: libkf6prison
Requires: qml6(org.kde.quickcharts.controls)
Requires: kf6-kirigami
Requires: qml6(org.kde.kirigamiaddons.formcard)
#Requires: wireguard-tools

Provides: plasma5-nm = 1:%version-%release
Obsoletes: plasma5-nm < 1:%version-%release

Source: %rname-%version.tar
# ALT
Patch11: alt-old-openconnectauth.patch
Patch12: alt-def-allow-all.patch
Patch13: alt-is-live.patch
Patch14: alt-revert.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-tools-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel qt6-webchannel-devel
%endif
BuildRequires: libcups-devel
BuildRequires: libvulkan-devel
BuildRequires: mobile-broadband-provider-info libqca-qt6-devel qcoro6-devel libqtkeychain-qt6-devel
BuildRequires: ModemManager-devel libopenconnect-devel
BuildRequires: libnm-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdeclarative-devel kf6-kirigami-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kpackage-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-prison-devel kf6-ksvg-devel
BuildRequires: kf6-modemmanager-qt-devel kf6-networkmanager-qt-devel kf6-kcmutils-devel
BuildRequires: qml6(org.kde.kirigamiaddons.formcard) kf6-kirigami-addons-devel
BuildRequires: plasma6-lib-devel

%description
Plasma applet and editor for managing your network connections in KDE using
the default NetworkManager service.

%package maxi
Group: Graphical desktop/KDE
Summary: %name maximum package
#BuildArch: noarch
Requires: %name
Requires: %name-connect-mobile
Requires: %name-connect-openvpn
Requires: %name-connect-fortisslvpn
Requires: %name-connect-vpnc
%if_enabled qtwebengine
Requires: %name-connect-openconnect
%endif
Requires: %name-connect-libreswan
Requires: %name-connect-strongswan
Requires: %name-connect-iodine
Requires: %name-connect-l2tp
Requires: %name-connect-pptp
Requires: %name-connect-sstp
Requires: %name-connect-ssh
Provides: plasma5-nm-maxi = 1:%version-%release
Obsoletes: plasma5-nm-maxi < 1:%version-%release
%description maxi
%summary.

%package connect-mobile
Group: Graphical desktop/KDE
Summary: Mobile support for %name
#BuildArch: noarch
Requires: %name
Requires: ModemManager NetworkManager-bluetooth NetworkManager-wwan mobile-broadband-provider-info
Provides: plasma5-nm-connect-mobile = 1:%version-%release
Obsoletes: plasma5-nm-connect-mobile < 1:%version-%release
%description connect-mobile
%summary.

%package connect-openvpn
Group: Graphical desktop/KDE
Summary: OpenVPN support for %name
Requires: %name
Requires: NetworkManager-openvpn
Provides: plasma5-nm-connect-openvpn = 1:%version-%release
Obsoletes: plasma5-nm-connect-openvpn < 1:%version-%release
%description connect-openvpn
%summary.

%package connect-fortisslvpn
Group: Graphical desktop/KDE
Summary: Fortinet SSLVPN support for %name
Requires: %name
Requires: NetworkManager-fortisslvpn
Provides: plasma5-nm-connect-fortisslvpn = 1:%version-%release
Obsoletes: plasma5-nm-connect-fortisslvpn < 1:%version-%release
%description connect-fortisslvpn
%summary.

%package connect-vpnc
Group: Graphical desktop/KDE
Summary: Vpnc support for %name
Requires: %name
Requires: NetworkManager-vpnc
Provides: plasma5-nm-connect-vpnc = 1:%version-%release
Obsoletes: plasma5-nm-connect-vpnc < 1:%version-%release
%description connect-vpnc
%summary.

%package connect-openconnect
Group: Graphical desktop/KDE
Summary: OpenConnect support for %name
Requires: %name
Requires: NetworkManager-openconnect
Provides: plasma5-nm-connect-openconnect = 1:%version-%release
Obsoletes: plasma5-nm-connect-openconnect < 1:%version-%release
%description connect-openconnect
%summary.

%package connect-iodine
Group: Graphical desktop/KDE
Summary: Iodine DNS tunnel support for %name
Requires: %name
Requires: NetworkManager-iodine
Provides: plasma5-nm-connect-iodine = 1:%version-%release
Obsoletes: plasma5-nm-connect-iodine < 1:%version-%release
%description connect-iodine
%summary.

%package connect-libreswan
Group: Graphical desktop/KDE
Summary: Openswan support for %name
Requires: %name
%if_enabled libreswan
Requires: NetworkManager-libreswan
%endif
Provides: plasma5-nm-connect-libreswan = 1:%version-%release
Obsoletes: plasma5-nm-connect-libreswan < 1:%version-%release
%description connect-libreswan
%summary.

%package connect-strongswan
Group: Graphical desktop/KDE
Summary: Strongswan support for %name
Requires: %name
Requires: NetworkManager-strongswan
Provides: plasma5-nm-connect-strongswan = 1:%version-%release
Obsoletes: plasma5-nm-connect-strongswan < 1:%version-%release
%description connect-strongswan
%summary.

%package connect-l2tp
Group: Graphical desktop/KDE
Summary: L2TP support for %name
Requires: %name
Requires: NetworkManager-l2tp
Provides: plasma5-nm-connect-l2tp = 1:%version-%release
Obsoletes: plasma5-nm-connect-l2tp < 1:%version-%release
%description connect-l2tp
%summary.

%package connect-pptp
Group: Graphical desktop/KDE
Summary: PPTP support for %name
Requires: %name
Requires: NetworkManager-pptp
Provides: plasma5-nm-connect-pptp = 1:%version-%release
Obsoletes: plasma5-nm-connect-pptp < 1:%version-%release
%description connect-pptp
%summary.

%package connect-sstp
Group: Graphical desktop/KDE
Summary: SSTP support for %name
Requires: %name
Requires: NetworkManager-sstp
Provides: plasma5-nm-connect-sstp = 1:%version-%release
Obsoletes: plasma5-nm-connect-sstp < 1:%version-%release
%description connect-sstp
%summary.

%package connect-ssh
Group: Graphical desktop/KDE
Summary: SSH support for %name
Requires: %name
Requires: ssh-provider-openssh-clients NetworkManager-ssh
Provides: plasma5-nm-connect-ssh = 1:%version-%release
Obsoletes: plasma5-nm-connect-ssh < 1:%version-%release
%description connect-ssh
%summary.

%prep
%setup -n %rname-%version
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

%build
%K6build \
    -DBUILD_OPENCONNECT:BOOL=%{?_enable_qtwebengine:ON}%{!?_enable_qtwebengine:OFF} \
    #

%install
%K6install
%K6install_move data kcm_networkmanagement

%find_lang %name --all-name

%files -f %name.lang
%dir %_K6plug/plasma/network/
%dir %_K6plug/plasma/network/vpn/
%doc LICENSES/*
%_K6lib/libplasmanm_*.so
%_K6plug/kf6/kded/networkmanagement.so
%_K6plug/plasma/applets/*networkmanagement*.so
%_K6plug/plasma/kcms/systemsettings_qwidgets/*networkmanagement*.so
%_K6qml/org/kde/plasma/networkmanagement/
%_K6xdgapp/*networkmanagement*.desktop
%_K6xdgapp/*vpnimport*.desktop
%_K6data/*networkmanagement/
%_K6notif/networkmanagement.notifyrc
%_datadir/qlogging-categories6/*.*categories
#%_datadir/metainfo/*.xml

%files maxi
%files connect-mobile
%_K6plug/plasma/kcms/systemsettings/*cellular*.so
%_K6plug/plasma/kcms/systemsettings/*mobile*.so
%_K6xdgapp/*cellular*.desktop
%_K6xdgapp/*mobile*.desktop

%files connect-iodine
%_K6plug/plasma/network/vpn/plasmanetworkmanagement_iodineui.so
%files connect-openvpn
%_K6plug/plasma/network/vpn/plasmanetworkmanagement_openvpnui.so
%files connect-fortisslvpn
%_K6plug/plasma/network/vpn/plasmanetworkmanagement_fortisslvpnui.so
%files connect-vpnc
%_K6plug/plasma/network/vpn/plasmanetworkmanagement_vpncui.so
%if_enabled qtwebengine
%files connect-openconnect
%_K6plug/plasma/network/vpn/plasmanetworkmanagement_openconnect_*.so
%endif
%files connect-libreswan
%_K6plug/plasma/network/vpn/plasmanetworkmanagement_libreswanui.so
%files connect-strongswan
%_K6plug/plasma/network/vpn/plasmanetworkmanagement_strongswanui.so
%files connect-l2tp
%_K6plug/plasma/network/vpn/plasmanetworkmanagement_l2tpui.so
%files connect-pptp
%_K6plug/plasma/network/vpn/plasmanetworkmanagement_pptpui.so
%files connect-sstp
%_K6plug/plasma/network/vpn/plasmanetworkmanagement_sstpui.so
%files connect-ssh
%_K6plug/plasma/network/vpn/plasmanetworkmanagement_sshui.so

%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Thu Oct 30 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt3
- add patch against kdebug#461055

* Wed Oct 29 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt2
- create system connections by default

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Tue Sep 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt2
- fix detect livecd

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt2
- fix requires

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Fri Nov 22 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt2
- require NetworkManager-libreswan for libreswan module

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

