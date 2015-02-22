%define mname ztfy
%define oname %mname.baseskin

Name: python-module-%oname
Version: 0.1.0
Release: alt2
Summary: ZTFY base skin package
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.baseskin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.formui
BuildPreReq: python-module-z3c.jsonrpc
BuildPreReq: python-module-z3c.layer.pagelet
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-ztfy.base

%py_provides %oname
%py_requires %mname z3c.form z3c.formui z3c.jsonrpc z3c.layer.pagelet
%py_requires zope.component zope.i18nmessageid zope.interface ztfy.utils
%py_requires ztfy.base

%description
ZTFY.baseskin is a base package for all ZTFY's skin-related packages.

It mainly contains:

* a whole set of skin-related interfaces shared by all skins
* a base layer
* a small set of forms, buttons and viewlets interfaces, classes and
  adapters shared by all skin-related packages.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ZTFY.baseskin is a base package for all ZTFY's skin-related packages.

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
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added necessary requirements
- Enabled testing

* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

