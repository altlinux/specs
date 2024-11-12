%define rname granatier

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Games/Arcade
Summary: Bomberman game
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-granatier = %EVR
Obsoletes: kde5-granatier < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: libssl-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: kf6-kcompletion-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel kf6-knewstuff-devel
BuildRequires: kf6-kservice-devel kf6-kxmlgui-devel kf6-kcolorscheme-devel
BuildRequires: kde6-libkdegames-devel

%description
Bomberman game.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data granatier
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/granatier
%_K6data/granatier
%_K6xdgapp/*granatier*.desktop
%_K6cfg/granatier.kcfg
%_K6icon/hicolor/*/apps/granatier.*
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml

%changelog
* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build

