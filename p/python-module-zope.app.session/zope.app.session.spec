%define oname zope.app.session

%def_with python3

Name: python-module-%oname
Version: 3.6.2
Release: alt3.1
Summary: Zope session
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.session/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app ZODB3 zope.annotation zope.app.appsetup
%py_requires zope.app.http zope.component zope.i18nmessageid
%py_requires zope.interface zope.location zope.minmax zope.publisher
%py_requires zope.session

%description
This package provides session support.

%package -n python3-module-%oname
Summary: Zope session
Group: Development/Python3
%py3_requires zope.app ZODB3 zope.annotation zope.app.appsetup
%py3_requires zope.app.http zope.component zope.i18nmessageid
%py3_requires zope.interface zope.location zope.minmax zope.publisher
%py3_requires zope.session

%description -n python3-module-%oname
This package provides session support.

%package -n python3-module-%oname-tests
Summary: Tests for Zope session
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.site zope.app.testing zope.app.zptpage
%py3_requires zope.app.securitypolicy zope.app.zcmlfiles

%description -n python3-module-%oname-tests
This package provides session support.

This package contains tests for Zope session.

%package tests
Summary: Tests for Zope session
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.site zope.app.testing zope.app.zptpage
%py_requires zope.app.securitypolicy zope.app.zcmlfiles

%description tests
This package provides session support.

This package contains tests for Zope session.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Initial build for Sisyphus

