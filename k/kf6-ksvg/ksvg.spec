%define rname ksvg

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: SVG-based themes rendering library
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel
BuildRequires: kf6-karchive-devel kf6-kconfig-devel kf6-kcolorscheme-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kguiaddons-devel kf6-kirigami-devel

%description
A library for rendering SVG-based themes with stylesheet re-coloring and on-disk caching.

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

%package -n libkf6svg
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6svg
KF6 library


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

%files devel
%_K6inc/KSvg/
%_K6link/lib*.so
%_K6lib/cmake/KF6Svg

%files -n libkf6svg
%_K6qml/org/kde/ksvg/
%_K6lib/libKF6Svg.so.*


%changelog
* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon Jun 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- initial build

