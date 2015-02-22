%define mname uwosh
%define oname %mname.transitionbuttons
Name: python-module-%oname
Version: 0.9.8
Release: alt1
Summary: Adds a button interface for the different state transitions
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/uwosh.transitionbuttons/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.users
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.app.form
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.viewlet

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore plone.app.registry plone.app.users
%py_requires plone.registry plone.app.layout zope.component zope.formlib
%py_requires zope.interface zope.schema zope.i18nmessageid zope.app.form
%py_requires z3c.form

%description
The TransitionButtons add-on is a simple plugin for the Plone platform
to make the state-change buttons in the edit bar more visibile. It just
adds a small portlet-like box with very obvious buttons to
publish/retract/etc the current document, assuming the user has rights
to do so.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing Products.DCWorkflow zope.configuration
%py_requires zope.viewlet

%description tests
The TransitionButtons add-on is a simple plugin for the Plone platform
to make the state-change buttons in the edit bar more visibile. It just
adds a small portlet-like box with very obvious buttons to
publish/retract/etc the current document, assuming the user has rights
to do so.

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
%doc *.txt *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1
- Initial build for Sisyphus

