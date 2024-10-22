%define rname zanshin

%define sover 6
%define libzanshin libzanshin%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Office
Summary: TODO Manager
Url: http://www.kde.org
License: LGPL-2.0-or-later and GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-zanshin = %EVR
Obsoletes: kde5-zanshin < %EVR
Requires: akonadi

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kio-devel kf6-kitemmodels-devel kf6-kpackage-devel kf6-kparts-devel
BuildRequires: kf6-krunner-devel kf6-ktextwidgets-devel
BuildRequires: akonadi-calendar-devel akonadi-devel kontactinterface-devel
BuildRequires: kidentitymanagement-devel kpimtextedit-devel

%description
A Getting Things Done application which aims at getting your mind like water.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/zanshin*
%_K6plug/kf6/krunner/*zanshin*.so
%_K6plug/pim6/kontact/*zanshin*.so
%_K6plug/*zanshin*.so
%_K6xdgapp/*zanshin*.desktop
%_K6icon/hicolor/*/apps/*zanshin*.*
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

