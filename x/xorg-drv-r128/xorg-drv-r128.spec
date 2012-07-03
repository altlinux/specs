Name: xorg-drv-r128
Version: 6.8.2
Release: alt1
Epoch: 4
Summary: ATI Rage 128 video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): xorg-sdk
BuildRequires: libXext-devel xorg-fontsproto-devel xorg-randrproto-devel xorg-renderproto-devel
BuildRequires: xorg-videoproto-devel xorg-xproto-devel xorg-xineramaproto-devel xorg-xf86miscproto-devel

%description
r128 is an Xorg driver for ATI Rage 128 based video cards. It contains full support for 8, 15, 16 and 24 bit pixel
depths, hardware acceleration of drawing primitives, hardware cursor, video modes up to 1800x1440@70Hz, doublescan
modes (e.g., 320x200 and 320x240), gamma correction at all pixel depths, a fully programming dot clock and robust text
mode restoration for VT switching. Dualhead is supported on M3/M4 mobile chips.

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
%_x11modulesdir/drivers/r128_drv.so
%_man4dir/r128.4*

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.2-alt1
- 6.8.2

* Mon Feb 13 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.1-alt7
- disabled dri

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.1-alt6
- requires XORG_ABI_VIDEODRV = 11.0

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.1-alt5
- requires XORG_ABI_VIDEODRV = 10.0

* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.1-alt4
- updated build dependencies

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.1-alt3
- requires XORG_ABI_VIDEODRV = 8.0

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.1-alt2
- removed unused fdi file

* Wed Oct 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.1-alt1
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
- renamed xorg-x11-drv-r128 to xorg-drv-ati
- added requires XORG_ABI_VIDEODRV = 2.0

* Fri Apr 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 4:6.8.0-alt3
- GIT snapshot 2008-03-02 (a4fafa97b31bb7da01dd92236b42a418ca482992)
- initial build xf86-video-r128 apart from xf86-video-ati
