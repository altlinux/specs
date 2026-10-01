%define rname skladnik

Name: %rname
Version: 26.08.1
Release: alt1
%K6init

Group: Games/Boards
Summary: Sokoban game
Url: https://invent.kde.org/games/skladnik
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel
BuildRequires: kde6-libkdegames-devel

%description
Skladnik is an implementation of the Japanese warehouse keeper game "sokoban".

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data %rname
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/%rname
%_K6xdgapp/*%{rname}*.desktop
%_K6icon/hicolor/*/apps/*%{rname}*
%_K6data/%{rname}/
%_datadir/metainfo/*%{rname}*.xml

%changelog
* Thu Oct 01 2026 Sergey V Turchin <zerg@altlinux.org> 26.08.1-alt1
- initial build
