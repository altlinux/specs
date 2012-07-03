%define oname z3c.menu.simple
Name: python-module-%oname
Version: 0.6.0
Release: alt2.1
Summary: A simple menu system for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.menu.simple/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.i18n zope.app.component zope.browserpage zope.schema
%py_requires zope.traversing zope.viewlet

%description
This package provides a simple menu implementation based on viewlets.

%package tests
Summary: Tests for A simple menu system for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testbrowser zope.component zope.app.testing z3c.testing

%description tests
This package provides a simple menu implementation based on viewlets.

This package contains tests for A simple menu system for Zope3.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

