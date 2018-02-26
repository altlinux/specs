%define oname pyramid

%def_with python3

Name: python-module-%oname
Version: 1.4
Release: alt1.dev.git20120503
Summary: Small, fast, down-to-earth Python web application development framework
License: Repoze Public License
Group: Development/Python
Url: http://pylonsproject.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/pyramid
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
BuildPreReq: python-module-PasteDeploy python-module-translationstring
BuildPreReq: python-module-venusian python-module-zope.deprecation
BuildPreReq: python-module-zope.interface python-module-repoze.lru
BuildPreReq: python-module-webob python-module-mako
BuildPreReq: python-module-chameleon.core python-module-markupsafe
BuildPreReq: python-module-zope.component python-module-virtualenv
BuildPreReq: python-module-repoze.sphinx.autointerface
BuildPreReq: python-module-webtest python-module-zope.event
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-PasteDeploy python3-module-translationstring
BuildPreReq: python3-module-venusian python3-module-zope.deprecation
BuildPreReq: python3-module-zope.interface python3-module-repoze.lru
BuildPreReq: python3-module-webob python3-module-mako
BuildPreReq: python3-module-chameleon.core python3-module-markupsafe
BuildPreReq: python3-module-zope.component python3-module-virtualenv
BuildPreReq: python3-module-repoze.sphinx.autointerface
BuildPreReq: python3-module-webtest python3-module-zope.event
%endif

%description
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

%if_with python3
%package -n python3-module-%oname
Summary: Small, fast, down-to-earth Python 3 web application development framework
Group: Development/Python3

%description -n python3-module-%oname
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

%package -n python3-module-%oname-tests
Summary: Tests for Pyramid (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

This package contains tests for Pyramid.
%endif

%package tests
Summary: Tests for Pyramid
Group: Development/Python
Requires: %name = %version-%release

%description tests
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

This package contains tests for Pyramid.

%package pickles
Summary: Pickles for Pyramid
Group: Development/Python

%description pickles
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

This package contains pickles for Pyramid.

%package docs
Summary: Documentation for Pyramid
Group: Development/Documentation

%description docs
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

This package contains documentation for Pyramid.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd
%endif

%python_install

export PYTHONPATH=%python_sitelibdir:%buildroot%python_sitelibdir
rm -f docs/api/interfaces.rst
pushd docs
%make pickle
%make html
cp -fR _build/pickle %buildroot%python_sitelibdir/%oname/
popd

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%_bindir/*
%exclude %_bindir/py3_*
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/py3_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev.git20120503
- New snapshot
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev.git20111212
- Version 1.4dev

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.a0.git20110513.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.a0.git20110513
- Initial build for Sisyphus

