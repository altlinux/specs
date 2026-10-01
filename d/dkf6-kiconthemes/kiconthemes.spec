%define rname kiconthemes

Name: dkf6-%rname
Version: 6.28.0
Release: alt0.dde.1
%DK6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 icon GUI utilities
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %name-%version.tar
# fix black icons during kf5->kf6
Patch1: accent-fallback.patch

BuildRequires(pre): rpm-build-dkf6
BuildRequires: deepin-extra-cmake-modules dqt6-svg-devel dqt6-tools-devel dqt6-declarative-devel
BuildRequires: vulkan-headers
BuildRequires: dkf6-ki18n-devel dkf6-karchive-devel dkf6-kconfigwidgets-devel dkf6-kwidgetsaddons-devel
BuildRequires: dkf6-kcolorscheme-devel
BuildRequires: dkf6-breeze-icons-devel

# find libraries
%add_findprov_lib_path %_DK6lib

%description
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
# Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: dqt6-svg-devel dkf6-karchive-devel dkf6-kitemviews-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libdkf6iconthemes
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6iconthemes
KF6 library

%package -n libdkf6iconwidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6iconwidgets
KF6 library


%prep
%setup -n %name-%version
%patch1 -p1

%build
%DK6build

%install
%DK6install
%find_lang %name --all-name
%DK6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_DK6data/qlogging-categories6/*.*categories

%files devel
%_DK6plug/designer/*.so
%exclude %_bindir/kiconfinder6
%_DK6bin/kiconfinder6
%_DK6inc/KIconThemes/
%_DK6inc/KIconWidgets/
%_DK6link/lib*.so
%_DK6lib/cmake/KF6IconThemes

%files -n libdkf6iconthemes
%_DK6lib/libKF6IconThemes.so.*
%_DK6plug/kiconthemes6/iconengines/KIconEnginePlugin.so
%_DK6qml/org/kde/iconthemes/

%files -n libdkf6iconwidgets
%_DK6lib/libKF6IconWidgets.so.*


%changelog
* Thu Oct 01 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.0-alt0.dde.1
- fork for independent deepin build

* Tue Jul 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.28.0-alt1
- new version

* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.27.0-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.26.0-alt1
- new version

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt1
- new version

* Fri Mar 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.24.0-alt1
- new version

* Mon Feb 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.0-alt1
- new version

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.0-alt1
- new version

* Mon Dec 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.21.0-alt1
- new version

* Thu Nov 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt1
- new version

* Fri Oct 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.19.0-alt1
- new version

* Mon Sep 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.18.0-alt1
- new version

* Mon Aug 25 2025 Sergey V Turchin <zerg@altlinux.org> 6.17.0-alt1
- new version

* Mon Aug 04 2025 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt1
- new version

* Mon Jul 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.15.0-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.13.0-alt1
- new version

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.11.0-alt1
- new version

* Mon Jan 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1
- new version

* Mon Dec 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.9.0-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Mon Sep 09 2024 Oleg Solovyov <mcpain@altlinux.org> 6.4.0-alt2
- fix black icons

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

