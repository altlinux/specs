%define rname kontact

%define pim_sover 6
%define libkontactprivate libkontactprivate%pim_sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Integrated solution to the KDE PIM
Url: http://www.kde.org
License:  GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-kontact = %EVR
Obsoletes: kde5-kontact < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-base-devel qt6-webengine-devel
BuildRequires: boost-devel libsasl2-devel
BuildRequires: kf6-kcmutils-devel kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdoctools-devel kf6-ktexttemplate-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kitemmodels-devel kf6-kparts-devel kf6-ktextwidgets-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kcontacts-devel
BuildRequires: akonadi-contacts-devel akonadi-devel akonadi-mime-devel grantleetheme-devel
BuildRequires: kidentitymanagement-devel kimap-devel kmime-devel kontactinterface-devel kpimtextedit-devel
BuildRequires: kde6-libkdepim-devel mailcommon-devel messagelib-devel pimcommon-devel

%description
Integrated solution to the KDE PIM.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-kontact-common = %EVR
Obsoletes: kde5-kontact-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkontactprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkontactprivate5 < %EVR
%description -n %libkontactprivate
%name library

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kontact kconf_update messageviewer
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/*kontact*
%_K6plug/pim6/kcms/kontact/*.so
%_K6xdgapp/*kontact*.desktop
%_K6data/messageviewer/about/default/*kontact*
%_K6cfg/*kontact*.kcfg
%_K6icon/*/*/apps/*kontact*.*
%_K6dbus_srv/*kontact*.service
%_datadir/metainfo/*.xml

#%files devel
#%_K6inc/kontact_version.h
#%_K6inc/kontact/
#%_K6link/lib*.so
#%_K6lib/cmake/kontact
#%_K6archdata/mkspecs/modules/qt_kontact.pri

%files -n %libkontactprivate
%_K6lib/libkontactprivate.so.%pim_sover
%_K6lib/libkontactprivate.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

