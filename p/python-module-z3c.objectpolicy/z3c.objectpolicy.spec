%define oname z3c.objectpolicy
Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: objectpolicy for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.objectpolicy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.interface zope.securitypolicy
%py_requires zope.app.security

%description
The objectpolicy package makes it easy to override the default
zope.securitypolicy.zopepolicy on an object by object basis.

%package tests
Summary: Tests for objectpolicy for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage zope.app.testing zope.configuration
%py_requires zope.testing

%description tests
The objectpolicy package makes it easy to override the default
zope.securitypolicy.zopepolicy on an object by object basis.

This package contains tests for objectpolicy for Zope3.


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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

