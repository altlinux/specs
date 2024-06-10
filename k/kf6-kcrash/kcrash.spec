%define rname kcrash

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 support for intercepting and handling application crashes
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar
Patch: alt-catch-sigterm.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel kf6-kcoreaddons-devel kf6-kwindowsystem-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel
BuildRequires: libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libxkbfile-devel

%description
KCrash provides support for intercepting and handling application crashes.

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

%package -n libkf6crash
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6crash
KF6 library


%prep
%setup -n %rname-%version
%patch -p2

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
#%_K6inc/kcrash_version.h
%_K6inc/KCrash/
%_K6link/lib*.so
%_K6lib/cmake/KF6Crash

%files -n libkf6crash
%_K6lib/libKF6Crash.so.*


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

