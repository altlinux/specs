%define oname zope.globalrequest
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Global way of retrieving the currently active request
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.globalrequest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope

%description
This package provides a global way to retrieve the currently active
request object in a zope-based web framework.

%package tests
Summary: Tests for zope.globalrequest
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.configuration zope.app.publisher
%py_requires zope.app.securitypolicy zope.app.testing
%py_requires zope.app.zcmlfiles zope.testbrowser

%description tests
This package provides a global way to retrieve the currently active
request object in a zope-based web framework.

This package contains tests for zope.globalrequest.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

