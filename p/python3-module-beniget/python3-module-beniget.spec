%define _unpackaged_files_terminate_build 1

%define pypi_name beniget
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.0
Release: alt1.1
Summary: Extract semantic information about static Python code
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/beniget/
Vcs: https://github.com/serge-sans-paille/beniget/
BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-gast
%endif

%description
Beniget provides a static over-approximation of the global and local definitions
inside Python Module/Class/Function. It can also compute def-use chains from
each definition.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# synced to .github/workflows/core.yml
%pyproject_run_pytest -vra --doctest-modules %mod_name/ tests/

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1.1
- Demodernized packaging.

* Wed Dec 03 2025 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.2.post1 -> 0.5.0.

* Fri Jun 28 2024 Stanislav Levin <slev@altlinux.org> 0.4.2.post1-alt1
- 0.4.1 -> 0.4.2.post1.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1.1
- NMU: added missing build dependency on setuptools.

* Sun Dec 04 2022 Anton Farygin <rider@altlinux.ru> 0.4.1-alt1
- first build for Sisyphus
