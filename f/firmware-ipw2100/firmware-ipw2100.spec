
%define firmware_name ipw2100

Name: firmware-%firmware_name
Version: 1.3
Release: alt2
License: distributable
Group: System/Kernel and hardware
Summary: Firmware for the Intel(R) PRO/Wireless 2100 Driver
Source0: %firmware_name-fw-%version.tgz
Url: http://%firmware_name.sourceforge.net/firmware.php
BuildArch: noarch


%description
This package contains the firmware for the ipw-2100 driver. Usage of
the firmware is subject to the terms contained in /lib/ipw2100-LICENSE.
Please read the license carefully.


%prep
%setup -q -c

%__tar -zxvf %SOURCE0

%install
install -d $RPM_BUILD_ROOT/lib/firmware

install -p *.fw $RPM_BUILD_ROOT/lib/firmware
cp -df LICENSE $RPM_BUILD_ROOT/lib/firmware/LICENSE-%firmware_name-fw

%files
%defattr(644,root,root,755)
/lib/firmware/*

%changelog
* Tue Feb 06 2007 Alexey Shabalin <shaba@altlinux.ru> 1.3-alt2
- drop Requires: hotplug (#9600)
- Use /lib/firmware dir without macros
- rename LICENSE file

* Thu Apr 07 2005 Alexey Shabalin <shaba@altlinux.ru> 1.3-alt1
- init release 
