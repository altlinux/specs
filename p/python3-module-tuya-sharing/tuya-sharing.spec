Name: python3-module-tuya-sharing
Version: 0.2.0
Release: alt1

Summary: Tuya Device Sharing SDK
License: MIT
Group: Development/Python
Url: https://github.com/tuya/tuya-device-sharing-sdk

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(requests)
BuildRequires: python3(cryptography)
BuildRequires: python3(paho)

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
* Tue Mar 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- 0.2.0 released

