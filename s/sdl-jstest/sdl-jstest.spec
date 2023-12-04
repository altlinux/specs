Name:    sdl-jstest
Version: 0.2.2
Release: alt1

Summary: Simple SDL joystick test application for the console
License: GPL-3.0
Group:   Games/Other
Url:     https://github.com/Grumbel/sdl-jstest

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libSDL2-devel libSDL-devel libncursesw-devel

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc *.md
%_bindir/*
%_man1dir/*
%_iconsdir/hicolor/scalable/apps/sdl-jstest.svg
%_iconsdir/hicolor/scalable/apps/sdl2-jstest.svg
%_datadir/%name/gamecontrollerdb.txt

%changelog
* Mon Dec 04 2023 Artyom Bystrov <arbars@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus
