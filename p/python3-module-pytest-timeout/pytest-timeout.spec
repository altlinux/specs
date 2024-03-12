%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-timeout

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.1
Release: alt1
Summary: pytest plugin which will terminate tests after a certain timeout
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-timeout/
Vcs: https://github.com/pytest-dev/pytest-timeout
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /dev/pts
%pyproject_builddeps_metadata
# not packaged yet
%add_pyproject_deps_check_filter pytest-github-actions-annotate-failures
%pyproject_builddeps_check
%endif

%description
This is a plugin which will terminate tests after a certain timeout.
When doing so it will show a stack dump of all threads running at the
time. This is useful when running tests under a continuous integration
server or simply if you don't know why the test suite hangs.

Note that while by default on POSIX systems py.test will continue to
execute the tests after a test has timed, out this is not always
possible. Often the only sure way to interrupt a hanging test is by
terminating the entire process. As this is a hard termination
(os._exit()) it will result in no teardown, JUnit XML output etc. But
the plugin will ensure you will have the debugging output on stderr
nevertheless, which is the most important part at this stage.

%prep
%setup
%autopatch -p1
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
%pyproject_run_pytest -ra

%files
%doc README.rst failure_demo.py
%python3_sitelibdir/pytest_timeout.py
%python3_sitelibdir/__pycache__/pytest_timeout.*.py*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Mar 11 2024 Stanislav Levin <slev@altlinux.org> 2.3.1-alt1
- 2.2.0 -> 2.3.1.

* Thu Feb 29 2024 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.0 -> 2.2.0.

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 1.3.3 -> 2.1.0.

* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 1.3.3-alt4
- Stopped Python2 package build.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 1.3.3-alt3
- Fixed testing against Pytest 5.

* Fri May 31 2019 Stanislav Levin <slev@altlinux.org> 1.3.3-alt2
- Fixed Pytest4.x compatibility errors.

* Thu Dec 27 2018 Stanislav Levin <slev@altlinux.org> 1.3.3-alt1
- 1.3.2 -> 1.3.3.

* Fri Nov 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1
- 1.2.0 -> 1.3.2.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.1
- NMU: Use buildreq for BR.

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

