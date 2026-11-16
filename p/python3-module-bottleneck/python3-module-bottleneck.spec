%define _unpackaged_files_terminate_build 1
%define pypi_name bottleneck
%def_with check

Name: python3-module-bottleneck
Version: 1.6.1
Release: alt1
Summary: Fast NumPy array functions written in C
License: BSD-2-Clause AND BSD-3-Clause AND MIT
Group: Development/Python3
Url: https://github.com/pydata/bottleneck
Vcs: https://github.com/pydata/bottleneck
Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev >= 3.11
BuildRequires: python3-module-setuptools >= 77.0.1
BuildRequires: python3-module-versioneer >= 0.29
# The devel package requires the matching NumPy runtime.
BuildRequires: libnumpy-py3-devel >= 1:2.0
BuildRequires: libnumpy-py3-devel < 1:2.8
%if_with check
BuildRequires: python3-module-pytest >= 9.0
%endif

%description
Bottleneck is a collection of fast NumPy array functions written in C.
It provides accelerated reductions, moving window functions, ranking,
partitioning and other operations, including NaN-aware variants.

%package tests
Summary: Tests for Bottleneck
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-module-pytest >= 9.0

%description tests
Upstream tests and test data for Bottleneck, used by bottleneck.test().

%prep
%setup -q -n %pypi_name-%version
# Stored gear tags do not populate Versioneer's archive decorations.
sed -i 's/^    git_refnames = .*/    git_refnames = "tag: v%version"/' bottleneck/_version.py

%build
%pyproject_build

%install
%pyproject_install

%check
%if_with check
# Test the installed wheel without importing the source package.
export PYTHONSAFEPATH=1
%pyproject_run_pytest -vra --import-mode=importlib --pyargs %pypi_name.tests
%endif

%files
%doc README.rst RELEASE.rst
%dir %python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name/*.py
%python3_sitelibdir/%pypi_name/*.so
%python3_sitelibdir/%pypi_name/__pycache__/
%python3_sitelibdir/%pypi_name/benchmark/
%python3_sitelibdir/%pypi_name/slow/
%dir %python3_sitelibdir/%pypi_name/tests
%python3_sitelibdir/%pypi_name/tests/__init__.py
%python3_sitelibdir/%pypi_name/tests/util.py
%dir %python3_sitelibdir/%pypi_name/tests/__pycache__
%python3_sitelibdir/%pypi_name/tests/__pycache__/__init__.*
%python3_sitelibdir/%pypi_name/tests/__pycache__/util.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files tests
%python3_sitelibdir/%pypi_name/src/
%python3_sitelibdir/%pypi_name/tests/*.py
%python3_sitelibdir/%pypi_name/tests/__pycache__/*.pyc
%exclude %python3_sitelibdir/%pypi_name/tests/__init__.py
%exclude %python3_sitelibdir/%pypi_name/tests/util.py
%exclude %python3_sitelibdir/%pypi_name/tests/__pycache__/__init__.*
%exclude %python3_sitelibdir/%pypi_name/tests/__pycache__/util.*
%python3_sitelibdir/%pypi_name/tests/data/

%changelog
* Fri Nov 13 2026 Vladislav Tatjanin <l27001@altlinux.org> 1.6.1-alt1
- Initial build.
