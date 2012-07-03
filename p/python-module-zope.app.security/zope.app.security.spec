%define oname zope.app.security
Name: python-module-%oname
Version: 3.7.5
Release: alt3.1
Summary: ZMI Views For Zope3 Security Components
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.security/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.localpermission zope.app.pagetemplate zope.login
%py_requires zope.app.publisher zope.authentication zope.i18n zope.app
%py_requires zope.i18nmessageid zope.interface zope.principalregistry
%py_requires zope.publisher zope.security zope.securitypolicy

%description
This package provides ZMI browser views for Zope security components.

It used to provide a large part of security functionality for Zope 3,
but it was factored out from this package to several little packages to
reduce dependencies and improve reusability.

%package tests
Summary: Tests for zope.app.security
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing

%description tests
This package provides ZMI browser views for Zope security components.

It used to provide a large part of security functionality for Zope 3,
but it was factored out from this package to several little packages to
reduce dependencies and improve reusability.

This package contains tests for zope.app.security.

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
%exclude %python_sitelibdir/*/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.5-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt1
- Initial build for Sisyphus

