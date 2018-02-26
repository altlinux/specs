Name: xorg-drv-mga
Version: 1.5.0
Release: alt1
Epoch: 1
Summary: Matrox video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk

%description
mga is an Xorg driver for Matrox video cards.  The driver is
fully accelerated, and provides support for the  following  framebuffer
depths:  8, 15, 16, 24, and an 8+24 overlay mode.  All visual types are
supported for depth 8, and both TrueColor and DirectColor  visuals  are
supported  for the other depths except 8+24 mode which supports Pseudo-
Color, GrayScale and TrueColor.   Multi-card  configurations  are  sup-
ported.   XVideo  is  supported  on G200 and newer systems, with either
TexturedVideo or video overlay.  The second head of dual-head cards  is
supported  for  the G450 and G550.  Support for the second head on G400
cards requires a binary-only "mga_hal" module that  is  available  from
Matrox  <http://www.matrox.com>, and may be on the CD supplied with the
card.  That module also provides various other enhancements, and may be
necessary  to  use  the  DVI  (digital)  output  on the G550 (and other
cards).

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-xorg-module-dir="%_x11modulesdir" \
	--disable-dri \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.0-alt1
- 1.5.0

* Mon Feb 13 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.13-alt5
- disabled dri

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.13-alt4
- requires XORG_ABI_VIDEODRV = 11.0

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.13-alt3
- requires XORG_ABI_VIDEODRV = 10.0

* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.13-alt2
- updated build dependencies

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.13-alt1
- 1.4.13

* Tue May 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.12-alt1
- 1.4.12

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.11-alt2
- removed unused fdi file

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.11-alt1
- 1.4.11

* Mon Apr 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.10-alt1
- 1.4.10

* Wed Mar 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.9-alt4
- late-bind a call into a loadable module

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.9-alt3
- requires XORG_ABI_VIDEODRV = 5.0

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.9-alt2
- requires XORG_ABI_VIDEODRV = 4.1

* Thu Jul 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.9-alt1
- 1.4.9

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.8-alt3
- renamed xorg-x11-drv-mga to xorg-drv-mga
- added requires XORG_ABI_VIDEODRV = 2.0

* Thu Apr 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.8-alt2
- death to cfb
- convert xinf to fdi

* Sat Jan 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.8-alt1
- 1.4.8

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.7-alt2
- rebuild with xorg-server-1.4

* Thu Sep 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.7-alt1
- 1.4.7

* Fri Jun 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.6.1-alt1
- 1.4.6.1

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.6-alt1
- 1.4.6

* Thu Nov 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.5-alt1
- 1.4.5:
  + Enabled the Exa composite hooks on G550.
  + Bug #2168: Fix graphics corruptions with Mystique rev 2.
  + Removed some duplicated register definitions.
  + Removed some unused defines from mga_reg.h.
  + Register name tweak.
  + Use register names in MGASaveScreenMerged() rather than magic numbers.
  + Replaced more magic values with register names.
  + Removed a duplicated register definition.
  + Made some XAA function static.

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.4-alt2
- added videoaliases file from RH

* Sat Oct 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.4-alt1
- 1.4.4

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.3-alt1
- 1.4.3

* Tue Sep 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.2-alt1
- 1.4.2

* Thu Aug 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.1-alt2.git20060809
- build for i586 and x86_64

* Thu Aug 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.1-alt1.git20060809
- GIT snapshot 2006-08-09

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.1-alt1
- 1.4.1

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1.3-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1.1-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt0.1
- initial release

