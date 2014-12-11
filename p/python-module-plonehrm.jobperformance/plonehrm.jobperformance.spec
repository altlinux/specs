%define mname plonehrm
%define oname %mname.jobperformance

Name: python-module-%oname
Version: 1.4
Release: alt2.dev.svn20100129
Summary: Job performance interviews for Plone HRM
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/plonehrm.jobperformance/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/plonehrm.jobperformance/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.autopermission
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.kss
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.plonehrm-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.autopermission Products.Archetypes
%py_requires Products.CMFCore Products.CMFPlone plone.app.kss
%py_requires zope.viewlet zope.interface zope.i18nmessageid
%py_requires Products.plonehrm

%description
This adds Job performance interviews to Plone HRM. See the
Products.plonehrm package.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase
%py_requires Products.plonehrm.tests

%description tests
This adds Job performance interviews to Plone HRM. See the
Products.plonehrm package.

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
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2.dev.svn20100129
- Added necessary requirements

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev.svn20100129
- Initial build for Sisyphus

