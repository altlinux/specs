%def_with check

Name: python3-module-aiozoneinfo
Version: 0.2.3
Release: alt1.1

Summary: Tools to fetch zoneinfo with asyncio
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/aiozoneinfo
VCS: https://github.com/bluetooth-devices/aiozoneinfo

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-pytest-asyncio
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
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/aiozoneinfo
%python3_sitelibdir/aiozoneinfo-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.2.3-alt1.1
- Demodernized packaging.

* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.3-alt1
- 0.2.3 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt1
- 0.2.1 released
