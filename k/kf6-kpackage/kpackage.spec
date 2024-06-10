%define rname kpackage

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 installing and loading packages of non binary content
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel
BuildRequires: kf6-karchive-devel kf6-kconfig-devel kf6-kcoreaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kdoctools-devel

%description
The Package framework lets the user to install and load packages
of non binary content such as scripted extensions or graphic assets,
as they were traditional plugins.

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

%package -n libkf6package
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6package
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
%_K6inc/KPackage/
%_K6link/lib*.so
%_K6lib/cmake/KF6Package

%files -n libkf6package
%_K6lib/libKF6Package.so.*
%_bindir/*6
%_K6bin/*


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

