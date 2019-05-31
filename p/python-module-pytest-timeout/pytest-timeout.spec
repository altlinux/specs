%define _unpackaged_files_terminate_build 1
%define oname pytest-timeout

%def_with check

Name: python-module-%oname
Version: 1.3.3
Release: alt2
Summary: pytest plugin which will terminate tests after a certain timeout
License: MIT
Group: Development/Python
# Source: https://bitbucket.org/pytest-dev/pytest-timeout
Url: https://pypi.org/project/pytest-timeout/

Source: %name-%version.tar.gz
Patch: pytest-timeout-1.3.3-Change-tests-to-use-pytest-param.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: /dev/pts
BuildRequires: python-module-tox
BuildRequires: python-module-pytest
BuildRequires: python-module-pexpect
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

%package -n python3-module-%oname
Summary: pytest plugin which will terminate tests after a certain timeout
Group: Development/Python3

%description -n python3-module-%oname
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

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    cp %_bindir\/py.test3 \{envbindir\}\/py.test\
    sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc README failure_demo.py
%python_sitelibdir/pytest_timeout.py*
%python_sitelibdir/pytest_timeout-*.egg-info/

%files -n python3-module-%oname
%doc README failure_demo.py
%python3_sitelibdir/pytest_timeout.py
%python3_sitelibdir/__pycache__/pytest_timeout.*.py*
%python3_sitelibdir/pytest_timeout-*.egg-info/

%changelog
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

