Name: firmware-rt61pci
Version: 1.2
Release: alt1

Summary: Firmware for Ralink RT2561/RT2661 A/B/G network adapters
License: Redistributable, no modification permitted
Group: System/Kernel and hardware

Url: http://www.ralinktech.com
Source: http://www.ralinktech.com.tw/data/RT61_Firmware_V%version.zip
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%define firmwaredir /lib/firmware

# Automatically added by buildreq on Thu Jan 22 2009
BuildRequires: unzip

%description
This package contains the firmware required by the rt61pci driver for Linux.
Usage of the firmware is subject to the terms and conditions contained
inside the provided LICENSE.ralink-firmware.txt file.
Please read it carefully.

%prep
%setup -n RT61_Firmware_V%version
sed -i 's/\r//' LICENSE.ralink-firmware.txt

%install
mkdir -p %buildroot%firmwaredir
install -pm644 *.bin %buildroot%firmwaredir

%files
%doc LICENSE.ralink-firmware.txt
%firmwaredir/*

%changelog
* Thu Jan 22 2009 Michael Shigorin <mike@altlinux.org> 1.2-alt1
- built for ALT Linux
- spec adapted from Fedora, thoroughly cleaned up

* Mon Sep 17 2007 kwizart < kwizart at gmail.com > - 1.2-4
- Disable dist tag
- Preserve timestamp
- Add license from Ralink
- Improved summary and description

* Mon Mar 19 2007 kwizart < kwizart at gmail.com > - 1.2-3
- Update Source url (uses .com.tw instead of .com)
- Fix License field

* Mon Feb 26 2007 kwizart < kwizat at gmail.com > - 1.2-2
- Update the download link

* Tue Sep 13 2006 kwizart < kwizart at gmail.com > - 1.2-1_FC5
- inital release.
