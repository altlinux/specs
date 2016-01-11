%define rname kpty

Name: kf5-%rname
Version: 5.18.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 interfacing with pseudo terminal devices
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Feb 13 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt5-core libqt5-test libstdc++-devel python-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kcoreaddons-devel kf5-ki18n-devel libutempter-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ kf5-kcoreaddons-devel kf5-ki18n-devel libutempter-devel qt5-base-devel

%description
This library provides primitives to interface with pseudo terminal devices
as well as a KProcess derived class for running child processes and
communicating with them using a pty.

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

%package -n libkf5pty
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5pty
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md

%files devel
%_K5inc/kpty_version.h
%_K5inc/KPty/
%_K5link/lib*.so
%_K5lib/cmake/KF5Pty
%_K5archdata/mkspecs/modules/qt_KPty.pri

%files -n libkf5pty
%_K5lib/libKF5Pty.so.*

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

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- test

* Tue Feb 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt0.1
- initial build
