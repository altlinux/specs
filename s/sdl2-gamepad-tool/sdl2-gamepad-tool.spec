Name:    sdl2-gamepad-tool
Version: 1.4.2
Release: alt1

Summary: SDL2 Gamepad Tool
License: MIT
Group:   System/Configuration/Hardware
URL:     https://generalarcade.com/gamepadtool/
VCS:     https://github.com/General-Arcade/sdl2-gamepad-tool

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: qt5-base-devel libSDL2-devel
Requires: hicolor-icon-theme

%description
Simple GUI tool to create and modify gamepad mappings for games that use the
SDL2 Game Controller API.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/gamepad-tool
%_desktopdir/gamepad-tool.desktop
%dir %_datadir/gamepad-tool
%_datadir/gamepad-tool/gamecontrollerdb.txt
%_iconsdir/hicolor/256x256/apps/gamepad-tool.png

%changelog
* Mon Aug 24 2026 Sergey Palcheh <minergenon@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus
