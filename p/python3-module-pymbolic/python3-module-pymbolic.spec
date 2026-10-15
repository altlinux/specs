%define pypi_name pymbolic

Name: python3-module-%pypi_name
Version: 2025.1
Release: alt1

Summary: A package for symbolic computation
License: MIT
Group: Development/Python3
Url: https://github.com/inducer/pymbolic

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_disabled check
%else
BuildRequires: python3-module-pytest
BuildRequires: python3-module-constantdict
BuildRequires: python3-module-pytools
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-numpy
BuildRequires: python3-module-sympy
%endif

# optional interop backends, imported only when used
%add_python3_req_skip matchpy multiset symengine sympy

%description
Pymbolic is a small expression tree and symbolic manipulation library.
It provides a mapper-based framework for traversing and transforming
expression trees, a parser, code generators and interoperability with
SymPy, SymEngine and Maxima.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# matchpy is not packaged
%pyproject_run_pytest -v test --ignore=test/test_matchpy.py

%files
%doc README.rst LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 2025.1-alt1
- initial build for Sisyphus
