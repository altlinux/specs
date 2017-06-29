Name: mednafen
Version: 0.9.45.1
Release: alt1

Summary: Multi-consoles Emulator
Group: Emulators
License: GPLv2+
Url: http://mednafen.sourceforge.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>

# http://downloads.sourceforge.net/%%name/%%name-%%version.tar.bz2
Source: %name-%version.tar.bz2

BuildRequires: gcc-c++
BuildRequires: libcdio-devel libvorbis-devel libSDL_net-devel
BuildRequires: libsndfile-devel zlib-devel bison
BuildRequires: libSDL-devel libGL-devel libX11-devel libGLU-devel
BuildRequires: libXaw-devel libXext-devel libXp-devel libXpm-devel xorg-cf-files
BuildRequires: libXrandr-devel libXi-devel libXcursor-devel libXinerama-devel

%description
A portable command-line driven, multi-system emulator which uses OpenGL and
SDL.
The following systems are supported:
* Atari Lynx
* Neo Geo Pocket (Color)
* WonderSwan
* GameBoy (Color)
* GameBoy Advance
* Nintendo Entertainment System
* Super Nintendo Entertainment System/Super Famicom
* Virtual Boy
* PC Engine/TurboGrafx 16 (CD)
* SuperGrafx
* PC-FX
* Sega Game Gear
* Sega Genesis/Megadrive
* Sega Master System
* Sony PlayStation

Mednafen has the ability to remap hotkey functions and virtual system
inputs to a keyboard, a joystick or both simultaneously. Save states are
supported, as is real-time game rewinding. Screen snapshots may be taken at the
press of a button and are saved in the popular PNG file format. To play Atari
Lynx games you will also need lynxboot.img which is not included for legal
reasons.


%prep
%setup -n %name

%build
%configure
%make_build

%install

%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog TODO README* Documentation/*
%_bindir/%name


%changelog
* Thu Jun 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.45.1-alt1
- Updated to 0.9.45.1

* Thu Aug 06 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.38.5-alt1
- 0.9.38.5
- built against libcdio.so.16

* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.13-alt3.1
- Fixed build with zlib 1.2.7

* Mon Apr 23 2012 Ilya Mashkin <oddity@altlinux.ru> 0.8.13-alt3
- version 0.8.D.3

* Mon Dec 20 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.13-alt2
- Fix Build

* Sun Jul 25 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.13-alt1
- version 0.8.D

* Wed Nov 18 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.12-alt2
- rebuild with new libcdio

* Thu Sep 24 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.12-alt1
- Initial build for ALT Linux
- version 0.8.C

