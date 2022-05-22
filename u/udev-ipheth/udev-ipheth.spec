Name:     udev-ipheth
Version:  1.05
Release:  alt1

%define modprobedir %_sysconfdir/modprobe.d/


Summary:  iPhone USB Ethernet Driver
License:  GPL-2.0+
Group:    System/Configuration/Hardware
Url:      https://github.com/dgiagio/ipheth
Requires: libimobiledevice

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:  ipheth-pair.tar
Source1: ipheth-modprobe.conf
Patch1:  ipheth-makefile-1.05.patch

BuildRequires: udev libimobiledevice-devel >= 1.3.0
Provides: ipheth-utils

%description 
USB tethering driver support utilities for the iPhone
Internet tethering driver for the iPhone which allows Linux systems to
make use of the phone's internet connection using a USB cable. Unlike
other solutions out there, you don't need to jailbreak your phone or
install third-party proxy applications.

This package provides the support utilities required to automatically
set up the tethered connection.


%prep
%setup -n ipheth-pair
%patch1 -p1


%build
%make_build VER=1.0

%install
%makeinstall_std
install -d %buildroot/%modprobedir/
install -m 644 %SOURCE1 %buildroot/%modprobedir/

%files
%modprobedir/*
/lib/udev/ipheth-pair
/lib/udev/rules.d/*

%changelog
* Sun May 22 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.05-alt1
- Initial build for Sisyphus

