%define rname kigo

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Games/Boards
Summary: %rname is an open-source implementation of the popular Go game
Url: https://www.kde.org/applications/games/kigo
License: GPL-2.0-or-later

Requires: gnugo-core
Provides:  kde5-kigo = %EVR
Obsoletes: kde5-kigo < %EVR

Source0: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: qt6-declarative-devel qt6-svg-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kcrash-devel kf6-kdoctools-devel
BuildRequires: kf6-knewstuff-devel kf6-kio-devel kf6-ktextwidgets-devel
BuildRequires: kde6-libkdegames-devel

%description
%rname is an open-source implementation of the popular Go game. Go is a
strategic board game for two players. It is also known as igo (Japanese), weiqi
or wei ch'i (Chinese) or baduk (Korean). Go is noted for being rich in strategic
complexity despite its simple rules. The game is played by two players who
alternately place black and white stones (playing pieces, now usually made of
glass or plastic) on the vacant intersections of a grid of 19x19 lines (9x9 or
13x13 for easier games).

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data %rname knsrcfiles
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/%rname
%_K6xdgapp/org.kde.%{rname}.desktop
%_K6icon/hicolor/*/*/%{rname}*.*
%_K6data/%{rname}/
%_K6cfg/%{rname}.kcfg
%_K6data/knsrcfiles/*%{rname}*.knsrc
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml

%changelog
* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build

