%define rname akregator

%define sover 6
%define libakregatorinterfaces libakregatorinterfaces%sover
%define libakregatorprivate libakregatorprivate%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Networking/News
Summary: RSS/Atom feed reader
Url: http://www.kde.org
License: GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-akregator = %EVR
Obsoletes: kde5-akregator < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-webengine-devel
BuildRequires: boost-devel libassuan-devel libsasl2-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-kcmutils-devel kf6-kcrash-devel  kf6-kdoctools-devel kf6-kiconthemes-devel kf6-kcontacts-devel
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kparts-devel kf6-ktexteditor-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kwindowsystem-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-syndication-devel kf6-syntax-highlighting-devel kf6-ktexttemplate-devel
BuildRequires: kde6-libkleo-devel
BuildRequires: akonadi-contacts-devel akonadi-devel akonadi-mime-devel grantleetheme-devel kimap-devel
BuildRequires: kmime-devel kontactinterface-devel kpimtextedit-devel kde6-libkdepim-devel messagelib-devel pimcommon-devel

%description
RSS/Atom feed reader for KDE.
 
%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Provides: kde5-akregator-common = %EVR
Obsoletes: kde5-akregator-common < %EVR
Requires: kf6-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libakregatorinterfaces
Group: System/Libraries
Summary: %name library
Requires: %name-common
Obsoletes: libakregatorinterfaces5 < %EVR
%description -n %libakregatorinterfaces
%name library

%package -n %libakregatorprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common
Obsoletes: libakregatorprivate5 < %EVR
%description -n %libakregatorprivate
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data akregator kconf_update kontact messageviewer
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/akregator
%_K6bin/akregatorstorageexporter
%_K6plug/akregator*.so
%_K6plug/pim6/kontact/*akregator*.so
%_K6plug/pim6/kcms/akregator/*akregator*.so
%_K6xdgapp/org.kde.akregator.desktop
%_K6cfg/*akregator*.kcfg
%_K6notif/akregator.notifyrc
%_K6icon/*/*/apps/akregator*.*
%_datadir/metainfo/*.xml

%files devel
%_K6dbus_iface/*akregator*.xml
#%_K6inc/akregator_version.h
#%_K6inc/akregator/
#%_K6link/lib*.so
#%_K6lib/cmake/akregator
#%_K6archdata/mkspecs/modules/qt_akregator.pri

%files -n %libakregatorinterfaces
%_K6lib/libakregatorinterfaces.so.%sover
%_K6lib/libakregatorinterfaces.so.*
%files -n %libakregatorprivate
%_K6lib/libakregatorprivate.so.%sover
%_K6lib/libakregatorprivate.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

