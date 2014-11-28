%define oname Products.DataGridField
Name: python-module-%oname
Version: 1.9.1
Release: alt1.git20141014
Summary: A table input component for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.DataGridField/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.DataGridField.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFTestCase
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes-tests
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.Archetypes Products.validation
%py_requires Products.CMFPlone zope.i18n zope.interface
%py_requires zope.i18nmessageid

%description
A table input component for the Plone Archetypes framework. Uses
JavaScript to make entering tabular data more user friendly process -
there are no round trip HTTP requests to the server when inserting or
deleting rows.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.CMFTestCase Products.PloneTestCase zope.testing
%py_requires Products.Archetypes.tests

%description tests
A table input component for the Plone Archetypes framework. Uses
JavaScript to make entering tabular data more user friendly process -
there are no round trip HTTP requests to the server when inserting or
deleting rows.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt1.git20141014
- Initial build for Sisyphus

