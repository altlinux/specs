%define oname zope.app.dav

%def_with python3

Name: python-module-%oname
Version: 3.5.3
Release: alt3.1
Summary: Zope WebDAV Support (Basic)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.dav/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires ZODB3 zope.annotation zope.container zope.app.file
%py_requires zope.app.form zope.component zope.configuration
%py_requires zope.dublincore zope.event zope.filerepresentation
%py_requires zope.interface zope.lifecycleevent zope.location
%py_requires zope.pagetemplate zope.publisher zope.schema zope.site
%py_requires zope.size zope.traversing

%description
This package provides basic WebDAV support for a Zope application. A
more advanced implementation is available in z3c.dav.

%package -n python3-module-%oname
Summary: Zope WebDAV Support (Basic)
Group: Development/Python3
%py3_requires ZODB3 zope.annotation zope.container zope.app.file
%py3_requires zope.app.form zope.component zope.configuration
%py3_requires zope.dublincore zope.event zope.filerepresentation
%py3_requires zope.interface zope.lifecycleevent zope.location
%py3_requires zope.pagetemplate zope.publisher zope.schema zope.site
%py3_requires zope.size zope.traversing

%description -n python3-module-%oname
This package provides basic WebDAV support for a Zope application. A
more advanced implementation is available in z3c.dav.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.dav
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.securitypolicy
%py3_requires zope.app.zcmlfiles zope.login

%description -n python3-module-%oname-tests
This package provides basic WebDAV support for a Zope application. A
more advanced implementation is available in z3c.dav.

This package contains tests for zope.app.dav.

%package tests
Summary: Tests for zope.app.dav
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.securitypolicy
%py_requires zope.app.zcmlfiles zope.login

%description tests
This package provides basic WebDAV support for a Zope application. A
more advanced implementation is available in z3c.dav.

This package contains tests for zope.app.dav.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.3-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus

