Name: xorg-drv-mach64
Version: 6.9.1
Release: alt1
Epoch: 4
Summary: ATI Mach 64 video driver
Group: System/X11
License: MIT/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): xorg-sdk
BuildRequires: xorg-xineramaproto-devel

%description
mach64 is an Xorg driver for ATI Mach 64 based video cards

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
%_x11modulesdir/drivers/mach64_drv.so

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:6.9.1-alt1
- 6.9.1

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:6.9.0-alt2
- requires XORG_ABI_VIDEODRV = 11.0

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:6.9.0-alt1
- 6.9.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.2-alt4
- requires XORG_ABI_VIDEODRV = 8.0

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.2-alt3
- requires XORG_ABI_VIDEODRV = 6.0

* Thu Jan 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.2-alt2
- disabled dri

* Wed Oct 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.2-alt1
- 6.8.2

* Thu Apr 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.1-alt1
- 6.8.1

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt8
- requires XORG_ABI_VIDEODRV = 5.0

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt7
- updated build dependencies

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt6
- requires XORG_ABI_VIDEODRV = 4.1

* Sun Aug 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt5
- 6.8.0 release

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt4
- renamed xorg-x11-drv-mach64 to xorg-drv-mach64
- added requires XORG_ABI_VIDEODRV = 2.0

* Fri Apr 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt3
- GIT snapshot 2008-03-26 (89a9ad75f3e50e25275b803617d5e74709ead269)
- initial build xf86-video-mach64 apart from xf86-video-ati

