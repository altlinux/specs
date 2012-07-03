%define oname zope.login
Name: python-module-%oname
Version: 1.0.0
Release: alt2.1
Summary: Login helpers for zope.publisher / authentication
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.login/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.authentication zope.component zope.interface
%py_requires zope.publisher

%description
This package provides a login helpers for zope.publisher based on the
concepts of zope.authentication.

%package tests
Summary: Tests for zope.login
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a login helpers for zope.publisher based on the
concepts of zope.authentication.

This package contains tests for zope.login.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

