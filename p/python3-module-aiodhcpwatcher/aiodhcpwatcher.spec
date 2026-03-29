%def_with check

Name: python3-module-aiodhcpwatcher
Version: 1.2.1
Release: alt1.1

Summary: Watch for DHCP packets with asyncio
License: GPLv3
Group: Development/Python
Url: https://pypi.org/project/aiodhcpwatcher/
VCS: https://github.com/bdraco/aiodhcpwatcher

Source0: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-scapy
%endif

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o=addopts= tests

%files
%python3_sitelibdir/aiodhcpwatcher
%python3_sitelibdir/aiodhcpwatcher-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1.1
- Demodernized packaging.

* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.1-alt1
- 1.2.1 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.2-alt1
- 1.0.2 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.0-alt1
- 1.0.0 released

* Fri Mar 15 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt1
- 0.8.1 released

* Tue Mar 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.0-alt1
- 0.8.0 released
