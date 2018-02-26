
%define firmware_name ipw2200

Name: firmware-%firmware_name
Version: 3.1
Release: alt1
License: distributable
Group: System/Kernel and hardware
Summary: Firmware for the Intel(R) PRO/Wireless 2200 Driver
Source0: %firmware_name-fw-%version.tgz
Url: http://%firmware_name.sourceforge.net/firmware.php
BuildArch: noarch
Provides: firmware-%firmware_name = %version
Provides: firmware-%firmware_name-3.0 = %version
Obsoletes: firmware-%firmware_name-3.0

%description
This package contains the firmware for the ipw-2200 driver. Usage of
the firmware is subject to the terms contained in /lib/LICENSE.ipw2200-fw
Please read the license carefully.

%prep
%setup -q -c

%__tar -zxvf %SOURCE0

%install
install -d $RPM_BUILD_ROOT/lib/firmware

install -p */*.fw $RPM_BUILD_ROOT/lib/firmware
cp -df */LICENSE.ipw2200-fw $RPM_BUILD_ROOT/lib/firmware/

%files
%defattr(644,root,root,755)
/lib/firmware/*

%changelog
* Fri Oct 02 2009 Alexey Shabalin <shaba@altlinux.ru> 3.1-alt1
- 3.1

* Fri Mar 02 2007 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt3
- add Provides: firmware-%%firmware_name = %%version

* Tue Feb 06 2007 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt2
- rename firmware-ipw2200-3.0 -> firmware-ipw2200
- drop Requires: hotplug (#9600)
- clenup spec

* Wed May 17 2006 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt1.1
- remove %%_lib  

* Wed May 17 2006 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt1
- init release firmware v3 for ipw2200 v1.1.1 and newer 

* Fri May 27 2005 Alexey Shabalin <shaba@altlinux.ru> 2.3-alt2
- rename package firmware-ipw2200-2.3 for kernel module v1.0.4

* Tue May 24 2005 Alexey Shabalin <shaba@altlinux.ru> 2.3-alt1
- update 2.3 firmware for kernel module v1.0.4 

* Thu Apr 07 2005 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- init release 
