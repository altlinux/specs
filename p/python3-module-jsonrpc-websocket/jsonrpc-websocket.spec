Name: python3-module-jsonrpc-websocket
Version: 3.2.1
Release: alt1

Summary: JSON-RPC websocket client library for asyncio
License: BSD
Group: Development/Python
URL: https://pypi.org/project/jsonrpc-websocket
VCS: https://github.com/emlove/jsonrpc-websocket

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
%python3_sitelibdir/jsonrpc_websocket
%python3_sitelibdir/jsonrpc_websocket-%version.dist-info

%changelog
* Tue Apr 28 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.1-alt1
- 3.2.1 released

* Thu Feb 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.0-alt1
- 3.2.0 released

* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.6-alt1
- 3.1.6 released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.5-alt1
- 3.1.5 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.4-alt1
- 3.1.4 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.2-alt1
- 3.1.2 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.0-alt1
- 3.1.0 released

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2.1 released

* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.2-alt1
- initial
