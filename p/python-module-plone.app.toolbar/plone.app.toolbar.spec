%define oname plone.app.toolbar

%def_disable check

Name: python-module-%oname
Version: 1.5.0
Release: alt1.dev.git20140823
Summary: Toolbar for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.toolbar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.toolbar.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-lxml python-module-nose
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.tiles
BuildPreReq: python-module-Products.ResourceRegistries
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.jquery
BuildPreReq: python-module-plone.app.search
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.querystring
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-plone.app.event
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-robotframework-selenium2library
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-portal

%py_provides %oname
%py_requires plone.app zope.component zope.i18nmessageid zope.viewlet
%py_requires zope.browsermenu zope.interface zope.traversing
%py_requires plone.memoize plone.tiles Products.ResourceRegistries
%py_requires plone.app.vocabularies plone.app.jquery plone.app.search
%py_requires plone.app.registry plone.app.querystring Products.CMFPlone
%py_requires plone.app.contenttypes plone.app.event

%description
The goal of plone.app.toolbar is to provide an even easier way to theme
Plone by creating managing toolbar inside iframe.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-robotframework-selenium2library
%py_requires Products.CMFCore plone.app.robotframework plone.app.testing
%py_requires plone.testing zope.configuration plone.app.contenttypes
%py_requires plone.app.robotframework.testing

%description tests
The goal of plone.app.toolbar is to provide an even easier way to theme
Plone by creating managing toolbar inside iframe.

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
py.test
nosetests

%files
%doc *.rst
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.dev.git20140823
- Initial build for Sisyphus

