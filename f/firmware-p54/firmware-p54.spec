%define _firmwaredir /lib/firmware

Name: firmware-p54
Version: 2.13
Release: alt2

Summary: Firmware for Intersil's Prism54 wireless cards
License: Distributable
Group: System/Kernel and hardware
Url: http://prism54.org/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: 2.13.12.0.arm
Source1: 2.13.24.0.lm86.arm
Source2: 2.13.24.0.lm87.arm
Source3: 2.13.12.0.a.5.2.arm

Conflicts: firmware-prism54 < 2.7.0.0-alt2
BuildArch: noarch

%description
Firmware for Intersil's Prism54 wireless cards.

%prep

%install
mkdir -p %buildroot%_firmwaredir
# SoftMAC
install -m644 %SOURCE0 %buildroot%_firmwaredir/isl3886pci
install -m644 %SOURCE1 %buildroot%_firmwaredir/isl3886usb
install -m644 %SOURCE2 %buildroot%_firmwaredir/isl3887usb
install -m644 %SOURCE3 %buildroot%_firmwaredir/3826.arm

%files
%_firmwaredir/*

%changelog
* Wed Jun 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.13-alt2
- added firmware for SPI/stlc4560

* Thu Mar 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.13-alt1
- SoftMAC firmware for p54pci and p54usb (requires kernel >= 2.6.29)
