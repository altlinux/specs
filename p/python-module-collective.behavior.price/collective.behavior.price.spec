%define mname collective.behavior
%define oname %mname.price
Name: python-module-%oname
Version: 0.4
Release: alt1.git20131028
Summary: Behavior to make content pricing
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.behavior.price/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.behavior.price.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-moneyed python-module-mock
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.behavior moneyed Products.CMFCore plone.supermodel
%py_requires plone.autoform plone.registry zope.i18nmessageid
%py_requires zope.schema zope.interface zope.component

%description
collective.behavior.price provides price related behavior to dexterity
content types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires mock plone.app.testing

%description tests
collective.behavior.price provides price related behavior to dexterity
content types.

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

install -p -m644 src/collective/behavior/__init__.py \
	%buildroot%python_sitelibdir/collective/behavior/

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/collective/behavior/price
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/behavior/price/tests

%files tests
%python_sitelibdir/collective/behavior/price/tests

%files -n python-module-%mname
%dir %python_sitelibdir/collective/behavior
%python_sitelibdir/collective/behavior/__init__.py*

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20131028
- Initial build for Sisyphus

