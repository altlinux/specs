%define oname zope.app.http

%def_with python3

Name: python-module-%oname
Version: 4.0.0
Release: alt2.a1.dev.1
Summary: HTTP Behavior for the Zope Publisher
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.http/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app zope.interface zope.publisher zope.container
%py_requires zope.filerepresentation

%description
This package implements the simplest HTTP behavior within the Zope
Publisher. It implements all HTTP verbs as views and defines the
necessary HTTP exceptions.

%package -n python3-module-%oname
Summary: HTTP Behavior for the Zope Publisher
Group: Development/Python3
%py3_requires zope.app zope.interface zope.publisher zope.container
%py3_requires zope.filerepresentation

%description -n python3-module-%oname
This package implements the simplest HTTP behavior within the Zope
Publisher. It implements all HTTP verbs as views and defines the
necessary HTTP exceptions.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.http
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles zope.app.wsgi
%py3_requires zope.securitypolicy zope.site zope.login

%description -n python3-module-%oname-tests
This package implements the simplest HTTP behavior within the Zope
Publisher. It implements all HTTP verbs as views and defines the
necessary HTTP exceptions.

This package contains tests for zope.app.http.

%package tests
Summary: Tests for zope.app.http
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.app.wsgi
%py_requires zope.securitypolicy zope.site zope.login

%description tests
This package implements the simplest HTTP behavior within the Zope
Publisher. It implements all HTTP verbs as views and defines the
necessary HTTP exceptions.

This package contains tests for zope.app.http.

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
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests
%exclude %python3_sitelibdir/*/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%python3_sitelibdir/*/*/*/*/tests
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt2.a1.dev.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1.dev
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1.dev
- Version 4.0.0a1.dev

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt1
- Version 3.10.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.10.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt1
- Initial build for Sisyphus

