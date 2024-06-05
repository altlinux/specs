%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-bdd

%def_with check

Name: python3-module-%pypi_name
Version: 7.2.0
Release: alt1

Summary: BDD library for the py.test runner
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-bdd/
Vcs: https://github.com/pytest-dev/pytest-bdd.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
pytest-bdd implements a subset of Gherkin language for the automation of
the project requirements testing and easier behavioral driven
development.

Unlike many other BDD tools it doesn't require a separate runner and
benefits from the power and flexibility of the pytest. It allows to
unify your unit and functional tests, easier continuous integration
server configuration and maximal reuse of the tests setup.

Pytest fixtures written for the unit tests can be reused for the setup
and actions mentioned in the feature steps with dependency injection,
which allows a true BDD just-enough specification of the requirements
without maintaining any context object containing the side effects of
the Gherkin imperative declarations.

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
%pyproject_run_pytest -ra

%files
%doc CHANGES.rst README.rst
%_bindir/pytest-bdd
%python3_sitelibdir/pytest_bdd/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jun 05 2024 Stanislav Levin <slev@altlinux.org> 7.2.0-alt1
- 7.1.2 -> 7.2.0.

* Mon Mar 18 2024 Stanislav Levin <slev@altlinux.org> 7.1.2-alt1
- 7.1.1 -> 7.1.2.

* Tue Mar 05 2024 Stanislav Levin <slev@altlinux.org> 7.1.1-alt1
- 6.0.1 -> 7.1.1.

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 6.0.1-alt1
- 4.1.0 -> 6.0.1.

* Mon Oct 11 2021 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1
- 4.0.2 -> 4.1.0.

* Sun Apr 18 2021 Stanislav Levin <slev@altlinux.org> 4.0.2-alt1
- 4.0.1 -> 4.0.2.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 4.0.1-alt1
- 3.2.1 -> 4.0.1.

* Mon Mar 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.2.1-alt1
- Version updated to 3.2.1

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.1.1-alt2
- disable python2

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1
- 3.1.0 -> 3.1.1.
- Fixed testing against Pytest 5.

* Tue Mar 26 2019 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 3.0.0 -> 3.1.0.

* Mon Dec 24 2018 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.19.0 -> 3.0.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.19.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.19.0-alt1
- Updated to upstream version 2.19.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.14.1-alt1.git20150713.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.1-alt1.git20150713
- Version 2.14.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.3-alt1.git20141229
- Version 2.5.3

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20141119
- Version 2.5.1

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.git20141110
- Initial build for Sisyphus

