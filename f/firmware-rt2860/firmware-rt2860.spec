Name: firmware-rt2860
Version: 11
Release: alt1

Summary: Firmware for Ralink RT2760/RT2790/RT2860/RT2890 A/B/G/N network adapters
License: Redistributable, no modification permitted
Group: System/Kernel and hardware

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Url: http://www.ralinktech.com
Source: RT2860_Firmware_V%version.zip

BuildArch: noarch

%define firmwaredir /lib/firmware

BuildPreReq: unzip

%description
This package contains the firmware required by the rt2800pci driver for Linux.
Usage of the firmware is subject to the terms and conditions contained
inside the provided LICENSE.ralink-firmware.txt file.
Please read it carefully.

Note that rt2860sta driver included in 2.6.29 kernel doesn't require
this package.

%prep
%setup -n RT2860_Firmware_V%version

%install
mkdir -p %buildroot%firmwaredir
install -pm644 *.bin %buildroot%firmwaredir

%files
%doc LICENSE.ralink-firmware.txt
%firmwaredir/*

%changelog
* Sat Sep 19 2009 Andrey Rahmatullin <wrar@altlinux.ru> 11-alt1
- initial build
