# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1
%define mname j01
%define oname %mname.form
Name: python-module-%oname
Version: 1.0.1
#Release: alt1
Summary: Enhanced zope 3 form with jsonrpc, history and a lot more
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/j01.form/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools python-module-nose
BuildPreReq: python-module-p01.schema
BuildPreReq: python-module-j01.dialog
BuildPreReq: python-module-j01.jsonrpc
BuildPreReq: python-module-z3c.form-tests
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-p01.checker
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname p01.schema j01.dialog j01.jsonrpc z3c.form zope.i18n
%py_requires z3c.template zope.component zope.browserpage zope.event
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.schema zope.traversing

%description
Twitter bootstrap 3 based z3c.form and widgets for Zope3. This package
also offers the z3c.form improvements from p10.form and j01.jsonrpc.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires p01.checker zope.testing z3c.form.tests

%description tests
Twitter bootstrap 3 based z3c.form and widgets for Zope3. This package
also offers the z3c.form improvements from p10.form and j01.jsonrpc.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1
- (AUTO) subst_x86_64.

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

