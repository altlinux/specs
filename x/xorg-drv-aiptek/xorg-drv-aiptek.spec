Name: xorg-drv-aiptek
Version: 1.4.1
Release: alt2
Epoch: 1
Summary: Aiptek USB Digital Tablet Input Driver for Linux
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_XINPUT = %get_xorg_abi_xinput

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: libXi-devel xorg-inputproto-devel xorg-randrproto-devel xorg-xproto-devel

%description
aiptek is an Xorg input driver for Aiptek HyperPen USB-based
tablet devices.  This driver only supports the USB protocol,  and  only
under  Linux;  for  RS-232C-based  HyperPens, please see the "hyperpen"
driver.

The aiptek driver functions as a pointer input device, and may be  used
as the X server's core pointer.

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
%_x11modulesdir/input/*.so
%_man4dir/*

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.1-alt2
- requires XORG_ABI_XINPUT = 16.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.1-alt1
- 1.4.1

* Wed May 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt2
- requires XORG_ABI_XINPUT = 12.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt1
- 1.3.1

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt2
- requires XORG_ABI_XINPUT = 4.0

* Tue Feb 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt3
- requires XORG_ABI_XINPUT = 2.1

* Wed Jun 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt2
- renamed xorg-x11-drv-aiptek to xorg-drv-aiptek
- added requires XORG_ABI_XINPUT = 2.0

* Wed Jan 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt1
- 1.1.1

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt2
- rebuild with xorg-server-1.4

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt1
- 1.0.1

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0.2-alt0.1
- initial release

