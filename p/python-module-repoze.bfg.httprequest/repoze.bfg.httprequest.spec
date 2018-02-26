%define oname repoze.bfg.httprequest
Name: python-module-%oname
Version: 0.4.2
Release: alt2.1
Summary: Adaptable request interfaces
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.httprequest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_provides repozehttprequestinterfaces

%py_requires repoze.bfg zope.interface zope.component zope.security
%py_requires zope.testing

%description
The motivation for this package is to encourage the use of request
type adaptation instead of depending on packages with request type
definitions.

%package tests
Summary: Tests for repoze.bfg.httprequest
Group: Development/Python
Requires: %name = %version-%release

%description tests
The motivation for this package is to encourage the use of request
type adaptation instead of depending on packages with request type
definitions.

This package contains tests for repoze.bfg.httprequest.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

