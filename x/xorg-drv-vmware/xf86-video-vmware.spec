%define uname xf86-video-vmware
Name: xorg-drv-vmware
Version: 13.0.0
Release: alt1
Summary: VMware SVGA Device video driver
License: MIT/X11
Epoch: 1
Group: System/X11
Url: http://cgit.freedesktop.org/xorg/driver/xf86-video-vmware

PreReq: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: xf86-video-vmware-%version.tar.gz

BuildRequires(Pre): xorg-sdk xorg-util-macros
BuildRequires: libXext-devel xorg-fontsproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: xorg-resourceproto-devel xorg-scrnsaverproto-devel

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
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Tue Feb 05 2013 Fr. Br. George <george@altlinux.ru> 1:13.0.0-alt1
- Autobuild version bump to 13.0.0

* Tue Feb 05 2013 Fr. Br. George <george@altlinux.ru> 0.0.0-alt1
- Initial zero version build

