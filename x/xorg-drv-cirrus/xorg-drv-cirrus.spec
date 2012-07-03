Name: xorg-drv-cirrus
Version: 1.4.0
Release: alt1
Epoch: 1
Summary: Cirrus Logic video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk

%description
cirrus is an Xorg driver for Cirrus Logic video chips

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
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt5
- requires XORG_ABI_VIDEODRV = 11.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt4
- requires XORG_ABI_VIDEODRV = 9.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt3
- requires XORG_ABI_VIDEODRV = 8.0

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt2
- removed unused fdi file

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt1
- 1.3.2

* Thu Jul 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt1
- 1.3.1

* Thu May 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt4
- requires XORG_ABI_VIDEODRV = 5.0

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt3
- requires XORG_ABI_VIDEODRV = 4.1

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt2
- renamed xorg-x11-drv-cirrus to xorg-drv-cirrus
- added requires XORG_ABI_VIDEODRV = 2.0

* Fri May 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt1
- 1.2.1

* Thu Apr 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt2
- rebuild
- convert xinf to fdi

* Wed Mar 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt4
- rebuild with xorg-server-1.4

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt3
- added videoaliases file from RH

* Thu Aug 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt2
- build for i586 and x86_64

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.2-alt0.1
- initial release

