%define rname bluez-qt

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 wrapper for Bluez DBus API
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Apr 28 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-qml libqt6-quicktest libqt6-test libqt6-widgets libstdc++-devel python-base qt6-base-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt6-declarative-devel

%description
Library for communication with Bluez system and session daemons.

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

%package -n libkf6bluezqt
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6bluezqt
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
#%_udevrulesdir/*-kde-bluetooth-*.rules

%files devel
%_pkgconfigdir/KF6BluezQt.pc
%_K6inc/BluezQt/
%_K6link/lib*.so
%_K6lib/cmake/KF6BluezQt

%files -n libkf6bluezqt
%_K6lib/libKF6BluezQt.so.*
%_K6qml/org/kde/bluezqt/


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

