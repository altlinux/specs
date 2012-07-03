Name: xorg-drv-ati
Version: 6.14.4
Release: alt1
Epoch: 4
Summary: ATI video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv
Requires: xorg-drv-radeon xorg-drv-r128 xorg-drv-mach64

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: libGL-devel libXext-devel xorg-fontsproto-devel xorg-randrproto-devel xorg-renderproto-devel
BuildRequires: xorg-videoproto-devel xorg-xf86driproto-devel xorg-xineramaproto-devel libudev-devel xorg-glproto-devel

%description
ati  is an Xorg wrapper driver for ATI video cards.  It autodetects whether your hardware has a Radeon,
Rage 128, or Mach64 or earlier class of chipset, and loads the radeon(4), r128(4) driver as appropriate.

The  ati  driver  supports  Radeon, Rage 128, and Mach64 and earlier chipsets by loading those drivers.
See those manpages for specific cards supported.

%package -n xorg-drv-radeon
Summary: ATI RADEON video driver
Group: System/X11
Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv
Requires: xorg-dri-radeon xorg-drv-multimedia

%description -n xorg-drv-radeon
radeon is an Xorg driver for ATI RADEON based video cards. It contains full support for 8, 15, 16 and 24 bit pixel
depths, dual-head setup, flat panel, hardware 2D acceleration, hardware 3D acceleration, hardware cursor, XV extension,
and the Xinerama extension.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--enable-dri \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_x11modulesdir/drivers/ati_drv.so
%_man4dir/ati.4*

%files -n xorg-drv-radeon
%_x11modulesdir/drivers/radeon_drv.so
%dir %_x11modulesdir/multimedia
%_x11modulesdir/multimedia/*.so
%_man4dir/radeon.4*

%changelog
* Thu Mar 29 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:6.14.4-alt1
- 6.14.4

* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:6.14.3-alt2
- requires XORG_ABI_VIDEODRV = 12.0

* Wed Nov 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:6.14.3-alt1
- 6.14.3

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:6.14.2-alt2
- requires XORG_ABI_VIDEODRV = 11.0

* Thu May 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:6.14.2-alt1
- 6.14.2

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:6.14.1-alt2
- requires XORG_ABI_VIDEODRV = 10.0

* Fri Mar 18 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:6.14.1-alt1
- 6.14.1

* Fri Feb 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:6.14.0-alt1
- 6.14.0

* Wed Dec 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.13.2-alt2
- fixed requires

* Tue Sep 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.13.2-alt1
- 6.13.2

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.13.1-alt2
- requires XORG_ABI_VIDEODRV = 8.0

* Wed Jul 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.13.1-alt1
- 6.13.1

* Sat Apr 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.13.0-alt2
- added some new pci ids

* Mon Apr 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.13.0-alt1
- 6.13.0

* Mon Mar 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.192-alt1
- 6.13 RC2

* Wed Mar 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.191-alt1
- 6.13 RC1

* Tue Oct 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.4-alt1
- 6.12.4

* Thu Sep 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.3-alt1
- 6.12.3

* Wed Aug 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.2-alt6
- added some new r7xx pci ids

* Fri Jul 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.2-alt5
- RV280: Added an AGP quirk

* Mon Jun 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.2-alt4
- added some missing M96 pci id

* Thu Jun 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.2-alt3
- added RV740 (HD4770) support

* Sun May 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.2-alt2
- merged 6.12-branch

* Wed Apr 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.2-alt1
- 6.12.2

* Thu Mar 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.1-alt1
- 6.12.1

* Sat Mar 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.12.0-alt1
- 6.12.0

* Fri Feb 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.11.0-alt3
- RS600: enabled the DRI by default

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.11.0-alt2
- requires XORG_ABI_VIDEODRV = 5.0

* Thu Feb 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.11.0-alt1
- 6.11.0

* Wed Jan 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.10.0-alt1
- 6.10.0 release

* Tue Dec 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.9.0.91-alt1
- 6.9.1 pre-release

* Mon Sep 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.9.0-alt3
- RV770 initial support

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.9.0-alt2
- requires XORG_ABI_VIDEODRV = 4.1

* Fri Jun 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.9.0-alt1
- 6.9.0 release

* Wed Jun 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.192-alt1
- 6.9.0 RC2

* Fri Jun 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.191-alt1
- 6.9.0rc1

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt5
- renamed xorg-x11-drv-{ati,radeon} to xorg-drv-{ati,radeon}
- added requires XORG_ABI_VIDEODRV = 2.0

* Wed May 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt4
- GIT snapshot 2008-05-14 (71fa57f871dba03260dba2180ce1dab44048ac1a)
  + Add RS600 support

* Fri Apr 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt3
- GIT snapshot 2008-04-18 (c5d62fa0e8f52c3264ff9db3ff10cdf5a806bfc0)

* Fri Apr 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt2
- added conflicts to %name <= 6.6.3 (close #15230)

* Thu Apr 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt1
- 6.8.0 release + git 2008-03-28 (9c62c820ba45ebc14d5f36f5d7885863800b6adb)
- XAA by defaults for not avivo
- convert xinf to fdi 

* Sun Mar 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:6.8.0-alt3
- separate packages

* Thu Mar 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:6.8.0-alt2
- 6.8.0 release + git fixes
- xf86-video-ati-6.7.195-rh-faster-ddc.patch: Speed up X startup by assuming the
  monitor doesn't need a dead chicken waved over it to get DDC.

* Wed Feb 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:6.8.0-alt1
- 6.8.0

* Fri Dec 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:6.7.197-alt1
- 6.8RC7

* Thu Nov 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:6.7.196-alt1
- 6.8RC6

* Wed Nov 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:6.6.3-alt6
- set XAA by defaults

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:6.6.3-alt5
- rebuild for xorg-server-1.4

* Tue Jul 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:6.6.3-alt4
- generate ati.xinf from atipciids.h

* Fri Jan 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:6.6.3-alt3
- fixed %%description

* Sun Nov 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:6.6.3-alt2
- added xf86-video-ati-6.6.3-git-XAA-page-flipping.patch

* Sat Nov 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:6.6.3-alt1
- 6.6.3

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:6.6.2-alt5
- added videoaliases file from RH

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:6.6.2-alt4
- added RH patches: xf86-video-ati-6.6.2-rh-ati-prefer-radeon-then-r128.patch,
		    xf86-video-ati-6.6.2-rh-r128-fp-dpms.patch,
		    xf86-video-ati-6.6.2-rh-r128-missing-xf86ForceHWCursor-symbol-bug168753.patch,
		    xf86-video-ati-6.6.2-rh-radeon-6.6.1-dotclock-filter.patch,
		    xf86-video-ati-6.6.2-rh-radeon-6.6.1-use-mtdriver.patch,
		    xf86-video-ati-6.6.2-rh-radeon-6.6.2-dac-fix.patch,
		    xf86-video-ati-6.6.2-rh-radeon-6.6.2-pmac-bios.patch,
		    xf86-video-ati-6.6.2-rh-radeon-6.6.2-usefbdev-patch.patch

* Sun Nov 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:6.6.2-alt3
- rollback to 6.6.2
- added xf86-video-ati-6.6.2-git-rn50-memmap.patch

* Sun Oct 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.6.3-alt2
- added OpenSuSE patches

* Fri Oct 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.6.3-alt1
- rollback to 6.6.3
- added xf86-video-ati-6.6.3-mach64-Use-private-DMA-buffers.patch

* Sun Oct 22 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.6.99-alt1.3
- GIT snapshot 2006-10-22:
	+ attempt to fix repeat picture acceleration

* Wed Oct 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.6.99-alt1.2
- GIT snapshot 2006-10-17

* Fri Oct 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.6.99-alt1
- 6.6.99

* Thu Oct 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.6.2-alt2.git20061003
- GIT snapshot 2006-10-03

* Mon Sep 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.6.2-alt2
- fixup the rn50/m6/m7 memory map problem

* Fri Aug 25 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.6.2-alt1
- 6.6.2

* Fri Jun 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.6.1-alt1
- 6.6.1

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.6.0-alt3
- CVS snapshot 2006-05-09

* Wed May 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.6.0-alt2.cvs20060503
- CVS snapshot 2006-05-03

* Thu Apr 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.6.0-alt1
- 6.6.0

* Sun Feb 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.5.7.3-alt4
- CVS snapshot 2006-02-17

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.5.7.3-alt3
- removed memmap_fix patch (problem for Radeon R100 QD)

* Sat Jan 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.5.7.3-alt2
- added memmap_fix patch

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:6.5.7.3-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:6.5.7.1-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:6.5.7-alt0.1
- initial release

