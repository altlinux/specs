%define firmware_name iwl6000
%define realname iwlwifi-6000

Name: firmware-%firmware_name
Version: 9.221.4.1
Release: alt1
Packager: Evgeny Sinelnikov <sin@altlinux.ru>
License: Redistributive
Group: System/Kernel and hardware
Summary: firmware for Intel 6000 Series Wi-Fi Adapters (6200AGN and 6300AGN)
Source: http://intellinuxwireless.org/iwlwifi/downloads/%realname-ucode-%version.tar.bz2
Url: http://intellinuxwireless.org/
BuildArch: noarch

%description
The file iwlwifi-6000-*.ucode provided in this package must be present on your
system in order for the Intel 6000 Series Wi-Fi Adapters (6200AGN and 6300AGN) driver for Linux
(iwlwifi-6000) to operate on your system.

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
* Sun Jul 25 2010 Evgeny Sinelnikov <sin@altlinux.ru> 9.221.4.1-alt1
- Version 9.221.4.1.
- Initial build for Sisyphus.
