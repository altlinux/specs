Name: xorg-xtrans-devel
Version: 1.2.7
Release: alt1

Summary: Abstract network code for X
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xtrans = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xmlto xorg-sgml-doctools xorg-util-macros

%description
%name is a library of code that is shared among various X packages to
handle network protocol transport in a modular fashion, allowing a
single place to add new transport types.  It is used by the X server,
libX11, libICE, the X font server, and related components.

It is however, *NOT* a shared library, but code which each consumer
includes and builds it's own copy of with various #ifdef flags to make
each copy slightly different.  To support this in the modular build
system, this package simply installs the C source files into
%_includedir/X11/Xtrans and installs a pkg-config file and an
autoconf m4 macro file with the flags needed to use it.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--host= \
	--build=

%install
%make DESTDIR=%buildroot install

%files
%dir %_docdir/xtrans
%_docdir/xtrans/*.html
%_includedir/X11
%_datadir/pkgconfig/*.pc
%_datadir/aclocal/*.m4

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Tue Nov 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Sun Oct 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Sat Aug 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Sun Jan 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Tue Oct 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sat Sep 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1.M41.1
- build for branch 4.1

* Fri Sep 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt2
- disabled abstract socket

* Thu Jul 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sun Jun 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt2
- rename xorg-x11-xtrans-devel to xorg-xtrans-devel

* Thu May 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- 1.2

* Thu Mar 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- 1.1

* Mon Feb 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt4
- fixed #ifdef checks that were using i386 to use __i386__

* Wed Oct 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt3
- update xtrans-1.0.3-abstract-sockets.patch

* Tue Aug 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt2
- Abstract sockets for PF_UNIX

* Wed Aug 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Jun 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sun Feb 12 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt3
- added PreReq xorg-x11-proto-devel

* Wed Jan 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- build as Arch

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Sun Nov 20 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial release

