%define oname zope.app.securitypolicy

%def_with python3

Name: python-module-%oname
Version: 3.6.1
Release: alt4.1
Summary: ZMI-based management views for zope.securitypolicy
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.securitypolicy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app zope.annotation zope.app.authentication
%py_requires zope.app.form zope.app.security zope.browser zope.component
%py_requires zope.configuration zope.exceptions zope.i18n
%py_requires zope.i18nmessageid zope.interface zope.location zope.schema
%py_requires zope.security zope.securitypolicy

%description
This package provides management views for zope.securitypolicy. It's
intended to be used within the "ZMI-based" browser interface.

It used to contain a security policy implementation ages ago, but the
implementation was moved to the UI-independent zope.securitypolicy
package.

%package -n python3-module-%oname
Summary: ZMI-based management views for zope.securitypolicy
Group: Development/Python3
%py3_requires zope.app zope.annotation zope.app.authentication
%py3_requires zope.app.form zope.app.security zope.browser zope.component
%py3_requires zope.configuration zope.exceptions zope.i18n
%py3_requires zope.i18nmessageid zope.interface zope.location zope.schema
%py3_requires zope.security zope.securitypolicy

%description -n python3-module-%oname
This package provides management views for zope.securitypolicy. It's
intended to be used within the "ZMI-based" browser interface.

It used to contain a security policy implementation ages ago, but the
implementation was moved to the UI-independent zope.securitypolicy
package.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.securitypolicy
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles zope.login
%py3_requires zope.publisher zope.testing 

%description -n python3-module-%oname-tests
This package provides management views for zope.securitypolicy. It's
intended to be used within the "ZMI-based" browser interface.

It used to contain a security policy implementation ages ago, but the
implementation was moved to the UI-independent zope.securitypolicy
package.

This package contains tests for zope.app.securitypolicy.

%package tests
Summary: Tests for zope.app.securitypolicy
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.login
%py_requires zope.publisher zope.testing 

%description tests
This package provides management views for zope.securitypolicy. It's
intended to be used within the "ZMI-based" browser interface.

It used to contain a security policy implementation ages ago, but the
implementation was moved to the UI-independent zope.securitypolicy
package.

This package contains tests for zope.app.securitypolicy.

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
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.1-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Moved all tests into tests package

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

