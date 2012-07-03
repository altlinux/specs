%define firmware_name iwl6050
%define realname iwlwifi-6050

Name: firmware-%firmware_name
Version: 41.28.5.1
Release: alt1
Packager: Evgeny Sinelnikov <sin@altlinux.ru>
License: Redistributive
Group: System/Kernel and hardware
Summary: firmware for Intel Wireless WiFi Link 6050AGN Network Connection Adapter
Source: http://intellinuxwireless.org/iwlwifi/downloads/%realname-ucode-%version.tar.bz2
Source1: iwlwifi-6050-4.ucode
Url: http://intellinuxwireless.org/
BuildArch: noarch

%description
The file iwlwifi-6050-*.ucode provided in this package must be present on your
system in order for the Intel Wireless WiFi Link 6050AGN driver for Linux
(iwlwifi-6050) to operate on your system.

%prep
%setup -q -n %realname-ucode-%version

%install
install -d $RPM_BUILD_ROOT/lib/firmware
install -p *.ucode $RPM_BUILD_ROOT/lib/firmware/
install -p %SOURCE1 $RPM_BUILD_ROOT/lib/firmware/
cp -df LICENSE.%realname-ucode $RPM_BUILD_ROOT/lib/firmware/%realname-LICENSE

%files
%defattr(644,root,root,755)
%doc README.%realname-ucode
/lib/firmware/%realname-LICENSE
/lib/firmware/*.ucode

%changelog
* Mon Jan 10 2011 Alexey I. Froloff <raorn@altlinux.org> 41.28.5.1-alt1
- Version 41.28.5.1.
- Packaged API v4 firmware

* Sun Jul 25 2010 Evgeny Sinelnikov <sin@altlinux.ru> 9.201.4.1-alt1
- Version 9.201.4.1.
- Initial build for Sisyphus.
