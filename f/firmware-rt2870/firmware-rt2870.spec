Name: firmware-rt2870
Version: 8
Release: alt1

Summary: Firmware for Ralink RT2870 ABGN network adapters
License: Redistributable, no modification permitted
Group: System/Kernel and hardware

Packager: Michael Shigorin <mike@altlinux.org>
Url: http://www.ralinktech.com
Source: RT2870_Firmware_V%version.tar.bz2

BuildRequires: unzip
BuildArch: noarch

%define firmwaredir /lib/firmware

%description
This package contains the firmware required by the rt2800pci driver.
Usage of the firmware is subject to the terms and conditions contained
inside the provided LICENSE.ralink-firmware.txt file.
Please read it carefully.

Note that rt2870sta driver included in 2.6.32 kernel might not require
this package, see also http://bugs.archlinux.org/task/16775

%prep
%setup -n RT2870_Firmware_V%version

%install
mkdir -p %buildroot%firmwaredir
install -pm644 rt2870.bin %buildroot%firmwaredir/

%files
%doc LICENSE.ralink-firmware.txt
%firmwaredir/rt2870.bin

%changelog
* Thu Jan 14 2010 Michael Shigorin <mike@altlinux.org> 8-alt1
- spec based on firmware-rt2860-11-alt1
- repackaged tarball from rt2870-firmware-8-2mdv2010.0
  (unzip complains regarding backslashes)
