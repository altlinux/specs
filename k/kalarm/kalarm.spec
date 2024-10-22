%define rname kalarm

%define pim_sover 6
%define libkalarmcalendar libkalarmcalendar%pim_sover
%define libkalarmplugin libkalarmplugin%pim_sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Personal Alarm Scheduler
Url: http://www.kde.org
License: LGPL-2.0-or-later

Provides: kde5-kalarm = %EVR
Obsoletes: kde5-kalarm < %EVR

Source: %rname-%version.tar
#Patch100: alt-kalarm-ignore-tz.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-phonon-devel
BuildRequires: boost-devel xsltproc libXres-devel libsasl2-devel
BuildRequires: libvlc-devel
BuildRequires: kf6-kcontacts-devel kf6-kholidays-devel kf6-kcalendarcore-devel kf6-ki18n-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kcmutils-devel kf6-kdoctools-devel kf6-kio-devel kf6-kwallet-devel kf6-knotifications-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kidletime-devel kf6-knotifyconfig-devel kf6-kitemmodels-devel
BuildRequires: kf6-kstatusnotifieritem-devel kf6-ktexttemplate-devel
BuildRequires: akonadi-contacts-devel akonadi-devel akonadi-mime-devel kcalutils-devel
BuildRequires: kidentitymanagement-devel kimap-devel kmailtransport-devel kmime-devel
BuildRequires: kpimtextedit-devel kde6-libkdepim-devel messagelib-devel pimcommon-devel

%description
Personal Alarm Scheduler.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-kalarm-common = %EVR
Obsoletes: kde5-kalarm-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkalarmcalendar
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkalarmcalendar5 < %EVR
%description -n %libkalarmcalendar
%name library

%package -n %libkalarmplugin
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkalarmplugin5 < %EVR
%description -n %libkalarmplugin
%name library

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kalarm kconf_update
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/kalarm
%_K6bin/kalarmautostart
%_K6exec/kauth/kalarm_helper
%_K6plug/pim6/kalarm/akonadiplugin.so
%_K6start/kalarm.autostart.desktop
%_K6xdgapp/org.kde.kalarm.desktop
%_K6cfg/*kalarm*.kcfg
%_K6data/kalarm/
%_K6icon/*/*/apps/kalarm.*
%_K6dbus_sys_srv/org.kde.kalarm.rtcwake.service
%_K6dbus/system.d/org.kde.kalarm.rtcwake.conf
%_K6notif/kalarm.notifyrc
%_datadir/polkit-1/actions/org.kde.kalarm.rtcwake.policy
%_datadir/metainfo/*.xml

%files -n %libkalarmcalendar
%_K6lib/libkalarmcalendar.so.%pim_sover
%_K6lib/libkalarmcalendar.so.*

%files -n %libkalarmplugin
%_K6lib/libkalarmplugin.so.%pim_sover
%_K6lib/libkalarmplugin.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

