%define rname kwindowsystem

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 Access to the windowing system
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel
BuildRequires: libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel
BuildRequires: libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel
BuildRequires: libxcb-devel libxcbutil-keysyms-devel libxcbutil-icccm-devel
BuildRequires: extra-cmake-modules qt6-base-devel qt6-tools-devel qt6-declarative-devel
BuildRequires: qt6-wayland-devel plasma-wayland-protocols

%description
Convenience access to certain properties and features of the windowing system.

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

%package -n libkf6windowsystem
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6windowsystem
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
%_K6inc/KWindowSystem/
%_K6link/lib*.so
%_K6lib/cmake/KF6WindowSystem
%_pkgconfigdir/KF6WindowSystem.pc

%files -n libkf6windowsystem
%_K6lib/libKF6WindowSystem.so.*
%_K6plug/kf6/kwindowsystem/
%_K6qml/org/kde/kwindowsystem/


%changelog
* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Wed Jul 17 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt2
- package qml with library

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

