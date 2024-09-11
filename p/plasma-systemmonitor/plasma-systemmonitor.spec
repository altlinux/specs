%define rname plasma-systemmonitor

%define sover 6
%define libplasmasystemmonitorpage libplasmasystemmonitorpage%sover
%define libplasmasystemmonitortable libplasmasystemmonitortable%sover

Name: %rname
Version: 6.1.5
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
%_K6cfg/*systemmonitor*
%_K6data/knsrcfiles/*systemmonitor*
%_K6data/plasma/kinfocenter/externalmodules/*systemmonitor*.desktop
%_K6data/kglobalaccel/*systemmonitor*.desktop
%_datadir/metainfo/*.xml

%files -n %libplasmasystemmonitorpage
%_K6lib/libPlasmaSystemMonitorPage.so.%sover
%_K6lib/libPlasmaSystemMonitorPage.so.*
%files -n %libplasmasystemmonitortable
%_K6lib/libPlasmaSystemMonitorTable.so.%sover
%_K6lib/libPlasmaSystemMonitorTable.so.*

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

