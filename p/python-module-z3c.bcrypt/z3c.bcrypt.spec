%define oname z3c.bcrypt
Name: python-module-%oname
Version: 1.1
Release: alt2.1
Summary: Password manager utility using bcrypt or pbkdf2 encoding. Useful with zope.password
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.bcrypt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires cryptacular zope.interface zope.password

%description
z3c.bcrypt provides zope.password compatible "password manager"
utilities that use bcrypt (or alternatively pbkdf2) encoding for storing
passwords.

Both encoding schemes are implemented in the cryptacular library that is
a dependency for this pacakge.

%package tests
Summary: Tests for z3c.bcrypt
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
z3c.bcrypt provides zope.password compatible "password manager"
utilities that use bcrypt (or alternatively pbkdf2) encoding for storing
passwords.

Both encoding schemes are implemented in the cryptacular library that is
a dependency for this pacakge.

aThis package contains tests for z3c.bcrypt.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

