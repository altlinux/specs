Name: bdftopcf
Version: 1.0.3
Release: alt1

Summary: convert X font from Bitmap Distribution Format to Portable Compiled Format
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: libfreetype-devel libXfont-devel libfontenc-devel pkg-config
BuildRequires: zlib-devel xorg-util-macros xorg-proto-devel

%description
Bdftopcf is a font compiler for the X server and font server.  Fonts in
Portable Compiled Format can be read by any architecture, although  the
file  is  structured  to allow one particular architecture to read them
directly without reformatting.  This allows fast reading on the  appro-
priate machine, but the files are still portable (but read more slowly)
on other machines.

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

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Thu Apr 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Wed Nov 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial release

