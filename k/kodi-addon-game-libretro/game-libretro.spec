Name: kodi-addon-game-libretro
Version: 22.7.0
Release: alt1

Summary: Libretro wrapper for Kodi
License: GPLv2
Group: Video
URL: https://github.com/kodi-game/game.libretro
VCS: https://github.com/kodi-game/game.libretro

ExcludeArch: i586

Source0: %name-%version.tar
Source1: libretro-common.tar.gz
Source2: rcheevos.tar.gz

BuildRequires: cmake gcc-c++ kodi-devel tinyxml-devel

%description
%summary

%prep
%setup

%build
%cmake	-DENABLE_INTERNAL_LIBRETROCOMMON=ON -DENABLE_INTERNAL_RCHEEVOS=ON \
%ifndef bootstrap
	-DLIBRETROCOMMON_URL=%SOURCE1 \
	-DRCHEEVOS_URL=%SOURCE2 \
%endif
	#

%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/kodi/addons/game.libretro
%_datadir/kodi/addons/game.libretro

%changelog
* Fri Sep 04 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 22.7.0-alt1
- 22.7.0 released

* Wed Apr 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 21.0.8-alt2
- fixed FTBFS with cmake4

* Tue Mar 25 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 21.0.8-alt1
- 21.0.8 released
