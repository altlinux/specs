Name: xvidtune
Version: 1.0.2
Release: alt1

Summary: video mode tuner for Xorg
License: MIT/X11
Group: System/X11
Packager: Valery Inozemtsev <shrek@altlinux.ru>
Url: http://xorg.freedesktop.org

Conflicts: xorg-x11-xapps <= 6.9 xorg-x11-apps <= 6.9

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXaw-devel libXxf86vm-devel xorg-util-macros

%description
Xvidtune is a client interface to the X server video mode extension.

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
* Sat Jan 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sat Nov 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt4
- rebuild with libXaw.so.7

* Thu Oct 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3
- added conflicts to xorg-x11-xapps <= 6.9 (#9477)

* Fri Jan 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- fixed #8954

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

