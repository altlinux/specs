Name: xorg-drv-keyboard
Version: 1.6.1
Release: alt3
Serial: 2
Summary: Keyboard input driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Source: xf86-input-keyboard-1.6.1.tar
PreReq: XORG_ABI_XINPUT = %get_xorg_abi_xinput
Provides: xorg-x11-drv-keyboard = %serial:%version-%release
Obsoletes: xorg-x11-drv-keyboard
Provides: xorg-drv-evdev

BuildPreReq: xorg-sdk xorg-util-macros
BuildRequires: libXext-devel libXi-devel xorg-kbproto-devel xorg-randrproto-devel xorg-xproto-devel

%description
kbd  is an Xorg input driver for keyboards.  The driver supports
the standard OS-provided keyboard interface, but these  are  cur-
rently  only  available  to  this  driver  module  for  Linux, BSD, and
Solaris.  This driver is  planned  to  replace  the  built-in  keyboard
driver in a future release of Xorg.

The kbd driver functions as a keyboard input device, and may be used as
the X server's core keyboard.

%prep
%setup -q -n xf86-input-keyboard-%version

%build
#%%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_x11modulesdir/input/*.so
%_man4dir/*

%changelog
* Thu Oct 25 2012 Led <led@altlinux.ru> 2:1.6.1-alt3
- added provides xord-drv-evdev

* Fri Oct 19 2012 Led <led@altlinux.ru> 2:1.6.1-alt2
- rebuild for XORG_ABI_XINPUT = 16.0

* Mon Jun 25 2012 Led <led@massivesolutions.co.uk> 2:1.6.1-alt1
- rebuild for XORG_ABI_XINPUT = 13.0

* Mon Jun 25 2012 Led <led@massivesolutions.co.uk> 2:1.6.1-alt0
- 1.6.1

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0-alt2
- requires XORG_ABI_XINPUT = 11.0

* Wed Oct 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0-alt1
- 1.4.0

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.2-alt2
- requires XORG_ABI_XINPUT = 4.0

* Wed Jan 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt1
- 1.3.2

* Mon Dec 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt9
- fdi: fixed XkbModel

* Fri Dec 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt8
- always console keyboard input source

* Thu Dec 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt7
- returned hal policy

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt6
- removed hal policy

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt5
- requires XORG_ABI_XINPUT = 2.1

* Wed Aug 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt4
- added hal policy for Logitech diNovo Media Desktop Laser Keyboard

* Thu Jun 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt3
- added some hal policy

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt2
- renamed xorg-x11-drv-keyboard to xorg-drv-keyboard
- added requires XORG_ABI_XINPUT = 2.0

* Thu May 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt1
- 1.3.1

* Fri Mar 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Wed Jan 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt3
- automatically inherit the vt's numlock and capslock status

* Tue Jan 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt2
- don't sleep(1) on VT entry

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt1
- 1.2.2

* Tue Dec 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt1
- 1.2.1

* Thu Nov 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt1
- 1.1.1

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt2
- prerequires xorg-x11-server-common >= 1.0.99.901

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1.3-alt2
- fixed requires

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1.3-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1.1-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt0.1
- initial release

