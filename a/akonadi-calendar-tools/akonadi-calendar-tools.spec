%define rname akonadi-calendar-tools

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Akonadi Calendar Tools
Url: http://www.kde.org
License: GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches
Provides: kde5-akonadi-calendar-tools = %EVR
Obsoletes: kde5-akonadi-calendar-tools < %EVR

Requires: akonadi-calendar

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: boost-devel
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-kcontacts-devel kf6-kcalendarcore-devel
BuildRequires: kf6-ki18n-devel kf6-kitemmodels-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: kidentitymanagement-devel kmime-devel kpimtextedit-devel
BuildRequires: akonadi-calendar-devel akonadi-contacts-devel akonadi-devel calendarsupport-devel
BuildRequires: kcalutils-devel kf6-kcontacts-devel kidentitymanagement-devel kmime-devel kpimtextedit-devel
BuildRequires: kde6-libkdepim-devel

%description
Akonadi Calendar Tools.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/*alendar*
%_K6xdgapp/*alendar*.desktop
%_K6icon/*/*/apps/*alendar*.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

