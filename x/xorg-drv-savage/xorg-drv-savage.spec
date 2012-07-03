Name: xorg-drv-savage
Version: 2.3.4
Release: alt1
Epoch: 1
Summary: S3 Savage video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk

%description
savage  is  an Xorg  driver  for the S3 Savage family video
accelerator chips.  2D, 3D, and Xv acceleration  is  supported  on  all
chips except the Savage2000 (2D only).  Dualhead operation is supported
on MX, IX, and SuperSavage chips.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-dri \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.4-alt1
- 2.3.4

* Mon Feb 13 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.2-alt5
- disabled dri

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.2-alt4
- requires XORG_ABI_VIDEODRV = 11.0

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.2-alt3
- requires XORG_ABI_VIDEODRV = 10.0

* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.2-alt2
- updated build dependencies

* Sun Dec 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.2-alt1
- 2.3.2

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.1-alt3
- requires XORG_ABI_VIDEODRV = 8.0

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.1-alt2
- removed unused fdi file

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.1-alt1
- 2.3.1

* Thu Jul 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.0-alt1
- 2.3.0

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.2.1-alt4
- requires XORG_ABI_VIDEODRV = 5.0

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.2.1-alt3
- requires XORG_ABI_VIDEODRV = 4.1

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.2.1-alt2
- renamed xorg-x11-drv-savage to xorg-drv-savage
- added requires XORG_ABI_VIDEODRV = 2.0

* Fri May 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.2.1-alt1
- 2.2.1

* Wed Mar 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.2.0-alt1
- 2.2.0

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.3-alt2
- rebuild with xorg-server-1.4

* Fri Aug 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.3-alt1
- 2.1.3

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.2-alt2
- added videoaliases file from RH

* Fri Sep 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.2-alt1
- 2.1.2

* Tue Sep 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.1-alt3.git20060919
- GIT snapshot 2006-09-19: fix DRI locking in savage driver.

* Thu Aug 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.1-alt3.git20060721
- build for i586 and x86_64

* Fri Jul 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.1-alt2.git20060721
- GIT snapshot 2006-07-21

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.1-alt2
- requires xorg-x11-server >= 1.0.99.901

* Mon May 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1.1-alt1
- 2.1.1

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.2.3-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.2.1-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.2-alt0.1
- initial release

