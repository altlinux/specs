%define oname zope.file

%def_with python3

Name: python-module-%oname
Version: 0.6.2
Release: alt2.1
Summary: Efficient File Implementation for Zope Applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.file/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope ZODB3 zope.browser zope.container zope.contenttype
%py_requires zope.event zope.interface zope.publisher zope.security
%py_requires zope.mimetype

%description
The zope.file package provides a content object used to store a file.
The interface supports efficient upload and download.

%package -n python3-module-%oname
Summary: Efficient File Implementation for Zope Applications
Group: Development/Python3
%py3_requires zope ZODB3 zope.browser zope.container zope.contenttype
%py3_requires zope.event zope.interface zope.publisher zope.security
%py3_requires zope.mimetype

%description -n python3-module-%oname
The zope.file package provides a content object used to store a file.
The interface supports efficient upload and download.

%package -n python3-module-%oname-tests
Summary: Tests for zope.file
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.server zope.app.testing zope.app.zcmlfiles
%py3_requires zope.login zope.password zope.securitypolicy
%py3_requires zope.testbrowser

%description -n python3-module-%oname-tests
The zope.file package provides a content object used to store a file.
The interface supports efficient upload and download.

This package contains tests for zope.file.

%package tests
Summary: Tests for zope.file
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.server zope.app.testing zope.app.zcmlfiles
%py_requires zope.login zope.password zope.securitypolicy
%py_requires zope.testbrowser

%description tests
The zope.file package provides a content object used to store a file.
The interface supports efficient upload and download.

This package contains tests for zope.file.

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

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

