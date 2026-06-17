%define rname baloo

%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%add_findreq_skiplist %_userunitdir/*.service

Name: kf6-%rname
Version: 6.27.0
Release: alt1
%K6init no_altplace

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 framework for searching and managing metadata
Url: http://www.kde.org
License: GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only

Provides: kf5-baloo = %EVR
Obsoletes: kf5-baloo < %EVR

Source: %rname-%version.tar
Patch1: alt-disable-indexing.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-tools-devel
BuildRequires: liblmdb-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kfilemetadata-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kidletime-devel 
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel
BuildRequires: kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
%summary.

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
Requires: kf6-kfilemetadata-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6baloo
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n libkf6baloo
KF6 library

%package -n libkf6balooengine
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n libkf6balooengine
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/baloo*
%_K6exec/baloo*
%_K6plug/kf6/kded/baloosearchmodule.so
%_K6plug/kf6/kio/*.so
%_K6qml/org/kde/baloo/
%_K6start/*baloo*.desktop
%_userunitdir/*.service

%files devel
%_K6inc/Baloo/
%_K6link/lib*.so
%_K6lib/cmake/KF6Baloo
%_K6dbus_iface/*aloo*.xml
%_pkgconfigdir/*aloo*.pc

%files -n libkf6baloo
%_K6lib/libKF6Baloo.so.*
%files -n libkf6balooengine
%_K6lib/libKF6BalooEngine.so.*


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

* Tue Oct 29 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt2
- obsolete libkf5baloowidgets

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jul 23 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt4
- obsolete kf5-baloo

* Wed Jul 17 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt3
- conflicts with kf5-baloo

* Mon Jul 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt2
- fix requires

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

