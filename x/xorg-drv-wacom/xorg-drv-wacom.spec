Name: xorg-drv-wacom
Version: 0.15.0
Release: alt1
Epoch: 1
Summary: Wacom input driver
License: GPLv2
Group: System/X11
Url: http://linuxwacom.sourceforge.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: XORG_ABI_XINPUT = %get_xorg_abi_xinput
Conflicts: linuxwacom

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: doxygen libX11-devel libXi-devel libXinerama-devel libXext-devel libXrandr-devel libudev-devel

%description
wacom is an X input driver for Wacom devices

%package devel
Summary: Wacom input driver development package
Group: Development/C
Requires: %name = %version-%release

%description devel
Wacom input driver development package

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--with-xorg-module-dir=%_x11modulesdir
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/xsetwacom
%_x11modulesdir/input/*.so
%_xorgsysconfigdir/*.conf
%_man1dir/*.1*
%_man4dir/*.4*

%files devel
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Thu May 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.15.0-alt1
- 0.15.0

* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.14.0-alt1
- 0.14.0

* Wed Feb 22 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.13.0-alt1
- 0.13.0

* Fri Dec 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.12.0-alt1
- 0.12.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.11.1-alt2
- requires XORG_ABI_XINPUT = 13.0

* Sun Jun 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.11.1-alt1
- 0.11.0

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.11.0-alt1
- 0.11.0

* Wed Feb 23 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.11-alt1
- 0.10.11

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.10-alt1
- 0.10.10

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.8-alt1
- 0.10.8

* Mon May 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.6-alt1
- 0.10.6

* Thu Feb 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.4-alt3
- added xorg.conf.d config

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.4-alt2
- requires XORG_ABI_XINPUT = 9.0

* Sat Jan 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.4-alt1
- 0.10.4

* Thu Dec 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.3-alt1
- 0.10.3

