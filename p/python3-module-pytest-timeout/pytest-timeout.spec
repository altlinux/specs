%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-timeout

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1
Summary: pytest plugin which will terminate tests after a certain timeout
License: MIT
Group: Development/Python3
# Source: https://github.com/pytest-dev/pytest-timeout
Url: https://pypi.org/project/pytest-timeout/

Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: /dev/pts
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pexpect
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

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject -- -vra

%files
%doc README.rst failure_demo.py
%python3_sitelibdir/pytest_timeout.py
%python3_sitelibdir/__pycache__/pytest_timeout.*.py*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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

