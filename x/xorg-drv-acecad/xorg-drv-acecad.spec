Name: xorg-drv-acecad
Version: 1.5.0
Release: alt2
Epoch: 1
Summary: Acecad Flair input driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_XINPUT = %get_xorg_abi_xinput
Provides: xorg-x11-drv-acecad = %epoch:%version-%release
Obsoletes: xorg-x11-drv-acecad

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk xorg-util-macros
BuildRequires: libsysfs-devel libXi-devel xorg-randrproto-devel xorg-xproto-devel

%description
acecad is an Xorg input driver for Acecad Flair devices...

The  acecad driver functions as a pointer input device, and may be used
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
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.0-alt2
- requires XORG_ABI_XINPUT = 16.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.0-alt1
- 1.5.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt3
- requires XORG_ABI_XINPUT = 12.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt2
- requires XORG_ABI_XINPUT = 11.0

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt2
- requires XORG_ABI_XINPUT = 4.0

* Tue Feb 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt3
- requires XORG_ABI_XINPUT = 2.1

* Wed Jun 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt2
- renamed xorg-x11-drv-acecad to xorg-drv-acecad
- added requires XORG_ABI_XINPUT = 2.0

* Sun Feb 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt1
- 1.2.2

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt1
- 1.2.1

* Sun Apr 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Thu Apr 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt1
- 1.1.1

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0.2-alt0.1
- initial release

