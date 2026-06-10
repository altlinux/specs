%define rname libkmahjongg

Name: kde6-%rname
Version: 26.04.2
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
* Tue Jun 09 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Thu Oct 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Fri May 30 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Feb 25 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build

