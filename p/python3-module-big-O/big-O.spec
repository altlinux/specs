%define _unpackaged_files_terminate_build 1
%define pypi_name big-O
%define mod_name big_o

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.2
Release: alt1
Summary: Empirical estimation of time complexity from execution time
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/big-O
VCS: https://github.com/pberkes/big_O.git
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

# PyPI wellknown name
%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(numpy)
BuildRequires: python3(numpy.testing)
%endif

%description
%pypi_name is a Python module to estimate the time complexity of Python code
from its execution time. It can be used to analyze how functions scale with
inputs of increasing size.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/big_O-%version.dist-info/
%exclude %python3_sitelibdir/%mod_name/test/

%changelog
* Mon Feb 27 2023 Stanislav Levin <slev@altlinux.org> 0.10.2-alt1
- Initial build for Sisyphus.
