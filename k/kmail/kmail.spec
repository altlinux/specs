%define rname kmail

%define pim_sover 6
%define libkmailprivate libkmailprivate%pim_sover
%define libmailfilteragentprivate libmailfilteragentprivate%pim_sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Networking/Mail
Summary: EMail client
Url: http://www.kde.org
License: LGPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-kmail = %EVR
Obsoletes: kde5-kmail < %EVR
Requires: akonadi kdepim-runtime akonadi-search

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-webengine-devel
BuildRequires: boost-devel libassuan-devel libldap-devel libsasl2-devel
BuildRequires: libgpgme-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-kcmutils-devel kf6-kdoctools-devel kf6-kio-devel kf6-kcalendarcore-devel kf6-ki18n-devel
BuildRequires: kf6-knotifyconfig-devel kf6-kwallet-devel kf6-syntax-highlighting-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kitemmodels-devel kf6-knotifications-devel kf6-kparts-devel kf6-sonnet-devel kf6-kiconthemes-devel
BuildRequires: kf6-kstatusnotifieritem-devel kf6-ktexttemplate-devel
BuildRequires: kde6-libkleo-devel
BuildRequires: akonadi-contacts-devel akonadi-devel akonadi-mime-devel akonadi-search-devel
BuildRequires: kcalutils-devel kf6-kcontacts-devel kidentitymanagement-devel kimap-devel kldap-devel
BuildRequires: kmailtransport-devel kmime-devel kontactinterface-devel kpimtextedit-devel ktnef-devel
BuildRequires: kde6-libgravatar-devel kde6-libkdepim-devel kde6-libksieve-devel mailcommon-devel messagelib-devel
BuildRequires: pimcommon-devel

%description
EMail client

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-kmail-common = %EVR
Obsoletes: kde5-kmail-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkmailprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkmailprivate5 < %EVR
%description -n %libkmailprivate
%name library

%package -n %libmailfilteragentprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libmailfilteragentprivate
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kmail2 kconf_update messageviewer kontact
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6icon/*/*/actions/*.*
%_K6icon/*/*/emblems/*.*
%_K6cfg/*.kcfg

%files
%_K6bin/kmail*
%_K6bin/akonadi_*_agent
%_K6plug/*.so
%_K6plug/pim6/akonadi/config/*.so
%_K6plug/pim6/kcms/kmail/*.so
%_K6plug/pim6/kcms/summary/*.so
%_K6plug/pim6/kontact/*.so
%_K6xdgapp/org.kde.*.desktop
%_K6xdgapp/kmail_view.desktop
%_K6data/kmail2/
%_K6icon/*/*/apps/kmail.*
%_K6notif/kmail2.notifyrc
%_K6notif/akonadi_*_agent.notifyrc
%_datadir/akonadi/agents/*.desktop
%_K6dbus_srv/*kmail*.service
%_datadir/metainfo/*.xml
#
%_K6bin/ktnef
%_K6xdgapp/org.kde.ktnef.desktop
%_K6icon/*/*/apps/ktnef.*

%files devel
#%_K6inc/kmail_version.h
#%_K6inc/kmail/
#%_K6link/lib*.so
#%_K6lib/cmake/kmail
#%_K6archdata/mkspecs/modules/qt_kmail.pri
%_K6dbus_iface/*kmail*.xml

%files -n %libkmailprivate
%_K6lib/libkmailprivate.so.%pim_sover
%_K6lib/libkmailprivate.so.*
%files -n %libmailfilteragentprivate
%_K6lib/libmailfilteragentprivate.so.%pim_sover
%_K6lib/libmailfilteragentprivate.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

