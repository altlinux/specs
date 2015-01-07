%define mname collective
%define oname %mname.geo.json
Name: python-module-%oname
Version: 0.3
Release: alt1.dev0.git20140805
Summary: Collective Geo GeoJson output
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.geo.json/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.geo.json.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-geojson python-module-pygeoif
BuildPreReq: python-module-openid
BuildPreReq: python-module-collective.geo.geographer
BuildPreReq: python-module-collective.geo.settings
BuildPreReq: python-module-collective.geo.contentlocations
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-collective.geo.mapwidget
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-zope.tales

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname.geo collective.geo.geographer geojson pygeoif
%py_requires collective.geo.settings collective.geo.contentlocations
%py_requires plone.api collective.geo.mapwidget Products.CMFCore
%py_requires plone.registry plone.theme zope.interface zope.component
%py_requires zope.tales

%description
Some web mapping clients like Leaflet or Polymaps accept json as an
input format. This product produces it.

It does not have any user interface, it just provides a GeoJson view for
contentitems, folders and collections. To test just append
/@@geo-json.json to the url.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
Some web mapping clients like Leaflet or Polymaps accept json as an
input format. This product produces it.

It does not have any user interface, it just provides a GeoJson view for
contentitems, folders and collections. To test just append
/@@geo-json.json to the url.

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
* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev0.git20140805
- Initial build for Sisyphus

