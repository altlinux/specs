%define rname plasma5support

%define sover 6
%define libplasma5support libplasma5support%sover
%define libplasma_geolocation_interface libplasma-geolocation-interface%sover
%define weather_ion_sover 7
%define libweather_ion libweather_ion%weather_ion_sover

Name: plasma6-%rname
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Migration aids for KF5 -> KF6 migration
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-freespace-thread-timer.patch
Patch2: alt-weather-fix-ua.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel libXfixes-devel
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-networkmanager-qt-devel
BuildRequires: kf6-knotifications-devel kf6-solid-devel kf6-kio-devel kf6-kidletime-devel
BuildRequires: kf6-kunitconversion-devel kf6-kholidays-devel
BuildRequires: plasma6-libksysguard-devel plasma6-activities-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Conflicts: plasma5-workspace-common < 1:6
Conflicts: plasma-workspace-common < 6.6
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
#Conflicts: plasma5-workspace-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libplasma5support
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libplasma5support
KF6 library

%package -n %libplasma_geolocation_interface
Epoch: 1
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %version-%release
%description -n %libplasma_geolocation_interface
KF6 library

%package -n %libweather_ion
Epoch: 1
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %version-%release
%description -n %libweather_ion
%name library

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

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

%files
%_K6plug/plasma5support/
%_K6qml/org/kde/plasma/plasma5support/
%_K6data/plasma5support/
%_K6data/plasma/weather_legacy/

%files devel
%_K6inc/?lasma5?upport/
%_K6inc/plasma/geolocation/
%_K6link/lib*.so
%_K6lib/cmake/Plasma5Support/

%files -n %libplasma5support
%_K6lib/libPlasma5Support.so.*
%_K6lib/libPlasma5Support.so.%sover
%files -n %libplasma_geolocation_interface
%_K6lib/libplasma-geolocation-interface.so.*
%_K6lib/libplasma-geolocation-interface.so.%sover
%files -n %libweather_ion
%_K6lib/libweather_ion.so.*
%_K6lib/libweather_ion.so.%weather_ion_sover

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

* Thu Sep 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt2
- add Epoch for libplasma-geolocation-interface to upgrade old one from plasma-workspace

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

* Wed Jul 03 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- initial build

