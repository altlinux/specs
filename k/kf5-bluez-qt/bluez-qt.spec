%define rname bluez-qt

Name: kf5-%rname
Version: 5.18.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 wrapper for Bluez DBus API
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Apr 28 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quicktest libqt5-test libqt5-widgets libstdc++-devel python-base qt5-base-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-declarative-devel

%description
Library for communication with Bluez system and session daemons.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5bluezqt
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5bluezqt
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md
/lib/udev/rules.d/*-kde-bluetooth-*.rules

%files devel
%_K5inc/bluezqt_version.h
%_K5inc/BluezQt/
%_K5link/lib*.so
%_K5lib/cmake/KF5BluezQt
%_K5archdata/mkspecs/modules/qt_BluezQt.pri

%files -n libkf5bluezqt
%_K5lib/libKF5BluezQt.so.*
%_K5qml/org/kde/bluezqt/

%changelog
* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- new version

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- new version

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Mon Sep 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- new version

* Fri Aug 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- initial build
