%define module zd1211

Name: firmware-%module
Version: 1.4
Release: alt1

Summary: Firmware for ZD1211 USB WLAN chip
License: GPL v2 or later
Group: System/Kernel and hardware

%define distname %module-firmware

Url: http://zd1211.ath.cx/
Source: http://downloads.sourceforge.net/zd1211/zd1211-firmware-%{version}.tar.bz2
Packager: Gleb F-Malinovskiy <glebfm@altlinux.org>

Provides: firmware-zd1211
BuildArch: noarch

%define firmwaredir /lib/firmware

%description
Firmware for USB WLAN sticks based on the ZyDAS ZD1211 chip

%prep
%setup -n zd1211-firmware

%install
install -d %buildroot%firmwaredir/zd1211
install -pm644 zd* %buildroot%firmwaredir/zd1211

%files
%doc README
%firmwaredir/zd1211

%changelog
* Thu Jul 01 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4-alt1
- Initial build

* Thu Oct  4 2007 lnussel@suse.de
- new version 1.4
  * Sync to vendor driver v2.21.0.0; According to Atheros, this
  firmware fixes a USB disconnect issue which most commonly
  appeared when running "lsusb" or "cat /proc/usb/devices" while
  using the device.
- update modaliases
* Tue Mar 13 2007 lnussel@suse.de
- new package for version 1.3
