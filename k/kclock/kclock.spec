%define rname kclock

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Clock
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf6-kirigami-addons
Requires: %name-common >= %EVR
Provides:  kde5-kclock = %EVR
Obsoletes: kde5-kclock < %EVR

Source: %rname-%version.tar
Patch1: alt-bindir.patch
Patch2: alt-clean-countries.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-wayland-devel
BuildRequires: qt6-multimedia-devel qt6-declarative-devel qt6-svg-devel
BuildRequires: kf6-kdbusaddons-devel kf6-ki18n-devel kf6-kirigami-devel kf6-knotifications-devel
BuildRequires: kf6-kpackage-devel kf6-kservice-devel kf6-kstatusnotifieritem-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kcrash-devel kf6-ksvg-devel kf6-kio-devel kf6-kjobwidgets-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: plasma-wayland-protocols
BuildRequires: plasma6-lib-devel

%description
A convergent clock application for Plasma.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-kclock-common = %EVR
Obsoletes: kde5-kclock-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common >= %EVR
Conflicts: kde5-kclock-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name


%files common -f %name.lang
%doc LICENSES/*

%files
%_K6bin/kclock*
%_K6plug/plasma/applets/*kclock*.so
%_K6start/*kclock*.desktop
%_K6data/krunner/dbusplugins/*kclock*.desktop
%_K6xdgapp/*kclock*.desktop
%_K6dbus_srv/*kclock*.service
%_K6icon/*/*/apps/*kclock*.*
%_K6data/plasma/plasmoids/org.kde.plasma.kclock*/
%_K6notif/*kclock*.notifyrc
%_datadir/metainfo/*.xml

%files devel
%_K6dbus_iface/org.kde.kclockd.*.xml



%changelog
* Mon Jun 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 13 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt2
- improve countries filter

* Tue Mar 10 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Wed Sep 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Mon Jun 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Thu May 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Wed Mar 19 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Feb 03 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

