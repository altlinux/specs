%define rname modemmanager-qt

Name: kf5-%rname
Version: 5.18.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Workspace 5 wrapper for ModemManager DBus API
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Feb 26 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt5-core libqt5-dbus libqt5-xml libstdc++-devel pkg-config python-base ruby ruby-stdlibs
#BuildRequires: ModemManager-devel extra-cmake-modules gcc-c++ python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: ModemManager-devel extra-cmake-modules gcc-c++ qt5-base-devel

%description
Qt wrapper for ModemManager DBus API

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
Provides: kf5-libmm-qt-devel = %version-%release
Obsoletes: kf5-libmm-qt-devel < %version-%release
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5modemmanagerqt
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5modemmanagerqt
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

%files devel
%_K5inc/modemmanagerqt_version.h
%_K5inc/ModemManagerQt/
%_K5link/lib*.so
%_K5lib/cmake/KF5ModemManagerQt
%_K5archdata/mkspecs/modules/qt_ModemManagerQt.pri

%files -n libkf5modemmanagerqt
%_K5lib/libKF5ModemManagerQt.so.*

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

* Wed Aug 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Mon May 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt2
- fix provides

* Wed Apr 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- initial build
