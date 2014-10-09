%define oname pyramid_chameleon

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.git20140713
Summary: Chameleon template compiler for pyramid
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_chameleon/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/pyramid_chameleon.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
BuildPreReq: python-module-chameleon.core python-module-pyramid-tests
BuildPreReq: python-module-PasteDeploy python-module-translationstring
BuildPreReq: python-module-venusian python-module-zope.deprecation
BuildPreReq: python-module-zope.interface python-module-repoze.lru
BuildPreReq: python-module-repoze.sphinx.autointerface
BuildPreReq: python-module-webob python-module-zope.component
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires paste.deploy zope.deprecation zope.interface repoze.lru
%py_requires zope.component

%description
These are bindings for the Chameleon templating system for the Pyramid
web framework.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
These are bindings for the Chameleon templating system for the Pyramid
web framework.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Chameleon template compiler for pyramid
Group: Development/Python3
%py3_provides %oname
%py3_requires paste.deploy zope.deprecation zope.interface repoze.lru
%py3_requires zope.component

%description -n python3-module-%oname
These are bindings for the Chameleon templating system for the Pyramid
web framework.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
These are bindings for the Chameleon templating system for the Pyramid
web framework.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
These are bindings for the Chameleon templating system for the Pyramid
web framework.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
These are bindings for the Chameleon templating system for the Pyramid
web framework.

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
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20140713
- Initial build for Sisyphus

