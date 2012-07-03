%define oname zope.app.http
Name: python-module-%oname
Version: 3.10.2
Release: alt1
Summary: HTTP Behavior for the Zope Publisher
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.http/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.interface zope.publisher zope.container
%py_requires zope.filerepresentation

%description
This package implements the simplest HTTP behavior within the Zope
Publisher. It implements all HTTP verbs as views and defines the
necessary HTTP exceptions.

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
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/tests

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt1
- Version 3.10.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.10.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt1
- Initial build for Sisyphus

