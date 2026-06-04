%define rname libksane

%define sover 6
%define libksanewidgets libksanewidgets6_%sover

Name: kde6-%rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: SANE Library interface
Url: http://www.kde.org
License: LGPL-2.1-only OR LGPL-3.0-only

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: ksanecore-devel
BuildRequires: kf6-kconfig-devel kf6-ki18n-devel kf6-ktextwidgets-devel kf6-kwallet-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-sonnet-devel

%description
Libksane is a KDE interface for SANE library to control flat scanners.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-libksane-common = %EVR
Obsoletes: kde5-libksane-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: ksanecore-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libksanewidgets
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libksanewidgets
%name library


%prep
%setup -n %rname-%version

find -type f -name \*.h -or -name \*.cpp | \
while read f ; do
    sed -i '/^#include/s|<KSaneCore/|<KSaneCore6/|' $f
done

%build
%add_optflags -I%_K6inc
%K6build \
    -DBUILD_WITH_QT6:BOOL=ON \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_K6icon/hicolor/*/actions/*.*

%files devel
%_K6inc/KSane*/
%_K6link/lib*.so
%_K6lib/cmake/KSane*/

%files -n %libksanewidgets
%_K6lib/libKSaneWidgets6.so.*


%changelog
* Thu Jun 04 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Fri May 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

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

