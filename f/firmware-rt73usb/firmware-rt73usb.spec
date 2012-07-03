Name: firmware-rt73usb
Version: 1.8
Release: alt2

Summary: Firmware for Ralink RT2571W/RT2671 A/B/G network adaptors
License: Redistributable, no modification permitted
Group: System/Kernel and hardware

Url: http://www.ralinktech.com
Source0: http://www.ralinktech.com.tw/data/RT71W_Firmware_V%version.zip
Source1: rt73.bin
Packager: Michael Shigorin <mike@altlinux.org>

Provides: firmware-rt73 = %version-%release
Obsoletes: firmware-rt73 <= 1.0.0-alt2
BuildArch: noarch

# FIXME: should be defined in rpm-build-$whatever
%define firmwaredir /lib/firmware

# Automatically added by buildreq on Thu Jan 22 2009
BuildRequires: unzip

%description
This package contains the firmware required by the rt73usb driver for Linux.
Usage of the firmware is subject to the terms and conditions contained
inside the provided LICENSE.ralink-firmware.txt file.
Please read it carefully.

%prep
%setup -n RT71W_Firmware_V%version
sed -i 's/\r//' LICENSE.ralink-firmware.txt

%install
install -pDm644 %SOURCE1 %buildroot%firmwaredir/rt73.bin

%files
%doc LICENSE.ralink-firmware.txt
%firmwaredir/rt73.bin

%changelog
* Sun Feb 22 2009 Michael Shigorin <mike@altlinux.org> 1.8-alt2
- oops, apparently there was firmware-rt73 built by Vitaly Lipatov
  from kernel-source-rt73 which got obsolete since the driver was
  merged into kernel proper; as it contained more recent rt73.bin
  from CVS (it hasn't changed since and was tested by me on actual
  hardware); merging spec, obsoleting old name
- NB: upstream notice:
  rt73sta.dat config file is deprecated and must be removed,
  along with the whole /etc/Wireless directory

* Thu Jan 22 2009 Michael Shigorin <mike@altlinux.org> 1.8-alt1
- built for ALT Linux
- spec adapted from Fedora, thoroughly cleaned up

* Sun Nov 04 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- cvs build from 20071104
- separate package with firmware
- add initial config, cleanup spec

* Tue Oct 23 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

* Mon Sep 17 2007 kwizart < kwizart at gmail.com > - 1.8-4
- Disable dist tag
- Preserve timestamp
- Add license from Ralink
- Improved summary and description

* Mon Mar 19 2007 kwizart < kwizart at gmail.com > - 1.8-3
- Update Source url (uses .com.tw instead of .com)
- Fix License field

* Mon Feb 26 2007 kwizart < kwizat at gmail.com > - 1.8-2
- Update the download link

* Tue Sep 13 2006 kwizart < kwizart at gmail.com > - 1.8-1_FC5
- inital release.
