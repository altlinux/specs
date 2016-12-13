Name: xorg-drv-amdgpu
Version: 1.2.0
Release: alt1
Summary: AMD GPU video driver for the Xorg X server
License: MIT/X11
Group: System/X11
Url: http://cgit.freedesktop.org/xorg/driver/xf86-video-amdgpu

PreReq: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk xorg-util-macros
BuildRequires: libGL-devel libgbm-devel libudev-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel
BuildRequires: xorg-fixesproto-devel xorg-damageproto-devel

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
* Thu Dec 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Thu Oct 13 2016 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Initial build for ALT

* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1:1.1.0-alt1
- Autobuild version bump to 1.1.0

