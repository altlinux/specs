%define oname zope.server
Name: python-module-%oname
Version: 3.8.5
Release: alt1
Summary: Zope Server (Web and FTP)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.server/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.interface zope.publisher zope.security

%description
This package contains generic base classes for channel-based servers,
the servers themselves and helper objects, such as tasks and requests.

%package tests
Summary: Tests for zope.server
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.i18n zope.component

%description tests
This package contains generic base classes for channel-based servers,
the servers themselves and helper objects, such as tasks and requests.

This package contains tests for zope.server.

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
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.5-alt1
- Version 3.8.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1
- Initial build for Sisyphus

