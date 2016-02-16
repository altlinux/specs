%define rname kpackage

Name: kf5-%rname
Version: 5.19.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 installing and loading packages of non binary content
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Feb 19 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libcloog-isl4 libgpg-error libqt5-core libqt5-test libqt5-xml libstdc++-devel python-base ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: kf5-karchive-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static

%description
The Package framework lets the user to install and load packages
of non binary content such as scripted extensions or graphic assets,
as they were traditional plugins.

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

%package -n libkf5package
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5package
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
%_K5inc/kpackage_version.h
%_K5inc/KPackage/
%_K5link/lib*.so
%_K5lib/cmake/KF5Package
#%_K5archdata/mkspecs/modules/qt_KPackage.pri

%files -n libkf5package
%_K5lib/libKF5Package.so.*
%_bindir/*5
%_K5bin/*
%_K5srvtyp/*.desktop

%changelog
* Tue Feb 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt1
- new version

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
- initial build
