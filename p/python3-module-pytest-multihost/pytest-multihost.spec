%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-multihost
%define mod_name pytest_multihost

%def_with check

Name: python3-module-%pypi_name
Version: 3.4
Release: alt2
Summary: Utility for writing multi-host tests for pytest
License: GPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-multihost
Vcs: https://pagure.io/python-pytest-multihost
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
%py3_provides %pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A pytest plugin for multi-host testing.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra test_pytestmultihost/ -m 'not needs_ssh'

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jan 26 2024 Stanislav Levin <slev@altlinux.org> 3.4-alt2
- Fixed FTBFS (Python 3.12).

* Mon Mar 29 2021 Stanislav Levin <slev@altlinux.org> 3.4-alt1
- 3.0 -> 3.4.

* Fri Dec 06 2019 Stanislav Levin <slev@altlinux.org> 3.0-alt2
- Dropped Python2 subpackage.

* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1
- 1.1 -> 3.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20141209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20141209.1
- NMU: Use buildreq for BR.

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141209
- Version 0.4

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20141126
- Initial build for Sisyphus

