%define firmware_name iwl1000
%define realname iwlwifi-1000

Name: firmware-%firmware_name
Version: 128.50.3.1
Release: alt1
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
License: Redistributive
Group: System/Kernel and hardware
Summary: firmware for Intel Wireless WiFi Link 1000BGN Network Connection Adapter
Source: http://intellinuxwireless.org/iwlwifi/downloads/%realname-ucode-%version.tar
Url: http://intellinuxwireless.org/
BuildArch: noarch

%description
The file iwlwifi-1000-*.ucode provided in this package must be present
on your system in order for the Intel Wireless WiFi Link 1000BGN driver
for Linux (iwlwifi-1000) to operate on your system.

%prep
%setup -n %realname-ucode-%version

%install
install -d %buildroot/lib/firmware
install -p -m644 *.ucode %buildroot/lib/firmware/
install -p -m644 LICENSE* %buildroot/lib/firmware/%realname-LICENSE

%files
%doc README*
/lib/firmware/%realname-LICENSE
/lib/firmware/*.ucode

%changelog
* Thu Jan 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 128.50.3.1-alt1
- Initial build for Sisyphus

