%define oname zope.app.securitypolicy
Name: python-module-%oname
Version: 3.6.1
Release: alt3.1
Summary: ZMI-based management views for zope.securitypolicy
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.securitypolicy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.annotation zope.app.authentication
%py_requires zope.app.form zope.app.security zope.browser zope.component
%py_requires zope.configuration zope.exceptions zope.i18n
%py_requires zope.i18nmessageid zope.interface zope.location zope.schema
%py_requires zope.security zope.securitypolicy

%description
This package provides management views for zope.securitypolicy. It's
intended to be used within the "ZMI-based" browser interface.

It used to contain a security policy implementation ages ago, but the
implementation was moved to the UI-independent zope.securitypolicy
package.

%package tests
Summary: Tests for zope.app.securitypolicy
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.login
%py_requires zope.publisher zope.testing 

%description tests
This package provides management views for zope.securitypolicy. It's
intended to be used within the "ZMI-based" browser interface.

It used to contain a security policy implementation ages ago, but the
implementation was moved to the UI-independent zope.securitypolicy
package.

This package contains tests for zope.app.securitypolicy.

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
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Moved all tests into tests package

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

