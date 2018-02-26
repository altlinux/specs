%define oname zope.authentication
Name: python-module-%oname
Version: 3.7.1
Release: alt2.1
Summary: Definition of authentication basics for the Zope Framework
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.authentication/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.browser zope.component zope.i18nmessageid
%py_requires zope.interface zope.schema zope.security

%description
This package provides a definition of authentication concepts for use in
Zope Framework.

%package tests
Summary: Tests for zope.authentication
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a definition of authentication concepts for use in
Zope Framework.

This package contains tests for zope.authentication.

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

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Initial build for Sisyphus

