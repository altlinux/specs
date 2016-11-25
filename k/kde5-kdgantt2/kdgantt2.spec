%define rname kdgantt2

%define sover 5
%define libkf5kdgantt2 libkf5kdgantt2%sover

Name: kde5-%rname
Version: 16.08.3
Release: alt1
%K5init

Group: System/Libraries
Summary: KDF5 %rname library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Apr 29 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-printsupport libqt5-test libqt5-widgets libstdc++-devel perl python-base python-modules python3 python3-base rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kf5-ki18n-devel python-module-google python3-dev qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules kf5-ki18n-devel qt5-base-devel

%description
%summary.

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

%package -n %libkf5kdgantt2
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5kdgantt2
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
#%doc COPYING*
%config(noreplace) %_K5xdgconf/kdgantt2.categories

%files devel
%_K5inc/kdgantt2_version.h
%_K5inc/???antt2/
%_K5link/lib*.so
%_K5lib/cmake/KF5KDGantt2/
%_K5archdata/mkspecs/modules/qt_KDGantt2.pri

%files -n %libkf5kdgantt2
%_K5lib/libKF5KDGantt2.so.%sover
%_K5lib/libKF5KDGantt2.so.*

%changelog
* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Fri Aug 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Thu Jun 30 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Wed Apr 27 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- initial build
