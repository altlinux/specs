%define rname pim-data-exporter

%define pim_sover 6
%define libpimdataexporterprivate libpimdataexporterprivate%pim_sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: PIM Setting Exporter
Url: http://www.kde.org
License: LGPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-pim-data-exporter = %EVR
Obsoletes: kde5-pim-data-exporter < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: boost-devel libassuan-devel libsasl2-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-kwallet-devel kf6-kholidays-devel kf6-karchive-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kcontacts-devel kf6-knotifications-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-kitemmodels-devel kf6-ki18n-devel kf6-ktexttemplate-devel
BuildRequires: kde6-libkleo-devel
BuildRequires: akonadi-calendar-devel akonadi-contacts-devel akonadi-devel akonadi-mime-devel calendarsupport-devel
BuildRequires: kidentitymanagement-devel
BuildRequires: kimap-devel kmailtransport-devel kmime-devel kpimtextedit-devel kde6-libkdepim-devel
BuildRequires: mailcommon-devel messagelib-devel pimcommon-devel akonadi-notes-devel

%description
PIM Setting Exporter allows to export and import PIM settings and local mail.
You can backup and restore settings from various programs.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-pim-data-exporter-common = %EVR
Obsoletes: kde5-pim-data-exporter-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libpimdataexporterprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libpimdataexporterprivate5 < %EVR
%description -n %libpimdataexporterprivate
%name library

%prep
%setup -n %rname-%version
for d in po/*/docs/pimsettingexporter ; do
    b_dir=`dirname "$d"`
    [ -e "$b_dir/pimdataexporter" ] || cp -ar "$d" "$b_dir/pimdataexporter"
done

%build
%K6build

%install
%K6install
%K6install_move data kconf_update
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/*pimdataexporter*
%_K6xdgapp/*pimdataexporter*.desktop
%_K6cfg/*pimdataexporter*
%_datadir/metainfo/*.xml

#%files devel
#%_K6inc/pim-data-exporter_version.h
#%_K6inc/pim-data-exporter/
#%_K6link/lib*.so
#%_K6lib/cmake/pim-data-exporter
#%_K6archdata/mkspecs/modules/qt_pim-data-exporter.pri

%files -n %libpimdataexporterprivate
%_K6lib/libpimdataexporterprivate.so.%pim_sover
%_K6lib/libpimdataexporterprivate.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

