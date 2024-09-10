%define rname kquickcharts

%define sover 1
%define libquickcharts libquickcharts%sover
%define libquickchartscontrols libquickchartscontrols%sover

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: High-performance charts QtQuick module
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Dec 18 2019 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libglvnd-devel libqt6-core libqt6-gui libqt6-network libqt6-qml libqt6-quick libqt6-quickcontrols2 libqt6-quicktemplates2 libsasl2-3 libstdc++-devel perl python-modules python2-base python3 python3-base python3-dev qt6-base-devel qt6-declarative-devel rpm-build-python3 rpm-build-qml sh4
#BuildRequires: appstream ccmake extra-cmake-modules git-core libssl-devel python-modules-compiler python3-module-mpl_toolkits qt6-declarative-devel qt6-wayland-devel rpm-build-kf6
BuildRequires(pre): rpm-build-kf6
BuildRequires: rpm-build-qml
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-shadertools-devel
#BuildRequires: qt6-wayland-devel

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
Requires: kde-common
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
%description -n %libquickchartscontrols
%name library

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files
%_K6qml/org/kde/quickcharts/

%files devel
%_K6lib/cmake/KF6QuickCharts/
%_K6link/lib*.so

%files -n %libquickcharts
%_K6lib/libQuickCharts.so.%sover
%_K6lib/libQuickCharts.so.*
%files -n %libquickchartscontrols
%_K6lib/libQuickChartsControls.so.%sover
%_K6lib/libQuickChartsControls.so.*


%changelog
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

