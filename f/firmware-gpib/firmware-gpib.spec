Name:         firmware-gpib
Version:      20080810
Release:      alt1

Summary:      Firmware for GPIB (IEEE 488) hardware.
Group:        System/Kernel and hardware
URL:          http://linux-gpib.sourceforge.net/
Source:       %name-%version.tar
License:      distributable
BuildArch:    noarch

%description
Firmware for GPIB (IEEE 488) hardware.

%prep
%setup -q

%install
%makeinstall_std

%files
%dir /lib/firmware/agilent_82357a
%dir /lib/firmware/ni_gpib_usb_b
/lib/firmware/agilent_82357a/*
/lib/firmware/ni_gpib_usb_b/*

%changelog
* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 20080810-alt1
- v.2008.08.10, first build for altlinux

