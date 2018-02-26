
%define firmware_name ipw3945

Name: firmware-%firmware_name
Version: 1.14.2
Release: alt2
Packager: Alex Karpov <karpov@altlinux.ru>
License: non-free
Group: System/Kernel and hardware
Summary: Firmware for the Intel(R) PRO/Wireless 3945ABG driver module
Source0: http://bughost.org/ipw3945/ucode/%firmware_name-ucode-%version.tgz
Url: http://bughost.org/ipw3945/
BuildArch: noarch

%description
This package contains the firmware for the ipw3945 driver. Usage of
the firmware is subject to the terms contained in /lib/firmware/%firmware_name-LICENSE.
Please read the license carefully.

%prep
%setup -q -n %firmware_name-ucode-%version

%install
install -d $RPM_BUILD_ROOT/lib/firmware
install -p *.ucode $RPM_BUILD_ROOT/lib/firmware/
cp -df LICENSE.%firmware_name-ucode $RPM_BUILD_ROOT/lib/firmware/%firmware_name-LICENSE

%files
%defattr(644,root,root,755)
%doc README.%firmware_name-ucode
/lib/firmware/%firmware_name-LICENSE
/lib/firmware/*.ucode

%changelog
* Sat May 05 2007 Alex Karpov <karpov@altlinux.ru> 1.14.2-alt2
- removed hotplug requirement (#11684)

* Tue Apr 10 2007 Alex Karpov <karpov@altlinux.ru> 1.14.2-alt1
- 1.14.2

* Fri Apr 28 2006 Grigory Batalov <bga@altlinux.ru> 1.13-alt1.1
- Use /lib/firmware dir without macros.

* Mon Apr 24 2006 Grigory Batalov <bga@altlinux.ru> 1.13-alt1
- Initial ALTLinux release.
