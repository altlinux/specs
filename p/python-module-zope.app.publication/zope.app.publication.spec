%define oname zope.app.publication

%def_with python3

Name: python-module-%oname
Version: 4.0.0
Release: alt2.a1.dev.1
Summary: Zope publication
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.publication/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.interface ZODB3 zope.authentication zope.component
%py_requires zope.error zope.browser zope.location zope.publisher
%py_requires zope.traversing zope.app

%description
Publication and traversal components.

%package -n python3-module-%oname
Summary: Zope publication
Group: Development/Python3
%py3_requires zope.interface ZODB3 zope.authentication zope.component
%py3_requires zope.error zope.browser zope.location zope.publisher
%py3_requires zope.traversing zope.app

%description -n python3-module-%oname
Publication and traversal components.

%package -n python3-module-%oname-tests
Summary: Tests for Zope publication
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.annotation zope.app.appsetup zope.app.exception
%py3_requires zope.app.http zope.app.wsgi zope.applicationcontrol
%py3_requires zope.browserpage zope.login zope.password
%py3_requires zope.principalregistry zope.security zope.securitypolicy
%py3_requires zope.site

%description -n python3-module-%oname-tests
Publication and traversal components.

This package contains tests for Zope publication.

%package tests
Summary: Tests for Zope publication
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.annotation zope.app.appsetup zope.app.exception
%py_requires zope.app.http zope.app.wsgi zope.applicationcontrol
%py_requires zope.browserpage zope.login zope.password
%py_requires zope.principalregistry zope.security zope.securitypolicy
%py_requires zope.site

%description tests
Publication and traversal components.

This package contains tests for Zope publication.

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

%files tests
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%python3_sitelibdir/*/*/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt2.a1.dev.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1.dev
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1.dev
- Version 4.0.0a1.dev

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt1
- Version 3.13.2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.13.1-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.1-alt3
- Add necessary requirements

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.1-alt2
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.1-alt1
- Initial build for Sisyphus

