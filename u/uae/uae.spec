Name: uae
Version: 0.8.29
Release: alt1
Group: Emulators
Summary: UAE Amiga Emulator
License: GPLv2
Source: %name-%version.tar.bz2
Url: http://www.amigaemulator.org/

# Automatically added by buildreq on Sun Apr 03 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel pkg-config xorg-xproto-devel
BuildRequires: libSDL-devel libalsa-devel libgtk+2-devel

%description
This version of UAE emulates:

- A 68000, 68010 or 68020 CPU, optionally a 68881 FPU
- OCS Graphics Chipset, plus big blits from the ECS Chipset
- Up to 2MB Chip RAM and up to 8MB Fast RAM, or 8MB Chip RAM without Fast RAM
- Up to 64MB Zorro III Fast RAM, independent of Chip RAM setting (68020 only)
- Up to 1MB Slow RAM, for extended compatibility with problem software
- Up to 8MB of graphics card memory, usable by software that supports
  Picasso 96 compatible graphics cards
- 4 x 3.5" floppy disk drives (DF0:, DF1:, DF2: and DF3:). It's not possible to
  read Amiga disks, so these are emulated with disk files.
- A hard-disk: either a harddisk image file or part of the native filesystem
- Joystick support (with option of mapping joystick to numeric keypad)
- Mouse support
- Ability to run in various screen modes (for better display quality or
  better speed)
- Full stereo sound support, consisting of 4 x 8bit channels
- Beta parallel and serial port support
- some other things which don't work well enough to mention them here...

%prep
%setup

%build
%configure  --with-sdl --with-x --with-sdl-gfx --with-alsa
%make_build

%install
%makeinstall
install -sD readdisk %buildroot/%_bindir/%name-readdisk

%files
%doc docs/*
%_bindir/*
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Sun Apr 03 2011 Fr. Br. George <george@altlinux.ru> 0.8.29-alt1
- Autobuild version bump to 0.8.29

