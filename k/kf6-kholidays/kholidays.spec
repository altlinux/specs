%define rname kholidays

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: Graphical desktop/KDE
Summary: KDE library for regional holiday information
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Mon May 21 2018 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libqt6-core libqt6-gui libqt6-network libqt6-qml libqt6-xml libstdc++-devel perl python-base python-modules python3 python3-base qt6-base-devel qt6-tools rpm-build-python3 rpm-build-qml ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules libssl-devel python3-dev qt6-declarative-devel qt6-tools-devel rpm-build-kf6 rpm-build-ruby
BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-tools-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6holidays
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6holidays
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
mkdir -p %buildroot/%_K6data/libkholidays/
%find_lang %name --with-kde --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
#%doc COPYING*
%_datadir/qlogging-categories6/*.*categories
%_K6data/libkholidays/

%files devel
#%_K6inc/kholidays_version.h
%_K6inc/KHolidays/
%_K6link/lib*.so
%_K6lib/cmake/KF6Holidays/
#%_K6plug/designer/*.so

%files -n libkf6holidays
%_K6lib/libKF6Holidays.so.*
%_K6qml/org/kde/kholidays/


%changelog
* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

