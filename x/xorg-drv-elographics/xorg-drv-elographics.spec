Name: xorg-drv-elographics
Version: 1.3.0
Release: alt2
Epoch: 1
Summary: Elographics input driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_XINPUT = %get_xorg_abi_xinput

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk

%description
elographics is an Xorg input driver for Elographics touchscreen devices.

The elographics driver functions as a pointer input device, and may  be
used as the X server's core pointer.

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
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt2
- requires XORG_ABI_XINPUT = 16.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.4-alt3
- requires XORG_ABI_XINPUT = 12.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.4-alt2
- requires XORG_ABI_XINPUT = 11.0

* Wed Jun 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.4-alt1
- 1.2.4

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.3-alt3
- requires XORG_ABI_XINPUT = 7.0

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.3-alt2
- requires XORG_ABI_XINPUT = 4.0

* Tue Oct 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.3-alt1
- 1.2.3

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt2
- requires XORG_ABI_XINPUT = 2.1

* Wed Jun 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt1
- 1.2.2

* Tue Jun 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt2
- renamed xorg-x11-drv-elographics to xorg-drv-elographics
- added requires XORG_ABI_XINPUT = 2.0

* Fri May 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt1
- 1.2.1

* Fri Mar 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt2
- rebuild with xorg-server-1.4

* Sat Nov 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0.2-alt0.1
- initial release

