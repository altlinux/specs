%define firmware_name iwl4965
%define realname iwlwifi-4965

Name: firmware-%firmware_name
Version: 228.61.2.24
Release: alt2
Serial: 2
Packager: Anton Farygin <rider@altlinux.ru>
License: Redistributive
Group: System/Kernel and hardware
Summary: firmware for Intel Wireless WiFi Link 4965AGN Network Connection Adapter
Source0: http://intellinuxwireless.org/iwlwifi/downloads/%realname-ucode-%version.tgz
Url: http://intellinuxwireless.org/
BuildArch: noarch

%description
The file iwlwifi-4965.ucode provided in this package is required to be present
on your system in order for the Intel Wireless WiFi Link 4965AGN driver for
Linux (iwlwifi-4965) to be able to operate on your system.

%prep
%setup -q -n %realname-ucode-%version

%install
install -d %buildroot/lib/firmware
install -p *.ucode %buildroot/lib/firmware/

%files
%defattr(644,root,root,755)
%doc README.%realname-ucode LICENSE.%realname-ucode
/lib/firmware/*.ucode

%changelog
* Tue Aug 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:228.61.2.24-alt2
- drop version 1 UCODE_API firmware

* Thu Sep 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:228.61.2.24-alt1
- new version

* Fri Dec 19 2008 Anton Farygin <rider@altlinux.ru> 2:228.57-alt1.23
- new version

* Fri Aug 08 2008 L.A. Kostis <lakostis@altlinux.ru> 2:228.57-alt1.21
- add version 1 UCODE_API firmware.
- combine 1 and 2 versions.

* Tue Jul 15 2008 L.A. Kostis <lakostis@altlinux.ru> 1:228.57.2.21-alt1
- new version.

* Mon Jan 21 2008 L.A. Kostis <lakostis@altlinux.org> 1:4.44.1.20-alt1
- new version.

* Fri Nov 09 2007 L.A. Kostis <lakostis@altlinux.ru> 4.44.17-alt2
- add IWL4965_UCODE_API for incompatibility with previous versions.

* Sun Nov 04 2007 L.A. Kostis <lakostis@altlinux.ru> 4.44.17-alt1
- initial build for Sisyphus.
- .spec based on firmware-ipw3945.

