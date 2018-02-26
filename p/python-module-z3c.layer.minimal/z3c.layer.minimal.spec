%define oname z3c.layer.minimal
Name: python-module-%oname
Version: 1.0.2
Release: alt2.1
Summary: Minimal layer setup for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.layer.minimal/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.http zope.app.publisher zope.configuration
%py_requires zope.traversing

%description
This package provides a minimal layer setup for Zope3.

%package tests
Summary: Tests for Minimal layer setup for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.securitypolicy zope.app.testing
%py_requires zope.app.zcmlfiles zope.securitypolicy zope.testbrowser

%description tests
This package provides a minimal layer setup for Zope3.

This package contains tests for Minimal layer setup for Zope3.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

