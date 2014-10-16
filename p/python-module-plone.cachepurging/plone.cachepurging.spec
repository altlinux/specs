%define oname plone.cachepurging
Name: python-module-%oname
Version: 1.0.8
Release: alt1.dev0.git20140911
Summary: Cache purging support for Zope 2 applications
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.cachepurging/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.cachepurging.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-five.globalrequest
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-z3c.caching
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone five.globalrequest plone.registry z3c.caching
%py_requires zope.annotation zope.component zope.event zope.interface
%py_requires zope.i18nmessageid zope.lifecycleevent zope.schema
%py_requires zope.testing

%description
The plone.cachepurging package provides cache purging for Zope 2
applications. It is inspired by (and borrows some code from)
Products.CMFSquidTool, but it is not tied to Squid. In fact, it is
tested mainly with Varnish, though it should also work with Squid and
Enfold Proxy.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
The plone.cachepurging package provides cache purging for Zope 2
applications. It is inspired by (and borrows some code from)
Products.CMFSquidTool, but it is not tied to Squid. In fact, it is
tested mainly with Varnish, though it should also work with Squid and
Enfold Proxy.

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
%exclude %python_sitelibdir/plone/*/tests

%files tests
%python_sitelibdir/plone/*/tests

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.dev0.git20140911
- Initial build for Sisyphus

