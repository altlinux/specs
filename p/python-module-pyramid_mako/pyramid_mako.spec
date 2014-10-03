%define oname pyramid_mako

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.git20140522
Summary: Mako template bindings for the Pyramid web framework
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_mako/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/pyramid_mako.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
BuildPreReq: python-module-repoze.sphinx.autointerface
BuildPreReq: python-module-mako python-module-pyramid
BuildPreReq: python-module-PasteDeploy python-module-translationstring
BuildPreReq: python-module-venusian python-module-zope.deprecation
BuildPreReq: python-module-repoze.lru python-module-webob
BuildPreReq: python-module-webtest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
These are bindings for the Mako templating system for the Pyramid web
framework.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
These are bindings for the Mako templating system for the Pyramid web
framework.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Mako template bindings for the Pyramid web framework
Group: Development/Python3

%description -n python3-module-%oname
These are bindings for the Mako templating system for the Pyramid web
framework.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
These are bindings for the Mako templating system for the Pyramid web
framework.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
These are bindings for the Mako templating system for the Pyramid web
framework.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
These are bindings for the Mako templating system for the Pyramid web
framework.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

cp -fR %_datadir/pylons_sphinx_theme docs/_themes
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
* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20140522
- Initial build for Sisyphus

