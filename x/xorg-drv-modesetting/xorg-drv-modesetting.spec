Name: xorg-drv-modesetting
Version: 0.6.0
Release: alt2
Summary: Generic modesetting driver fo Xorg 
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar

BuildRequires(Pre): xorg-sdk
BuildRequires: libGL-devel xorg-glproto-devel xorg-xf86driproto-devel libudev-devel libXext-devel
BuildRequires: xorg-resourceproto-devel xorg-scrnsaverproto-devel

%description
Generic kernel modesetting driver for Linux.
It is to be used like -fbdev was as a generic fallback driver when the
main driver isn't available.
It doesn't provide any acceleration features except shadowfb.
It also can be used as the driver for chipsets where userspace
acceleration isn't useful, usb devices, dumb framebuffers etc.

%prep
%setup -q

%build
mkdir m4
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install
install -m0640 -D cirrus-kms.xinf %buildroot/usr/share/hwdatabase/videoaliases/cirrus-kms.xinf

%files
%_x11modulesdir/drivers/*.so
%_man4dir/*
%doc COPYING README
/usr/share/hwdatabase/videoaliases/cirrus-kms.xinf

%changelog
* Sat Jan 19 2013 Michael Shigorin <mike@altlinux.org> 0.6.0-alt2
- rebuilt against xorg 1.13.1.901

* Wed Jan  9 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Thu Nov 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5.0-alt2
- fixed garbage drawn by gdk-pixbuf

* Thu Sep 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5.0-alt1
- bump version to 0.5.0

* Thu Sep  6 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.0-alt2
- update from git
- xinf file for installer added

* Mon Jun 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Thu Jun 21 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.0-alt2
- update from git

* Wed May 16 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Wed May 2 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2.0-alt2
- updated from git

* Tue Mar 27 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2.0-alt1
- first build
