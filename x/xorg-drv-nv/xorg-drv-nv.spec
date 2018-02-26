Name: xorg-drv-nv
Version: 2.1.18
Release: alt5
Epoch: 1
Summary: NVIDIA video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk

%description
nv  is  an  Xorg  driver for NVIDIA video cards.  The driver
supports 2D acceleration and provides support for the following  frame-
buffer depths: 8, 15, 16 (except Riva128) and 24.  All visual types are
supported for depth 8, TrueColor and DirectColor visuals are  supported
for  the other depths with the exception of the Riva128 which only sup-
ports TrueColor in the higher depths.

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
%_man4dir/*.4*

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.18-alt5
- requires XORG_ABI_VIDEODRV = 12.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.18-alt4
- requires XORG_ABI_VIDEODRV = 11.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.18-alt3
- requires XORG_ABI_VIDEODRV = 9.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.18-alt2
- requires XORG_ABI_VIDEODRV = 8.0

* Mon Aug 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.18-alt1
- 2.1.18

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.17-alt1
- 2.1.17

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.16-alt2
- requires XORG_ABI_VIDEODRV = 6.0

* Wed Dec 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.16-alt1
- 2.1.16

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.15-alt1
- 2.1.15

* Thu Jul 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.14-alt1
- 2.1.14

* Sun Jun 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.13-alt2
- new chip support

* Tue Apr 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.13-alt1
- 2.1.13

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.12-alt2
- requires XORG_ABI_VIDEODRV = 5.0

* Thu Aug 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.12-alt1
- 2.1.12

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.11-alt1
- 2.1.11
- requires XORG_ABI_VIDEODRV = 4.1

* Mon Aug 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.10-alt2
- more chips names

* Tue Jul 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.10-alt1
- 2.1.10

* Wed Jun 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.9-alt4
- added GeForce GTX 280 and 260 chips

* Fri Jun 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.9-alt3
- added GeForce 9 mobile chips

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.9-alt2
- renamed xorg-x11-drv-nv to xorg-drv-nv
- added requires XORG_ABI_VIDEODRV = 2.0

* Sat May 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.9-alt1
- 2.1.9
- convert xinf to fdi

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.8-alt1
- 2.1.8

* Sun Jan 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.7-alt1
- 2.1.7

* Wed Oct 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.6-alt1
- 2.1.6:
  + Fix LVDS detection on certain laptops.
  + Unwedge the hardware if the BIOS left it stuck.

* Sun Sep 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.5-alt1
- 2.1.5

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.3-alt2
- rebuild with xorg-server-1.4

* Thu Aug 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.3-alt1
- 2.1.3

* Sat Jul 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.2-alt1
- 2.1.2

* Tue Jul 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.1-alt1
- 2.1.1:
  + support GeForce 8400M G

* Tue Jun 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.0-alt1
- 2.1.0
- update xinf file

* Thu May 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.96-alt1
- 2.0.96

* Fri May 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.95-alt1
- 2.0.95

* Fri Apr 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.2-alt1
- 2.0.2

* Wed Mar 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.1-alt1
- 2.0.1

* Wed Mar 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.0-alt2
- added xf86-video-nv-2.0.0-git-hang-fix.patch: fix a hang during initialization.

* Mon Mar 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.0-alt1
- 2.0.0

* Sun Feb 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt2
- added PreReq xorg-x11-extensions-glx (fixed #10760)

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt1
- 1.2.2

* Sat Dec 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt1
- 1.2.1

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt2
- added videoaliases file from RH

* Sun Jul 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.2-alt2
- requires xorg-x11-server >= 1.0.99.901

* Wed Apr 26 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.2-alt1
- 1.1.2

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt1
- 1.1.1

* Tue Mar 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2.0-alt1
- 1.0.2.0

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1.2-alt0.1
- initial release

