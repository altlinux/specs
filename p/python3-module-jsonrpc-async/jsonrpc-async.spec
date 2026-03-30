%def_with check

Name: python3-module-jsonrpc-async
Version: 2.1.3
Release: alt1.1

Summary: JSON-RPC client implementation for asyncio python code
License: BSD
Group: Development/Python
Url: https://pypi.org/project/jsonrpc-async
VCS: http://github.com/emlove/jsonrpc-async

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest-aiohttp
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-aiohttp-tests
BuildRequires: python3-module-jsonrpc-base
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
%pyproject_run_pytest -o addopts= tests.py

%files
%doc LICENSE.* README.*
%python3_sitelibdir/jsonrpc_async
%python3_sitelibdir/jsonrpc_async-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.1.3-alt1.1
- Demodernized packaging.

* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.3-alt1
- 2.1.3 released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.2-alt1
- 2.1.2 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Tue Apr 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt1
- initial
