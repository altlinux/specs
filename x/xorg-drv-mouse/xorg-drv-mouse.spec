Name: xorg-drv-mouse
Version: 1.7.2
Release: alt3
Serial: 1
Summary: Mouse input driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Source: xf86-input-mouse-%version.tar
PreReq: XORG_ABI_XINPUT = %get_xorg_abi_xinput
Provides: xorg-x11-drv-mouse = %serial:%version-%release
Obsoletes: xorg-x11-drv-mouse
Provides: xorg-drv-evdev

BuildPreReq: xorg-util-macros xorg-sdk
BuildRequires: libXext-devel libXi-devel xorg-randrproto-devel xorg-xproto-devel

%description
mouse is an Xorg input driver for mice.  The driver supports
most available mouse types and interfaces.  USB mice are only supported
on  some OSs, and the level of support for PS/2 mice depends on the OS.

The mouse driver functions as a pointer input device, and may  be  used
as  the X server's core pointer.  Multiple mice are supported by multi-
ple instances of this driver.

%prep
%setup -q -n xf86-input-mouse-%version

%build
#%%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%dir %_x11modulesdir/input
%_x11modulesdir/input/*.so
%_man4dir/*

%changelog
* Thu Oct 25 2012 Led <led@altlinux.ru> 1:1.7.2-alt3
- added provides xord-drv-evdev

* Fri Oct 19 2012 Led <led@altlinux.ru> 1:1.7.2-alt2
- rebuild for XORG_ABI_XINPUT = 16.0

* Mon Jun 25 2012 Led <led@massivesolutions.co.uk> 1:1.7.2-alt1
- 1.7.2
- rebuild for XORG_ABI_XINPUT = 13.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.0-alt2
- requires XORG_ABI_XINPUT = 11.0

* Wed Oct 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.0-alt1
- 1.5.0

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt2
- requires XORG_ABI_XINPUT = 4.0

* Sat Jan 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Fri Oct 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt6
- drop fdi for IBM TrackPoint

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt5
- requires XORG_ABI_XINPUT = 2.1

* Thu Aug 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt4
- fixed requires (close #16243)

* Thu Jun 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt3
- added hal policy for TPPS/2 IBM TrackPoint

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt2
- renamed xorg-x11-drv-mouse to xorg-drv-mouse
- added requires XORG_ABI_XINPUT = 2.0

* Fri Mar 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Tue Jan 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.3-alt2
- don't flush buttons, release events can cause paste events

* Thu Oct 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.3-alt1
- 1.2.3

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt2
- rebuild for xorg-server-1.4

* Thu Aug 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt1
- 1.2.2

* Thu Nov 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt1
- 1.2.1:
  + Work around race condition during VT switch.

* Thu Nov 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.2-alt1
- 1.1.2

* Mon Aug 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt2
- mouse.4x -> mousedrv.4

* Sat May 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt1
- 1.1.1

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt2
- prereq xorg-x11-server-common >= 1.0.99.901

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Wed Mar 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.4-alt1
- 1.0.4

* Tue Jan 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.3.1-alt3
- CVS snapshot 2006-01-17

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.3.1-alt2
- fixed requires

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.3.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt0.1
- initial release

