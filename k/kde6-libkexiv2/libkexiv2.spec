%define rname libkexiv2

%define sover 0
%define libkexiv2 libkexiv2qt6_%sover

Name: kde6-%rname
Version: 24.08.1
Release: alt1
%K6init altplace

Group: Graphical desktop/KDE
Summary: EXIV2 Library interface for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: libexiv2-devel

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkexiv2
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkexiv2
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/KExiv2*/
%_K6link/lib*.so
%_K6lib/cmake/KExiv2*/

%files -n %libkexiv2
%_K6lib/libKExiv2Qt6.so.%sover
%_K6lib/libKExiv2Qt6.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

