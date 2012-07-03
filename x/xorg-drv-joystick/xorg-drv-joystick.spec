Name: xorg-drv-joystick
Version: 1.6.1
Release: alt1
Epoch: 1
Summary: joystick input driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_XINPUT = %get_xorg_abi_xinput

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk xorg-util-macros
BuildRequires: libmtdev-devel libXi-devel xorg-kbproto-devel xorg-randrproto-devel xorg-xproto-devel

%description
joystick is an Xorg input driver

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
%_man4dir/*.4*

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.6.1-alt1
- 1.6.1

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.6.0-alt2
- requires XORG_ABI_XINPUT = 13.0

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.6.0-alt1
- 1.6.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.0-alt3
- requires XORG_ABI_XINPUT = 12.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.0-alt2
- requires XORG_ABI_XINPUT = 11.0

* Sun Nov 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.0-alt1
- 1.5.0

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.99.2-alt1
- 1.4.99.2

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt2
- requires XORG_ABI_XINPUT = 4.0

* Wed Jan 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Sat Sep 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.3-alt1
- 1.3.3

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt3
- requires XORG_ABI_XINPUT = 2.1

* Tue Jun 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt2
- renamed xorg-x11-drv-joystick to xorg-drv-joystick
- added requires XORG_ABI_XINPUT = 2.0

* Mon Apr 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt1
- 1.3.1

* Sat Dec 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt1
- 1.3.1

* Sat Oct 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.3-alt2
- rebuild with xorg-server-1.4

* Thu Aug 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.3-alt1
- 1.2.3

* Sun Apr 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Tue Mar 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt1
- 1.1.1

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0.2-alt0.1
- initial release

