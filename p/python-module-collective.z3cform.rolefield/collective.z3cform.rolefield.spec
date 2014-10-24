%define mname collective.z3cform
%define oname %mname.rolefield
Name: python-module-%oname
Version: 0.4
Release: alt1.dev0.git20140214
Summary: A field for managing local roles
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.z3cform.rolefield/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.z3cform.rolefield.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.schemaevent
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-mock
BuildPreReq: python-module-ecreall.helpers.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-openid

%py_provides %oname
%py_requires %mname zope.schemaevent plone.api

%description
A z3cform field that manage local roles. This give the ability to assign
local roles to selected element (that are by default Plone groups).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ecreall.helpers.testing plone.app.testing
%py_requires plone.app.dexterity

%description tests
A z3cform field that manage local roles. This give the ability to assign
local roles to selected element (that are by default Plone groups).

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
%doc *.rst docs/*
%python_sitelibdir/collective/z3cform/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/z3cform/*/test*
%exclude %python_sitelibdir/collective/z3cform/*/*/test*

%files tests
%python_sitelibdir/collective/z3cform/*/test*
%python_sitelibdir/collective/z3cform/*/*/test*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.dev0.git20140214
- Initial build for Sisyphus

