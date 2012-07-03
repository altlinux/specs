Name: mkfontdir
Version: 1.0.7
Release: alt1
Summary: create an index of X font files in a directory
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
For each directory argument, mkfontdir reads all of the font  files  in
the  directory searching for properties named "FONT", or (failing that)
the name of the file stripped of its suffix.  These  are  converted  to
lower case and used as font names, and, along with the name of the font
file, are written out to the file "fonts.dir" in the directory.  The  X
server and font server use "fonts.dir" to find font files.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--host= \
	--build=

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Sun Nov 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Sun Oct 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Mon Apr 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Wed Nov 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

