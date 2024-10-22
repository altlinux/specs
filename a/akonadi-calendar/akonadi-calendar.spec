%define rname akonadi-calendar

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Akonadi Calendar Integration
Url: http://www.kde.org
License: LGPL-2.1-or-later

ExcludeArch: %not_qt6_qtwebengine_arches
Provides: kde5-akonadi-calendar = %EVR
Obsoletes: kde5-akonadi-calendar < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: boost-devel-headers libsasl2-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel
BuildRequires: kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel
BuildRequires: kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel kf6-ktexttemplate-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: akonadi-devel kf6-kcalendarcore-devel kcalutils-devel kf6-kcontacts-devel kidentitymanagement-devel
BuildRequires: kmailtransport-devel kmime-devel kpimtextedit-devel
BuildRequires: akonadi-mime-devel akonadi-contacts-devel grantleetheme-devel
BuildRequires: messagelib-devel pimcommon-devel kde6-libkdepim-devel kimap-devel
BuildRequires: kde6-libkleo-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-akonadi-calendar-common = %EVR
Obsoletes: kde5-akonadi-calendar-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkpim6akonadicalendar
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkf5akonadicalendar < %EVR
%description -n libkpim6akonadicalendar
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6start/org.kde.kalendarac.desktop
%_K6bin/kalendarac
%_K6plug/kf6/org.kde.kcalendarcore.calendars/
%_K6plug/akonadi_serializer_kcalcore.so
%_K6dbus_srv/org.kde.kalendarac.service
%_K6notif/kalendarac.notifyrc
%_datadir/akonadi/plugins/serializer/akonadi_serializer_kcalcore.desktop

%files devel
%_includedir/KPim6/AkonadiCalendar/
%_K6link/lib*.so
%_K6lib/cmake/K*AkonadiCalendar/

%files -n libkpim6akonadicalendar
%_K6lib/libKPim6AkonadiCalendar.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

