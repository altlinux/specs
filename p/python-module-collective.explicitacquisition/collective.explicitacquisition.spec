%define mname collective
%define oname %mname.explicitacquisition
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20150218
Summary: Disallow access to acquired content outside the current path
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.explicitacquisition/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.explicitacquisition.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zExceptions python-module-mockup
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone-tests
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.contenttypes-tests
BuildPreReq: python-module-plone.app.event-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore Products.CMFPlone zExceptions
%py_requires zope.component zope.interface

%description
Access to acquired content should not be allowed.

This package is a repackaging of @gotcha's Products.CMFPlone branch
"publication through explicit acquisition", which solves ticket 13793:
https://dev.plone.org/ticket/13793.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.CMFPlone.testing plone.app.imaging
%py_requires plone.app.testing plone.app.contenttypes.testing
%py_requires plone.app.event.testing

%description tests
Access to acquired content should not be allowed.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20150218
- Initial build for Sisyphus

