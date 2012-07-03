Name: xorg-drv-synaptics
Version: 1.6.2
Release: alt1
Epoch: 1
Summary: Synaptics touchpad input driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: XORG_ABI_XINPUT = %get_xorg_abi_xinput

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: libX11-devel libXi-devel libXtst-devel xorg-randrproto-devel libmtdev-devel kernel-headers-std-def

%description
synaptics  is  an  Xorg  input driver for the touchpads from
Synaptics Incorporated. Even tough these touchpads (by default, operat-
ing  in a compatibility mode emulating a standard mouse) can be handled
by the normal evdev or mouse drivers, this driver allows more  advanced
features of the touchpad to become available.

%package devel
Summary: Synaptics touchpad input driver development package
Group: Development/C
Requires: %name = %version-%release

%description devel
Synaptics touchpad input driver development package

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
%_bindir/*
%_x11modulesdir/input/*.so
%_xorgsysconfigdir/*.conf
%_man1dir/*
%_man4dir/*

%files devel
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Wed Jun 13 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.6.2-alt1
- 1.6.2

* Fri May 11 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.6.1-alt1
- 1.6.1

* Thu May 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.6.0-alt1
- 1.6.0

* Mon Apr 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.99.903-alt1
- 1.6.0 RC3

* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.99.902-alt1
- 1.6.0 RC2

* Wed Mar 14 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.99.901-alt1
- 1.6.0 RC1

* Sun Mar 11 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.99-alt1
- 1.5.99

* Sun Sep 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.0-alt2
- installed upstream config

* Fri Sep 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.0-alt1
- 1.5.0

* Tue Aug 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.1-alt1
- 1.4.1

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt2
- requires XORG_ABI_XINPUT = 12.2

* Fri Mar 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Wed Sep 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt3
- requires XORG_ABI_XINPUT = 11.0

* Sat Apr 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt2
- moved configuration of hal

* Fri Mar 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.2-alt1
- 1.2.2

* Thu Feb 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt2
- added xorg.conf.d config

* Fri Oct 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Wed Oct 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.99.1-alt1
- 1.1.99.1

* Mon Aug 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.3-alt1
- 1.1.3

* Thu May 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.2-alt1
- 1.1.2

* Thu May 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt1
- 1.1.1

* Mon Mar 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Fri Feb 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt2
- requires XORG_ABI_XINPUT = 4.0

* Tue Feb 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt0.M50.1
- build for branch 5.0

* Mon Feb 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt1
- 1.0.0

* Wed Dec 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.3-alt3
- fdi: added AlpsPS/2 ALPS DualPoint TouchPad

* Wed Dec 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.3-alt2
- fdi: added ETPS/2 Elantech Touchpad

* Mon Dec 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.3-alt1
- 1.0 RC3

* Thu Dec 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.2-alt1
- 1.0 RC2

* Mon Nov 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.1-alt2
- updated config file

* Fri Nov 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.1-alt1
- 1.0 RC1

* Tue Sep 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.2-alt0.M41.1
- build for branch 4.1

* Thu Sep 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.2-alt1
- 0.15.2

* Sun Sep 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.1-alt1
- 0.15.1

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.0-alt6
- requires XORG_ABI_XINPUT = 2.1

* Wed Aug 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.0-alt4
- 0.15.0 release
- fdi: added AlpsPS/2 ALPS GlidePoint 

* Tue Aug 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.0-alt3
- fdi: enabled tap buttons

* Wed Jul 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.0-alt2
- fixed undefined psm_proto_operations

* Sat Jul 12 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.0-alt1
- initial build

