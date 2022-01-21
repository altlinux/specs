Name: mednafen
Version: 1.29.0
Release: alt1

Summary: Multi-consoles Emulator
Group: Emulators
License: GPLv2+
Url: http://mednafen.sourceforge.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>

# http://downloads.sourceforge.net/%%name/%%name-%%version.tar.bz2
Source: %name-%version.tar.xz
Patch1: mednafen-e2k.patch
Patch2: libco-ppc64v2-swap-global.patch

BuildRequires: gcc-c++ liblzo2-devel libsndfile-devel libflac-devel
BuildRequires: libcdio-devel libvorbis-devel libSDL_net-devel
BuildRequires: libsndfile-devel zlib-devel bison
BuildRequires: libSDL2-devel libGL-devel libX11-devel libGLU-devel
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
%patch1 -p1
#patch2 -p1

%build
# This package has a configure test which uses ASMs, but does not link the
# resultant .o files.  As such the ASM test is always successful in pure
# LTO mode.  We can use -ffat-lto-objects to force code generation.
#
# -ffat-lto-objects is the default for F33, but is expected to be removed
# in F34.  So we list it explicitly here.
%define _lto_cflags -flto=auto -ffat-lto-objects

CFLAGS="$RPM_OPT_FLAGS -Wl,-z,relro -Wl,-z,now"
CXXFLAGS="$RPM_OPT_FLAGS -Wl,-z,relro -Wl,-z,now"

export CFLAGS
export CXXFLAGS

%configure --disable-rpath \
	    --with-external-lzo



%make_build

%install

%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog TODO README* Documentation/*
%_bindir/%name


%changelog
* Fri Jan 21 2022 Ilya Mashkin <oddity@altlinux.ru> 1.29.0-alt1
- version 1.29.0

* Sat Nov 27 2021 Ilya Mashkin <oddity@altlinux.ru> 1.28.0-alt1
- version 1.28.0

* Mon Jun 14 2021 Ilya Mashkin <oddity@altlinux.ru> 1.27.1-alt1
- version 1.27.1

* Tue Apr 13 2021 Ilya Mashkin <oddity@altlinux.ru> 1.27.0-alt1
- version 1.27.0

* Sat Mar 20 2021 Ilya Mashkin <oddity@altlinux.ru> 1.26.1-alt2
- fix for e2k

* Tue Mar 16 2021 Ilya Mashkin <oddity@altlinux.ru> 1.26.1-alt1
- version 1.26.1

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

