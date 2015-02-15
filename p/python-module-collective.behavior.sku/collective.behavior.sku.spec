%define mname collective.behavior
%define oname %mname.sku
Name: python-module-%oname
Version: 0.4
Release: alt1.git20140213
Summary: Behavior to add sku field
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.behavior.sku/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.behavior.sku.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-hexagonit.testing
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-z3c.form

%py_provides %oname
%py_requires %mname plone.behavior plone.supermodel plone.autoform
%py_requires zope.i18nmessageid zope.schema zope.interface

%description
collective.behavior.sku provides behavior add SKU field to dexterity
content types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires hexagonit.testing plone.app.dexterity Products.ZCatalog
%py_requires Products.CMFCore plone.dexterity plone.app.testing z3c.form
%py_requires zope.testing zope.lifecycleevent

%description tests
collective.behavior.sku provides behavior add SKU field to dexterity
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
%python_sitelibdir/collective/behavior/sku
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/behavior/sku/tests

%files tests
%python_sitelibdir/collective/behavior/sku/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140213
- Initial build for Sisyphus

