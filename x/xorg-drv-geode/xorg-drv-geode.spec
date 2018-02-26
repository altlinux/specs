Name: xorg-drv-geode
Version: 2.11.13
Release: alt1
Epoch: 2
Summary: AMD Geode GX and LX Xorg graphics Driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch: %ix86
BuildRequires(Pre): xorg-sdk
BuildRequires: xorg-xf86dgaproto-devel xorg-util-macros

%description
geode  is  an  Xorg driver for Advanced Micro Devicess GEODE processor
family.  It uses the CIMARRON kit provided by Advanced  Micro  Devices.
The  driver  is  accelerated,  and  provides  support for the following
framebuffer depths: 8, 16 and 24.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-visibility \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc README TODO
%_x11modulesdir/drivers/*.so

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.13-alt1
- 2.11.13

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.12-alt3
- requires XORG_ABI_VIDEODRV = 11.0

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.12-alt2
- requires XORG_ABI_VIDEODRV = 10.0

* Fri Mar 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.12-alt1
- 2.11.12

* Tue Nov 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.10-alt1
- 2.11.10

* Mon Aug 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.9-alt1
- 2.11.9

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.8-alt2
- requires XORG_ABI_VIDEODRV = 8.0

* Tue Aug 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.8-alt1
- 2.11.8

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.7-alt2
- requires XORG_ABI_VIDEODRV = 6.0

* Thu Feb 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.7-alt1
- 2.11.7

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.6-alt1
- 2.11.6

* Fri Jun 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.3-alt1
- 2.11.3

* Tue May 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.2-alt1
- 2.11.2

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.1-alt2
- requires XORG_ABI_VIDEODRV = 5.0

* Tue Feb 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.1-alt1
- 2.11.1

* Wed Jan 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.11.0-alt1
- 2.11.0

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.10.1-alt2
- requires XORG_ABI_VIDEODRV = 4.1

* Fri Aug 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.10.1-alt1
- 2.10.1

* Sat Jun 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.10.0-alt1
- 2.10.0

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.9.0-alt2
- renamed xorg-x11-drv-geode to xorg-drv-geode
- added requires XORG_ABI_VIDEODRV = 2.0

* Thu May 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.9.0-alt1
- 2.9.0

* Tue Apr 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.8.0-alt2
- obsoletes xorg-x11-drv-nsc

* Thu Apr 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.8.0-alt1
- 2.8.0
- convert xinf file to fdi

* Fri Mar 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.7.7.7-alt1
- 2.7.7.7

* Mon Jan 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.7.7.5-alt1
- 2.7.7.5

* Sat Jan 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.7.7.4-alt1
- 2.7.7.4

* Mon Oct 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.7.7.3-alt1
- 2.7.7.3

* Tue Oct 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.7.7.2-alt2
- added amd.xinf

* Mon Oct 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.7.7.2-alt1
- 2.7.7.2

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.7.6.5-alt3
- rebuild with xorg-server-1.4

* Mon Jul 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.7.6.5-alt2
- GIT snapshot 2007-07-13 (bb0f0afc6c5cf849081a007af0c2d3485e87e9c4)

* Thu Aug 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.7.6.5-alt1.git20060807
- GIT snapshot 2006-08-07

* Fri Aug 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.7.6.5-alt1
- initial release

