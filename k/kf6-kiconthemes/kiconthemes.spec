%define rname kiconthemes

Name: kf6-%rname
Version: 6.27.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 icon GUI utilities
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar
# fix black icons during kf5->kf6
Patch1: accent-fallback.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-svg-devel qt6-tools-devel qt6-declarative-devel
BuildRequires: kf6-ki18n-devel kf6-karchive-devel kf6-kconfigwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-breeze-icons-devel

%description
This library contains classes to improve the handling of icons
in applications using the KDE Frameworks.

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
Requires: qt6-svg-devel kf6-karchive-devel kf6-kitemviews-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6iconthemes
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6iconthemes
KF6 library

%package -n libkf6iconwidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6iconwidgets
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1

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
%_K6plug/designer/*.so
%_bindir/kiconfinder6
%_K6bin/kiconfinder6
%_K6inc/KIconThemes/
%_K6inc/KIconWidgets/
%_K6link/lib*.so
%_K6lib/cmake/KF6IconThemes

%files -n libkf6iconthemes
%_K6lib/libKF6IconThemes.so.*
%_K6plug/kiconthemes6/iconengines/KIconEnginePlugin.so
%_K6qml/org/kde/iconthemes/

%files -n libkf6iconwidgets
%_K6lib/libKF6IconWidgets.so.*


%changelog
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

