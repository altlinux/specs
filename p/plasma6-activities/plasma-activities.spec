
%define sover 6
%define libplasmaactivities libplasmaactivities%sover

%define rname plasma-activities
Name: plasma6-activities
Version: 6.1.5
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE Activity core
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-base-devel qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: libxkbcommon-devel
BuildRequires: boost-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel

%description
Core components for the KDE Activity concept.

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

%package -n %libplasmaactivities
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libplasmaactivities
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data locale
%find_lang %name --all-name
%K6find_qtlang %name --append --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/*
%_K6qml/org/kde/activities/

%files devel
%_K6inc/PlasmaActivities/
%_K6link/lib*.so
%_K6lib/cmake/PlasmaActivities/
%_pkgconfigdir/PlasmaActivities.pc

%files -n %libplasmaactivities
%_K6lib/libPlasmaActivities.so.%sover
%_K6lib/libPlasmaActivities.so.*


%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- initial build
