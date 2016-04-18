%define uname xf86-video-amdgpu
Name: xorg-drv-amdgpu
Version: 1.1.0
Release: alt1
Summary: AMD GPU video driver for the Xorg X server
License: MIT/X11
Group: System/X11
Url: http://cgit.freedesktop.org/xorg/driver/xf86-video-amdgpu

PreReq: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: xf86-video-amdgpu-%version.tar.gz

BuildRequires(Pre): xorg-sdk xorg-util-macros

# Automatically added by buildreq on Mon Apr 18 2016
# optimized out: libdrm-devel libpciaccess-devel libpixman-devel perl pkg-config python-base xorg-dri2proto-devel xorg-dri3proto-devel xorg-fontsproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-presentproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xf86driproto-devel xorg-xineramaproto-devel xorg-xproto-devel
BuildRequires: libGL-devel libgbm-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-sdk

%description
%summary

%prep
%setup -n %uname-%version

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
* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Initial build for ALT

* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1:1.1.0-alt1
- Autobuild version bump to 1.1.0

