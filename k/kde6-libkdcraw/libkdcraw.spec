%define rname libkdcraw

%define sover 5
%define libkdcrawqt libkdcrawqt6_%sover

Name: kde6-%rname
Version: 25.12.3
Release: alt2
%K6init altplace

Group: Graphical desktop/KDE
Summary: LibRaw C++ interface for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-libraw-ver.patch

BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: libraw0-devel

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

%package -n %libkdcrawqt
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdcrawqt
%name library


%prep
%setup -n %rname-%version
#%patch1 -p1

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
%_K6inc/KDcraw*/
%_K6link/lib*.so
%_K6lib/cmake/KDcraw*/

%files -n %libkdcrawqt
%_K6lib/libKDcrawQt6.so.%sover
%_K6lib/libKDcrawQt6.so.*


%changelog
* Thu Apr 30 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt2
- build with libraw0-devel

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Mon Sep 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Thu Jul 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Tue Jun 10 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Mon May 12 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Apr 21 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.0-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Tue Feb 18 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Jan 20 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Wed Nov 13 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Fri Oct 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

