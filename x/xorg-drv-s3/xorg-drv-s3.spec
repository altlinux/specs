Name: xorg-drv-s3
Version: 0.6.3
Release: alt6
Epoch: 1
Summary: S3 video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk

%description
s3 is an Xorg driver for S3 video chipsets

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
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.3-alt6
- requires XORG_ABI_VIDEODRV = 12.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.3-alt5
- requires XORG_ABI_VIDEODRV = 11.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.3-alt4
- requires XORG_ABI_VIDEODRV = 9.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.3-alt3
- requires XORG_ABI_VIDEODRV = 8.0

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.3-alt2
- removed unused fdi file

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.3-alt1
- 0.6.3

* Thu Jul 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.2-alt1
- 0.6.2

* Mon May 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.1-alt3
- enabled Xv for Trio64V+ and Trio64UV+

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.1-alt2
- requires XORG_ABI_VIDEODRV = 5.0

* Mon Dec 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.1-alt1
- 0.6.1

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.0-alt3
- requires XORG_ABI_VIDEODRV = 4.1

* Thu Jun 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.0-alt2
- renamed xorg-x11-drv-s3 to xorg-drv-s3
- added requires XORG_ABI_VIDEODRV = 2.0
- converted xinf to fdi

* Wed Mar 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.6.0-alt1
- 0.6.0

* Thu Mar 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5.0-alt3
- xf86-video-s3-0.5.0-alt-newmmio.patch

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5.0-alt2
- rebuild with xorg-server-1.4

* Tue Nov 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5.0-alt1
- 0.5.0:
  + full fix for older cards

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.1-alt3
- added videoaliases file from RH

* Thu Aug 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.1-alt2
- build for i586 and x86_64

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.1-alt1
- 0.4.1

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.3.5.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.3.5.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.3.5.2-alt0.1
- initial release

