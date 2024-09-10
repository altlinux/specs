%define rname kdeclarative

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 integration of QML and KDE work spaces
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPL-2.0-or-later

Requires: %name-common = %version-%release

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-shadertools-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kpackage-devel kf6-knotifications-devel

%description
KDeclarative provides integration of QML and KDE work spaces.
It's comprises two parts: a library used by the C++ part of your application
to intergrate QML with KDE Frameworks specific features, and a series of
QML imports that offer bindings to some of the Frameworks.

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
Requires: qt6-declarative-devel libepoxy-devel kf6-kio-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6declarative
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6declarative
KF6 library

%package -n libkf6quickaddons
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6quickaddons
KF6 library

%package -n libkf6calendarevents
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6calendarevents
KF6 library

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md

%files
%_K6qml/*/

%files devel
%_K6inc/KDeclarative/
%_K6link/lib*.so
%_K6lib/cmake/KF6Declarative

%files -n libkf6calendarevents
%_K6lib/libKF6CalendarEvents.so.*


%changelog
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

