%define _unpackaged_files_terminate_build 1

Name: tetzle
Version: 3.0.3
Release: alt1

Summary: Jigsaw puzzle game
License: GPL-3.0-or-later
Group: Games/Puzzles
Url: https://github.com/gottcode/tetzle

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel

%description
Any image can be imported and used to create puzzles with a wide
range of sizes. Games are saved automatically, and you can select
between currently in progress games.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc ChangeLog COPYING CREDITS README
%_bindir/%name
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/*/apps/%{name}.png
%_iconsdir/hicolor/scalable/apps/%{name}.svg
%dir %_datadir/%name/
%_datadir/%name/*
%_datadir/metainfo/%{name}.appdata.xml
%_man6dir/%{name}.6*

%changelog
* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 3.0.3-alt1
- Initial build for Sisyphus
