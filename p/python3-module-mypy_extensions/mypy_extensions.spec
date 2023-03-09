%define _unpackaged_files_terminate_build 1

%define pypi_name mypy-extensions
%define mod_name mypy_extensions
%def_with check

Name: python3-module-%mod_name
Version: 1.0.0
Release: alt1
Summary: Type system extensions for programs checked with the mypy type checker
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mypy-extensions/
VCS: https://github.com/python/mypy_extensions
BuildArch: noarch
Source: %name-%version.tar
# well-known PyPI names
Provides: python3-module-%pypi_name = %EVR
%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
The %pypi_name module defines extensions to the standard "typing" module
that are supported by the mypy type checker and the mypyc compiler.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover tests

%files
%doc README.md
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 07 2023 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- 0.4.3 -> 1.0.0.

* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1
- 0.4.1 -> 0.4.3.

* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
