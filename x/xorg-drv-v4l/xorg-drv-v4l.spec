Name: xorg-drv-v4l
Version: 0.2.0
Release: alt10
Epoch: 1
Summary: video4linux driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk

%description
v4l  is an Xorg driver for video4linux cards.  It provides a
Xvideo extention port for video overlay.  Just add the  driver  to  the
module  list  within the module section of your Xorg file if
you want to use it.  There are no config options.

Note that the the extmod module is also required for the Xvideo support
(and lots of other extentions too).

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
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.0-alt10
- requires XORG_ABI_VIDEODRV = 12.0

* Tue Aug 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.0-alt9
- requires XORG_ABI_VIDEODRV = 11.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.0-alt8
- requires XORG_ABI_VIDEODRV = 9.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.0-alt7
- requires XORG_ABI_VIDEODRV = 8.0

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.0-alt6
- requires XORG_ABI_VIDEODRV = 6.0

* Fri Feb 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.0-alt5
- requires XORG_ABI_VIDEODRV = 5.0

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.0-alt4
- requires XORG_ABI_VIDEODRV = 4.1

* Tue Jun 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.0-alt3
- real 0.2.0 release

* Thu Jun 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.0-alt2
- renamed xorg-x11-drv-v4l to xorg-drv-v4l
- added requires XORG_ABI_VIDEODRV = 2.0

* Thu Mar 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.0-alt1
- 0.2.0

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.1-alt3
- rebuild with xorg-server-1.4

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.1-alt2
- requires xorg-x11-server >= 1.0.99.901

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.1-alt1
- 0.1.1

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.0.1.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.0.1.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.0.1.2-alt0.1
- initial release

