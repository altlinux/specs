%define _unpackaged_files_terminate_build 1
%define pypi_name boolean.py

%def_with check

Name: python3-module-%pypi_name
Version: 5.0
Release: alt1.2
Summary: Define boolean algebras, create and parse boolean expressions and create custom boolean DSL
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/boolean.py
VCS: https://github.com/bastikr/boolean.py.git
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-tox
%endif

%description
This library helps you deal with boolean expressions and algebra with variables
and the boolean functions AND, OR, NOT.

You can parse expressions from strings and simplify and compare expressions. You
can also easily create your custom algreba and mini DSL and create custom
tokenizers to handle custom expressions.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# don't ship tests
rm %buildroot%python3_sitelibdir/boolean/test_boolean.py

%check
%pyproject_run_pytest -ra boolean

%files
%doc README.rst
%python3_sitelibdir/boolean/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 5.0-alt1.2
- Demodernized packaging.

* Fri Apr 18 2025 Stanislav Levin <slev@altlinux.org> 5.0-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Fri Apr 04 2025 Stanislav Levin <slev@altlinux.org> 5.0-alt1
- 4.0 -> 5.0.

* Wed Mar 20 2024 Stanislav Levin <slev@altlinux.org> 4.0-alt2
- Mapped PyPI name to distro's one.

* Wed Oct 05 2022 Stanislav Levin <slev@altlinux.org> 4.0-alt1
- Initial build for Sisyphus.
