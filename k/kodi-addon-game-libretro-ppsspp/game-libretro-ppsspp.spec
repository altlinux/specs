Name: kodi-addon-game-libretro-ppsspp
Version: 0.0.1.29
Release: alt1

Summary: Libretro PPSSPP for Kodi
License: GPLv2
Group: Video
URL: https://github.com/kodi-game/game.libretro.ppsspp
VCS: https://github.com/kodi-game/game.libretro.ppsspp

ExcludeArch: i586

Requires: ppsspp-libretro
Autoreq: yes, nosymlinks

Source0: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel ppsspp-libretro

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
ln -svf ../../../../lib/libretro/ppsspp_libretro.so \
 %buildroot%_libdir/kodi/addons/game.libretro.ppsspp/game.libretro.ppsspp.so

%files
%_libdir/kodi/addons/game.libretro.ppsspp
%_datadir/kodi/addons/game.libretro.ppsspp

%changelog
* Fri Sep 04 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.1.29-alt1
- 0.0.1.29 released

* Tue Mar 25 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.1.28-alt1
- 0.0.1.28 released

