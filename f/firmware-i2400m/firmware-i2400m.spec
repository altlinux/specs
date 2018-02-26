%define firmware_name i2400m
%define realname i2400m-fw

Name: firmware-%firmware_name
Version: 1.5.0
Release: alt1

Summary: Firmware for Intel Wireless WiMAX Connection devices
Group: System/Kernel and hardware
License: Redistributable
Url: http://linuxwimax.org/

Source: %realname-%version.tar
BuildArch: noarch

%description
This package contains firmware for i2400m based devices (Intel
Wireless WiMAX Connection 5x50 and 6x50).

%prep
%setup -n %realname-%version

%install
install -d %buildroot/lib/firmware
install -p *.sbcf %buildroot/lib/firmware/

%files
%doc README LICENSE
/lib/firmware/*.sbcf

%changelog
* Sat Sep 11 2010 Alexey I. Froloff <raorn@altlinux.org> 1.5.0-alt1
- [1.5.0]
