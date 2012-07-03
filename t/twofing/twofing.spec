Name: twofing
Version: 0.0.9
Release: alt2
Summary: Daemon for two-finger gestures support on touchscreen 
License: BSD-like
Group: System/X11
Url: http://plippo.de/dev_twofing.htm
Packager: Michail Yakushin <silicium@altlinux.ru>

Source: %name-%version.tar

Patch0: pegatron-udev.patch
Patch1: desktop.patch

BuildRequires(Pre): xorg-sdk libX11-devel libXtst-devel libXrandr-devel

%description
twofing is a daemon which runs in the background and recognizes
two-finger gestures performed on a touchscreen and converts them into
mouse and keyboard events. This way, such gestures can be used in almost
all existing applications (even ones where you wouldn't expect it, like
Wine applications) without having to modify them.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%make_build

%install
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_sysconfdir/udev/rules.d/
%make DESTDIR=%buildroot install
mkdir -p %buildroot/%_sysconfdir/xdg/autostart/
install -m0644 %name.desktop %buildroot/%_sysconfdir/xdg/autostart/

%files
%_bindir/*
%_sysconfdir/udev/rules.d/*
%_sysconfdir/xdg/autostart/*

%changelog
* Fri May 11 2012 Paul Wolneykien <manowar@altlinux.ru> 0.0.9-alt2
- Fix/improve udev rules.

* Tue Mar 27 2012 Paul Wolneykien <manowar@altlinux.ru> 0.0.9-alt1
- Version 0.0.9

* Tue Feb 28 2012 Paul Wolneykien <manowar@altlinux.ru> 0.0.9a-alt1
- Version 0.0.9a.

* Mon Dec 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.0.7-alt2
- usb id for pegatron lucid added
- autostart desktop file added

* Mon Oct 10 2011 Michail Yakushin <silicium@altlinux.ru> 0.0.7-alt1
- inital build for sisyphus


