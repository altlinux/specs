Name: xbacklight
Version: 1.1.1
Release: alt1
Summary: adjust backlight brightness using RandR extension
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXrandr-devel libXrender-devel xorg-util-macros

%description
Xbacklight is used to adjust the backlight brightness where  supported.
It  finds  all  outputs on the X server supporting backlight brightness
control and changes them all in the same way.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Sat Oct 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Fri Sep 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- initial release
