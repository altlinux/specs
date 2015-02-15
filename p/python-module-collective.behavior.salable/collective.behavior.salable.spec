%define mname collective.behavior
%define oname %mname.salable
Name: python-module-%oname
Version: 0.5
Release: alt1.git20131028
Summary: Behavior to make content salable
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.behavior.salable/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.behavior.salable.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-mock
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-Products.ZCatalog

%py_provides %oname
%py_requires %mname plone.behavior Products.CMFCore plone.supermodel
%py_requires plone.autoform zope.i18nmessageid zope.schema
%py_requires zope.interface

%description
collective.behavior.salable provides behavior to switch dexterity
content types salable.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires mock plone.app.testing Products.PluginIndexes

%description tests
collective.behavior.salable provides behavior to switch dexterity
content types salable.

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
%python_sitelibdir/collective/behavior/salable
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/behavior/salable/tests

%files tests
%python_sitelibdir/collective/behavior/salable/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20131028
- Initial build for Sisyphus

