%define oname plone.app.relations
Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20111010
Summary: Provides a content centric API for the engine from plone.relations
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.relations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.relations.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.relations
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.hookable
BuildPreReq: python-module-zope.untrustedpython
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.password-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app plone.relations zope.site zope.intid
%py_requires Products.PluggableAuthService Products.CMFCore
%py_requires Products.PlonePAS

%description
A set of components to provide a content centric API for the engine from
plone.relations, as well as a few different core relationship types and
policies.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.password.testing
%py_requires zope.security.testing Products.PloneTestCase

%description tests
A set of components to provide a content centric API for the engine from
plone.relations, as well as a few different core relationship types and
policies.

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
%exclude %python_sitelibdir/plone/app/*/tests.*

%files tests
%python_sitelibdir/plone/app/*/tests.*

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20111010
- Initial build for Sisyphus

