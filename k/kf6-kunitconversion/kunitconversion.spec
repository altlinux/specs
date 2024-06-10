%define rname kunitconversion

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 converting physical units
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Feb 17 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt6-core libqt6-network libqt6-test libqt6-xml libstdc++-devel python-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf6-ki18n-devel python-module-google qt6-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel
BuildRequires: kf6-ki18n-devel

%description
KUnitConversion provides functions to convert values in different physical
units. It supports converting different prefixes (e.g. kilo, mega, giga) as
well as converting between different unit systems (e.g. liters, gallons).

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

%package -n libkf6unitconversion
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6unitconversion
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
#%_K6inc/kunitconversion_version.h
%_K6inc/KUnitConversion/
%_K6link/lib*.so
%_K6lib/cmake/KF6UnitConversion

%files -n libkf6unitconversion
%_K6lib/libKF6UnitConversion.so.*


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

