%define rname knavalbattle

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Games/Strategy
Summary: Battleship game with built-in game server
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-knavalbattle = %EVR
Obsoletes: kde5-knavalbattle < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kdnssd-devel kf6-kcolorscheme-devel
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-sonnet-devel kf6-kcrash-devel
BuildRequires: kde6-libkdegames-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data knavalbattle kconf_update
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/knavalbattle
%_K6data/knavalbattle/
%_K6icon/*/*/apps/knavalbattle.*
%_K6xdgapp/org.kde.knavalbattle.desktop
%_datadir/metainfo/*.xml


%changelog
* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build

