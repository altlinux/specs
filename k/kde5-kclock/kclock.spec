%define rname kclock

Name: kde5-%rname
Version: 23.08.3
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Clock
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf5-kirigami-addons
Requires: %name-common

Source: %rname-%version.tar
Patch1: alt-bindir.patch
Patch2: alt-clean-countries.patch

# Automatically added by buildreq on Fri Aug 27 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kconfig-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kjobwidgets-common kf5-kwidgetsaddons-common kf5-kwindowsystem-devel libctf-nobfd0 libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-sql libqt5-svg libqt5-test libqt5-texttospeech libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcbutil-keysyms python-modules python2-base python3 python3-base python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 rpm-build-qml rpm-macros-python sh4 tzdata
#BuildRequires: appstream extra-cmake-modules kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kservice-devel kf5-plasma-framework-devel python-modules-compiler python3-dev qt5-multimedia-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-translations qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: qt5-multimedia-devel qt5-quickcontrols2-devel qt5-svg-devel
BuildRequires: kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-knotifications-devel
BuildRequires: kf5-kpackage-devel kf5-kservice-devel kf5-plasma-framework-devel
BuildRequires: kf5-kirigami-addons-devel

%description
A convergent clock application for Plasma.

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
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5clock
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkf5clock
%name library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name


%files common -f %name.lang
%doc LICENSES/*

%files
%_K5bin/kclock*
%_K5plug/plasma/applets/*kclock*.so
%_K5start/*kclock*.desktop
%_K5xdgapp/*kclock*.desktop
%_K5dbus_srv/*kclock*.service
%_K5icon/*/*/apps/*kclock*.*
%_kf5_data/plasma/plasmoids/org.kde.plasma.kclock*/
%_K5notif/*kclock*.notifyrc
%_datadir/metainfo/*.xml

%files devel
%_K5dbus_iface/org.kde.kclockd.*.xml


%changelog
* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Thu Nov 09 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt2
- package metainfo

* Mon Oct 16 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Wed Jun 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Wed Apr 26 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.0-alt1
- new version

* Fri Feb 03 2023 Sergey V Turchin <zerg@altlinux.org> 23.01.0-alt1
- new version

* Mon Dec 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.11-alt1
- new version

* Wed Oct 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.09-alt1
- new version

* Tue Jul 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.06-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 22.04-alt1
- new version

* Mon Feb 14 2022 Sergey V Turchin <zerg@altlinux.org> 22.02-alt1
- new version

* Fri Dec 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.12-alt1
- new version

* Wed Sep 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08-alt1
- new version

* Mon Sep 06 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt2
- fix kclockd start service
- fix requires

* Wed Aug 18 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt1
- initial build
