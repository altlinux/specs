%define rname kmines

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Games/Strategy
Summary: The classical mine sweeper
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kmines = %EVR
Obsoletes: kde5-kmines < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-phonon-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel  kf6-kdoctools-devel kf6-ki18n-devel
BuildRequires: kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifyconfig-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: kde6-libkdegames-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kmines
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kmines
%_K6data/kmines/
%_K6icon/*/*/apps/kmines.*
%_K6xdgapp/org.kde.kmines.desktop
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml


%changelog
* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build

