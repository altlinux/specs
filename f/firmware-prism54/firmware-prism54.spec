%define _firmwaredir /lib/firmware

Name: firmware-prism54
Version: 2.7.0.0
Release: alt2

Summary: Firmware for Prism GT 54 MBit/s wireless cards
License: Distributable
Group: System/Kernel and hardware
Url: http://prism54.org/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: prism54-1.0.4.3.arm
Source1: prism54-1.1.0.0.arm

BuildArch: noarch

%description
Firmware for Prism GT 54 MBit/s wireless cards.

%prep

%install
mkdir -p %buildroot%_firmwaredir
# FullMAC
install -m644 %SOURCE0 %buildroot%_firmwaredir/
install -m644 %SOURCE1 %buildroot%_firmwaredir/
ln -s prism54-1.1.0.0.arm %buildroot%_firmwaredir/isl3877
ln -s prism54-1.0.4.3.arm %buildroot%_firmwaredir/isl3880
ln -s prism54-1.0.4.3.arm %buildroot%_firmwaredir/isl3890

%files
%_firmwaredir/*

%changelog
* Thu Mar 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0.0-alt2
- removed SoftMAC firmware

* Thu Feb 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0.0-alt1
- added SoftMAC firmware for p54pci and p54usb drivers

* Sun Jul 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4.3-alt3
- added firmware for ISL3877
- removed requires hotplug

* Tue Jan 25 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4.3-alt2
- moved firmware dir to /lib/firmware

* Mon Jan 17 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4.3-alt1
- initial release

