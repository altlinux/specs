Name: xorg-drv-vesa
Version: 2.3.1
Release: alt1
Epoch: 1
Summary: Generic VESA video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk xorg-util-macros
BuildRequires: libXext-devel xorg-fontsproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel

%description
vesa is an Xorg driver for generic VESA video cards.  It can
drive most VESA-compatible video cards, but only makes use of the basic
standard  VESA core that is common to these cards.  The driver supports
depths 8, 15 16 and 24.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%dir %_x11modulesdir/drivers
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.1-alt1
- 2.3.1

* Mon Mar 05 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.0-alt4
- requires XORG_ABI_VIDEODRV = 12.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.0-alt3
- requires XORG_ABI_VIDEODRV = 11.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.0-alt2
- requires XORG_ABI_VIDEODRV = 10.0

* Fri Aug 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.0-alt1
- 2.3.0

* Tue Oct 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.2.1-alt1
- requires XORG_ABI_VIDEODRV = 6.0

* Fri Feb 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.2.0-alt2
- requires XORG_ABI_VIDEODRV = 5.0

* Wed Feb 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.2.0-alt1
- updated build dependencies

* Mon Dec 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.0-alt1
- 2.1.0

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.0-alt3
- requires XORG_ABI_VIDEODRV = 4.1

* Sun Aug 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.0-alt2
- fixed mode check (close #16872)

* Tue Jul 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.0-alt1
- 2.0.0

* Fri Jun 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.99.1-alt1
- 1.99.1

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt5
- renamed xorg-x11-drv-vesa to xorg-drv-vesa
- added requires XORG_ABI_VIDEODRV = 2.0

* Thu Apr 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt4
- death to mfb

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt3
- rebuild with xorg-server-1.4

* Sun Jul 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt2
- merged RH patches (close #12215)

* Fri Dec 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt1
- 1.2.2

* Sat Jun 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt1
- 1.2.1

* Fri May 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt2
- prereq xorg-x11-server-common >= 1.0.99.901

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1.3-alt2
- fixed requires

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1.3-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1.1-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt0.1
- initial release

