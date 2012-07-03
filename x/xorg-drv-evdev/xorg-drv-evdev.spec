%define _xconfdir %_sysconfdir/X11/xorg.conf.d

Name: xorg-drv-evdev
Version: 2.7.0
Release: alt1
Epoch: 2
Summary: Generic Linux input driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: XORG_ABI_XINPUT = %get_xorg_abi_xinput
Provides: xorg-drv-mouse = %epoch:%version-%release xorg-drv-keyboard = %epoch:%version-%release
Obsoletes: xorg-drv-mouse xorg-drv-keyboard

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: libmtdev-devel libxkbfile-devel libudev-devel xorg-xextproto-devel
BuildRequires: xorg-inputproto-devel xorg-randrproto-devel xorg-xproto-devel

%description
evdev  is  an  Xorg  input  driver for Linux generic event devices.
It therefore supports all input devices that the kernel knows
about, including most mice and keyboards.

%package devel
Summary: Generic Linux input driver development package
Group: Development/C
Requires: %name = %version-%release

%description devel
Generic Linux input driver development package

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

mkdir -p %buildroot%_xconfdir
install -m644 *.conf %buildroot%_xconfdir/
install -pD -m644 99-x11-keyboard.rules %buildroot%_sysconfdir/udev/rules.d/99-x11-keyboard.rules

%files
%config(noreplace) %_xconfdir/*.conf
%_sysconfdir/udev/rules.d/99-x11-keyboard.rules
%_x11modulesdir/input/*.so
%_man4dir/*

%files devel
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Wed Mar 07 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:2.7.0-alt1
- 2.7.0

* Mon Mar 05 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:2.6.0-alt4
- requires XORG_ABI_XINPUT = 16.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:2.6.0-alt3
- requires XORG_ABI_XINPUT = 13.0

* Sat Feb 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:2.6.0-alt2
- requires XORG_ABI_XINPUT = 12.2

* Tue Jan 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:2.6.0-alt1
- 2.6.0

* Wed Jan 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:2.5.99.903-alt1
- 2.6 RC3

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.5.99.902-alt1
- 2.6 RC2

* Mon Nov 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.5.99.901-alt1
- 2.6 RC1

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.5.0-alt2
- obsoletes xorg-drv-keybord, xorg-drv-mouse
- IBM TrackPoint: added an example of XAxisMapping (closes: #24020)

* Mon Aug 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.5.0-alt1
- 2.5.0

* Fri Aug 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.4.0-alt3
- requires XORG_ABI_XINPUT = 11.0

* Thu Apr 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.4.0-alt2
- removed unnecessary configs

* Tue Apr 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.4.0-alt1
- 2.4.0

* Mon Apr 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.3.2-alt3
- rewrited configs for udev backend

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2.3.2-alt2
- requires XORG_ABI_XINPUT = 7.0

* Fri Dec 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.3.2-alt1
- 2.3.2

* Thu Dec 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.3.1-alt1
- 2.3.1

* Mon Oct 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.3.0-alt1
- 2.3.0

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.2.99.2-alt1
- 2.2.99.2

* Tue Oct 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.2.99.1-alt1
- 2.2.99.1

* Fri Aug 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.2.5-alt1
- 2.2.5

* Thu Aug 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.2.4-alt1
- 2.2.4

* Thu Jul 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.2.3-alt1
- 2.2.3

* Thu Apr 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.2.2-alt1
- 2.2.2

* Tue Mar 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.2.1-alt1
- 2.2.1

* Mon Mar 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.2.0-alt1
- 2.2.0

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.1.3-alt3
- requires XORG_ABI_XINPUT = 4.0

* Sat Feb 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.1.3-alt2
- TrackPoint: set wheel button to 2 (close #18868)

* Tue Feb 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.1.3-alt1
- 2.1.3

* Mon Feb 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.1.2-alt1
- 2.1.2

* Tue Jan 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.1.1-alt1
- 2.1.1

* Tue Jan 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2.1.0-alt3
- fixed XkbModel parsing error

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.1.0-alt2
- x11-input-mouse-thinkpad.fdi: removed XAxisMapping

* Wed Nov 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.1.0-alt1
- 2.1.0

* Mon Nov 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.99.3-alt1
- 2.1 RC3

* Sat Nov 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.99.2-alt2
- add fdi for support touchscreen

* Fri Oct 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.99.2-alt1
- 2.1 RC2

* Fri Oct 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.7-alt1
- 2.0.7

* Mon Oct 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.6-alt2
- Set pInfo->fd to -1 on DEVICE_CLOSE

* Thu Oct 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.6-alt1
- 2.0.6

* Fri Sep 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.5-alt1
- 2.0.5

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.4-alt2
- requires XORG_ABI_XINPUT = 2.1

* Fri Aug 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.4-alt1
- 2.0.4

* Fri Aug 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.3-alt1
- 2.0.3

* Mon Jul 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.2-alt1
- 2.0.2

* Mon Jun 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.1-alt2
- fixed xorg/module version

* Sun Jun 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.1-alt1
- 2.0.1

* Wed Jun 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:2.0.0-alt1
- 2.0.0 release

* Wed Jun 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.99.4-alt1
- 2.0 RC4

* Wed Jun 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.99.3-alt1
- 2.0 RC3

* Tue Jun 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.99.2-alt3
- added middle-mouse button emulation

* Sat Jun 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.99.2-alt2
- fixed parameters of InitValuatorClassRec

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.99.2-alt1
- 2.0 RC2
- renamed xorg-x11-drv-evdev to xorg-drv-evdev
- added requires XORG_ABI_XINPUT = 2.0

* Tue Jan 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt3
- initialise b_map_data to correct size

* Tue Jan 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt2
- don't flush buttons on init

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.5-alt1
- 1.1.5

* Thu Nov 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.4-alt1
- 1.1.4

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.3-alt1
- 1.1.3

* Tue May 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.2-alt3
- CVS snapshot 2006-05-15

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.2-alt2
- requires xorg-x11-server >= 1.0.99.901

* Mon May 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.2-alt1
- 1.1.2

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt1
- 1.1.1

* Sun Mar 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.5-alt2
- CVS snapshot 20060227

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0.2-alt0.1
- initial release

