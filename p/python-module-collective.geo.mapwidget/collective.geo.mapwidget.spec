%define mname collective
%define oname %mname.geo.mapwidget
Name: python-module-%oname
Version: 2.1.4
Release: alt1.dev0.git20141113
Summary: Some handy page macros and adapters to easily manage multiple maps on one page
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.geo.mapwidget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.geo.mapwidget.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-BeautifulSoup python-module-geopy
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-collective.geo.openlayers
BuildPreReq: python-module-collective.geo.settings
BuildPreReq: python-module-collective.z3cform.colorpicker
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form

%py_provides %oname
%py_requires %mname.geo Products.CMFCore plone.app.z3cform z3c.form
%py_requires collective.geo.openlayers collective.geo.settings
%py_requires collective.z3cform.colorpicker Products.CMFPlone
%py_requires plone.registry plone.memoize plone.z3cform
%py_requires plone.indexer zope.component zope.schema
%py_requires zope.interface zope.publisher zope.event zope.i18nmessageid

%description
collective.geo.mapwidget provides some handy page macros and adapters to
easily manage multiple maps on one page.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
collective.geo.mapwidget provides some handy page macros and adapters to
easily manage multiple maps on one page.

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
%doc *.rst docs/*
%python_sitelibdir/%mname/geo/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/geo/*/test*

%files tests
%python_sitelibdir/%mname/geo/*/test*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1.dev0.git20141113
- Initial build for Sisyphus

