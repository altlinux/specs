%define rname korganizer

%define pim_sover 6
%define libkorganizer_core libkorganizer_core%pim_sover
%define libkorganizer_interfaces libkorganizer_interfaces%pim_sover
%define libkorganizerprivate libkorganizerprivate%pim_sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Electronic organizer
Url: http://www.kde.org
License: LGPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-korganizer = %EVR
Obsoletes: kde5-korganizer < %EVR
Requires: akonadi kdepim-runtime akonadi-search akonadi-calendar

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-base-devel qt6-phonon-devel qt6-tools-devel
BuildRequires: boost-devel libXres-devel libassuan-devel libldap-devel libsasl2-devel
BuildRequires: kf6-kcmutils-devel kf6-kdoctools-devel kf6-kio-devel kf6-knewstuff-devel kf6-kwallet-devel kf6-kholidays-devel kf6-kcalendarcore-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kparts-devel kf6-kitemmodels-devel kf6-ktexttemplate-devel
BuildRequires: akonadi-calendar-devel akonadi-contacts-devel akonadi-devel akonadi-mime-devel akonadi-notes-devel
BuildRequires: akonadi-search-devel calendarsupport-devel eventviews-devel incidenceeditor-devel
BuildRequires: kcalutils-devel kf6-kcontacts-devel kidentitymanagement-devel kimap-devel
BuildRequires: kldap-devel kmailtransport-devel kmime-devel kontactinterface-devel kpimtextedit-devel
BuildRequires: kde6-libkdepim-devel messagelib-devel pimcommon-devel

%description
Electronic organizer.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-korganizer-common = %EVR
Obsoletes: kde5-korganizer-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkorganizer_core
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkorganizer_core5 < %EVR
%description -n %libkorganizer_core
%name library

%package -n %libkorganizer_interfaces
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkorganizer_interfaces5 < %EVR
%description -n %libkorganizer_interfaces
%name library

%package -n %libkorganizerprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkorganizerprivate5 < %EVR
%description -n %libkorganizerprivate
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DDATA_INSTALL_DIR=%_K6data \
    #

%install
%K6install
%K6install_move data korganizer kontact kconf_update knsrcfiles
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/korganizer
%_K6plug/*korganizer*.so
%_K6plug/pim6/korganizer/*.so
%_K6plug/pim6/kcms/korganizer/
%_K6plug/pim6/kcms/summary/*.so
%_K6plug/pim6/kontact/kontact_*.so
%_K6xdgapp/*korganizer*.desktop
%_K6data/korganizer/
%_K6data/knsrcfiles/*korganizer*
%_K6cfg/*korganizer*
%_K6icon/*/*/apps/*korg*.*
%_K6icon/*/*/apps/quickview.*
%_K6icon/*/*/status/*moon-phase*.*
%_K6dbus_srv/*korga*.service
%_datadir/metainfo/*.xml

%files devel
#%_K6link/lib*.so
%_K6dbus_iface/org.kde.*.xml

%files -n %libkorganizer_core
%_K6lib/libkorganizer_core.so.%pim_sover
%_K6lib/libkorganizer_core.so.*
%files -n %libkorganizer_interfaces
%_K6lib/libkorganizer_interfaces.so.%pim_sover
%_K6lib/libkorganizer_interfaces.so.*
%files -n %libkorganizerprivate
%_K6lib/libkorganizerprivate.so.%pim_sover
%_K6lib/libkorganizerprivate.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

