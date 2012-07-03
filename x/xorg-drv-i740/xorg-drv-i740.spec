Name: xorg-drv-i740
Version: 1.3.2
Release: alt5
Serial: 1
Summary: Intel i740 video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv
Provides: xorg-x11-drv-i740 = %serial:%version-%release
Obsoletes: xorg-x11-drv-i740

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk

ExclusiveArch: %ix86

%description
i740 is an Xorg driver for Intel i740 video cards.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-static

%make_build

%install
%makeinstall_std

%files
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 1:1.3.2-alt5
- rebuilt with current XORG_ABI_VIDEODRV

* Thu Mar 08 2012 Michael Shigorin <mike@altlinux.org> 1:1.3.2-alt4
- rebuilt (actually works with AGP i740 8M)
- dropped *.xinf
- minor spec cleanup

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt3
- requires XORG_ABI_VIDEODRV = 8.0

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt2
- removed unused fdi file

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt1
- 1.3.2

* Thu Jul 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt1
- 1.3.1

* Thu Mar 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt4
- requires XORG_ABI_VIDEODRV = 5.0

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt3
- requires XORG_ABI_VIDEODRV = 4.1

* Thu Jun 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt2
- renamed xorg-x11-drv-i740 to xorg-drv-i740
- added requires XORG_ABI_VIDEODRV = 2.0
- converted xinf to fdi

* Wed Mar 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt3
- rebuild with xorg-server-1.4

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt2
- added videoaliases file from RH

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.2-alt0.1
- initial release

