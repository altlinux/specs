Name: python3-module-tuya-iot
Version: 0.6.6
Release: alt1

Summary: A Python Tuya Open API
License: MIT
Group: Development/Python3
Url: https://github.com/tuya/tuya-iot-python-sdk

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools
BuildRequires: python3(requests) python3(Crypto) python3(paho)

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/tuya_iot
%python3_sitelibdir/tuya_iot_py_sdk-%version-*-info

%changelog
* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.6-alt1
- 0.6.6 released
