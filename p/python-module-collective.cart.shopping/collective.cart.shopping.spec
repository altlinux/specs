%define mname collective.cart
%define oname %mname.shopping
Name: python-module-%oname
Version: 0.12.1
Release: alt1.git20150122
Summary: Shopping site suit for Plone
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.cart.shopping/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.cart.shopping.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.behavior.discount
BuildPreReq: python-module-collective.behavior.size
BuildPreReq: python-module-collective.behavior.sku
BuildPreReq: python-module-collective.behavior.stock
BuildPreReq: python-module-collective.behavior.vat
BuildPreReq: python-module-collective.cart.core-tests
BuildPreReq: python-module-collective.cart.shipping
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-hexagonit.testing
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.MailHost
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.contentlisting
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.app.viewletmanager
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.event zope.schema zope.annotation zope.viewlet
%py_requires zope.lifecycleevent zope.interface zope.publisher z3c.form
%py_requires plone.app.viewletmanager zope.i18nmessageid zope.component
%py_requires plone.app.layout plone.browserlayer plone.autoform
%py_requires plone.app.contentlisting plone.supermodel plone.memoize
%py_requires Products.validation Products.ZCatalog plone.dexterity
%py_requires Products.CMFCore Products.ATContentTypes Products.MailHost
%py_requires collective.behavior.discount collective.behavior.size
%py_requires collective.behavior.sku collective.behavior.stock
%py_requires collective.behavior.vat collective.cart.core plone.uuid
%py_requires collective.cart.shipping plone.app.textfield plone.registry
%py_requires plone.namedfile Products.statusmessages Products.CMFPlone

%description
collective.cart.shopping adds shop content type to Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires hexagonit.testing plone.testing plone.app.testing
%py_requires zope.testing collective.cart.core.tests

%description tests
collective.cart.shopping adds shop content type to Plone.

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
%python_sitelibdir/collective/cart/shopping
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/cart/shopping/tests

%files tests
%python_sitelibdir/collective/cart/shopping/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.1-alt1.git20150122
- Initial build for Sisyphus

