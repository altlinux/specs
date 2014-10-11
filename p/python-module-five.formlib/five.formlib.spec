%define oname five.formlib
Name: python-module-%oname
Version: 1.0.4
Release: alt1
Summary: zope.formlib integration for Zope 2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/five.formlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-transaction python-module-zope.app.form
BuildPreReq: python-module-zope.browser python-module-zope.component
BuildPreReq: python-module-zope.event python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid python-module-docutils
BuildPreReq: python-module-zope.interface python-module-zope.location
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.publisher python-module-zope.schema
BuildPreReq: python-module-ExtensionClass

%py_provides %oname
Requires: python-module-Zope2
%py_requires five zope.app.form zope.browser zope.component zope.event
%py_requires zope.formlib zope.i18nmessageid zope.interface zope.schema
%py_requires zope.lifecycleevent zope.location zope.publisher
%py_requires ExtensionClass

%description
five.formlib provides integration of the zope.formlib and zope.app.form
packages into the Zope2 application server.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
five.formlib provides integration of the zope.formlib and zope.app.form
packages into the Zope2 application server.

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
%doc *.txt
%python_sitelibdir/five/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/five/*/tests

%files tests
%python_sitelibdir/five/*/tests

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus

