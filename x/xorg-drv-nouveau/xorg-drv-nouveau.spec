Name: xorg-drv-nouveau
Version: 0.0.16
Release: alt9
Epoch: 2
Summary: NVIDIA video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: xorg-dri-nouveau
Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: libGL-devel xorg-glproto-devel xorg-xf86driproto-devel libudev-devel

%description
nouveau  is  an Xorg  driver  for  NVIDIA video cards.  The
driver supports 2D acceleration and provides support for the  following
framebuffer  depths: (15,) 16  and 24.  TrueColor visuals are supported
for these depths

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
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Mon Mar 05 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt9
- requires XORG_ABI_VIDEODRV = 12.0

* Thu Dec 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt8
- update to master git.3d9f6b32

* Tue Nov 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt7
- updated to master git.9fa0c6c

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt6
- updated to master git.169512f

* Tue Jul 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt5
- updated to master git.de9d1ba

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt4
- updated to master git.8378443

* Mon Feb 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt3.bc5dec2
- updated to master git.bc5dec2

* Thu Feb 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt3.c123618
- updated to master git.c123618

* Sat Jan 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt3
- updated to master git.b795ca6

* Tue Aug 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt2
- GIT snapshot 2010-08-13 (00d390952c912d4e9fc2c962caaeb90bf563d5b1)

* Sat Mar 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.16-alt1
- GIT snapshot 2010-03-05 (c642b9f7a13bdeecd0a83ddcbf6d6d4f2c287501)

* Thu Feb 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.15-alt3
- don't requires firmware

* Sat Feb 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.15-alt2
- GIT snapshot 2010-02-10 (9b4118d6d1fa488db86cd7d2875beea9cdefb096)

* Mon Feb 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:0.0.15-alt1
- initial release

