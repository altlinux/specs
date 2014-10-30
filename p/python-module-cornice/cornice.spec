%define oname cornice

%def_with python3

Name: python-module-%oname
Version: 0.18
Release: alt1.git20141013
Summary: Define Web Services in Pyramid
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/cornice/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mozilla-services/cornice.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mozilla-sphinx-theme python-module-demoapp
BuildPreReq: python-module-pyramid-tests python-module-simplejson
BuildPreReq: python-module-colander python-module-coverage
BuildPreReq: python-module-mock python-module-webtest
BuildPreReq: python-module-rxjson
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-simplejson
BuildPreReq: python3-module-colander python3-module-coverage
BuildPreReq: python3-module-mock python3-module-webtest
BuildPreReq: python3-module-rxjson python3-module-PasteDeploy
BuildPreReq: python3-module-zope.deprecation python3-module-repoze.lru
BuildPreReq: python3-module-sphinx python3-module-babel
BuildPreReq: python3-module-snowballstemmer python3-module-docutils
%endif

%py_provides %oname

%description
Cornice provides helpers to build & document Web Services with Pyramid.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Cornice provides helpers to build & document Web Services with Pyramid.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Define Web Services in Pyramid
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Cornice provides helpers to build & document Web Services with Pyramid.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Cornice provides helpers to build & document Web Services with Pyramid.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Cornice provides helpers to build & document Web Services with Pyramid.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Cornice provides helpers to build & document Web Services with Pyramid.

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

%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
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
%doc examples docs/build/html

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.git20141013
- Initial build for Sisyphus

