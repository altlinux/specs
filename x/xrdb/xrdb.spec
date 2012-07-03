Name: xrdb
Version: 1.0.9
Release: alt1
Summary: X server resource database utility
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.org>

Requires: cpp

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXmu-devel xorg-util-macros

%description
Xrdb  is  used to get or set the contents of the RESOURCE_MANAGER prop-
erty on the root window of screen 0, or the  SCREEN_RESOURCES  property
on  the root window of any or all screens, or everything combined.  You
would normally run this program from your X startup file.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-cpp=%_bindir/cpp

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue Apr 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Thu Feb 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Thu Nov 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Fri Aug 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Jan 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Wed Apr 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- CVS snapshot 2006-04-03

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

