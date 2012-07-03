%define oname pyramid_zcml
Name: python-module-%oname
Version: 0.8
Release: alt1
Summary: Zope Config Markup Language support for Pyramid
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_zcml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
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

%py_requires pyramid paste.script

%description
pyramid_zcml is a package which provides ZCML (Zope Configuration Markup
Language) directives for all "configurator" methods available in the
Pyramid web framework.

%package tests
Summary: Tests for pyramid_zcml
Group: Development/Python
Requires: %name = %version-%release
%py_requires sphinx docutils repoze.sphinx.autointerface webtest
%py_requires venusian

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

%build
%python_build

export PYTHONPATH=$PWD
pushd docs
%make html
%make pickle
popd

%install
%python_install

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Version 0.8

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

