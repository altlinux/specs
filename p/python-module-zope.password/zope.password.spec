%define oname zope.password
Name: python-module-%oname
Version: 3.6.1
Release: alt2.1
Summary: Password encoding and checking utilities
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.password/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.component zope.configuration zope.interface

%description
This package provides a password manager mechanism. Password manager is
an utility object that can encode and check encoded passwords.

%package tests
Summary: Tests for zope.password
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.schema

%description tests
This package provides a password manager mechanism. Password manager is
an utility object that can encode and check encoded passwords.

This package contains tests for zope.password.

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

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

