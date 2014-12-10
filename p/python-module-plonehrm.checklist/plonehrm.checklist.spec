%define mname plonehrm
%define oname %mname.checklist
Name: python-module-%oname
Version: 1.3
Release: alt1
Summary: Checklists for Plone HRM
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plonehrm.checklist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.autopermission
BuildPreReq: python-module-Products.SecureMailHost
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plonehrm.notifications
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
#BuildPreReq: python-module-Products.plonehrm-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.autopermission Products.SecureMailHost
%py_requires Products.CMFCore Products.Archetypes plonehrm.notifications
%py_requires zope.interface zope.i18n zope.viewlet zope.annotation
%py_requires zope.i18nmessageid
#py_requires Products.plonehrm

%description
With this package you can add checklists to an Employee. There you can
keep track of things that need doing, like getting a copy of their
passport for your administration.

If you set a due date for a checklist item and tick the email
notification option, a reminder will also be sent.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase
#py_requires Products.plonehrm.tests

%description tests
With this package you can add checklists to an Employee. There you can
keep track of things that need doing, like getting a copy of their
passport for your administration.

If you set a due date for a checklist item and tick the email
notification option, a reminder will also be sent.

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
%doc PKG-INFO docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

