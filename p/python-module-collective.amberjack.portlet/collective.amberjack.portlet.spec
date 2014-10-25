%define mname collective.amberjack
%define oname %mname.portlet
Name: python-module-%oname
Version: 1.1.1
Release: alt1.git20131218
Summary: Collective amberjack tours portlet
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.amberjack.portlet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.amberjack.portlet.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.amberjack.core
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
%py_requires %mname.core plone.app.portlets plone.portlets

%description
This package provides portlet for collective.amberjack package.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.security.testing
%py_requires Products.PloneTestCase

%description tests
This package provides portlet for collective.amberjack package.

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
%python_sitelibdir/collective/amberjack/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/amberjack/*/tests

%files tests
%python_sitelibdir/collective/amberjack/*/tests

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20131218
- Initial build for Sisyphus

