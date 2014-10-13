%define oname plone.portlets
Name: python-module-%oname
Version: 2.2.1
Release: alt1.dev0.git20140826
Summary: An extension of zope.viewlet to support dynamic portlets
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.portlets/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.portlets.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.security

%py_provides %oname
%py_requires zope.container zope.contentprovider zope.interface
%py_requires plone ZODB3 plone.memoize zope.annotation zope.component
%py_requires zope.publisher zope.schema zope.site

%description
plone.portlets provides a generic infrastructure for managing portlets.

Portlets are a bit like viewlets, except they can be manipulated at
runtime, using local components. This package is used by
plone.app.portlets to provide Plone-specific portlets, but should be
generic enough to work on other platforms. It should work in a "pure
Zope Toolkit" environment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.browserpage zope.configuration zope.location
%py_requires zope.security

%description tests
plone.portlets provides a generic infrastructure for managing portlets.

Portlets are a bit like viewlets, except they can be manipulated at
runtime, using local components. This package is used by
plone.app.portlets to provide Plone-specific portlets, but should be
generic enough to work on other platforms. It should work in a "pure
Zope Toolkit" environment.

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
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.dev0.git20140826
- Initial build for Sisyphus

