%define rname attica

Name: kf5-%rname
Version: 5.18.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 Open Collaboration Services API
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Feb 17 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt5-core libqt5-network libstdc++-devel pkg-config python-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel

%description
Attica is a Qt library that implements the Open Collaboration Services API.
It grants easy access to the services such as querying information about persons and contents.
The library is used in KNewStuff3 as content provider.

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

%package -n libkf5attica
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5attica
KF5 library


%prep
%setup -n %rname-%version
find ./ -type f -and \( -name \*.cmake -or -name \*.h \) | \
while read f ; do
    sed -i 's|CMAKE_LIBATTICA_VERSION_|ATTICA_VERSION_|g' $f
done

%build
%K5build

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING README.md

%files devel
%_K5inc/attica_version.h
%_K5inc/Attica/
%_K5link/lib*.so
%_K5lib/cmake/KF5Attica
%_K5archdata/mkspecs/modules/qt_Attica.pri
%_pkgconfigdir/*.pc

%files -n libkf5attica
%_K5lib/libKF5Attica.so.*

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
- initial build
