%define rname modemmanager-qt

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 wrapper for ModemManager DBus API
Url: http://www.kde.org
License: LGPL-2.1-only OR LGPL-3.0-only

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: ModemManager-devel extra-cmake-modules qt6-base-devel

%description
Qt wrapper for ModemManager DBus API

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
Requires: ModemManager-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6modemmanagerqt
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6modemmanagerqt
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
#%_K6inc/modemmanagerqt_version.h
%_K6inc/ModemManagerQt/
%_K6link/lib*.so
%_K6lib/cmake/KF6ModemManagerQt

%files -n libkf6modemmanagerqt
%_K6lib/libKF6ModemManagerQt.so.*


%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

