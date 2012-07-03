Name: xset
Version: 1.2.1
Release: alt1
Summary: user preference utility for X
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXext-devel libXmu-devel xorg-util-macros

%description
This program is used to set various user preference options of the display

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--without-fontcache \
	--without-xf86misc

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Thu Nov 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Tue Sep 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Mon Aug 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt4
- disabled XFree86-Misc

* Sat Nov 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt3
- disabled xprint

* Sat Aug 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt2
- disabled fontcache

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Tue Aug 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

