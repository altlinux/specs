%define mname ftw
%define oname %mname.geo
Name: python-module-%oname
Version: 1.3.3
Release: alt1.dev0.git20141107
Summary: Integration package for collective.geo.* packages
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.geo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.geo.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-geopy python-module-mocker
BuildPreReq: python-module-unittest2 python-module-transaction
BuildPreReq: python-module-collective.geo.settings
BuildPreReq: python-module-collective.geo.openlayers
BuildPreReq: python-module-collective.geo.geographer
BuildPreReq: python-module-collective.geo.contentlocations
BuildPreReq: python-module-collective.geo.kml
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-zope.schema

%py_provides %oname
%py_requires %mname collective.geo.settings collective.geo.openlayers
%py_requires collective.geo.geographer collective.geo.contentlocations
%py_requires collective.geo.kml plone.app.dexterity ftw.upgrade
%py_requires Products.statusmessages Products.Archetypes plone.memoize
%py_requires Products.CMFCore plone.dexterity zope.interface
%py_requires zope.component zope.viewlet zope.i18nmessageid

%description
This product helps integrating the collective.geo.* packages and aims to
provide some sensible defaults. Besides some integration glue it defines
a new interface IGeocodableLocation that can be used to create adapters
that knows how to represent the location of a content type with
address-like fields as a string suitable for passing to a geocoding API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testbrowser ftw.testing plone.app.testing plone.testing
%py_requires zope.configuration plone.directives.form plone.registry
%py_requires Products.ATContentTypes zope.schema

%description tests
This product helps integrating the collective.geo.* packages and aims to
provide some sensible defaults. Besides some integration glue it defines
a new interface IGeocodableLocation that can be used to create adapters
that knows how to represent the location of a content type with
address-like fields as a string suitable for passing to a geocoding API.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1.dev0.git20141107
- Initial build for Sisyphus

