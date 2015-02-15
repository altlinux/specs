%define mname collective.cart
%define oname %mname.stock
Name: python-module-%oname
Version: 0.5
Release: alt1
Summary: Adds stock content type
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.cart.stock/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-hexagonit.testing
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.app.dexterity plone.supermodel plone.dexterity
%py_requires zope.i18nmessageid zope.lifecycleevent zope.component
%py_requires zope.schema zope.interface

%description
collective.cart.stock adds stock content type for stocking articles.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires hexagonit.testing Products.CMFCore plone.browserlayer
%py_requires plone.app.testing zope.testing

%description tests
collective.cart.stock adds stock content type for stocking articles.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires collective

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/collective/cart/__init__.py \
	%buildroot%python_sitelibdir/collective/cart/

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/collective/cart/stock
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/cart/stock/tests

%files tests
%python_sitelibdir/collective/cart/stock/tests

%files -n python-module-%mname
%dir %python_sitelibdir/collective/cart
%python_sitelibdir/collective/cart/__init__.py*

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

