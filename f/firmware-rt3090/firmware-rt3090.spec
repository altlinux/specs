Name: firmware-rt3090
Version: 2.2.1.0
Release: alt1

# Firmware file common/rt2860.bin from
# http://www.ralinktech.com.tw/data/drivers/2009_0612_RT3090_Linux_STA_V2.1.0.0_DPO.tar.gz
# It's renamed in install to rt3090.bin.  rt2860-firmware package isn't used or
# updated because I'm not sure if this firmware also supports rt2860 devices
Summary: Firmware for Ralink RT3090 WiFi adapters
License: Redistributable, no modification permitted
Group: System/Kernel and hardware

Url: http://www.ralinktech.com
Source: 2009_1221_RT3090_Linux_STA_v2.2.1.0.tgz
Packager: Michael Shigorin <mike@altlinux.org>

Provides: firmware-rt3090
BuildArch: noarch

# FIXME: should be defined in rpm-build-$whatever
%define firmwaredir /lib/firmware

%description
This package contains the firmware required by the rt3090 driver.
There wasn't a separate license text in the tarball, and the site
only required to acknowledge GPLv2+ to download it.

%prep
%setup -n 2009_1221_RT3090_Linux_STA_v2.2.1.0

%install
install -pDm644 common/rt2860.bin %buildroot%firmwaredir/rt3090.bin

%files
%firmwaredir/rt3090.bin

%changelog
* Thu Jan 14 2010 Michael Shigorin <mike@altlinux.org> 2.2.1.0-alt1
- 2.2.1.0

* Thu Jan 14 2010 Michael Shigorin <mike@altlinux.org> 2.1.0.0-alt1
- spec based on firmware-rt73usb-1.8-alt2
  and rt3090-firmware-2.1.0.0-2mdv2010.0
