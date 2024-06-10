%define rname prison

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6  barcode abstraction layer
Url: http://www.kde.org
License: MIT

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-multimedia-devel
BuildRequires: libdmtx-devel libqrencode-devel libzxing-cpp-devel

%description
A barcode abstraction layer providing uniform access to generation of barcodes with data.

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

%package -n libkf6prison
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6prison
KF6 library

%package -n libkf6prisonscanner
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6prisonscanner
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
%_K6inc/?rison*/
%_K6link/lib*.so
%_K6lib/cmake/KF6Prison

%files -n libkf6prison
%_K6lib/libKF6Prison.so.*
%dir %_K6qml/org/kde/prison/
%_K6qml/org/kde/prison/
%exclude %_K6qml/org/kde/prison/scanner/

%files -n libkf6prisonscanner
%_K6lib/libKF6PrisonScanner.so.*
%_K6qml/org/kde/prison/scanner/


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

