%define rname prison

Name: kf5-%rname
Version: 5.42.0
Release: alt2%ubt
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5  barcode abstraction layer
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Feb 13 2017 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libqt5-core libqt5-gui libstdc++-devel perl python-base python-modules python3 python3-base rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules libdmtx-devel libqrencode-devel python-module-google python3-dev qt5-base-devel rpm-build-kf5 rpm-build-ruby selinux-policy
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: libdmtx-devel libqrencode-devel

%description
A barcode abstraction layer providing uniform access to generation of barcodes with data.

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

%package -n libkf5prison
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5prison
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
%doc LICENSE README.md
%config(noreplace) %_K5xdgconf/*.*categories

%files devel
%_K5inc/prison_version.h
%_K5inc/?rison/
%_K5link/lib*.so
%_K5lib/cmake/KF5Prison
%_K5archdata/mkspecs/modules/qt_Prison.pri
#%_pkgconfigdir/*.pc

%files -n libkf5prison
%_K5lib/libKF5Prison.so.*

%changelog
* Mon Jan 22 2018 Sergey V Turchin <zerg@altlinux.org> 5.42.0-alt2%ubt
- package categories config

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 5.42.0-alt1%ubt
- new version

* Tue Dec 12 2017 Sergey V Turchin <zerg@altlinux.org> 5.41.0-alt1%ubt
- new version

* Tue Nov 21 2017 Sergey V Turchin <zerg@altlinux.org> 5.40.0-alt1%ubt
- new version

* Tue Oct 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.39.0-alt1%ubt
- new version

* Tue Sep 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.38.0-alt1%ubt
- new version

* Wed Aug 16 2017 Sergey V Turchin <zerg@altlinux.org> 5.37.0-alt1%ubt
- new version

* Mon Jul 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.36.0-alt1%ubt
- new version

* Thu Jun 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.35.0-alt1%ubt
- new version

* Fri May 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.34.0-alt1%ubt
- new version

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.33.0-alt1%ubt
- new version

* Wed Mar 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.32.0-alt1%ubt
- new version

* Mon Feb 13 2017 Sergey V Turchin <zerg@altlinux.org> 5.31.0-alt1%ubt
- initial build
