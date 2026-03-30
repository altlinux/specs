Name: python3-module-wsdiscovery
Version: 2.1.2
Release: alt1.1

Provides: python3-module-ws-discovery = %EVR
Obsoletes: python3-module-ws-discovery

Summary: WS-Discovery implementation for Python
License: LGPLv3
Group: Development/Python
Url: https://pypi.org/project/WSDiscovery
VCS: https://github.com/andreikop/python-ws-discovery

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
%_bindir/wsdiscover
%_bindir/wspublish
%python3_sitelibdir/wsdiscovery
%python3_sitelibdir/wsdiscovery-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.1.2-alt1.1
- Demodernized packaging.

* Thu Oct 23 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.2-alt1
- 2.1.2 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- initial
