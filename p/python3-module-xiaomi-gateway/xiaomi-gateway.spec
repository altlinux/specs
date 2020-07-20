Name: python3-module-xiaomi-gateway
Version: 0.13.0
Release: alt1

Summary: Python library to communicate with the Xiaomi Gateway
License: BSD
Group: Development/Python
Url: https://pypi.org/project/PyXiaomiGateway/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/xiaomi_gateway
%python3_sitelibdir/PyXiaomiGateway-%version-*-info

%changelog
* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.0-alt1
- initial
