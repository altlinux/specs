Name: xorg-drv-intel
Version: 2.19.0
Release: alt1
Epoch: 7
Summary: Intel integrated graphics chipsets
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv xorg-dri-intel

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: libGL-devel libX11-devel libXext-devel libXvMC-devel xorg-inputproto-devel xorg-fontsproto-devel xorg-randrproto-devel
BuildRequires: xorg-renderproto-devel xorg-xextproto-devel xorg-xf86driproto-devel xorg-dri2proto-devel xorg-xineramaproto-devel
BuildRequires: libXrender-devel libxcbutil-devel xorg-util-macros libXfixes-devel libudev-devel intel-gen4asm

%description
intel  is  an  Xorg  driver  for  Intel  integrated  graphics
chipsets.  The driver supports depths 8, 15, 16  and  24.   All  visual
types are supported in depth 8.  For the i810/i815 other depths support
the TrueColor and DirectColor visuals.  For the 830M  and  later,  only
the  TrueColor  visual  is  supported  for  depths greater than 8.  The
driver supports hardware accelerated 3D via the Direct Rendering Infra-
structure  (DRI),  but only in depth 16 for the i810/i815 and depths 16
and 24 for the 830M and later

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
%_libdir/*.so.*
%_x11modulesdir/drivers/*.so
%_man4dir/i*.4*

%changelog
* Tue May 01 2012 Valery Inozemtsev <shrek@altlinux.ru> 7:2.19.0-alt1
- 2.19.0

* Mon Mar 05 2012 Valery Inozemtsev <shrek@altlinux.ru> 7:2.18.0-alt2
- requires XORG_ABI_VIDEODRV = 12.0

* Fri Feb 24 2012 Valery Inozemtsev <shrek@altlinux.ru> 7:2.18.0-alt1
- 2.18.0

* Thu Nov 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 7:2.17.0-alt1
- 2.17.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 7:2.16.0-alt2
- requires XORG_ABI_VIDEODRV = 11.0

* Fri Aug 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 7:2.16.0-alt1
- 2.16.0

* Sun Jul 31 2011 Valery Inozemtsev <shrek@altlinux.ru> 7:2.15.901-alt1
- 2.16 RC1

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 7:2.15.0-alt2
- requires XORG_ABI_VIDEODRV = 10.0

* Thu Apr 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 7:2.15.0-alt1
- 2.15.0

* Mon Apr 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 7:2.14.0-alt2
- updated build dependencies

* Sat Jan 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 7:2.14.0-alt1
- Intel 2010Q4 release

* Fri Dec 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 7:2.13.902-alt1
- 2.14 RC2

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 7:2.13.901-alt1
- 2.14 RC1

* Thu Sep 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 7:2.13.0-alt1
- Intel 2010Q3 release

* Wed Sep 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 7:2.12.902-alt1
- 2.13 RC2

* Wed Sep 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 7:2.12.901-alt1
- 2.13 RC1

* Fri Aug 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 7:2.12.0-alt2
- requires XORG_ABI_VIDEODRV = 8.0

* Fri Jun 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 7:2.12.0-alt1
- 2.12.0

* Thu Apr 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 7:2.10.0-alt7
- 2.10.0 (closes: #23291)

* Mon Mar 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 6:2.11.0-alt1
- 2.11.0

* Sun Mar 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 6:2.10.903-alt1
- 2.11 RC3

* Tue Mar 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 6:2.10.902-alt1
- 2.11 RC2

* Sat Feb 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 6:2.10.901-alt1
- 2.11 RC1

* Thu Feb 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 6:2.10.0-alt6
- 2.10 branch 2010-02-25 (6fd45abb31807dea0b9ebe708d840b1369353a8c)

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 6:2.10.0-alt5
- requires XORG_ABI_VIDEODRV = 6.0

* Sat Feb 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 6:2.10.0-alt4
- updated serial

* Fri Feb 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 5:2.10.0-alt2
- /etc/modprobe.d/i915-kms.conf: enabled KMS (closes: #22828)

* Tue Jan 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 5:2.10.0-alt1
- 2.10.0 release

* Tue Dec 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.9.99.901-alt1
- 2.10.0 RC1

* Mon Oct 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.9.1-alt2
- 2.9.1

* Mon Oct 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.9.0-alt4
- requires XORG_ABI_VIDEODRV = 6.0

* Sun Oct 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.9.0-alt3
- don't drop frontbuffer from crtc in I830CloseScreen

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.9.0-alt2
- fixed fd.o #24383, #24459

* Tue Sep 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.9.0-alt1
- 2.9.0

* Mon Sep 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.8.99.902-alt1
- 2.9 RC2

* Wed Aug 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.8.1-alt1
- 2.8.1

* Thu Aug 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.8.0-alt5
- fixed sampler indexes on i965 planar video

* Tue Jul 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.8.0-alt4
- 2.8.0 release

* Fri Jul 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.8.0-alt3.rc2
- fixed 915-class Render after the 8xx-class Render fix

* Thu Jul 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.8.0-alt2.rc2
- fixed batchbuffer wrapping problems with 8xx render

* Mon Jul 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.8.0-alt1.rc2
- 2.8 RC2

* Mon Jul 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.8.0-alt1.rc1
- 2.8 RC1 + git 2009-07-11 (34c674dd45879b8ba8395b93b16c8a9e7b848f1f)

* Thu Jun 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.7.99.901-alt1
- 2.8 RC1

* Fri Jun 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.7.99.1-alt2
- 2.8 development snapshot 2009-06-05

* Wed Apr 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.7.99.1-alt1
- 2.8 development snapshot

* Mon Apr 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.7.0-alt2
- added i965+ fixes

* Thu Apr 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.7.0-alt1
- 2.7.0

* Sat Apr 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.6.99.903-alt1
- 2.7 RC3

* Thu Mar 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.6.99.902-alt1
- 2.7 RC2

* Tue Mar 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.6.99.901-alt1
- 2.7 RC1

* Sat Mar 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.6.3-alt3
- fixed another VT switch leak

* Fri Mar 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.6.3-alt2
- fixed serious memory leak at Enter/LeaveVT

* Tue Mar 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.6.3-alt1
- 2.6.3

* Sat Feb 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.6.2-alt3
- UXA: disabled MITSHM

* Fri Feb 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.6.2-alt2
- updated build dependencies

* Wed Feb 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.6.2-alt1
- 2.6.2

* Thu Jan 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.6.1-alt1
- 2.6.1

* Wed Jan 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 5:2.5.1-alt3
- rollback to 2.5.1

* Thu Jan 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:2.6.0-alt1
- 2.6.0

* Fri Jan 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:2.5.99.2-alt1
- 2.6.0 RC2

* Fri Jan 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:2.5.1-alt3
- 2.5.1

* Mon Jan 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:2.4.3-alt3
- rollback to 2.4.3, wait GEM in kernel/Mesa

* Sun Dec 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.5.1-alt2
- updated build dependencies

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.3-alt2
- updated build dependencies

* Fri Nov 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.5.1-alt1
- 2.5.1

* Fri Nov 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.3-alt0.M41.1
- build for branch 4.1

* Thu Nov 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.3-alt1
- 2.4.3

* Fri Nov 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.2-alt9.M41.1
- build for branch 4.1

* Fri Nov 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.2-alt10
- use LFP data pointers instead of array (close #17811)

* Sun Sep 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.2-alt8
- disabled TTM

* Sat Sep 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.2-alt7
- Pipe A force quirk for Toshiba Satellite A30
- fixed upscaling limit
- fixed timer leak

* Mon Sep 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.2-alt5.M41.1
- build for branch 4.1

* Mon Sep 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.2-alt6
- added new option "TTM", TTM disabled by defaults

* Sat Sep 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.2-alt5
- enabled TTM

* Fri Sep 12 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.2-alt4
- added support for G41 chipset

* Fri Sep 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.2-alt3
- set EXA by defaults

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.2-alt2
- requires XORG_ABI_VIDEODRV = 4.1

* Tue Aug 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.2-alt1
- 2.4.2

* Fri Aug 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.1-alt1
- 2.4.1

* Fri Aug 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.4.0-alt1
- 2.4.0

* Wed Jun 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.3.2-alt2
- add support for Intel 4 series chipsets

* Wed Jun 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.3.2-alt1
- 2.3.2

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.3.1-alt3
- rename xorg-x11-drv-intel to xorg-drv-intel
- add requires XORG_ABI_VIDEODRV = 2.0

* Sat May 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.3.1-alt2
- fix/check vt switch

* Mon May 12 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.3.1-alt1
- 2.3.1

* Sat May 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.3.0-alt2
- xf86-video-intel-2.3-branch 2008-05-10:
  + fixed freeze on two X start (close #15479)

* Wed Apr 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.3.0-alt1
- 2.3.0
- XAA by defaults for all chips

* Fri Apr 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.2.1-alt4
- obsoletes xorg-x11-drv-i810
- convert xinf to fdi

* Thu Mar 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.2.1-alt3
- XAA by defaults for i8xx only

* Tue Mar 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.2.1-alt2
- disable DRI memory manager
- reset XV after mode switch

* Sat Feb 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.2.1-alt1
- 2.2.1

* Wed Feb 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.2.0.90-alt1
- 2.2.1 pre-release

* Fri Jan 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.2.0-alt5
- fix VT switch

* Sat Jan 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:2.2.0-alt4
- xf86-video-intel-2.2-branch

* Sat Dec 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.2.0-alt3
- removed provides/obsoletes i810
- fixed intel.xinf

* Sat Nov 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.2.0-alt2
- fix typo in 1920x1080 resolution entry

* Fri Nov 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.2.0-alt1
- 2.2.0
- drop legacy driver

* Wed Oct 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.1.1-alt3
- added backlight control methods patch (close #13211)

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.1.1-alt2
- rebuild with xorg-server-1.4

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.1.1-alt1
- 2.1.1
- legacy driver version 1.6.5

* Thu Aug 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.1.0-alt3
- added 0x8086:0x2562 845G/GL/GE (close #12515)

* Tue Jul 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.1.0-alt2
- generate intel.xinf from common.h
- added 0x8086:0x5641 PCI_CHIP_I845_G (close #12423)

* Tue Jul 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.1.0-alt1
- 2.1.0

* Tue Jun 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.0.0-alt8
- fix left G33 issues
- update xinf file

* Wed Jun 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.0.0-alt7
- add support for the G33, Q33, and Q35 chipsets

* Thu May 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.0.0-alt6
- add support for the i945GME, i965GME and i965GLE chipsets

* Fri Apr 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.0.0-alt5
- returned old driver i810

* Fri Apr 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.0.0-alt4
- drop XV patches

* Wed Apr 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.0.0-alt3
- fixed XV on i8xx chipsets

* Tue Apr 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.0.0-alt2
- removed old driver i810

* Fri Apr 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:2.0.0-alt1
- 2.0 release

* Tue Apr 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.9.94-alt1
- 2.0RC4

* Tue Mar 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.9.93-alt1
- 2.0.RC3
- update xinf

* Wed Mar 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.9.92-alt1
- 2.0RC2

* Thu Jan 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 3:1.7.4-alt1
- 1.7.4:
  + Fix bug #8536, i915 BIOS fails when restarting Xserver.

* Wed Dec 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.7.3-alt3
- removed modesetting driver

* Sun Dec 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.7.3-alt2
- added modesetting driver (intel_drv.so) for i9xx

* Thu Dec 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.7.3-alt1
- 1.7.3

* Thu Nov 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.7.2-alt4
- added xf86-video-intel-1.7.2-git-DRM-memory-manager,
	xf86-video-intel-1.7.2-git-Xv-hang-G965.patch,
	xf86-video-i810-setcursorposition.diff,
	xf86-video-i810-update-port-attributes.diff,
	xf86-video-i810-video-debug.diff
- added RH patches:
	xf86-video-intel-1.7.2-rh-i810-match-server-sync-ranges.patch

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.7.2-alt3
- rollback to 1.7.2 release
- added videoaliases file from RH

* Thu Nov 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.7.2-alt2
- GIT snapshot 2006-11-08

* Fri Oct 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.7.2-alt1
- 1.7.2:
  + suspend/resume regression from 1.5 driver

* Mon Oct 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.7.0-alt1
- 1.7.0

* Tue Aug 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.5-alt1.git20060829
- GIT snapshot 2006-08-29

* Fri Aug 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.5-alt1
- 1.6.5

* Tue Aug 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.3-alt1
- 1.6.3

* Wed Jul 26 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.1-alt1
- 1.6.1

* Sun Jun 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.0-alt3
- fix VT switch DRI locking

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.0-alt2
- requires xorg-x11-server >= 1.0.99.901

* Thu Apr 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.6.0-alt1
- 1.6.0

* Sun Mar 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 3:1.4.1.3-alt1
- rollback 1.4.1.3

* Sun Mar 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.2.0-alt1
- 1.5.2.0 (requires xorg-x11-server >= 1.0.1-alt14)

* Fri Feb 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.1.3-alt1
- rollback 1.4.1.3 (1.5.0.0 problematic)

* Tue Jan 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.0.0-alt1
- 1.5.0.0

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.1.3-alt2
- removed files spectre (%%ghost %%_libdir/*.so)

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.1.3-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.1.1-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.1-alt0.1
- initial release

