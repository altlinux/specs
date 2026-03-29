Name: python3-module-tuya-sharing
Version: 0.2.9
Release: alt1.1

Summary: Tuya Device Sharing SDK
License: MIT
Group: Development/Python
URL: https://pypi.org/project/tuya-device-sharing-sdk
VCS: https://github.com/tuya/tuya-device-sharing-sdk

Provides: python3-module-tuya-device-sharing-sdk = %EVR

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-requests
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-paho

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/tuya_sharing
%python3_sitelibdir/tuya_device_sharing_sdk-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.2.9-alt1.1
- Demodernized packaging.

* Fri Feb 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.9-alt1
- 0.2.9 released

* Tue Mar 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- 0.2.0 released
