%define rname kcalutils

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE calendar utility library
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libical-devel
# grantlee6-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: kf6-kcalendarcore-devel kidentitymanagement-devel kpimtextedit-devel kf6-karchive-devel kf6-kauth-devel
BuildRequires: kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel kf6-ktexttemplate-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkpim6calendarutils
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkpim6calendarutils
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kcalendar
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories
#%_K6data/kcalendar/

%files devel
%_includedir/KPim6/KCalUtils/
%_K6link/lib*.so
%_K6lib/cmake/K*CalendarUtils/

%files -n libkpim6calendarutils
%_K6plug/kf6/ktexttemplate/kcalendar_grantlee_plugin.so
%_K6lib/libKPim6CalendarUtils.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

