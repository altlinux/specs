%define oname z3c.image
Name: python-module-%oname
Version: 1.0.0
Release: alt2.1
Summary: Image utils for zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.image/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.cache zope.app.file zope.cachedescriptors
%py_requires zope.datetime zope.dublincore zope.interface zope.publisher
%py_requires zope.security

%description
Image utils for zope3.

%package tests
Summary: Tests for Image utils for zope3
Group: Development/Python
Requires: %name = %version-%release
%add_python_req_skip adapter
%py_requires zope.app.testing zope.app.server zope.app.authentication
%py_requires zope.app.securitypolicy zope.app.zcmlfiles
%py_requires zope.lifecycleevent zope.testbrowser zope.testing

%description tests
Image utils for zope3.

This package contains tests for Image utils for zope3.

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
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

