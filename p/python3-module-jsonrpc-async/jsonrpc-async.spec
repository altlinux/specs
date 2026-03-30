Name: python3-module-jsonrpc-async
Version: 2.1.3
Release: alt2

Summary: JSON-RPC client implementation for asyncio python code
License: BSD
Group: Development/Python
URL: https://pypi.org/project/jsonrpc-async
VCS: http://github.com/emlove/jsonrpc-async

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements-test.txt

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
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.3-alt2
- revert unsolicited packaging changes

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
