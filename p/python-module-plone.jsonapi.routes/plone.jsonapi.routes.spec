%define mname plone.jsonapi
%define oname %mname.routes
Name: python-module-%oname
Version: 0.4
Release: alt1.git20150113
Summary: Plone JSONAPI Route Providers
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.jsonapi.routes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/plone.jsonapi.routes.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2 python-modules-json
BuildPreReq: python-module-openid
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.jsonapi.core
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.AdvancedQuery
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-sphinx-devel

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.api plone.jsonapi.core json Products.ZCatalog
%py_requires Products.ATContentTypes Products.CMFCore Products.CMFPlone
%py_requires Products.AdvancedQuery plone.dexterity zope.globalrequest
%py_requires zope.component zope.interface

%description
This is an add-on package for plone.jsonapi.core which provides some
basic URLs for Plone standard contents (and more).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing unittest2 zope.configuration

%description tests
This is an add-on package for plone.jsonapi.core which provides some
basic URLs for Plone standard contents (and more).

This package contains tests for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%make -C docs html

%check
python setup.py test

%files
%doc *.rst docs/_build/html
%python_sitelibdir/plone/jsonapi/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/jsonapi/*/tests

%files tests
%python_sitelibdir/plone/jsonapi/*/tests

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20150113
- Initial build for Sisyphus

