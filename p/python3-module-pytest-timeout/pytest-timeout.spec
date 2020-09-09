%define _unpackaged_files_terminate_build 1
%define oname pytest-timeout

%def_with check

Name: python3-module-%oname
Version: 1.3.3
Release: alt4
Summary: pytest plugin which will terminate tests after a certain timeout
License: MIT
Group: Development/Python3
# Source: https://bitbucket.org/pytest-dev/pytest-timeout
Url: https://pypi.org/project/pytest-timeout/

Source: %name-%version.tar.gz
Patch: pytest-timeout-1.3.3-Change-tests-to-use-pytest-param.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: /dev/pts
BuildRequires: python3-module-tox
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
%patch -p1

%build
%python3_build

%install
%python3_install

%check
sed -i '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/py.test\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -vvr

%files
%doc README failure_demo.py
%python3_sitelibdir/pytest_timeout.py
%python3_sitelibdir/__pycache__/pytest_timeout.*.py*
%python3_sitelibdir/pytest_timeout-*.egg-info/

%changelog
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

