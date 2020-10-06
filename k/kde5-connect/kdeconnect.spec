%define rname kdeconnect-kde

%define sover 1
%define libkdeconnectcore libkdeconnectcore%sover
%define libkdeconnectpluginkcm libkdeconnectpluginkcm%sover
%define libkdeconnectinterfaces libkdeconnectinterfaces%sover
%define libkdeconnectsmshelper libkdeconnectsmshelper%sover

Name: kde5-connect
Version: 20.08.1
Release: alt3
%K5init

Group: Communications
Summary: KDE Connect client for communication with smartphones
Url: http://www.kde.org
License: GPLv2+

Provides: %rname = %version
Provides: kde-connect = %version kdeconnect-kde = %version
Requires: libqt5-quickparticles
Requires: /usr/bin/sshfs qca-qt5-ossl
Requires: kf5-kirigami
# KF5PeopleVCard

Source: %rname-%version.tar
Patch1: alt-hide-menu-item.patch
Patch2: alt-kf5-requires.patch

Patch10: f183b5447bad47655c21af87214579f03bf3a163.diff
Patch11: b279c52101d3f7cc30a26086d58de0b5f1c547fa.diff
Patch12: d35b88c1b25fe13715f9170f18674d476ca9acdc.diff
Patch13: b496e66899e5bc9547b6537a7f44ab44dd0aaf38.diff
Patch14: 5310eae85dbdf92fba30375238a2481f2e34943e.diff
Patch15: 721ba9faafb79aac73973410ee1dd3624ded97a5.diff
Patch16: ae58b9dec49c809b85b5404cee17946116f8a706.diff
Patch17: 66c768aa9e7fba30b119c8b801efd49ed1270b0a.diff
Patch18: 85b691e40f525e22ca5cc4ebe79c361d71d7dc05.diff
Patch19: 48180b46552d40729a36b7431e97bbe2b5379306.diff


# Automatically added by buildreq on Fri Feb 05 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ gtk-update-icon-cache libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbusmenu-qt52 libgpg-error libjson-c libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libwayland-client libxcbutil-keysyms libxkbfile-devel pkg-config python-base python-modules python3 python3-base qt5-base-devel ruby ruby-stdlibs xorg-inputproto-devel xorg-kbproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kservice-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libfakekey-devel libqca-qt5-devel python-module-google qt5-declarative-devel qt5-x11extras-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-declarative-devel qt5-multimedia-devel qt5-x11extras-devel
BuildRequires: libfakekey-devel libqca-qt5-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel
BuildRequires: kf5-kservice-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel
BuildRequires: kf5-kdoctools-devel kf5-kirigami-devel kf5-kpeople-devel
# KF5PulseAudioQt

%description
KDE Connect adds communication between KDE and your smartphone.

Currently, you can pair with your Android devices over Wifi using the
KDE Connect app from Albert Vaka which you can obtain via Google Play, F-Droid
or the project website.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkdeconnectcore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkdeconnectcore
KF5 library

%package -n %libkdeconnectpluginkcm
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkdeconnectpluginkcm
KF5 library

%package -n %libkdeconnectinterfaces
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkdeconnectinterfaces
KF5 library

%package -n %libkdeconnectsmshelper
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkdeconnectsmshelper
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1

%build
%K5build \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    #

%install
%K5install
%K5install_move data plasma locale
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories5/*.*categories

%files
%_K5bin/kdeconnect-*
%_K5exec/kdeconnectd
%_K5start/org.kde.kdeconnect.*.desktop
%_K5xdgapp/org.kde.kdeconnect*.desktop
%_K5plug/kf5/*/*kdeconnect*.so
%_K5plug/*kdeconnect*.so
%_K5plug/kdeconnect/
%_K5qml/org/kde/kdeconnect/
%_K5dbus_srv/org.kde.kdeconnect.service
%_K5notif/kdeconnect.notifyrc
%_K5icon/hicolor/*/apps/*kdeconnect*.*
%_K5icon/hicolor/*/status/*ted.*
%_K5srv/*kdeconnect*.*
%_K5srvtyp/*kdeconnect*.*
%_K5data/plasma/plasmoids/org.kde.kdeconnect/
%_datadir/metainfo/*kdeconnect*.xml
%_datadir/zsh/site-functions/_kdeconnect

%files -n %libkdeconnectcore
%_K5lib/libkdeconnectcore.so.%sover
%_K5lib/libkdeconnectcore.so.*
%files -n %libkdeconnectpluginkcm
%_K5lib/libkdeconnectpluginkcm.so.%sover
%_K5lib/libkdeconnectpluginkcm.so.*
%files -n %libkdeconnectinterfaces
%_K5lib/libkdeconnectinterfaces.so.%sover
%_K5lib/libkdeconnectinterfaces.so.*
%files -n %libkdeconnectsmshelper
%_K5lib/libkdeconnectsmshelper.so.%sover
%_K5lib/libkdeconnectsmshelper.so.*

%changelog
* Tue Oct 06 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt3
- reduce KF5 requires

* Mon Oct 05 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt2
- security (fixes: CVE-2020-26164)

* Mon Oct 05 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 1.4-alt3
- hide inappropriate menu item (Closes: 38032)

* Mon Dec 23 2019 Sergey V Turchin <zerg@altlinux.org> 1.4-alt2
- fix requires

* Thu Dec 19 2019 Sergey V Turchin <zerg@altlinux.org> 1.4-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 1.3.5-alt1
- new version

* Tue Mar 26 2019 Sergey V Turchin <zerg@altlinux.org> 1.3.4-alt1
- new version

* Wed Feb 13 2019 Sergey V Turchin <zerg@altlinux.org> 1.3.3-alt1
- new version

* Thu Apr 12 2018 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- new version

* Wed Jan 24 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1
- new version

* Thu Jun 29 2017 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- new version

* Mon Aug 29 2016 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- new version

* Fri Feb 05 2016 Sergey V Turchin <zerg@altlinux.org> 0.9-alt1
- initial build
