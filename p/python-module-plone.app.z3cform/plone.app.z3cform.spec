%define oname plone.app.z3cform

Name: python-module-%oname
Version: 1.0.1
Release: alt2.dev0.git20140823
Summary: A Plone specific integration and HTML mark-up for z3c.form
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.z3cform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.z3cform.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.widgets
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.formwidget.query
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app Products.CMFCore plone.app.widgets plone.protect
%py_requires plone.z3cform z3c.form z3c.formwidget.query zope.i18n
%py_requires zope.browserpage zope.component zope.globalrequest
%py_requires zope.i18nmessageid zope.interface zope.schema
%py_requires zope.traversing
%py_requires Products.CMFPlone

%description
A collection of widgets, templates and other components for use with
z3c.form and Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.browserlayer plone.testing
%py_requires zope.contentprovider zope.publisher zope.testing

%description tests
A collection of widgets, templates and other components for use with
z3c.form and Plone.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/tests

%files tests
%python_sitelibdir/plone/app/*/tests

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.dev0.git20140823
- Added necessary requirements
- Enabled testing

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.dev0.git20140823
- Initial build for Sisyphus

