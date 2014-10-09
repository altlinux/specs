%define oname pyramid_deform

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.git20140131
Summary: Bindings to the Deform form library for the Pyramid web framework
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_deform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/pyramid_deform.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
BuildPreReq: python-module-colander python-module-deform
BuildPreReq: python-module-pyramid python-module-zope.deprecation
BuildPreReq: python-module-peppercorn python-module-chameleon.core
BuildPreReq: python-module-PasteDeploy python-module-venusian
BuildPreReq: python-module-zope.interface python-module-repoze.lru
BuildPreReq: python-module-webob python-module-mock
BuildPreReq: python-module-coverage python-module-nose
BuildPreReq: python-module-zope.component
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires colander pyramid deform zope.deprecation peppercorn webob
%py_requires chameleon paste.deploy venusian zope.interface repoze.lru

%description
pyramid_deform provides bindings for the Pyramid web framework to the
Deform form library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires mock

%description tests
pyramid_deform provides bindings for the Pyramid web framework to the
Deform form library.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Bindings to the Deform form library for the Pyramid web framework
Group: Development/Python3
%py3_provides %oname
%py3_requires colander pyramid deform zope.deprecation peppercorn webob
%py3_requires chameleon paste.deploy venusian zope.interface repoze.lru

%description -n python3-module-%oname
pyramid_deform provides bindings for the Pyramid web framework to the
Deform form library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires mock

%description -n python3-module-%oname-tests
pyramid_deform provides bindings for the Pyramid web framework to the
Deform form library.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyramid_deform provides bindings for the Pyramid web framework to the
Deform form library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyramid_deform provides bindings for the Pyramid web framework to the
Deform form library.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/
cp -fR %_datadir/pylons_sphinx_theme docs/_themes

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
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20140131
- Initial build for Sisyphus

