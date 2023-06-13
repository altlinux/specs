%define _unpackaged_files_terminate_build 1
%define pypi_name big-O
%define mod_name big_o

%def_with check

Name: python3-module-%pypi_name
Version: 0.11.0
Release: alt1
Summary: Empirical estimation of time complexity from execution time
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/big-O
VCS: https://github.com/pberkes/big_O.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
# tests deps are installed directly by pip
BuildRequires: python3-module-pytest
# tests are packaged separately
BuildRequires: python3-module-numpy-testing
%endif

%description
%pypi_name is a Python module to estimate the time complexity of Python code
from its execution time. It can be used to analyze how functions scale with
inputs of increasing size.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore big_o/test

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/big_O-%version.dist-info/
%exclude %python3_sitelibdir/%mod_name/test/

%changelog
* Fri Jun 09 2023 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1
- 0.10.2 -> 0.11.0.

* Mon Feb 27 2023 Stanislav Levin <slev@altlinux.org> 0.10.2-alt1
- Initial build for Sisyphus.
