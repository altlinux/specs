Name: bitmap
Version: 1.0.6
Release: alt1
Summary: bitmap,  bmtoa, atobm - bitmap editor and converter utilities for the X Window System
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libICE-devel libSM-devel libX11-devel libXau-devel libXaw-devel libXext-devel libXmu-devel
BuildRequires: libXpm-devel libXt-devel xorg-bitmaps xorg-util-macros libXdmcp-devel xorg-proto-devel

%description
The  bitmap program is a rudimentary tool for creating or editing rect-
angular images made up of 1's and 0's.   Bitmaps  are  used  in  X  for
defining  clipping  regions,  cursor  shapes, icon shapes, and tile and
stipple patterns.

The bmtoa and atobm filters convert bitmap files (FILE FORMAT)  to  and
from  ASCII  strings.  They are most commonly used to quickly print out
bitmaps and to generate versions for including in text.

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
%_sysconfdir/X11/app-defaults/*
%_includedir/X11/bitmaps
%_bindir/*
%_man1dir/*

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sat Nov 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- rebuild with libXaw.so.7

* Wed Jan 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Wed Nov 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

