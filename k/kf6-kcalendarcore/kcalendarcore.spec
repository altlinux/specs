%define rname kcalendarcore

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init altplace

Group: Graphical desktop/KDE
Summary: KDE calendar access library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel
BuildRequires: libical-devel libuuid-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel 
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel
BuildRequires: kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

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
Requires: libical-devel
Provides: kcalcore-devel = %EVR
Obsoletes: kcalcore-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6calendarcore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6calendarcore
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
#find_lang %name --with-kde --all-name

#files common -f %name.lang
%files common
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/KCalendarCore/
%_K6link/lib*.so
%_K6lib/cmake/KF6CalendarCore/
%_pkgconfigdir/KF6CalendarCore.pc

%files -n libkf6calendarcore
%_K6lib/libKF6CalendarCore.so.*


%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build
