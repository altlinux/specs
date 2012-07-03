Name: mednafen
Version: 0.8.13
Release: alt3

Summary: Multi-consoles Emulator
License: GPLv2+
Url: http://mednafen.sourceforge.net/

Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: Emulators
Source0: http://downloads.sourceforge.net/%name/%name-0.8.D.3.tar.bz2
BuildRequires: libcdio-devel libvorbis-devel libSDL_net-devel
BuildRequires: libsndfile-devel zlib-devel bison gettext
 #gcc gcc-c++
BuildRequires: gcc4.4 gcc4.4-c++
BuildRequires: libSDL-devel libGL-devel libX11-devel libGLU-devel
BuildRequires: libXaw-devel libXext-devel libXp-devel libXpm-devel xorg-cf-files
BuildRequires: libXrandr-devel libXi-devel libXcursor-devel libXinerama-devel


%description
A portable command-line driven, multi-system emulator which uses OpenGL and
SDL. It emulates the following:
* Atari Lynx
* Famicom
* GameBoy (Color)
* GameBoy Advance
* Neo Geo Pocket (Color)
* NES (NTSC & PAL)
* PC Engine
* TurboGrafx 16 (CD)
* SuperGrafx
* PC-FX
Mednafen has the ability to remap hotkey functions and virtual system
inputs to a keyboard, a joystick or both simultaneously. Save states are
supported, as is real-time game rewinding. Screen snapshots may be taken at the
press of a button and are saved in the popular PNG file format. To play Atari
Lynx games you will also need lynxboot.img which is not included for legal
reasons.


%prep
%setup -q -n %name

find ./src -type f -exec chmod 644 '{}' +
find ./src -type d -exec chmod 755 '{}' +

%build
export CC=gcc-4.4 CXX=g++-4.4
#autoreconf -i
%configure
%make

%install

%makeinstall
%find_lang %name

%files -f %name.lang
%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL TODO Documentation/*
%_bindir/%name


%changelog
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

