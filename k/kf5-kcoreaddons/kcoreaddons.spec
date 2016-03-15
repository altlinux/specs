%define rname kcoreaddons

Name: kf5-%rname
Version: 5.20.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 Tier 1 addon with various classes on top of QtCore
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Dec 25 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt5-core libqt5-gui libqt5-test libqt5-widgets libqt5-xml libstdc++-devel python-base qt5-base-devel qt5-tools ruby ruby-stdlibs shared-mime-info
#BuildRequires: extra-cmake-modules gcc-c++ python-module-google qt5-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: gcc-c++ extra-cmake-modules qt5-base-devel qt5-tools-devel

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

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

%package -n libkf5coreaddons
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5coreaddons
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE4_DEFAULT_HOME=".kde4" \
    -D_KDE4_DEFAULT_HOME_POSTFIX=4 \
    #

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md
%_xdgmimedir/packages/kde5.xml

%files devel
%_K5bin/desktoptojson
%_K5inc/kcoreaddons_version.h
%_K5inc/KCoreAddons/
%_K5link/lib*.so
%_K5lib/cmake/KF5CoreAddons
%_K5archdata/mkspecs/modules/qt_KCoreAddons.pri

%files -n libkf5coreaddons
%_K5lib/libKF5CoreAddons.so.*

%changelog
* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.20.0-alt1
- new version

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
- test

* Fri Jan 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt0.1
- test

* Mon Dec 22 2014 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- initial build
