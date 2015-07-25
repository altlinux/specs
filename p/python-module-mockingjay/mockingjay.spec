%define oname mockingjay

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150528
Summary: A simple library to build mock http services based on HTTPretty
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/mockingjay
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kevinjqiu/mockingjay.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-wheel python-module-httpretty
BuildPreReq: python-module-jinja2 python-module-requests
BuildPreReq: python-module-debug python-module-pytest-cov
BuildPreReq: python-module-coveralls
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-wheel python3-module-httpretty
BuildPreReq: python3-module-jinja2 python3-module-requests
BuildPreReq: python3-module-debug python3-module-pytest-cov
BuildPreReq: python3-module-coveralls python3-module-docopt
%endif

%py_provides %oname
%py_requires wheel httpretty jinja2

%description
A simple library to build mock http services based on HTTPretty.

Features:
* Provides a fluent interface for building service mocks using HTTPretty
* Allows mocking of response body using templated fixtures
* Automatic assertion of request attributes (headers, body, etc)

%if_with python3
%package -n python3-module-%oname
Summary: A simple library to build mock http services based on HTTPretty
Group: Development/Python3
%py3_provides %oname
%py3_requires wheel httpretty jinja2

%description -n python3-module-%oname
A simple library to build mock http services based on HTTPretty.

Features:
* Provides a fluent interface for building service mocks using HTTPretty
* Allows mocking of response body using templated fixtures
* Automatic assertion of request attributes (headers, body, etc)
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A simple library to build mock http services based on HTTPretty.

Features:
* Provides a fluent interface for building service mocks using HTTPretty
* Allows mocking of response body using templated fixtures
* Automatic assertion of request attributes (headers, body, etc)

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A simple library to build mock http services based on HTTPretty.

Features:
* Provides a fluent interface for building service mocks using HTTPretty
* Allows mocking of response body using templated fixtures
* Automatic assertion of request attributes (headers, body, etc)

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make docs
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
py.test -vv -s tests/
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150528
- Initial build for Sisyphus

