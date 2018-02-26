%define oname zope.app.authentication
Name: python-module-%oname
Version: 3.9
Release: alt2.1
Summary: Principals and groups management for the pluggable authentication utility
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.authentication/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app ZODB3 zope.authentication zope.component
%py_requires zope.container zope.dublincore zope.event zope.exceptions
%py_requires zope.formlib zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.location zope.password zope.pluggableauth zope.schema
%py_requires zope.security zope.traversing zope.app.container
%py_requires zope.app.component

%description
This package provides a flexible and pluggable authentication utility
for Zope 3, using zope.pluggableauth. Several common plugins are provided.

%package tests
Summary: Tests for zope.app.authentication
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.securitypolicy zope.app.zcmlfiles
%py_requires zope.securitypolicy zope.testbrowser zope.publisher
%py_requires zope.testing zope.session zope.formlib zope.publisher
%py_requires zope.site zope.login

%description tests
This package provides a flexible and pluggable authentication utility
for Zope 3, using zope.pluggableauth. Several common plugins are provided.

This package contains tests for zope.app.authentication.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9-alt1
- Initial build for Sisyphus

