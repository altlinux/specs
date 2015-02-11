%define oname doubles

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0.5
Release: alt1.git20150205
Summary: Test doubles for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/doubles/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/uber/doubles.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-coverage python-module-coveralls
BuildPreReq: python-module-flake8 python-module-pyroma
BuildPreReq: python-module-nose
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coverage python3-module-coveralls
BuildPreReq: python3-module-flake8 python3-module-pyroma
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
Doubles is a Python package that provides test doubles for use in
automated tests.

It provides functionality for stubbing, mocking, and verification of
test doubles against the real objects they double. In contrast to the
Mock package, it provides a clear, expressive syntax and better safety
guarantees to prevent API drift and to improve confidence in tests using
doubles. It comes with drop-in support for test suites run by Pytest,
Nose, or standard unittest.

%package -n python3-module-%oname
Summary: Test doubles for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Doubles is a Python package that provides test doubles for use in
automated tests.

It provides functionality for stubbing, mocking, and verification of
test doubles against the real objects they double. In contrast to the
Mock package, it provides a clear, expressive syntax and better safety
guarantees to prevent API drift and to improve confidence in tests using
doubles. It comes with drop-in support for test suites run by Pytest,
Nose, or standard unittest.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Doubles is a Python package that provides test doubles for use in
automated tests.

It provides functionality for stubbing, mocking, and verification of
test doubles against the real objects they double. In contrast to the
Mock package, it provides a clear, expressive syntax and better safety
guarantees to prevent API drift and to improve confidence in tests using
doubles. It comes with drop-in support for test suites run by Pytest,
Nose, or standard unittest.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Doubles is a Python package that provides test doubles for use in
automated tests.

It provides functionality for stubbing, mocking, and verification of
test doubles against the real objects they double. In contrast to the
Mock package, it provides a clear, expressive syntax and better safety
guarantees to prevent API drift and to improve confidence in tests using
doubles. It comes with drop-in support for test suites run by Pytest,
Nose, or standard unittest.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.git20150205
- Initial build for Sisyphus

