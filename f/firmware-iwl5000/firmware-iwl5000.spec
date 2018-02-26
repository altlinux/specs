%define firmware_name iwl5000
%define realname iwlwifi-5000

Name: firmware-%firmware_name
Version: 8.24.2.12
Release: alt1
Packager: L.A. Kostis <lakostis@altlinux.ru>
License: Redistributive
Group: System/Kernel and hardware
Summary: firmware for Intel Wireless WiFi Link 5000AGN Network Connection Adapter
Source0: http://intellinuxwireless.org/iwlwifi/downloads/%realname-ucode-%version.tar.bz2
Url: http://intellinuxwireless.org/
BuildArch: noarch

%description
The file iwlwifi-5000-*.ucode provided in this package must be present on your
system in order for the Intel Wireless WiFi Link 5000AGN driver for Linux
(iwlwifi-5000) to operate on your system.

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
* Sun Jun 28 2009 L.A. Kostis <lakostis@altlinux.ru> 8.24.2.12-alt1
- Updated to version 8.24.2.12.
- Leave v1 uCode for compatibility with older kernels.

* Tue Jul 15 2008 L.A. Kostis <lakostis@altlinux.ru> 5.4.A.11-alt1
- initial build for Sisyphus.

