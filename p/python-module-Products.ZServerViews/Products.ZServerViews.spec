%define oname Products.ZServerViews
Name: python-module-%oname
Version: 0.2.1
Release: alt1.dev0.git20130124
Summary: Infrastructure for plugging views that run directly at the ZServer thread
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ZServerViews/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/leorochael/Products.ZServerViews.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2 ipython
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zconfig-tests

%py_provides %oname
Requires: python-module-Zope2

%description
This Zope add-on product provides for easy configuration of ZServer
Views.

A ZServer View is a (supposedly) small and fast WSGI application that
runs directly from within the ZServer thread (a.k.a. medusa thread).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing ZConfig.components.logger.tests

%description tests
This Zope add-on product provides for easy configuration of ZServer
Views.

A ZServer View is a (supposedly) small and fast WSGI application that
runs directly from within the ZServer thread (a.k.a. medusa thread).

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
%doc *.txt *.rst
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.dev0.git20130124
- Initial build for Sisyphus

