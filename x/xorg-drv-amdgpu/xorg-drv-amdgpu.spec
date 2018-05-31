Name: xorg-drv-amdgpu
Version: 18.0.1
Release: alt1
Summary: AMD GPU video driver for the Xorg X server
License: MIT/X11
Group: System/X11
Url: http://cgit.freedesktop.org/xorg/driver/xf86-video-amdgpu

PreReq: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk xorg-util-macros
BuildRequires: libGL-devel libgbm-devel libudev-devel xorg-proto-devel

%description
%summary

%prep
%setup -q

%build
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%dir %_x11modulesdir/drivers
%_xorgsysconfigdir/*
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Mon May 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 18.0.1-alt1
- 18.0.1

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt0.M80P.1
- backport to p8 branch

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Thu Mar 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Thu Dec 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Thu Oct 13 2016 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Initial build for ALT

* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1:1.1.0-alt1
- Autobuild version bump to 1.1.0

