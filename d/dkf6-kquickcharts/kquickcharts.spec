%define rname kquickcharts

%define sover 1
%define libquickcharts libdquickcharts%sover
%define libquickchartscontrols libdquickchartscontrols%sover

Name: dkf6-%rname
Version: 6.28.0
Release: alt0.dde.1
%DK6init altplace

Group: System/Libraries
Summary: High-performance charts QtQuick module
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %name-%version.tar

# Automatically added by buildreq on Wed Dec 18 2019 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libglvnd-devel libqt6-core libqt6-gui libqt6-network libqt6-qml libqt6-quick libqt6-quickcontrols2 libqt6-quicktemplates2 libsasl2-3 libstdc++-devel perl python-modules python2-base python3 python3-base python3-dev qt6-base-devel qt6-declarative-devel rpm-build-python3 rpm-build-qml sh4
#BuildRequires: appstream ccmake extra-cmake-modules git-core libssl-devel python-modules-compiler python3-module-mpl_toolkits qt6-declarative-devel qt6-wayland-devel rpm-build-kf6
BuildRequires(pre): rpm-build-dkf6
BuildRequires: rpm-build-dqml6
BuildRequires: deepin-extra-cmake-modules dqt6-base-devel dqt6-declarative-devel dqt6-shadertools-devel dqt6-tools-devel
BuildRequires: vulkan-headers libdqt6-quick libdqt6-quickcontrols2 libdqt6-qmlcompiler
#BuildRequires: dqt6-wayland-devel

# find libraries
%add_findprov_lib_path %_DK6lib

%description
A QtQuick module providing high-performance charts.
The Quick Charts module provides a set of charts that can be used from QtQuick
applications. They are intended to be used for both simple display of data as
well as continuous display of high-volume data (often referred to as plotters).
The charts use a system called distance fields for their accelerated rendering,
which provides ways of using the GPU for rendering 2D shapes without loss of
quality.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
# Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libquickcharts
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libquickcharts
%name library

%package -n %libquickchartscontrols
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
Requires: libdqt6-qml = %_dqt6_version
%description -n %libquickchartscontrols
%name library

%prep
%setup -n %name-%version

%build
%DK6build

%install
%DK6install
%find_lang %name --all-name
%DK6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_DK6data/qlogging-categories6/*.*categories

%files
%_DK6qml/org/kde/quickcharts/

%files devel
%_DK6lib/cmake/KF6QuickCharts/
%_DK6link/lib*.so

%files -n %libquickcharts
%_DK6lib/libQuickCharts.so.%sover
%_DK6lib/libQuickCharts.so.*
%files -n %libquickchartscontrols
%_DK6lib/libQuickChartsControls.so.%sover
%_DK6lib/libQuickChartsControls.so.*


%changelog
* Thu Aug 13 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.0-alt0.dde.1
- fork for independent deepin build

* Tue Jul 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.28.0-alt1
- new version

* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.27.0-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.26.0-alt1
- new version

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt1
- new version

* Fri Mar 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.24.0-alt1
- new version

* Mon Feb 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.0-alt1
- new version

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.0-alt1
- new version

* Mon Dec 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.21.0-alt1
- new version

* Thu Nov 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt1
- new version

* Fri Oct 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.19.0-alt1
- new version

* Mon Sep 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.18.0-alt1
- new version

* Mon Aug 25 2025 Sergey V Turchin <zerg@altlinux.org> 6.17.0-alt1
- new version

* Mon Aug 04 2025 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt1
- new version

* Mon Jul 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.15.0-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.13.0-alt1
- new version

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.11.0-alt1
- new version

* Mon Jan 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1
- new version

* Mon Dec 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.9.0-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

