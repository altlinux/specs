Name: xf86dga
Version: 1.0.3
Release: alt1

Summary: test program for the XFree86-DGA extension
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: libICE-devel libSM-devel libX11-devel libXau-devel
BuildRequires: libXaw-devel libXext-devel libXmu-devel libXpm-devel
BuildRequires: libXt-devel libXxf86dga-devel pkg-config xf86dgaproto
BuildRequires: xproto libXdmcp-devel xorg-util-macros

%description
Dga  is  a  simple test client for the XFree86-DGA extension.  It fills
the screen with a different colour for each  key  pressed.   It  prints
some basic framebuffer parameters, and also keyboard and pointer events
to stdout.  To exit, hit the `q' key.  Hitting the `b' key runs a  sim-
ple  benchmark,  measuring  raw  framebuffer write and read speed (this
takes one second each).

%prep
%setup

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
* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial release

