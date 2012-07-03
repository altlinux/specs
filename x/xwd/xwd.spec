Name: xwd
Version: 1.0.5
Release: alt1

Summary: dump an image of an X window
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: libX11-devel libXmu-devel pkg-config xorg-proto-devel xorg-util-macros

%description
Xwd is an X Window System window dumping utility.  Xwd allows  X  users
to  store  window images in a specially formatted dump file.  This file
can then be read by various other X utilities for redisplay,  printing,
editing, formatting, archiving, image processing, etc.  The target win-
dow is selected by clicking the pointer in  the  desired  window.   The
keyboard  bell is rung once at the beginning of the dump and twice when
the dump is completed.

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
* Wed Mar 21 2012 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Wed Jan 25 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

