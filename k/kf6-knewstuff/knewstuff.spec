%define rname knewstuff

Name: kf6-%rname
Version: 6.27.0
Release: alt1
%K6init no_altplace

Group: System/Libraries
Summary: KDE Frameworks 6 downloading and sharing additional application data
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: kf6-kirigami

Source: %rname-%version.tar
Patch1: alt-check-ghns-auth.patch
Patch2: alt-warning.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-tools-devel
BuildRequires: kf6-attica-devel kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel
BuildRequires: kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kpackage-devel kf6-syndication-devel kf6-kirigami-devel

%description
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

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

%package -n libkf6newstuff
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6newstuff
KF6 library

%package -n libkf6newstuffcore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6newstuffcore
KF6 library

%package -n libkf6newstuffwidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6newstuffwidgets
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories
#%_kf6_data/kmoretools/

%files
%_K6bin/knewstuff*
%_K6xdgapp/*knewstuff*.desktop

%files devel
%_K6plug/designer/*newstuff*.so
%_K6inc/KNewStuff*/
%_K6link/lib*.so
%_K6lib/cmake/*NewStuff*/

%files -n libkf6newstuffcore
%_K6lib/libKF6NewStuffCore.so.*

%files -n libkf6newstuffwidgets
%_K6lib/libKF6NewStuffWidgets.so.*
%_K6qml/org/kde/newstuff/


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

* Fri Mar 28 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt2
- more serious warning about downloadable content

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

* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Thu Jul 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt2
- move qml into library packge

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

