%define oname z3c.authviewlet
Name: python-module-%oname
Version: 0.8.0
Release: alt2.1
Summary: Authentication viewlet for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.authviewlet
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.layer.pagelet zope.authentication zope.component
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.viewlet

%description
This package provides an authentication viewlet implementation for
Zope3.

%package tests
Summary: Tests for Authentication viewlet for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.layer.pagelet zope.app.authentication zope.app.testing
%py_requires zope.testbrowser zope.testing

%description tests
This package provides an authentication viewlet implementation for
Zope3.

This package contains tests for Authentication viewlet for Zope3.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus

