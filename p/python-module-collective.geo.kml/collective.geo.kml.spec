%define mname collective
%define oname %mname.geo.kml
Name: python-module-%oname
Version: 3.3
Release: alt1.dev0.git20140818
Summary: Kml view for collective.geo
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.geo.kml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.geo.kml.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-collective.geo.mapwidget
BuildPreReq: python-module-collective.geo.geographer
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-collective.geo.settings
BuildPreReq: python-module-collective.contentleadimage
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname.geo Products.CMFCore collective.geo.mapwidget
%py_requires collective.geo.geographer collective.geo.settings
%py_requires collective.contentleadimage plone.registry plone.app.layout
%py_requires plone.memoize plone.theme zope.interface zope.component
%py_requires zope.publisher zope.schema zope.traversing
%py_requires zope.i18nmessageid

%description
collective.geo.kml provides KML views for georeferenced objects,
allowing Plone containers and collections to be visualized in Google
Earth.

It also provides a map view to Plone Folder and Topic content types to
display kml data.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
collective.geo.kml provides KML views for georeferenced objects,
allowing Plone containers and collections to be visualized in Google
Earth.

It also provides a map view to Plone Folder and Topic content types to
display kml data.

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
rm -fR build
py.test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/geo/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/geo/*/test*

%files tests
%python_sitelibdir/%mname/geo/*/test*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1.dev0.git20140818
- Initial build for Sisyphus

