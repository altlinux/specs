%define rname plasma-activities-stats

%define sover 1
%define libplasmaactivitiesstats libplasmaactivitiesstats%sover

Name: plasma6-activities-stats
Version: 6.1.2
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE activity manager statistics
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: plasma6-activities-devel

%description
Library to access the usage statistics data collected by the KDE activity manager.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Conflicts: plasma5-workspace-common < 1:6
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libplasmaactivitiesstats
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Requires: plasma6-activities
%description -n %libplasmaactivitiesstats
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/PlasmaActivitiesStats/
%_K6link/lib*.so
%_K6lib/cmake/PlasmaActivitiesStats/
%_pkgconfigdir/PlasmaActivitiesStats.pc

%files -n %libplasmaactivitiesstats
%_K6lib/libPlasmaActivitiesStats.so.*
%_K6lib/libPlasmaActivitiesStats.so.%sover


%changelog
* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jul 03 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- initial build

