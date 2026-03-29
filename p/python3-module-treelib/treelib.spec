%define _unpackaged_files_terminate_build 1
%define pypi_name treelib
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.8.0
Release: alt1.1
Summary: A Python implementation of tree structure
License: %asl
Group: Development/Python
Url: https://pypi.org/project/treelib/
Vcs: https://github.com/caesar0301/treelib
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-autoflake
BuildRequires: python3-module-autopep8
BuildRequires: python3-module-black
BuildRequires: python3-module-flake8
BuildRequires: python3-module-isort
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov

BuildRequires: python3-module-six
%endif

%description
Tree implementation in python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# .github/workflows/python-package.yml
%pyproject_run_pytest -vra

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.8.0-alt1.1
- Demodernized packaging.

* Tue Jul 01 2025 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1
- 1.7.0 -> 1.8.0.

* Fri Oct 18 2024 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- 1.6.1 -> 1.7.0.

* Wed May 04 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus.
