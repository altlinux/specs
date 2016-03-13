%define oname z3c.image

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt3.1
Summary: Image utils for zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.image/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app.cache zope.app.file zope.cachedescriptors
%py_requires zope.datetime zope.dublincore zope.interface zope.publisher
%py_requires zope.security

%description
Image utils for zope3.

%package -n python3-module-%oname
Summary: Image utils for zope3
Group: Development/Python3
%py3_requires zope.app.cache zope.app.file zope.cachedescriptors
%py3_requires zope.datetime zope.dublincore zope.interface zope.publisher
%py3_requires zope.security

%description -n python3-module-%oname
Image utils for zope3.

%package -n python3-module-%oname-tests
Summary: Tests for Image utils for zope3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%add_python3_req_skip adapter
%py3_requires zope.app.testing zope.app.server zope.app.authentication
%py3_requires zope.app.securitypolicy zope.app.zcmlfiles
%py3_requires zope.lifecycleevent zope.testbrowser zope.testing

%description -n python3-module-%oname-tests
Image utils for zope3.

This package contains tests for Image utils for zope3.

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
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

