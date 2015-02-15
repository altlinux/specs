%define mname collective.cart
%define oname %mname.shipping
Name: python-module-%oname
Version: 0.7
Release: alt1.git20131028
Summary: Adds shipping methods to Plone
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.cart.shipping/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.cart.shipping.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.ATCountryWidget
BuildPreReq: python-module-Products.PythonField
BuildPreReq: python-module-collective.behavior.vat
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-hexagonit.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.ATCountryWidget Products.PythonField
%py_requires collective.behavior.vat plone.app.dexterity zope.schema
%py_requires Products.CMFCore Products.Archetypes plone.supermodel
%py_requires Products.ATContentTypes plone.dexterity zope.i18nmessageid
%py_requires zope.component zope.interface

%description
Shipping method plug-in for collective.cart.core.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires hexagonit.testing plone.registry plone.browserlayer
%py_requires plone.app.testing zope.testing

%description tests
Shipping method plug-in for collective.cart.core.

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
%python_sitelibdir/collective/cart/shipping
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/cart/shipping/tests

%files tests
%python_sitelibdir/collective/cart/shipping/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20131028
- Initial build for Sisyphus

