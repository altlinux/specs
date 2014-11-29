%define mname plone.app
%define oname %mname.kss

%def_disable check

Name: python-module-%oname
Version: 1.8.0
Release: alt1.dev0.git20121117
Summary: KSS (Kinetic Style Sheets) for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.kss/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.kss.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-kss.core-tests
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.PloneTestCase
#BuildPreReq: python-module-archetypes.kss

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname kss.core plone.portlets plone.app.layout zope.i18n
%py_requires plone.app.portlets plone.locking zope.component
%py_requires zope.contentprovider zope.deprecation zope.i18nmessageid
%py_requires zope.interface zope.lifecycleevent zope.viewlet
%py_requires Products.CMFCore Products.DCWorkflow
%py_requires Products.statusmessages
#py_requires archetypes.kss

%description
This product gives generic KSS support for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase kss.core.tests

%description tests
This product gives generic KSS support for Plone.

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
%doc *.txt docs/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/tests

%files tests
%python_sitelibdir/plone/app/*/tests

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.dev0.git20121117
- Initial build for Sisyphus

