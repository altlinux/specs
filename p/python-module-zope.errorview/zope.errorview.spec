%define oname zope.errorview
Name: python-module-%oname
Version: 0.11
Release: alt1
Summary: Basic HTTP and Browser exception views
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.errorview/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.interface zope.publisher zope.security

%description
Provides basic HTTP and Browser views for common exceptions.

%package tests
Summary: Tests for zope.errorview
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Provides basic HTTP and Browser views for common exceptions.

This package contains tests for zope.errorview.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Version 0.11

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1
- Initial build for Sisyphus

