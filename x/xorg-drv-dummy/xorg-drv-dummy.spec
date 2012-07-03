Name: xorg-drv-dummy
Version: 0.3.5
Release: alt1
Summary: dummy video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv
Provides: xorg-x11-drv-dummy = %version-%release
Obsoletes: xorg-x11-drv-dummy

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: xorg-fontsproto-devel xorg-randrproto-devel xorg-renderproto-devel
BuildRequires: xorg-videoproto-devel xorg-xf86dgaproto-devel xorg-xproto-devel

%description
dummy is an Xorg driver for dummy video cards.

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

%changelog
* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.3.5-alt1
- 0.3.5

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.3.4-alt4
- requires XORG_ABI_VIDEODRV = 11.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.3.4-alt3
- requires XORG_ABI_VIDEODRV = 9.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.3.4-alt2
- added fake functions "glwMDrawingAreaWidgetClass"

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.3.4-alt1
- 0.3.4

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.2-alt2
- requires XORG_ABI_VIDEODRV = 6.0

* Thu Jul 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Wed Mar 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.1-alt4
- dropped fake functions

* Wed Mar 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.1-alt3
- updated deprecated functions

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.1-alt2
- requires XORG_ABI_VIDEODRV = 5.0

* Mon Jan 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt3
- requires XORG_ABI_VIDEODRV = 4.1

* Wed Jun 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt2
- renamed xorg-x11-drv-dummy to xorg-drv-dummy
- added requires XORG_ABI_VIDEODRV = 2.0

* Thu Mar 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt1
- initial release
