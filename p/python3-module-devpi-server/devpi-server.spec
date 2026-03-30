%define _unpackaged_files_terminate_build 1
%define pypi_name devpi-server
%define mod_name devpi_server

%def_with check

Name: python3-module-%pypi_name
Version: 6.19.2
Release: alt1.1
Summary: Reliable private and pypi.org caching server
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/devpi-server
Vcs: https://github.com/devpi/devpi
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
Requires: python3-modules-sqlite3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-execnet
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-instafail
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-webtest

BuildRequires: python3-module-argon2-cffi
BuildRequires: python3-module-attrs
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-devpi-common
BuildRequires: python3-module-httpx
BuildRequires: python3-module-itsdangerous
BuildRequires: python3-module-lazy
BuildRequires: python3-module-passlib
BuildRequires: python3-module-platformdirs
BuildRequires: python3-module-pluggy
BuildRequires: python3-module-py
BuildRequires: python3-module-pyramid
BuildRequires: python3-module-repoze-lru
BuildRequires: python3-module-requests
BuildRequires: python3-module-ruamel-yaml
BuildRequires: python3-module-strictyaml
BuildRequires: python3-module-waitress
BuildRequires: python3-modules-sqlite3
%endif

%add_python3_req_skip requests.packages.urllib3.response

%description
Server for private package indexes and PyPI caching.

%prep
%setup
%autopatch -p1
cd server

%build
cd server
%pyproject_build

%install
cd server
%pyproject_install

# tests are packaged on purpose because they are required by other devpi
# packages. Don't want to bother with splitting entry points. Tests don't
# have third party dependencies (don't enable autoreq for python)

%check
cd server
%pyproject_run_pytest -ra

%files
%_bindir/devpi-*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/pytest_devpi_server/
%python3_sitelibdir/test_devpi_server/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 6.19.2-alt1.1
- Demodernized packaging.

* Wed Mar 18 2026 Stanislav Levin <slev@altlinux.org> 6.19.2-alt1
- 6.19.1 -> 6.19.2.

* Tue Feb 10 2026 Stanislav Levin <slev@altlinux.org> 6.19.1-alt1
- 6.19.0 -> 6.19.1.

* Mon Feb 09 2026 Stanislav Levin <slev@altlinux.org> 6.19.0-alt1
- 6.17.0 -> 6.19.0.

* Tue Sep 02 2025 Stanislav Levin <slev@altlinux.org> 6.17.0-alt1
- 6.16.0 -> 6.17.0.

* Thu Jun 26 2025 Stanislav Levin <slev@altlinux.org> 6.16.0-alt1
- 6.15.0 -> 6.16.0.

* Mon May 19 2025 Stanislav Levin <slev@altlinux.org> 6.15.0-alt1
- 6.14.0 -> 6.15.0.

* Sat Dec 28 2024 Stanislav Levin <slev@altlinux.org> 6.14.0-alt1
- Initial build for Sisyphus.
