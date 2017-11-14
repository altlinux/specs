%define rname libkmahjongg

Name: kde5-%rname
Version: 17.08.3
Release: alt1%ubt
%K5init

Group: System/Libraries
Summary: Mahjongg library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Mar 23 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel python-base python-modules python3 qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kf5-kauth-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kwidgetsaddons-devel python-module-google python3-base qt5-svg-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-svg-devel
BuildRequires: kf5-kauth-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kwidgetsaddons-devel

%description
Library used for loading and rendering of Mahjongg tilesets and associated backgrounds.

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

%package -n libkf5kmahjongglib
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5kmahjongglib
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kmahjongglib
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_K5data/kmahjongglib/

%files devel
#%_K5inc/libkmahjongg_version.h
%_K5inc/KF5KMahjongg/
%_K5link/lib*.so
%_K5lib/cmake/KF5KMahjongglib/
#%_K5archdata/mkspecs/modules/qt_libkmahjongg.pri

%files -n libkf5kmahjongglib
%_K5lib/libKF5KMahjongglib.so.*

%changelog
* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Mon Jun 05 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Tue Apr 11 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Fri Sep 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Tue Jul 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Mon May 16 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
