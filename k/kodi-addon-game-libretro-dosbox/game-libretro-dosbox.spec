Name: kodi-addon-game-libretro-dosbox
Version: 0.74.0.31
Release: alt1

Summary: Libretro dosbox for Kodi
License: GPLv2
Group: Video
Url: https://github.com/kodi-game/game.libretro.dosbox

Requires: libretro-computers-dosbox
Autoreq: yes, nosymlinks

Source0: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel libretro-computers-dosbox

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
ln -svf ../../../../lib/libretro/dosbox_libretro.so \
 %buildroot%_libdir/kodi/addons/game.libretro.dosbox/game.libretro.dosbox.so

%files
%_libdir/kodi/addons/game.libretro.dosbox
%_datadir/kodi/addons/game.libretro.dosbox

%changelog
* Tue Mar 25 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.74.0.31-alt1
- 0.74.0.31 released

