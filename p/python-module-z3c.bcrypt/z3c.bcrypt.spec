%define oname z3c.bcrypt

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt2.1
Summary: Password manager utility using bcrypt or pbkdf2 encoding. Useful with zope.password
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.bcrypt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires cryptacular zope.interface zope.password

%description
z3c.bcrypt provides zope.password compatible "password manager"
utilities that use bcrypt (or alternatively pbkdf2) encoding for storing
passwords.

Both encoding schemes are implemented in the cryptacular library that is
a dependency for this pacakge.

%package -n python3-module-%oname
Summary: Password manager utility using bcrypt or pbkdf2 encoding. Useful with zope.password
Group: Development/Python3
%py3_requires cryptacular zope.interface zope.password

%description -n python3-module-%oname
z3c.bcrypt provides zope.password compatible "password manager"
utilities that use bcrypt (or alternatively pbkdf2) encoding for storing
passwords.

Both encoding schemes are implemented in the cryptacular library that is
a dependency for this pacakge.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.bcrypt
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
z3c.bcrypt provides zope.password compatible "password manager"
utilities that use bcrypt (or alternatively pbkdf2) encoding for storing
passwords.

Both encoding schemes are implemented in the cryptacular library that is
a dependency for this pacakge.

This package contains tests for z3c.bcrypt.

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

This package contains tests for z3c.bcrypt.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

