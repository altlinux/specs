%define oname zope.app.exception

%def_with python3

Name: python-module-%oname
Version: 3.6.3
Release: alt2.1
Summary: Zope 3 exception views
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.exception/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app zope.interface zope.publisher zope.browser
%py_requires zope.browserpage

%description
This packages provides Zope 3 browser views for some generic exceptions.

%package -n python3-module-%oname
Summary: Zope 3 exception views
Group: Development/Python3
%py3_requires zope.app zope.interface zope.publisher zope.browser
%py3_requires zope.browserpage

%description -n python3-module-%oname
This packages provides Zope 3 browser views for some generic exceptions.

%package -n python3-module-%oname-tests
Summary: Tests for Zope 3 exception views
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles zope.login
%py3_requires zope.securitypolicy

%description -n python3-module-%oname-tests
This packages provides Zope 3 browser views for some generic exceptions.

This package contains tests for Zope 3 exception views.

%package tests
Summary: Tests for Zope 3 exception views
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.login
%py_requires zope.securitypolicy

%description tests
This packages provides Zope 3 browser views for some generic exceptions.

This package contains tests for Zope 3 exception views.

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Version 3.6.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Initial build for Sisyphus

