%define rname kreversi

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Games/Boards
Summary: Old reversi board game, also known as othello
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdeclarative-devel 
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kpackage-devel
BuildRequires: kde6-libkdegames-devel

%description
KReversi is a simple one player strategy game played against the computer.
If a player's piece is captured by an opposing player, that piece is turned over
to reveal the color of that player. A winner is declared when one player has more
pieces of his own color on the board and there are no more possible moves.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kreversi
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kreversi
%_K6data/kreversi/
%_K6icon/hicolor/*/apps/*kreversi*.*
%_K6icon/hicolor/*/actions/*moves*.*
%_K6xdgapp/*kreversi*.desktop
%_K6notif/*kreversi*
%_datadir/metainfo/*.xml

%changelog
* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build

