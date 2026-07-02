%define rname plasma-systemmonitor

%define sover 6
%define libplasmasystemmonitorpage libplasmasystemmonitorpage%sover
%define libplasmasystemmonitortable libplasmasystemmonitortable%sover

Name: %rname
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma 5 system resources monitor
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: lm_sensors qt6-declarative plasma6-libksysguard ksystemstats
Provides: plasma5-systemmonitor = %EVR
Obsoletes: plasma5-systemmonitor < %EVR

Source: %rname-%version.tar
Patch1: alt-uid-1000.patch
Patch2: alt-soname.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: rpm-build-python3
BuildRequires: qt6-base-devel qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: plasma6-libksysguard-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kdbusaddons-devel kf6-kdeclarative-devel kf6-kglobalaccel-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-kirigami-devel kf6-kitemmodels-devel kf6-knewstuff-devel kf6-kpackage-devel

%description
%name provides an interface for monitoring system sensors,
process information and other system resources. It is built on top of the faces
system also used to provide widgets for plasma-desktop and makes use of the
ksystemstats daemon to provide sensor information. It allows extensive
customisation of pages, so it can be made to show exactly which data people
want to see.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libplasmasystemmonitorpage
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libplasmasystemmonitorpage
%name library

%package -n %libplasmasystemmonitortable
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libplasmasystemmonitortable
%name library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
sed -i "s|@PROJECT_VERSION@|%version|" src/page/CMakeLists.txt src/table/CMakeLists.txt
sed -i "s|@PROJECT_VERSION_MAJOR@|%sover|" src/page/CMakeLists.txt src/table/CMakeLists.txt

%build
%K6build

%install
%K6install
%K6install_move data ksysguard plasma-systemmonitor knsrcfiles plasma
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6bin/plasma-systemmonitor
%_K6qml/org/kde/ksysguard/*
%_K6data/ksysguard/
%_K6data/plasma-systemmonitor/
%_K6xdgapp/*systemmonitor*.desktop
#%_K6cfg/*systemmonitor*
%_K6data/knsrcfiles/*systemmonitor*
%_K6data/plasma/kinfocenter/externalmodules/*systemmonitor*.desktop
%_K6data/kglobalaccel/*systemmonitor*.desktop
%_K6conf_up/plasma-systemmonitor*
%_datadir/metainfo/*.xml

%files -n %libplasmasystemmonitorpage
%_K6lib/libPlasmaSystemMonitorPage.so.%sover
%_K6lib/libPlasmaSystemMonitorPage.so.*
%files -n %libplasmasystemmonitortable
%_K6lib/libPlasmaSystemMonitorTable.so.%sover
%_K6lib/libPlasmaSystemMonitorTable.so.*

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

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

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

