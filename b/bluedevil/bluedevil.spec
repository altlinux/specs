%define rname bluedevil

Name: %rname
Version: 6.1.5
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 bluetooth stack
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: bluez >= 5.0 obexd
Provides: plasma5-bluedevil = 1:%version-%release
Obsoletes: plasma5-bluedevil < 1:%version-%release

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-bluez-qt-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-kdeclarative-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-kdoctools-devel kf6-kcmutils-devel
BuildRequires: kf6-kded-devel kf6-kpackage-devel kf6-ksvg-devel kf6-kirigami-devel
BuildRequires: plasma6-lib-devel

%description
BlueDevil is the new bluetooth stack for KDE, it's composed of:
KCM, KDED, KIO, Library and some other small applications.

%prep
%setup -n %rname-%version


%build
%K6build \
    #

%install
%K6install
%K6install_move data locale bluedevilwizard remoteview kpackage

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/*
%_K6plug/plasma/kcms/systemsettings/*.so
%_K6plug/kf6/kded/*.so
%_K6plug/kf6/kio/*.so
%_K6qml/org/kde/plasma/private/bluetooth/
%_K6data/plasma/plasmoids/org.kde.plasma.bluetooth/
%_K6data/bluedevilwizard/
%_K6data/remoteview/bluetooth-network.desktop
%_K6xdgapp/*.desktop
%_K6notif/*.notifyrc
%_K6xdgmime/*.xml
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml



%changelog
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

