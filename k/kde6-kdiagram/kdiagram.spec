%define rname kdiagram

%define kchart_sover 3
%define libkchart libkchart6_%kchart_sover
%define kgantt_sover 3
%define libkgantt libkgantt6_%kgantt_sover


Name: kde6-%rname
Version: 3.0.1
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE business diagrams libraries
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-svg-devel qt6-tools-devel
BuildRequires: libvulkan-devel

%description
Powerful libraries (KChart, KGantt) for creating business diagrams.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: qt6-svg-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkchart
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkchart
%name library

%package -n %libkgantt
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkgantt
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6find_qtlang %name --all-name

%files common -f %name.lang

%files devel
%_K6inc/KChart*/
%_K6inc/KGantt*/
%_K6link/lib*.so
%_K6lib/cmake/KChart*/
%_K6lib/cmake/KGantt*/
%_K6archdata/mkspecs/modules/qt_*.pri

%files -n %libkchart
%_K6lib/libKChart6.so.%kchart_sover
%_K6lib/libKChart6.so.*
%files -n %libkgantt
%_K6lib/libKGantt6.so.%kgantt_sover
%_K6lib/libKGantt6.so.*

%changelog
* Fri Sep 20 2024 Sergey V Turchin <zerg@altlinux.org> 3.0.1-alt1
- initial build
