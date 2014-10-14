%define oname plone.caching
Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20140903
Summary: Zope 2 integration for z3c.caching
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.caching/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.caching.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-docutils
BuildPreReq: python-module-z3c.caching
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.transformchain
BuildPreReq: python-module-five.globalrequest

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone z3c.caching plone.registry zope.interface zope.schema
%py_requires zope.component zope.i18nmessageid plone.transformchain
%py_requires five.globalrequest

%description
The ``plone.caching`` package provides a framework for the management of
cache headers, built atop `z3c.caching`.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The ``plone.caching`` package provides a framework for the management of
cache headers, built atop `z3c.caching`.

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
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20140903
- Initial build for Sisyphus

