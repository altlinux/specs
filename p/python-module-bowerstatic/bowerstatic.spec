%define oname bowerstatic

%def_with python3

Name: python-module-%oname
Version: 0.6
Release: alt1.dev0.git20141111
Summary: A Bower-centric static file server for WSGI
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/bowerstatic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/faassen/bowerstatic.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-webob python-module-pytest-cov
BuildPreReq: python-module-webtest
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-webob python3-module-pytest-cov
BuildPreReq: python3-module-webtest
%endif

%py_provides %oname

%description
BowerStatic is a WSGI-based framework that you can integrate with your
WSGI-using web application or framework to help it serve static
resources.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
BowerStatic is a WSGI-based framework that you can integrate with your
WSGI-using web application or framework to help it serve static
resources.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A Bower-centric static file server for WSGI
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
BowerStatic is a WSGI-based framework that you can integrate with your
WSGI-using web application or framework to help it serve static
resources.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
BowerStatic is a WSGI-based framework that you can integrate with your
WSGI-using web application or framework to help it serve static
resources.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
BowerStatic is a WSGI-based framework that you can integrate with your
WSGI-using web application or framework to help it serve static
resources.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
BowerStatic is a WSGI-based framework that you can integrate with your
WSGI-using web application or framework to help it serve static
resources.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
rm -fR build
py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.dev0.git20141111
- Initial build for Sisyphus

