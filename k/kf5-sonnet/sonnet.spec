%define rname sonnet

Name: kf5-%rname
Version: 5.18.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 multi-language spell checker
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-find-hunspell.patch

# Automatically added by buildreq on Fri Dec 26 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt5-core libqt5-gui libqt5-test libqt5-widgets libqt5-xml libstdc++-devel python-base qt5-base-devel qt5-tools ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ libhunspell-devel python-module-google qt5-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-tools-devel libhunspell-devel

%description
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins.

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5sonnetcore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5sonnetcore
KF5 library

%package -n libkf5sonnetui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5sonnetui
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md
%dir %_K5plug/kf5/sonnet/
%_K5data/sonnet/

%files devel
%_K5inc/sonnet_version.h
%_K5inc/Sonnet*/
%_K5link/lib*.so
%_K5lib/cmake/KF5Sonnet
%_K5archdata/mkspecs/modules/qt_Sonnet*.pri

%files -n libkf5sonnetcore
%_K5lib/libKF5SonnetCore.so.*
%_K5plug/kf5/sonnet/hunspell.so
%files -n libkf5sonnetui
%_K5lib/libKF5SonnetUi.so.*

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

* Fri Jan 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt0.1
- test

* Mon Dec 22 2014 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- initial build
