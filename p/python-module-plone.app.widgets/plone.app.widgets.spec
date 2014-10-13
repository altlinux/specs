%define oname plone.app.widgets

%def_disable check

Name: python-module-%oname
Version: 1.8.0
Release: alt1.dev0.git20141009
Summary: Integrating plone.widgets into plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.widgets/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.widgets.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-pytz python-module-mock
BuildPreReq: python-module-Products.ResourceRegistries
BuildPreReq: python-module-plone.app.jquery
BuildPreReq: python-module-plone.app.search
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-plone.app.testing
#BuildPreReq: python-module-plone.app.vocabularies
#BuildPreReq: python-module-plone.app.registry
#BuildPreReq: python-module-plone.app.querystring
#BuildPreReq: python-module-Products.Archetypes
#BuildPreReq: python-module-plone.app.dexterity
#BuildPreReq: python-module-plone.app.contenttypes
#BuildPreReq: python-module-plone.app.event

%py_provides %oname
%py_requires plone.app Products.ResourceRegistries plone.app.jquery
%py_requires plone.app.search archetypes.schemaextender
#py_requires plone.app.vocabularies plone.app.registry
#py_requires plone.app.querystring Products.Archetypes
#py_requires plone.app.dexterity plone.app.contenttypes
#py_requires plone.app.event

%description
The goal of plone.app.widgets is to provide an implementation for a new
set of javascript widgets being developed outside Plone as part of
Mockup project. It overrides explicit widgets used in dexterity and
archetypes to provide tested and modularized widgets based on the
concept of patterns.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.robotframework plone.app.testing

%description tests
The goal of plone.app.widgets is to provide an implementation for a new
set of javascript widgets being developed outside Plone as part of
Mockup project. It overrides explicit widgets used in dexterity and
archetypes to provide tested and modularized widgets based on the
concept of patterns.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst docs/source/*.rst
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.dev0.git20141009
- Initial build for Sisyphus

