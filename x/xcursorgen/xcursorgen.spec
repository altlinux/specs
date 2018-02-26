Name: xcursorgen
Version: 1.0.5
Release: alt1
Summary: create an X cursor file from a collection of PNG images
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: XOrg Maintainer Team <xorg@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXcursor-devel libpng-devel xorg-util-macros

%description
Xcursorgen  reads  the  config-file  to  find the list of cursor images
along with their hotspot and nominal size information.  Xcursorgen con-
verts  all  of the images to Xcursor format and writes them to the out-
put-file.

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
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Fri Sep 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- rebuild with libpng12 1.2.37-alt2

* Tue Aug 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri May 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Apr 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- CVS snapshot 2006-04-03

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Wed Nov 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

