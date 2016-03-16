%define oname zope.app.security

%def_with python3

Name: python-module-%oname
Version: 3.7.5
Release: alt4.1
Summary: ZMI Views For Zope3 Security Components
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.security/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app.localpermission zope.app.pagetemplate zope.login
%py_requires zope.app.publisher zope.authentication zope.i18n zope.app
%py_requires zope.i18nmessageid zope.interface zope.principalregistry
%py_requires zope.publisher zope.security zope.securitypolicy

%description
This package provides ZMI browser views for Zope security components.

It used to provide a large part of security functionality for Zope 3,
but it was factored out from this package to several little packages to
reduce dependencies and improve reusability.

%package -n python3-module-%oname
Summary: ZMI Views For Zope3 Security Components
Group: Development/Python3
%py3_requires zope.app.localpermission zope.app.pagetemplate zope.login
%py3_requires zope.app.publisher zope.authentication zope.i18n zope.app
%py3_requires zope.i18nmessageid zope.interface zope.principalregistry
%py3_requires zope.publisher zope.security zope.securitypolicy

%description -n python3-module-%oname
This package provides ZMI browser views for Zope security components.

It used to provide a large part of security functionality for Zope 3,
but it was factored out from this package to several little packages to
reduce dependencies and improve reusability.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.security
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.testing

%description -n python3-module-%oname-tests
This package provides ZMI browser views for Zope security components.

It used to provide a large part of security functionality for Zope 3,
but it was factored out from this package to several little packages to
reduce dependencies and improve reusability.

This package contains tests for zope.app.security.

%package tests
Summary: Tests for zope.app.security
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing

%description tests
This package provides ZMI browser views for Zope security components.

It used to provide a large part of security functionality for Zope 3,
but it was factored out from this package to several little packages to
reduce dependencies and improve reusability.

This package contains tests for zope.app.security.

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
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests
%exclude %python3_sitelibdir/*/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%python3_sitelibdir/*/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/*/tests.*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7.5-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.5-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt1
- Initial build for Sisyphus

