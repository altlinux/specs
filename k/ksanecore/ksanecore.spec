%define rname ksanecore

%define sover 1
%define libksanecore libksanecore6_%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Qt interface for the SANE library
Url: http://www.kde.org
License: LGPL-2.1-only OR LGPL-3.0-only

Source: %rname-%version.tar
Patch1: alt-headers-place.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libsane-devel
BuildRequires: kf6-ki18n-devel

%description
KSaneCore is a library that provides a Qt interface for the SANE library for scanner hardware.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-ksanecore-common = %EVR
Obsoletes: kde5-ksanecore-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libksanecore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libksanecore
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data locale
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files devel
%_K6inc/KSaneCore*/
%_K6link/lib*.so
%_K6lib/cmake/KSaneCore*/

%files -n %libksanecore
%_K6lib/libKSaneCore6.so.%sover
%_K6lib/libKSaneCore6.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

