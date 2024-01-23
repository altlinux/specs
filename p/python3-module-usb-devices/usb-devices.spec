Name: python3-module-usb-devices
Version: 0.4.5
Release: alt1

Summary: Bluetooth USB adapters
License: MIT
Group: Development/Python
Url: https://pypi.org/project/usb-devices/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/usb_devices
%python3_sitelibdir/usb_devices-%version.dist-info

%changelog
* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.5-alt1
- 0.4.5 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released
