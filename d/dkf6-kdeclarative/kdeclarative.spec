%define rname kdeclarative

%define sover 0
%define libkquickcontrolsprivate libdkquickcontrolsprivate%sover

Name: dkf6-%rname
Version: 6.28.0
Release: alt0.dde.1
%DK6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 integration of QML and KDE work spaces
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPL-2.0-or-later

Requires: %name-common = %version-%release

Source: %name-%version.tar

# prevent hasher-privd limits
BuildRequires(pre): rpm-build-dkf6
# BuildRequires: dkf6-kauth-devel dkf6-kbookmarks-devel dkf6-kcodecs-devel dkf6-kcompletion-devel dkf6-kconfig-devel
# BuildRequires: dkf6-kconfigwidgets-devel dkf6-kcoreaddons-devel dkf6-kdbusaddons-devel dkf6-kglobalaccel-devel
# BuildRequires: dkf6-kguiaddons-devel dkf6-ki18n-devel dkf6-kiconthemes-devel dkf6-kio-devel dkf6-kitemviews-devel
# BuildRequires: dkf6-kjobwidgets-devel dkf6-kservice-devel dkf6-ktextwidgets-devel dkf6-kwidgetsaddons-devel
# BuildRequires: dkf6-kwindowsystem-devel dkf6-kxmlgui-devel dkf6-solid-devel dkf6-sonnet-devel
# BuildRequires: dkf6-kpackage-devel dkf6-knotifications-devel
BuildRequires: deepin-extra-cmake-modules dqt6-declarative-devel dqt6-shadertools-devel dqt6-tools-devel
BuildRequires: vulkan-headers spirv-tools libdqt6-qmlcompiler
BuildRequires: dkf6-kconfig-devel
BuildRequires: dkf6-kglobalaccel-devel
BuildRequires: dkf6-kguiaddons-devel dkf6-ki18n-devel
BuildRequires: dkf6-kwidgetsaddons-devel


# find libraries
%add_findprov_lib_path %_DK6lib

%description
KDeclarative provides integration of QML and KDE work spaces.
It's comprises two parts: a library used by the C++ part of your application
to intergrate QML with KDE Frameworks specific features, and a series of
QML imports that offer bindings to some of the Frameworks.

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
# Requires: dqt6-declarative-devel libepoxy-devel dkf6-kio-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkquickcontrolsprivate
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libkquickcontrolsprivate
KF6 library

%package -n libdkf6calendarevents
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n libdkf6calendarevents
KF6 library

%prep
%setup -n %name-%version

%build
%DK6build

%install
%DK6install
%find_lang %name --all-name
%DK6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md

%files
%_DK6qml/*/

%files devel
%_DK6inc/KDeclarative/
%_DK6link/lib*.so
%_DK6lib/cmake/KF6Declarative

%files -n libdkf6calendarevents
%_DK6lib/libKF6CalendarEvents.so.*

%files -n %libkquickcontrolsprivate
%_DK6lib/libkquickcontrolsprivate.so.%sover
%_DK6lib/libkquickcontrolsprivate.so.*

%changelog
* Thu Oct 08 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.0-alt0.dde.1
- fork for independent deepin buildings

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

* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

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

