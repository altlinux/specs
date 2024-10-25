%define rname kweathercore

%define sover 6
%define libkweathercore libkweathercore%sover

Name: %rname
Version: 24.08.2
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: QToolButton with color popup menu with lets you select a color
Url: https://invent.kde.org/libraries/kweathercore
License: LGPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-clear-country-name.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-declarative-devel qt6-positioning-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kholidays-devel kf6-ki18n-devel

%description
%summary

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
Conflicts: kde5-kweathercore-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkweathercore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkweathercore
%name library

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --with-kde --all-name


%files common -f %name.lang

%files devel
%_K6inc/KWeatherCore/
%_K6inc/kweathercore_version.h
%_libdir/cmake/KWeatherCore/
%_K6link/lib*.so
%_K6archdata/mkspecs/modules/qt_KWeatherCore.pri

%files -n %libkweathercore
%doc LICENSES/* README.md
%_K6lib/libKWeatherCore.so.%sover
%_K6lib/libKWeatherCore.so.*

%changelog
* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

