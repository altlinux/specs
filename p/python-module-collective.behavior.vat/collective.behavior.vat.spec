%define mname collective.behavior
%define oname %mname.vat
Name: python-module-%oname
Version: 0.5
Release: alt1.git20131028
Summary: Adds VAT field to dexterity content type
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.behavior.vat/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.behavior.vat.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-hexagonit.testing
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname plone.behavior Products.CMFCore plone.supermodel
%py_requires plone.registry plone.autoform zope.i18nmessageid
%py_requires zope.interface zope.schema zope.component

%description
collective.behavior.vat provides VAT related behavior to dexterity
content types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires hexagonit.testing plone.app.dexterity plone.app.testing
%py_requires zope.testing

%description tests
collective.behavior.vat provides VAT related behavior to dexterity
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
%python_sitelibdir/collective/behavior/vat
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/behavior/vat/tests

%files tests
%python_sitelibdir/collective/behavior/vat/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20131028
- Initial build for Sisyphus

