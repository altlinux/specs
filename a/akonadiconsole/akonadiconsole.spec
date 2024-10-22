%define rname akonadiconsole

%define sover 6
%define libakonadiconsole libakonadiconsole%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Akonadi Console
Url: http://www.kde.org
License: LGPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches
Provides: kde5-akonadiconsole = %EVR
Obsoletes: kde5-akonadiconsole < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: boost-devel libassuan-devel libsasl2-devel libxapian-devel
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-ki18n-devel kf6-kcalendarcore-devel kf6-kcontacts-devel
BuildRequires: kf6-kitemmodels-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel
BuildRequires: kf6-kitemviews-devel kf6-ktexttemplate-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: kidentitymanagement-devel kimap-devel kmime-devel kpimtextedit-devel
BuildRequires: akonadi-calendar-devel akonadi-contacts-devel akonadi-devel akonadi-mime-devel calendarsupport-devel
BuildRequires: kde6-libkdepim-devel messagelib-devel pimcommon-devel akonadi-search-devel
BuildRequires: kde6-libkleo-devel

%description
Akonadi Management and Debugging Console.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-akonadiconsole-common = %EVR
Obsoletes: kde5-akonadiconsole-common < %EVR
%description common
%name common package

%package -n %libakonadiconsole
Group: System/Libraries
Summary: %name library
Requires: %name-common
Obsoletes: libakonadiconsole5 < %EVR
%description -n %libakonadiconsole
%name library

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kconf_update
%find_lang %name --with-kde --all-name

desktop-file-install \
    --mode=0755 --dir %buildroot/%_K6xdgapp \
    --add-category=System \
    --remove-category=Development \
    %buildroot/%_K6xdgapp/org.kde.akonadiconsole.desktop

%files common -f %name.lang

%files
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/*akonadiconsole*
%_K6xdgapp/*akonadiconsole*
%_K6icon/*/*/apps/*akonadiconsole*

%files -n %libakonadiconsole
%_K6lib/libakonadiconsole.so.%sover
%_K6lib/libakonadiconsole.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

