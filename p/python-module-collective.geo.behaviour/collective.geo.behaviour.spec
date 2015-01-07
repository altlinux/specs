%define mname collective
%define oname %mname.geo.behaviour
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20140226
Summary: collective.geo Dexterity integration
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.geo.behaviour/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.geo.behaviour.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-pygeoif
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-collective.geo.geographer
BuildPreReq: python-module-collective.geo.mapwidget
BuildPreReq: python-module-collective.z3cform.mapwidget
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-collective.geo.settings
BuildPreReq: python-module-collective.z3cform.colorpicker
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.configuration

%py_provides %oname
%py_requires %mname.geo plone.behavior plone.autoform plone.supermodel
%py_requires zope.schema zope.interface zope.component pygeoif
%py_requires collective.geo.geographer collective.geo.mapwidget
%py_requires collective.z3cform.mapwidget collective.geo.settings
%py_requires collective.z3cform.colorpicker Products.CMFCore
%py_requires zope.i18nmessageid

%description
This package provides the ability to assign geographical information to
Dexterity-based (plone.app.dexterity) content types within Plone and
does so using collective.geo.geographer and collective.geo.mapwidget.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.dexterity zope.configuration

%description tests
This package provides the ability to assign geographical information to
Dexterity-based (plone.app.dexterity) content types within Plone and
does so using collective.geo.geographer and collective.geo.mapwidget.

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
* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20140226
- Initial build for Sisyphus

