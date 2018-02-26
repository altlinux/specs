Name: xorg-drv-sis
Version: 0.10.4
Release: alt1
Epoch: 1
Summary: SiS and XGI video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: xorg-xf86dgaproto-devel

%description
sis is an Xorg driver for SiS (Silicon Integrated  Systems)
and XGI video chips. The driver is accelerated and provides support for
colordepths of 8, 16 and 24 bpp. XVideo, Render  and  other  extensions
are supported as well.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-dri \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.4-alt1
- 0.10.4

* Mon Feb 13 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.3-alt5
- disabled dri

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.3-alt4
- requires XORG_ABI_VIDEODRV = 11.0

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.3-alt3
- requires XORG_ABI_VIDEODRV = 10.0

* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.3-alt2
- updated build dependencies

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.3-alt1
- 0.10.3

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.2-alt2
- removed unused fdi file

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.2-alt1
- 0.10.2

* Fri Feb 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.1-alt2
- requires XORG_ABI_VIDEODRV = 5.0

* Mon Dec 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.1-alt1
- 0.10.1

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.0-alt5
- requires XORG_ABI_VIDEODRV = 4.1

* Thu Jun 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.0-alt3
- renamed xorg-x11-drv-sis to xorg-drv-sis
- added requires XORG_ABI_VIDEODRV = 2.0

* Fri Apr 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.0-alt2
- obsoletes xorg-x11-drv-xgi
- convert xinf to fdi

* Wed Mar 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.0-alt1
- 0.10.0

* Fri Nov 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.9.4-alt1
- 0.9.4

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.9.3-alt2
- rebuild with xorg-server-1.4

* Thu Nov 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.9.3-alt1
- 0.9.3

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.9.2-alt2
- added videoaliases file from RH

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.9.2-alt1
- 0.9.2

* Thu Aug 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.9.1-alt4
- build for i586 and x86_64

* Wed Aug 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.9.1-alt3
- build for i586 only

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.9.1-alt2
- requires xorg-x11-server >= 1.0.99.901

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.9.1-alt1
- 0.9.1

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.8.1.3-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.8.1.1-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.8.1-alt0.1
- initial release

