%define rname kirigami-addons

%define sover 6
%define libkirigamiaddonsstatefulapp libkirigamiaddonsstatefulapp%sover
%define libkirigamiapp libkirigamiapp%sover
%define libkirigamiaddonscomponents libkirigamiaddonscomponents%sover

Name: kf6-%rname
Version: 1.12.1
Release: alt1
%K6init

Group: System/Libraries
Summary: Set of widgets for Kirigami-based applications
Url:  https://invent.kde.org/libraries/kirigami-addons
License: GPL-2.0-or-later or LGPL-2.0-or-later

Requires: kde-common
# all
Requires: kf6-kirigami
# qmlmodels
Requires: libqt6-qmlmodels
# treeview
Requires: libkf6itemmodels
# kiconthemes
Requires: libkf6iconthemes

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-tools-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-ki18n-devel kf6-kconfig-devel kf6-kirigami-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kguiaddons-devel kf6-kcolorscheme-devel kf6-kcrash-devel kf6-kiconthemes-devel

%description
Set of "widgets" i.e visual end user components along with a code to support them.
Components are usable by both touch and desktop experiences providing a native experience on both,
and look native with any QQC2 style (qqc2-desktop-theme, Material or Plasma)

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name-common >= %EVR
%description devel
This package contains the development files for %name.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package -n %libkirigamiaddonsstatefulapp
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamiaddonsstatefulapp
%name library

%package -n %libkirigamiapp
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamiapp
%name library

%package -n %libkirigamiaddonscomponents
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamiaddonscomponents
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6qml/org/kde/kirigamiaddons/

%files devel
%_K6inc/KirigamiAddonsStatefulApp/
%_K6inc/KirigamiAddons/*/
%_libdir/cmake/KF6KirigamiAddons/
%_K6link/lib*.so
%_K6data/kdevappwizard/templates/*kirigamiaddons*

%files -n %libkirigamiaddonsstatefulapp
%_K6lib/libKirigamiAddonsStatefulApp.so.%sover
%_K6lib/libKirigamiAddonsStatefulApp.so.*

%files -n %libkirigamiapp
%_K6lib/libKirigamiApp.so.%sover
%_K6lib/libKirigamiApp.so.*

%files -n %libkirigamiaddonscomponents
%_K6lib/libKirigamiAddonsComponents.so.%sover
%_K6lib/libKirigamiAddonsComponents.so.*

%changelog
* Tue Jun 30 2026 Sergey V Turchin <zerg@altlinux.org> 1.12.1-alt1
- new version

* Mon Jan 12 2026 Sergey V Turchin <zerg@altlinux.org> 1.11.0-alt1
- new version

* Mon Dec 22 2025 Sergey V Turchin <zerg@altlinux.org> 1.10.0-alt1
- new version

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt1
- new version

* Mon Jun 30 2025 Sergey V Turchin <zerg@altlinux.org> 1.8.1-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt1
- new version

* Tue Dec 03 2024 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt1
- new version

* Mon Sep 23 2024 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt1
- new version

* Thu Jun 27 2024 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- initial build
