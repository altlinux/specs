%define _unpackaged_files_terminate_build 1
%define oname pytest-timeout

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.2.0
Release: alt1
Summary: py.test plugin to abort hanging tests
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-timeout
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/cc/b7/b2a61365ea6b6d2e8881360ae7ed8dad0327ad2df89f2f0be4a02304deb2/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides pytest_timeout

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

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

%if_with python3
%package -n python3-module-%oname
Summary: py.test plugin to abort hanging tests
Group: Development/Python3
%py3_provides pytest_timeout

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
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test -v
export PYTHONPATH=%buildroot%python_sitelibdir
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version -vv
popd
%endif

%files
%doc README failure_demo.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README failure_demo.py
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.1
- NMU: Use buildreq for BR.

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

