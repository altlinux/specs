%define oname plone.principalsource
Name: python-module-%oname
Version: 1.0
Release: alt1.b2.git20130315
Summary: A queriable source for accessing users and/or groups
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.principalsource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/starzel/plone.principalsource.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-z3c.formwidget.query
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
%py_requires plone z3c.formwidget.query zope.schema zope.component
%py_requires zope.interface Products.CMFCore
%py_requires Products.PluggableAuthService

%description
This package provides a queriable sources (vocabularies) that return PAS
users, groups or principals (both users and groups).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.component.testing
%py_requires zope.security.testing

%description tests
This package provides a queriable sources (vocabularies) that return PAS
users, groups or principals (both users and groups).

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b2.git20130315
- Initial build for Sisyphus

