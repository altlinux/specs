Name: python3-module-xbee-helper
Version: 0.0.7
Release: alt1.1

Summary: XBee serial communication API helpers
License: BSD
Group: Development/Python
Url: https://pypi.org/project/xbee-helper/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup
sed -i '/pytest-runner/d' setup.py

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE* README.*
%python3_sitelibdir/xbee_helper
%python3_sitelibdir/xbee_helper-%version-*-info

%changelog
* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 0.0.7-alt1.1
- NMU: updated build dependencies

* Fri Jan 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.7-alt1
- initial
