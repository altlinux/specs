Name: xfontsel
Version: 1.0.4
Release: alt1
Summary: point and click selection of X11 font names
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libICE-devel libSM-devel libX11-devel libXau-devel libXaw-devel libXext-devel libXmu-devel
BuildRequires: libXpm-devel libXt-devel xorg-proto-devel xorg-util-macros libXdmcp-devel

%description
The xfontsel application provides a simple way  to  display  the  fonts
known  to  your  X  server, examine samples of each, and retrieve the X
Logical Font Description ("XLFD") full name for a font.

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
%_bindir/*
%_man1dir/*

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Tue Oct 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Nov 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- rebuild with libXaw.so.7

* Fri Feb 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

