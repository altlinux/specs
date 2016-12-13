Name: xorg-drv-nouveau
Version: 1.0.13
Release: alt2
Epoch: 2
Summary: NVIDIA video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: xorg-dri-nouveau
Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: libGL-devel xorg-glproto-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-xf86driproto-devel libudev-devel

%description
nouveau  is  an Xorg  driver  for  NVIDIA video cards.  The
driver supports 2D acceleration and provides support for the  following
framebuffer  depths: (15,) 16  and 24.  TrueColor visuals are supported
for these depths

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
* Thu Dec 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.13-alt2
- git snapshot master.1516d35

* Thu Oct 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.13-alt1
- 1.0.13

* Mon Apr 25 2016 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.12-alt1
- 1.0.12

* Fri Nov 27 2015 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.11-alt4
- git snapshot master.6e6d8ac

* Thu Feb 05 2015 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.11-alt3
- requires XORG_ABI_VIDEODRV = 19.0

* Fri Oct 10 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.11-alt2
- requires XORG_ABI_VIDEODRV = 18.0

* Sun Sep 07 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.11-alt1
- 1.0.11

* Thu Jan 09 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.10-alt2
- requires XORG_ABI_VIDEODRV = 15.0

* Thu Nov 07 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.10-alt1
- 1.0.10

* Sun Aug 04 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.9-alt1
- 1.0.9

* Sat Jun 15 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.8-alt1
- 1.0.8

* Thu Mar 28 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.7-alt1
- 1.0.7

* Wed Mar 06 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.6-alt3
- requires XORG_ABI_VIDEODRV = 14.1

* Fri Jan 18 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.6-alt2
- requires XORG_ABI_VIDEODRV = 13.1

* Tue Jan 08 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.6-alt1
- 1.0.6

* Fri Nov 09 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.4-alt1
- 1.0.4

* Fri Oct 26 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.3-alt1
- 1.0.3

* Wed Sep 12 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.2-alt1
- 1.0.2

* Mon Sep 10 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.1-alt1
- 1.0.1

* Mon Aug 27 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt10
- requires XORG_ABI_VIDEODRV = 12.1

* Mon Mar 05 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt9
- requires XORG_ABI_VIDEODRV = 12.0

* Thu Dec 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt8
- update to master git.3d9f6b32

* Tue Nov 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt7
- updated to master git.9fa0c6c

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt6
- updated to master git.169512f

* Tue Jul 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt5
- updated to master git.de9d1ba

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt4
- updated to master git.8378443

* Mon Feb 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt3.bc5dec2
- updated to master git.bc5dec2

* Thu Feb 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt3.c123618
- updated to master git.c123618

* Sat Jan 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt3
- updated to master git.b795ca6

* Tue Aug 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt2
- GIT snapshot 2010-08-13 (00d390952c912d4e9fc2c962caaeb90bf563d5b1)

* Sat Mar 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt1
- GIT snapshot 2010-03-05 (c642b9f7a13bdeecd0a83ddcbf6d6d4f2c287501)

* Thu Feb 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.15-alt3
- don't requires firmware

* Sat Feb 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.15-alt2
- GIT snapshot 2010-02-10 (9b4118d6d1fa488db86cd7d2875beea9cdefb096)

* Mon Feb 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.15-alt1
- initial release

