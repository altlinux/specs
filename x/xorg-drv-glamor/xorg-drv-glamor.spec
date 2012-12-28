Name: xorg-drv-glamor
Version: 0.5
Release: alt1.f1457c
Summary: Glamor video driver
License: BSD
Group: System/X11
Url: http://www.freedesktop.org/wiki/Software/Glamor
Packager: L.A. Kostis <lakostis@altlinux.org>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Provides: libglamor = %version-%release
Obsoletes: libglamor <= 0.5-alt0.1

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: libdrm-devel libGL-devel libpixman-devel libEGL-devel libgbm-devel 
BuildRequires: pkgconfig

%description
The glamor module is an open-source 2D graphics common driver for the X
Window System as implemented by X.org. It supports a variety of graphics
chipsets which have OpenGL/EGL/GBM supports.

Its a GL-based rendering acceleration library for X server:

* It uses GL functions and shader to complete the 2D graphics operations.
* It uses normal texture to represent a drawable pixmap if possible.
* It calls GL functions to render to the texture directly. 

%package -n libglamor-devel
Summary: libglamor development environment
Group: Development/C
Requires: libglamor = %version-%release libpixman-devel

%description -n libglamor-devel
This package contains all files which are needs to compile programs using
the libglamor library

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--with-xorg-conf-dir=%_x11sysconfdir/xorg.conf.d \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_x11sysconfdir/xorg.conf.d/*.conf
%_x11modulesdir/libglamor*.so
%doc COPYING README ReleaseNote

%files -n libglamor-devel
%_x11includedir/xorg/*
%_pkgconfigdir/*.pc

%changelog
* Fri Dec 28 2012 L.A. Kostis <lakostis@altlinux.ru> 0.5-alt1.f1457c
- move conf to sysconfdir (tnx legion@).
- combine libglamor and -drv.
- update release (GIT f1457c).

* Fri Dec 28 2012 L.A. Kostis <lakostis@altlinux.ru> 0.5-alt0.1
- initial build for ALTLinux.

