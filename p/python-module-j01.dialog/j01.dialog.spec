# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1
%define mname j01
%define oname %mname.dialog
Name: python-module-%oname
Version: 1.0.0
#Release: alt1
Summary: Dialog box based on JQuery for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/j01.dialog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools python-module-nose
BuildPreReq: python-module-j01.jsonrpc
BuildPreReq: python-module-z3c.jsonrpc-tests
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-p01.checker
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-z3c.form-tests

%py_provides %oname
%py_requires %mname j01.jsonrpc z3c.jsonrpc z3c.template zope.interface
%py_requires zope.publisher

%description
This package provides an Zope3 javascript dialog box built with the
JQuery javascript library for display common browser pages.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires p01.checker zope.testing z3c.form.tests z3c.jsonrpc.tests

%description tests
This package provides an Zope3 javascript dialog box built with the
JQuery javascript library for display common browser pages.

This package contains tests for %oname.

%prep
%setup

sed -i 's|\r||' $(find src -name '*.txt')

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
nosetests -v

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.1
- (AUTO) subst_x86_64.

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

