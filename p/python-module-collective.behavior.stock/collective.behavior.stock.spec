%define mname collective.behavior
%define oname %mname.stock
Name: python-module-%oname
Version: 0.6
Release: alt1.git20131028
Summary: Provides stock related behavior to dexterity content types
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.behavior.stock/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.behavior.stock.git
# branch: 4.3
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-mock
BuildPreReq: python-module-collective.cart.stock
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.interface

%py_provides %oname
%py_requires %mname collective.cart.stock plone.behavior plone.autoform
%py_requires Products.CMFCore plone.supermodel zope.i18nmessageid
%py_requires zope.schema zope.lifecycleevent zope.interface

%description
collective.behavior.stock provides stock related behavior to dexterity
content types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires mock plone.app.dexterity plone.app.testing

%description tests
collective.behavior.stock provides stock related behavior to dexterity
content types.

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
%python_sitelibdir/collective/behavior/stock
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/behavior/stock/tests

%files tests
%python_sitelibdir/collective/behavior/stock/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20131028
- Initial build for Sisyphus

