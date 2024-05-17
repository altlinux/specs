%global __find_debuginfo_files %nil

Summary:	An interface for emulator and game ports
Name:		libretro
Version:	20240406
Release:	alt2
# Actually, various for each core but mostly GPLv2
License:	GPL2
Group:		Emulators
Url:		http://www.libretro.com
# fetched via libretro-fetch.sh from git and re-packed
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	nasm gcc gcc-c++
# /usr/bin/xxd is needed for libretro-fuse build
BuildRequires:	build-essential
BuildRequires:	libstdc++-devel
BuildRequires:	vim-common
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpcap)
BuildRequires:	libstdc++-devel-static

Requires: %name-2048
Requires: %name-bluemsx
Requires: %name-bsnes2014_accuracy
Requires: %name-bsnes2014_balanced
Requires: %name-bsnes2014_performance
Requires: %name-bsnes_mercury_accuracy
Requires: %name-bsnes_mercury_balanced
Requires: %name-bsnes_mercury_performance
Requires: %name-chimerasnes
Requires: %name-fbneo
Requires: %name-fceumm
Requires: %name-fmsx
Requires: %name-gambatte
Requires: %name-genesis_plus_gx
Requires: %name-gpsp
Requires: %name-handy
Requires: %name-hatari
Requires: %name-mednafen_gba
Requires: %name-mednafen_lynx
Requires: %name-mednafen_ngp
Requires: %name-mednafen_pce_fast
Requires: %name-mednafen_pcfx
Requires: %name-mednafen_supergrafx
Requires: %name-mednafen_vb
Requires: %name-mednafen_wswan
Requires: %name-meteor
Requires: %name-mgba
Requires: %name-mu
Requires: %name-nestopia
Requires: %name-numero
Requires: %name-nxengine
Requires: %name-o2em
Requires: %name-Opera
Requires: %name-picodrive
Requires: %name-prboom
Requires: %name-prosystem
Requires: %name-quicknes
Requires: %name-snes9x2005
Requires: %name-snes9x2010
Requires: %name-snes9x
Requires: %name-stella
Requires: %name-tgbdual
Requires: %name-vbam
Requires: %name-vba_next
Requires: %name-vecx
Requires: %name-virtualjaguar

ExcludeArch: ppc64le

%description
For each emulator 'core', RetroArch makes use of a library API that we like
to call 'libretro'.

Think of libretro as an interface for emulator and game ports. You can make
a libretro port once and expect the same code to run on all the platforms
that RetroArch supports. It's designed with simplicity and ease of use in
mind so that the porter can worry about the port at hand instead of having
to wrestle with an obfuscatory API.

The purpose of the project is to help ease the work of the emulator/game
porter by giving him an API that allows him to target multiple platforms
at once without having to redo any code. He doesn't have to worry about
writing input/video/audio drivers - all of that is supplied to him by
RetroArch. All he has to do is to have the emulator port hook into the
libretro API and that's it - we take care of the rest.

%package Opera
Summary:	Opera/4DO core for libretro (3DO)
Group:		Emulators
Provides:	libretro-core

%description Opera
Opera is a fork of 4DO, originally a port of 4DO, itself a fork of FreeDO, to libretro.

The fork/rename occurred due to the original 4DO project being dormant and
to differenciate the project due to new development and focus.

One of several BIOS ROMs must be placed into your RetroArch / libretro "System Directory" folder.
"norsa" versions have the RSA encryption check disabled which should allow unsigned software to run.

%package fbneo
Summary:	Final Burn core for libretro (arcade)
Group:		Emulators
Provides:	libretro-core 

%description fbneo
Final Burn  core for libretro. It's used to run arcade games.

It should be able to load:
- Capcom CPS-1 and CPS-2
- SNK Neo-Geo
- Toaplan
- Cave hardware
- and various games on miscellaneous hardware

%package fceumm
Summary:	FCE Ultra mappers modified core for libretro (NES)
Group:		Emulators
Provides:	libretro-core 

%description fceumm
FCE Ultra mappers modified core for libretro. It's used to run Nintendo games.

%package fmsx
Summary:	fMSX core for libretro (MSX)
Group:		Emulators
Provides:	libretro-core 

%description fmsx
fMSX core for libretro. It's used to run MSX games.

%package gambatte
Summary:	Gambatte core for libretro (GBC)
Group:		Emulators
Provides:	libretro-core 

%description gambatte
Gambatte core for libretro. It's used to run Game Boy Color games.

%package gpsp
Summary:	gpSP core for libretro (GBA)
Group:		Emulators
Provides:	libretro-core 

%description gpsp
gpSP core for libretro. It's used to run Game Boy Advance games.

It requires GBA BIOS (gba_bios.bin) so place it in your RetroArch/libretro
"System Directory" folder.

%package handy
Summary:	Handy core for libretro (LNX)
Group:		Emulators
Provides:	libretro-core 

%description handy
Handy core for libretro. It's used to run Atari Lynx games.

%package meteor
Summary:	Meteor core for libretro (GBA)
Group:		Emulators
Provides:	libretro-core 

%description meteor
Meteor core for libretro. It's used to run Game Boy Advance games.

%package mgba
Summary:	mGBA core for libretro (GBA)
Group:		Emulators
Provides:	libretro-core 

%description mgba
mGBA core for libretro. It's used to run Game Boy Advance games.

%package nestopia
Summary:	Nestopia core for libretro (NES)
Group:		Emulators
Provides:	libretro-core 

%description nestopia
Nestopia core for libretro. It's used to run Nintendo games.

%package nxengine
Summary:	NXEngine core for libretro (Cave Story)
Group:		Emulators
Provides:	libretro-core 

%description nxengine
NXEngine core for libretro. It's used to run Cave Story (Doukutsu Monogatari).

%package o2em
Summary:	O2EM core for libretro (Odyssey 2)
Group:		Emulators
Provides:	libretro-core 

%description o2em
O2EM core for libretro. It's used to run Magnavox Odyssey 2 & Videopac+ games.

Place "o2rom.bin" in your RetroArch/libretro "System Directory" folder.

%package quicknes
Summary:	QuickNES core for libretro (NES)
Group:		Emulators
Provides:	libretro-core 

%description quicknes
QuickNES core for libretro. It's used to run Nintendo games.

%package tgbdual
Summary:	TGB Dual core for libretro (GBC)
Group:		Emulators
Provides:	libretro-core 

%description tgbdual
TGB Dual core for libretro. It's used to run Game Boy and Game Boy Color games.

%package vbam
Summary:	VBA-M core for libretro (GBA)
Group:		Emulators
Provides:	libretro-core 

%description vbam
VBA-M core for libretro. It's used to run Game Boy Advance games.

%package vecx
Summary:	VECX core for libretro (Vectrex)
Group:		Emulators
Provides:	libretro-core 

%description vecx
VECX core for libretro. It's used to run Vectrex games.

The original Vectrex games are freely available for non-commercial use.

%package 2048
Summary:	2048 game core for libretro
Group:		Emulators
Provides:	libretro-core 

%description 2048
%summary

%package bluemsx
Summary: bluemsx core for libretro
Group: Emulators
Provides: libretro-core

%description bluemsx
bluemsx core for libretro. It's used to run MSX games

%package bsnes2014_accuracy
Summary: bsnes2014_accuracy core for libretro
Group: Emulators
Provides: libretro-core

%description bsnes2014_accuracy
bsnes2014_accuracy core for libretro. It's used to run SNES games

%package bsnes2014_balanced
Summary: bsnes2014_balanced core for libretro
Group: Emulators
Provides: libretro-core

%description bsnes2014_balanced
bsnes2014_balanced core for libretro. It's used to run SNES games

%package bsnes2014_performance
Summary: bsnes2014_performance core for libretro
Group: Emulators
Provides: libretro-core

%description bsnes2014_performance
bsnes2014_performance core for libretro. It's used to run SNES games

%package bsnes_mercury_accuracy
Summary: bsnes_mercury_accuracy core for libretro
Group: Emulators
Provides: libretro-core

%description bsnes_mercury_accuracy
bsnes_mercury_accuracy core for libretro.

%package bsnes_mercury_balanced
Summary: bsnes_mercury_balanced core for libretro
Group: Emulators
Provides: libretro-core

%description bsnes_mercury_balanced
bsnes_mercury_balanced core for libretro. It's used to run SNES games

%package bsnes_mercury_performance
Summary: bsnes_mercury_performance core for libretro
Group: Emulators
Provides: libretro-core

%description bsnes_mercury_performance
bsnes_mercury_performance core for libretro. It's used to run SNES games

%package chimerasnes
Summary: chimerasnes core for libretro
Group: Emulators
Provides: libretro-core

%description chimerasnes
chimerasnes core for libretro. It's used to run SNES games

%package genesis_plus_gx
Summary: genesis_plus_gx core for libretro
Group: Emulators
Provides: libretro-core

%description genesis_plus_gx
genesis_plus_gx core for libretro.

%package hatari
Summary: hatari core for libretro
Group: Emulators
Provides: libretro-core

%description hatari
hatari core for libretro.

%package mednafen_gba
Summary: mednafen_gba core for libretro
Group: Emulators
Provides: libretro-core

%description mednafen_gba
mednafen_gba core for libretro.

%package mednafen_lynx
Summary: mednafen_lynx core for libretro
Group: Emulators
Provides: libretro-core

%description mednafen_lynx
mednafen_lynx core for libretro.

%package mednafen_ngp
Summary: mednafen_ngp core for libretro
Group: Emulators
Provides: libretro-core

%description mednafen_ngp
mednafen_ngp core for libretro.

%package mednafen_pce_fast
Summary: mednafen_pce_fast core for libretro
Group: Emulators
Provides: libretro-core

%description mednafen_pce_fast
mednafen_pce_fast core for libretro.

%package mednafen_pcfx
Summary: mednafen_pcfx core for libretro
Group: Emulators
Provides: libretro-core

%description mednafen_pcfx
mednafen_pcfx core for libretro.

%package mednafen_supergrafx
Summary: mednafen_supergrafx core for libretro
Group: Emulators
Provides: libretro-core

%description mednafen_supergrafx
mednafen_supergrafx core for libretro.

%package mednafen_vb
Summary: mednafen_vb core for libretro
Group: Emulators
Provides: libretro-core

%description mednafen_vb
mednafen_vb core for libretro.

%package mednafen_wswan
Summary: mednafen_wswan core for libretro
Group: Emulators
Provides: libretro-core

%description mednafen_wswan
mednafen_wswan core for libretro.

%package mu
Summary: mu core for libretro
Group: Emulators
Provides: libretro-core

%description mu
mu core for libretro.

%package numero
Summary: numero core for libretro
Group: Emulators
Provides: libretro-core

%description numero
numero core for libretro.

%package picodrive
Summary: picodrive core for libretro
Group: Emulators
Provides: libretro-core

%description picodrive
picodrive core for libretro.

%package prboom
Summary: prboom core for libretro
Group: Emulators
Provides: libretro-core

%description prboom
prboom core for libretro.

%package prosystem
Summary: prosystem core for libretro
Group: Emulators
Provides: libretro-core

%description prosystem
prosystem core for libretro.

%package snes9x2005
Summary: snes9x2005 core for libretro
Group: Emulators
Provides: libretro-core

%description snes9x2005
snes9x2005 core for libretro.

%package snes9x2010
Summary: snes9x2010 core for libretro
Group: Emulators
Provides: libretro-core

%description snes9x2010
snes9x2010 core for libretro.

%package snes9x
Summary: snes9x core for libretro
Group: Emulators
Provides: libretro-core

%description snes9x
snes9x core for libretro.

%package stella
Summary: stella core for libretro
Group: Emulators
Provides: libretro-core

%description stella
stella core for libretro.

%package vba_next
Summary: vba_next core for libretro
Group: Emulators
Provides: libretro-core

%description vba_next
vba_next core for libretro.

%package virtualjaguar
Summary: virtualjaguar core for libretro
Group: Emulators
Provides: libretro-core

%description virtualjaguar
virtualjaguar core for libretro.

%package bsnes_cplusplus98
Summary:  bsnes_cplusplus98 core for libretro
Group: Emulators
Provides: libretro-core

%description  bsnes_cplusplus98
 bsnes_cplusplus98 core for libretro.

%package dinothawr
Summary:  dinothawr core for libretro
Group: Emulators
Provides: libretro-core

%description  dinothawr
 dinothawr core for libretro.

%package gw
Summary: gw core for libretro
Group: Emulators
Provides: libretro-core

%description gw
 gw core for libretro.

%package lutro
Summary:  lutro core for libretro
Group: Emulators
Provides: libretro-core

%description lutro
 lutro core for libretro.

%package mame2003
Summary: mame2003 core for libretro
Group: Emulators
Provides: libretro-core

%description mame2003
 mame2003 core for libretro.

# needs jit
%ifnarch %e2k
%package mednafen_psx_hw
Summary: mednafen_psx_hw core for libretro
Group: Emulators
Provides: libretro-core

%description mednafen_psx_hw
 mednafen_psx_hw core for libretro.

%package mednafen_psx
Summary:  mednafen_psx core for libretro
Group: Emulators
Provides: libretro-core

%description  mednafen_psx
 mednafen_psx core for libretro.

%package pcsx_rearmed
Summary: pcsx_rearmed core for libretro
Group: Emulators
Provides: libretro-core

%description pcsx_rearmed
 pcsx_rearmed core for libretro.
%endif

%package tyrquake
Summary: tyrquake core for libretro
Group: Emulators
Provides: libretro-core

%description tyrquake
 tyrquake core for libretro
 
%prep
%setup -q
%ifarch %e2k
# error: in "goto *expr", expr must have type "void *"
# but "labels as values" are slow with LCC, better to disable it
sed -i '/defined(__ICC)/c #if 0' \
	libretro-mednafen_supergrafx/mednafen/pce_fast/ioread.inc \
	libretro-mednafen_pce_fast/libretro.cpp
sed -i 's/#ifdef _MSC_VER/#if 1/' libretro-mednafen_{vb,pcfx}/mednafen/hw_cpu/v810/v810_oploop.inc
sed -i 's/HAVE_COMPUTED_GOTO/0/' libretro-beetle_psx/mednafen/psx/cpu.cpp
%endif

%build

./libretro-build.sh

# ProSystem system files path
mkdir -p %{buildroot}%{_libexecdir}/%{name}/prosystem/

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
./libretro-install.sh %{buildroot}%{_libexecdir}/%{name}

# Core info files placed into separate package
rm -f %{buildroot}%{_libexecdir}/%{name}/*.info

%files

%files Opera
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/opera_libretro.so

%files fbneo
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/fbneo_libretro.so

%files fceumm
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/fceumm_libretro.so

%files fmsx
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/fmsx_libretro.so

%files gambatte
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/gambatte_libretro.so

%files gpsp
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/gpsp_libretro.so

%files handy
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/handy_libretro.so

%files meteor
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/meteor_libretro.so

%files mgba
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mgba_libretro.so

%files nestopia
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/nestopia_libretro.so

%files nxengine
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/nxengine_libretro.so

%files o2em
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/o2em_libretro.so

%files quicknes
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/quicknes_libretro.so

%files tgbdual
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/tgbdual_libretro.so

%files vbam
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/vbam_libretro.so

%files vecx
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/vecx_libretro.so

%files 2048
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/2048_libretro.so

%files bluemsx
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/bluemsx_libretro.so

%files bsnes2014_accuracy
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/bsnes2014_accuracy_libretro.so

%files bsnes2014_balanced
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/bsnes2014_balanced_libretro.so

%files bsnes2014_performance
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/bsnes2014_performance_libretro.so

%files bsnes_mercury_accuracy
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/bsnes_mercury_accuracy_libretro.so

%files bsnes_mercury_balanced
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/bsnes_mercury_balanced_libretro.so

%files bsnes_mercury_performance
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/bsnes_mercury_performance_libretro.so

%files chimerasnes
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/chimerasnes_libretro.so

%files genesis_plus_gx
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/genesis_plus_gx_libretro.so

%files hatari
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/hatari_libretro.so

%files mednafen_gba
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mednafen_gba_libretro.so

%files mednafen_lynx
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mednafen_lynx_libretro.so

%files mednafen_ngp
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mednafen_ngp_libretro.so

%files mednafen_pce_fast
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mednafen_pce_fast_libretro.so

%files mednafen_pcfx
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mednafen_pcfx_libretro.so

%files mednafen_supergrafx
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mednafen_supergrafx_libretro.so

%files mednafen_vb
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mednafen_vb_libretro.so

%files mednafen_wswan
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mednafen_wswan_libretro.so

%files mu
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mu_libretro.so

%files numero
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/numero_libretro.so

%files picodrive
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/picodrive_libretro.so

%files prboom
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/prboom_libretro.so

%files prosystem
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/prosystem_libretro.so

%files snes9x2005
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/snes9x2005_libretro.so

%files snes9x2010
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/snes9x2010_libretro.so

%files snes9x
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/snes9x_libretro.so

%files stella
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/stella_libretro.so

%files vba_next
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/vba_next_libretro.so

%files virtualjaguar
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/virtualjaguar_libretro.so

%files bsnes_cplusplus98
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/bsnes_cplusplus98_libretro.so

%files dinothawr
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/dinothawr_libretro.so

%files gw
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/gw_libretro.so

%files lutro
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/lutro_libretro.so

%files mame2003
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mame2003_libretro.so

%ifnarch %e2k
%files mednafen_psx_hw
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mednafen_psx_hw_libretro.so

%files mednafen_psx
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mednafen_psx_libretro.so

%files pcsx_rearmed
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/pcsx_rearmed_libretro.so
%endif

%files tyrquake
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/tyrquake_libretro.so

%changelog
* Thu May 16 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 20240406-alt2
- Fixed build for Elbrus

* Sat Apr  6 2024  Artyom Bystrov <arbars@altlinux.org> 20240406-alt1
- update to new version
- added new cores:
  bsnes_cplusplus98
  dinothawr
  gw
  lutro
  mame2003
  mednafen_psx
  mednafen_psx_hw
  pcsx_rearmed
  tyrquake 

* Wed Mar 20 2024 Artyom Bystrov <arbars@altlinux.org> 20200729-alt1
- Initial commit for Sisyphus
