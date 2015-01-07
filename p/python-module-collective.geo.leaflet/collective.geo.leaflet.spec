%define mname collective
%define oname %mname.geo.leaflet
Name: python-module-%oname
Version: 0.1
Release: alt1.b6.dev0.git20150106
Summary: Add geo views for dexterity content with leaflet js library
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.geo.leaflet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.geo.leaflet.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.api python-module-openid
BuildPreReq: python-module-collective.geo.settings
BuildPreReq: python-module-collective.geo.geographer
BuildPreReq: python-module-collective.geo.mapwidget
BuildPreReq: python-module-collective.geo.behaviour
BuildPreReq: python-module-collective.js.leaflet
BuildPreReq: python-module-collective.geo.contentlocations
BuildPreReq: python-module-collective.geo.json
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.browserlayer

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.component zope.publisher
%py_requires plone.app.layout zope.i18nmessageid zope.tales zope.schema
%py_requires Products.CMFPlone plone.dexterity plone.indexer
%py_requires Products.CMFCore Products.CMFQuickInstallerTool
%py_requires %mname.geo plone.api collective.geo.settings zope.interface
%py_requires collective.geo.geographer collective.geo.mapwidget
%py_requires collective.geo.behaviour collective.js.leaflet
%py_requires collective.geo.contentlocations collective.geo.json

%description
This package use the collective.geo.* suite with leaflet.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.robotframework.testing plone.app.testing
%py_requires plone.registry plone.browserlayer

%description tests
This package use the collective.geo.* suite with leaflet.

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
%exclude %python_sitelibdir/%mname/geo/*/*/test*

%files tests
%python_sitelibdir/%mname/geo/*/test*
%python_sitelibdir/%mname/geo/*/*/test*

%changelog
* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.b6.dev0.git20150106
- Initial build for Sisyphus

