%define module zd1211

Name: firmware-%module
Version: 1.5
Release: alt1

Summary: Firmware for ZD1211 USB WLAN chip
License: GPL v2 or later
Group: System/Kernel and hardware

Url: http://zd1211.ath.cx/
Source: http://downloads.sourceforge.net/zd1211/zd1211-firmware-%version.tar.bz2

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
* Fri Jun 20 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5-alt1
- New version.

* Thu Jul 01 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4-alt1
- Initial build
