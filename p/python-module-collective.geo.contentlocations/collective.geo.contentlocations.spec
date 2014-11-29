%define mname collective
%define oname %mname.geo.contentlocations
Name: python-module-%oname
Version: 3.2
Release: alt1.dev0.git20140226
Summary: Geo reference for plone contents
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.geo.contentlocations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.geo.contentlocations.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-pygeoif
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-collective.geo.mapwidget
BuildPreReq: python-module-collective.z3cform.mapwidget
BuildPreReq: python-module-collective.geo.geographer
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-collective.geo.settings
BuildPreReq: python-module-collective.z3cform.colorpicker
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname.geo Products.CMFCore Products.Archetypes pygeoif
%py_requires collective.geo.mapwidget collective.z3cform.mapwidget
%py_requires collective.geo.geographer collective.geo.settings z3c.form
%py_requires collective.z3cform.colorpicker Products.CMFPlone zope.event
%py_requires plone.dexterity plone.registry plone.z3cform.fieldsets
%py_requires plone.z3cform.layout plone.indexer zope.lifecycleevent
%py_requires zope.interface zope.annotation zope.component zope.schema
%py_requires zope.i18nmessageid

%description
collective.geo.contentlocations is a GUI for collective.geo.geographer.

It provides some simple forms to add geographical coordinates and
associated settings to Plone content types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
collective.geo.contentlocations is a GUI for collective.geo.geographer.

It provides some simple forms to add geographical coordinates and
associated settings to Plone content types.

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
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.dev0.git20140226
- Initial build for Sisyphus

