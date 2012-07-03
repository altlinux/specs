%define WIP WIP4
Name: e-uae
Version: 0.8.29
Release: alt1
Group: Emulators
Summary: Experimental UAE Amiga Emulator
License: GPLv2
Source: %name-%version-%WIP.tar.bz2
Url: http://www.rcdrummond.net/uae/

# Automatically added by buildreq on Sun Apr 03 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libGL-devel libGLU-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel pkg-config xorg-xproto-devel
BuildRequires: libSDL-devel libalsa-devel libgtk+2-devel zlib-devel

%description
This is a version of UAE, the Ubiquitous Amiga Emulator, with an
emulation core largely based on WinUAE. It attempts to bring many of the
great features of WinUAE to non-Windows platforms. This version now
finally has a name, E-UAE, since that's what everybody was calling it
anyway. The 'E' can stand for anything you fancy. Experimental, extreme,
exciting, egalitarian, eggplant, ...

Currently it will build and run (with a varying degree of supported
features) on Linux and other Unices, Mac OS X, BeOS, AmigaOS itself
(either for 68k machines or PPC machines with AmigaOS 4.0 and the
AmigaOS clones MorphOS and AROS). OS X requires either LibSDL or an
X server for graphics output, but native graphics are supported on
AmigaOS and BeOS, although, at the moment, SDL is also preferred on BeOS
since the native driver is incomplete.

E-UAE is open-source software and is made available under the terms of
the GNU GPL. E-UAE is based on the work of dozens of contributors
including Bernd Schmidt (the original author and maintainer of UAE),
Bernie Meyer (the author of the x86 JIT compiler), Toni Wilen (the
current maintainer of WinUAE), and many more.

To make full use of E-UAE you will need access to an image of some
version of the Amiga Kickstart ROM (although UAE does include a ROM
emulation which may work with some old games). The Amiga Kickstart ROMs
are copyrighted material and may not be freely distributed (so don't ask
me for a copy). If you don't have an Amiga from which you can legally
make a ROM image, a selection of ROM images are available for purchase
online from Cloanto - publishers of the Amiga Forever distribution.1

%prep
%setup -n %name-%version-%WIP

%build
%configure --with-alsa --with-sdl-gl --with-sdl-gfx --enable-ui --enable-audio --disable-sdltest --disable-gtktest --enable-bsdsock

%make_build

%install
%makeinstall
mv %buildroot/%_bindir/uae %buildroot/%_bindir/%name

%files
%doc docs/*
%_bindir/*

%changelog
* Sun Apr 03 2011 Fr. Br. George <george@altlinux.ru> 0.8.29-alt1
- Initial build from scratch

