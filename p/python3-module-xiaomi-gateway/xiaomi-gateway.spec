Name: python3-module-xiaomi-gateway
Version: 0.14.3
Release: alt2.1

Provides: python3-module-pyxiaomigateway = %EVR

Summary: Python library to communicate with the Xiaomi Gateway
License: BSD
Group: Development/Python
Url: https://pypi.org/project/PyXiaomiGateway
VCS: https://github.com/Danielhiversen/PyXiaomiGateway

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/xiaomi_gateway
%python3_sitelibdir/pyxiaomigateway-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.14.3-alt2.1
- Demodernized packaging.

* Thu Oct 23 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.14.3-alt2
- provide pyxiaomigateway

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 0.14.3-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Thu Nov 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.3-alt1
- 0.14.3 released

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.4-alt1
- 0.13.4 released

* Fri Oct 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.3-alt1
- 0.13.3 released

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.2-alt1
- 0.13.2 released

* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.0-alt1
- initial
