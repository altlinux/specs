%define mname collective.cart
%define oname %mname.core
Name: python-module-%oname
Version: 0.9.1
Release: alt1.git20150120
Summary: Yet another cart for Plone
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.cart.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.cart.core.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.base-tests
BuildPreReq: python-module-collective.behavior.salable
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-hexagonit.testing
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.annotation

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.base collective.behavior.salable z3c.form
%py_requires plone.app.dexterity Products.statusmessages plone.dexterity
%py_requires Products.CMFCore plone.uuid plone.supermodel plone.portlets
%py_requires plone.app.portlets zope.i18nmessageid zope.interface
%py_requires zope.lifecycleevent zope.component zope.schema zope.event
%py_requires zope.viewlet

%description
collective.cart.core is yet another cart for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires hexagonit.testing plone.app.testing plone.browserlayer
%py_requires plone.app.layout zope.testing zope.publisher
%py_requires zope.annotation collective.base.tests

%description tests
collective.cart.core is yet another cart for Plone.

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
%doc *.rst
%python_sitelibdir/collective/cart/core
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/cart/core/tests

%files tests
%python_sitelibdir/collective/cart/core/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150120
- Initial build for Sisyphus

