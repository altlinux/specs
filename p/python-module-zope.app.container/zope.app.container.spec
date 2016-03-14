%define oname zope.app.container

%def_with python3

Name: python-module-%oname
Version: 3.9.2
Release: alt2.1
Summary: Zope Container
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.container/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.browser zope.component zope.container
%py_requires zope.copypastemove zope.dublincore zope.event
%py_requires zope.exceptions zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.lifecycleevent zope.location zope.publisher
%py_requires zope.schema zope.security zope.size zope.traversing
%py_requires zope.app.publisher zope.app

%description
This package define interfaces of container components, and provides
sample container implementations such as a BTreeContainer and
OrderedContainer.

%package -n python3-module-%oname
Summary: Zope Container
Group: Development/Python3
%py3_requires zope.browser zope.component zope.container
%py3_requires zope.copypastemove zope.dublincore zope.event
%py3_requires zope.exceptions zope.i18n zope.i18nmessageid zope.interface
%py3_requires zope.lifecycleevent zope.location zope.publisher
%py3_requires zope.schema zope.security zope.size zope.traversing
%py3_requires zope.app.publisher zope.app

%description -n python3-module-%oname
This package define interfaces of container components, and provides
sample container implementations such as a BTreeContainer and
OrderedContainer.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Container
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles zope.login
%py3_requires zope.securitypolicy six

%description -n python3-module-%oname-tests
This package define interfaces of container components, and provides
sample container implementations such as a BTreeContainer and
OrderedContainer.

This package contains tests for Zope Container.

%package tests
Summary: Tests for Zope Container
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.login
%py_requires zope.securitypolicy

%description tests
This package define interfaces of container components, and provides
sample container implementations such as a BTreeContainer and
OrderedContainer.

This package contains tests for Zope Container.

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.9.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt1
- Version 3.9.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1
- Initial build for Sisyphus

