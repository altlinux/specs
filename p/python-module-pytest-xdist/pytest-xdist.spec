%define oname pytest-xdist

%def_with python3

Name: python-module-%oname
Version: 1.11
Release: alt1.hg20140924.1
Summary: py.test xdist plugin for distributed testing and loop-on-failing modes
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-xdist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/hpk42/pytest-xdist
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides xdist

%description
The pytest-xdist plugin extends py.test with some unique test execution
modes:

* test run parallelization: if you have multiple CPUs or hosts you can
  use those for a combined test run. This allows to speed up development
  or to use special resources of remote machines.
* --boxed: (not available on Windows) run each test in a boxed
  subprocess to survive SEGFAULTS or otherwise dying processes
* --looponfail: run your tests repeatedly in a subprocess. After each
  run py.test waits until a file in your project changes and then
  re-runs the previously failing tests. This is repeated until all tests
  pass after which again a full run is performed.
* Multi-Platform coverage: you can specify different Python interpreters
  or different platforms and run tests in parallel on all of them.

%package -n python3-module-%oname
Summary: py.test xdist plugin for distributed testing and loop-on-failing modes
Group: Development/Python3
%py3_provides xdist

%description -n python3-module-%oname
The pytest-xdist plugin extends py.test with some unique test execution
modes:

* test run parallelization: if you have multiple CPUs or hosts you can
  use those for a combined test run. This allows to speed up development
  or to use special resources of remote machines.
* --boxed: (not available on Windows) run each test in a boxed
  subprocess to survive SEGFAULTS or otherwise dying processes
* --looponfail: run your tests repeatedly in a subprocess. After each
  run py.test waits until a file in your project changes and then
  re-runs the previously failing tests. This is repeated until all tests
  pass after which again a full run is performed.
* Multi-Platform coverage: you can specify different Python interpreters
  or different platforms and run tests in parallel on all of them.

%prep
%setup

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

%files
%doc CHANGELOG *.txt example
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.txt example
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11-alt1.hg20140924.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.hg20140924
- Initial build for Sisyphus

