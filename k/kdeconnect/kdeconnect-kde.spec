%define rname kdeconnect-kde

%define sover 24
%define libkdeconnectcore libkdeconnectcore%sover
%define libkdeconnectpluginkcm libkdeconnectpluginkcm%sover

%add_findreq_skiplist %_datadir/nautilus-python/extensions/*.py

Name: kdeconnect
Version: 24.08.1
Release: alt1
%K6init

Group: Communications
Summary: KDE Connect client for communication with smartphones
Url: http://www.kde.org
License: LGPL-2.1-or-later

Provides: kde5-connect = %EVR
Obsoletes: kde5-connect < %EVR
Provides: kde-connect = %version

Requires: libqt6-quickparticles
Requires: /usr/bin/sshfs qca-qt6-ossl
Requires: kf6-kirigami kf6-kirigami-addons
#Requires: kpeoplevcard

Source: %rname-%version.tar
Patch: alt-plasmoid-placement.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-declarative-devel qt6-multimedia-devel qt6-connectivity-devel
BuildRequires: qt6-declarative-devel qt6-wayland-devel
BuildRequires: extra-cmake-modules
BuildRequires: libdbus-devel
BuildRequires: libgio-devel libxkbcommon-devel
BuildRequires: pulseaudio-qt6-devel
BuildRequires: libfakekey-devel libqca-qt6-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel
BuildRequires: kf6-kservice-devel plasma6-kwayland-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kf6-kdoctools-devel kf6-kirigami-devel kf6-kpeople-devel kf6-qqc2-desktop-style-devel
BuildRequires: kf6-kpackage-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-modemmanager-qt-devel ModemManager-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: plasma-wayland-protocols

%description
KDE Connect adds communication between KDE and your smartphone.

Currently, you can pair with your Android devices over Wifi using the
KDE Connect app from Albert Vaka which you can obtain via Google Play, F-Droid
or the project website.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-connect-common = %EVR
Obsoletes: kde5-connect-common < %EVR
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
Summary: KF6 library
Requires: %name-common >= %EVR
Obsoletes: libkdeconnectcore23 < %EVR
Obsoletes: libkdeconnectinterfaces23 < %EVR
%description -n %libkdeconnectcore
KF6 library

%package -n %libkdeconnectpluginkcm
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
Obsoletes: libkdeconnectpluginkcm23 < %EVR
%description -n %libkdeconnectpluginkcm
KF6 library

%prep
%setup -n %rname-%version
#%patch -p1

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%K6build \
    -DLIBEXEC_INSTALL_DIR=%_K6exec \
    #

%install
%K6install
%K6install_move data plasma locale kdeconnect
for d in %buildroot/%_K6doc/* ; do
    [ -d $d/kdeconnect-kde -a ! -d $d/kdeconnect ] \
	&& cp -ar $d/kdeconnect-kde $d/kdeconnect \
	||:
done

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_K6icon/hicolor/*/status/*connect*.*
%_K6icon/hicolor/*/status/*trust*.*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/kdeconnect*
%_K6start/*kdeconnect*.desktop
%_K6xdgapp/*kdeconnect*.desktop
%_K6plug/kf6/*/*kdeconnect*.so
%_K6plug/plasma/kcms/systemsettings_qwidgets/*kdeconnect*.so
%_K6plug/kdeconnect/
%_K6qml/org/kde/kdeconnect/
%_K6dbus_srv/org.kde.kdeconnect.service
%_K6notif/kdeconnect.notifyrc
%_K6icon/hicolor/*/apps/*kdeconnect*.*
#%_K6srv/*kdeconnect*.*
%_K6data/plasma/plasmoids/org.kde.kdeconnect/
%_K6data/kdeconnect/
%_datadir/metainfo/*kdeconnect*.xml
%_datadir/zsh/site-functions/_kdeconnect
#
%_datadir/deepin/dde-file-manager/oem-menuextensions/*connect*.desktop
%_datadir/Thunar/sendto/kdeconnect-thunar.desktop
%_datadir/contractor/kdeconnect.contract
%_datadir/nautilus-python/extensions/kdeconnect-share.py

%files -n %libkdeconnectcore
%_K6lib/libkdeconnectcore.so.%sover
%_K6lib/libkdeconnectcore.so.*
%files -n %libkdeconnectpluginkcm
%_K6lib/libkdeconnectpluginkcm.so.%sover
%_K6lib/libkdeconnectpluginkcm.so.*

%changelog
* Thu Oct 03 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

