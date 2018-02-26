Name: xdpyinfo
Version: 1.3.0
Release: alt1

Summary: display information utility for X
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXcomposite-devel libXext-devel libXi-devel libXinerama-devel libXrender-devel libXtst-devel
BuildRequires: libXxf86dga-devel libXxf86vm-devel libdmx-devel xorg-util-macros

%description
Xdpyinfo is a utility for displaying information about an X server.  It
is  used to examine the capabilities of a server, the predefined values
for various parameters used in communicating between  clients  and  the
server, and the different types of screens and visuals that are available.

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
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Tue Oct 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Feb 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Mon Aug 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt4
- disabled XFree86-Misc

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt3
- updated build dependencies

* Sat Nov 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- disabled xprint

* Thu May 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Wed Mar 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

