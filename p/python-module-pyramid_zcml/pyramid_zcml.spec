%define oname pyramid_zcml

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt2
Summary: Zope Config Markup Language support for Pyramid
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_zcml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
BuildPreReq: python-module-PasteScript python-module-pyramid
BuildPreReq: python-module-PasteDeploy python-module-translationstring
BuildPreReq: python-module-venusian python-module-zope.interface
BuildPreReq: python-module-zope.deprecation python-module-zope.component
BuildPreReq: python-module-zope.configuration python-module-repoze.lru
BuildPreReq: python-module-webob python-module-mako
BuildPreReq: python-module-chameleon.core python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid python-module-zope.event
BuildPreReq: python-module-markupsafe python-module-ordereddict
BuildPreReq: python-module-webtest python-module-unittest2
BuildPreReq: python-module-repoze.sphinx.autointerface
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires pyramid paste.script zope.configuration zope.schema
%py_requires zope.interface pyramid.config pyramid.threadlocal
%py_requires pyramid.asset pyramid.exceptions pyramid.authorization
%py_requires pyramid.authentication pyramid.scaffolds pyramid.view
%py_requires pyramid.response

%description
pyramid_zcml is a package which provides ZCML (Zope Configuration Markup
Language) directives for all "configurator" methods available in the
Pyramid web framework.

%package -n python3-module-%oname
Summary: Zope Config Markup Language support for Pyramid
Group: Development/Python3
%py3_requires pyramid paste.script zope.configuration zope.schema
%py3_requires zope.interface pyramid.config pyramid.threadlocal
%py3_requires pyramid.asset pyramid.exceptions pyramid.authorization
%py3_requires pyramid.authentication pyramid.scaffolds pyramid.view
%py3_requires pyramid.response

%description -n python3-module-%oname
pyramid_zcml is a package which provides ZCML (Zope Configuration Markup
Language) directives for all "configurator" methods available in the
Pyramid web framework.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_zcml
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires sphinx docutils repoze.sphinx.autointerface webtest
%py3_requires venusian pyramid.security pyramid.registry
%py3_requires pyramid.interfaces pyramid.static pyramid.renderers
%py3_requires pyramid.testing

%description -n python3-module-%oname-tests
pyramid_zcml is a package which provides ZCML (Zope Configuration Markup
Language) directives for all "configurator" methods available in the
Pyramid web framework.

This package contains tests for pyramid_zcml.

%package tests
Summary: Tests for pyramid_zcml
Group: Development/Python
Requires: %name = %version-%release
%py_requires sphinx docutils repoze.sphinx.autointerface webtest
%py_requires venusian pyramid.security pyramid.registry
%py_requires pyramid.interfaces pyramid.static pyramid.renderers
%py_requires pyramid.testing

%description tests
pyramid_zcml is a package which provides ZCML (Zope Configuration Markup
Language) directives for all "configurator" methods available in the
Pyramid web framework.

This package contains tests for pyramid_zcml.

%package pickles
Summary: Pickles for pyramid_zcml
Group: Development/Python

%description pickles
pyramid_zcml is a package which provides ZCML (Zope Configuration Markup
Language) directives for all "configurator" methods available in the
Pyramid web framework.

This package contains pickles for pyramid_zcml.

%package docs
Summary: Documentation for pyramid_zcml
Group: Development/Documentation

%description docs
pyramid_zcml is a package which provides ZCML (Zope Configuration Markup
Language) directives for all "configurator" methods available in the
Pyramid web framework.

This package contains documentation for pyramid_zcml.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%if 0
export PYTHONPATH=$PWD
pushd docs
%make html
%make pickle
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if 0
install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%if 0
%exclude %python_sitelibdir/%oname/pickle
%endif

%files tests
%python_sitelibdir/*/tests

%if 0
%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Added module for Python 3

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Version 0.8

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

