%define oname zope.login

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt3.1
Summary: Login helpers for zope.publisher / authentication
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.login/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.authentication zope.component zope.interface
%py_requires zope.publisher

%description
This package provides a login helpers for zope.publisher based on the
concepts of zope.authentication.

%package -n python3-module-%oname
Summary: Login helpers for zope.publisher / authentication
Group: Development/Python3
%py3_requires zope zope.authentication zope.component zope.interface
%py3_requires zope.publisher

%description -n python3-module-%oname
This package provides a login helpers for zope.publisher based on the
concepts of zope.authentication.

%package -n python3-module-%oname-tests
Summary: Tests for zope.login
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides a login helpers for zope.publisher based on the
concepts of zope.authentication.

This package contains tests for zope.login.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt3
- Version 2.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

