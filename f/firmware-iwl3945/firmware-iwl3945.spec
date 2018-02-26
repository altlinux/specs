
%define firmware_name iwl3945
%define realname iwlwifi-3945

Name: firmware-%firmware_name
Version: 15.32
Release: alt1.2.9
Serial: 2
Packager: L.A. Kostis <lakostis@altlinux.ru>
License: Redistributive
Group: System/Kernel and hardware
Summary: firmware for Intel PRO/Wireless 3945ABG/BG Network Connection Adapter
Source0: http://intellinuxwireless.org/iwlwifi/downloads/%realname-ucode-%version.tar.bz2
Url: http://intellinuxwireless.org/
BuildArch: noarch

%description
The file iwlwifi-3945.ucode provided in this package is required to be
present on your system in order for the Intel PRO/Wireless 3945ABG/BG Network
Connection Adapter driver for Linux (iwlwifi-3945) to be able to operate
on your system.

%prep
%setup -q -n %realname-ucode-%version

%install
install -d $RPM_BUILD_ROOT/lib/firmware
install -p *.ucode $RPM_BUILD_ROOT/lib/firmware/
cp -df LICENSE.%realname-ucode $RPM_BUILD_ROOT/lib/firmware/%realname-LICENSE

%files
%defattr(644,root,root,755)
%doc README.%realname-ucode
/lib/firmware/%realname-LICENSE
/lib/firmware/*.ucode

%changelog
* Sun Jun 28 2009 L.A. Kostis <lakostis@altlinux.ru> 2:15.32-alt1.2.9
- Update UCODE_API v2 to version 15.32.2.9.

* Wed Oct 22 2008 L.A. Kostis <lakostis@altlinux.ru> 2:15.28-alt1.8
- new 15.28.x.8 uCode:
  + Version 15.28.x.8
   - Allow full active dwell time after scan auto-switches from passive to
   active scan
   - Allow direct probes on passive-scan channels (after auto-switch)
   - Expand coverage in Event Log

- combine IWL3945_UCODE_API and IWL3945_UCODE_API version 2.

* Sun Sep 21 2008 L.A. Kostis <lakostis@altlinux.ru> 1:15.28.1.6-alt2
- add lost serial.

* Sun Sep 21 2008 L.A. Kostis <lakostis@altlinux.ru> 15.28.1.6-alt1
- version 15.28.1.6.

* Mon Jan 21 2008 L.A. Kostis <lakostis@altlinux.org> 1:2.14.1.5-alt1
- new version.

* Fri Nov 09 2007 L.A. Kostis <lakostis@altlinux.ru> 2.14.4-alt2
- add IWL3945_UCODE_API tag for incompatibility with previous versions.

* Sun Nov 04 2007 L.A. Kostis <lakostis@altlinux.ru> 2.14.4-alt1
- initial build for Sisyphus.
- .spec based on firmware-ipw3945.

