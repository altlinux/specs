%define mname plonehrm
%define oname %mname.contracts
Name: python-module-%oname
Version: 3.10
Release: alt2
Summary: Contracts for Plone HRM
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plonehrm.contracts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.autopermission
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-plonehrm.notifications
BuildPreReq: python-module-zope.app.annotation
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.plonehrm

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.autopermission Products.CMFCore zope.i18n
%py_requires Products.Archetypes Products.validation zope.annotation
%py_requires plonehrm.notifications zope.app.annotation zope.interface
%py_requires zope.component zope.event zope.i18nmessageid
%py_requires Products.plonehrm

%description
Add contracts to Employees. See the Products.plonehrm package.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing

%description tests
Add contracts to Employees. See the Products.plonehrm package.

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
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt2
- Added necessary requirements

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt1
- Initial build for Sisyphus

