%define _unpackaged_files_terminate_build 1
%define pypi_name a2wsgi
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.10.10
Release: alt1.1
Summary: Convert WSGI app from/to ASGI app
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/a2wsgi/
Vcs: https://github.com/abersheeran/a2wsgi
BuildArch: noarch
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pdm-backend

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-httpx
BuildRequires: python3-module-starlette
%endif

%description
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.10.10-alt1.1
- Demodernized packaging.

* Fri Jul 04 2025 Stanislav Levin <slev@altlinux.org> 1.10.10-alt1
- 1.10.7 -> 1.10.10.

* Tue Oct 01 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.10.7-alt1
- 1.10.7 released

* Tue May 07 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.10.4-alt1
- 1.10.4 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt1
- 1.7.0 released
