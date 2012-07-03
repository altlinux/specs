Name: mkfontscale
Version: 1.1.0
Release: alt1
Summary: create an index of scalable font files for X
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: bzlib-devel libfontenc-devel libfreetype-devel xorg-xproto-devel xorg-util-macros zlib-devel

%description
For each directory argument, mkfontscale reads all of the scalable font
files in the directory.  For every font file found, an  X11  font  name
(XLFD)  is  generated,  and is written together with the file name to a
file fonts.scale in the directory.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-bzip2

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt2
- updated build dependencies

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Sun Oct 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Fri Dec 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Sun May 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Wed Nov 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

