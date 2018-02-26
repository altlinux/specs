Name: xorg-drv-s3virge
Version: 1.10.4
Release: alt6
Epoch: 1
Summary: S3 ViRGE video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk

%description
s3virge  is  an  Xorg  driver for S3 based video cards.  The
driver is fully accelerated, and provides  support  for  the  following
framebuffer  depths: 8, 15, 16, and 24.  All visual types are supported
for depth 8, and TrueColor visuals are supported for the other  depths.
XVideo  hardware  up scaling is supported in depth 16 and 24 on the DX,
GX, GX2, MX, MX+, and Trio3D/2X.  Doublescan modes  are  supported  and
tested  in  depth 8 and 16 on DX, but disable XVideo.  Doublescan modes
on other chipsets are untested.

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
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.4-alt6
- requires XORG_ABI_VIDEODRV = 12.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.4-alt5
- requires XORG_ABI_VIDEODRV = 11.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.4-alt4
- requires XORG_ABI_VIDEODRV = 9.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.4-alt3
- requires XORG_ABI_VIDEODRV = 8.0

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.4-alt2
- removed unused fdi file

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.4-alt1
- 1.10.4

* Thu Jul 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.3-alt1
- 1.10.3

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.2-alt2
- requires XORG_ABI_VIDEODRV = 5.0

* Mon Dec 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.2-alt1
- 1.10.2

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.1-alt3
- requires XORG_ABI_VIDEODRV = 4.1

* Wed Jun 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.1-alt2
- renamed xorg-x11-drv-s3virge to xorg-drv-s3virge
- added requires XORG_ABI_VIDEODRV = 2.0

* Fri May 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.1-alt1
- 1.10.1

* Wed Mar 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.0-alt1
- 1.10.0

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.9.1-alt4
- rebuild with xorg-server-1.4

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.9.1-alt3
- added videoaliases file from RH

* Thu Aug 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.9.1-alt2
- build for i586 and x86_64

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.9.1-alt1
- 1.9.1

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.6.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.6.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.6.2-alt0.1
- initial release

