%define rname libkmahjongg

Name: kde6-%rname
Version: 24.08.3
Release: alt1
%K6init

Group: System/Libraries
Summary: Mahjongg library
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kwidgetsaddons-devel kf6-kcolorscheme-devel

%description
Library used for loading and rendering of Mahjongg tilesets and associated backgrounds.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-libkmahjongg-common = %EVR
Obsoletes: kde5-libkmahjongg-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkmahjongg6
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkf5kmahjongglib < %EVR
%description -n libkmahjongg6
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data kmahjongglib
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_K6data/kmahjongglib/
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/KMahjongg?/
%_K6link/lib*.so
%_K6lib/cmake/KMahjongglib?/

%files -n libkmahjongg6
%_K6lib/libKMahjongg6.so.*

%changelog
* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build

