%define oname zope.pluggableauth
Name: python-module-%oname
Version: 1.3
Release: alt2.1
Summary: Pluggable Authentication Utility
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.pluggableauth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope ZODB3 zope.authentication zope.component
%py_requires zope.container zope.event zope.i18nmessageid zope.interface
%py_requires zope.password zope.publisher zope.schema zope.security
%py_requires zope.session zope.site zope.traversing

%description
Based on zope.authentication, this package provides a flexible and
pluggable authentication utility. Several common plugins are provided.

%package tests
Summary: Tests for Pluggable Authentication Utility
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.component

%description tests
Based on zope.authentication, this package provides a flexible and
pluggable authentication utility. Several common plugins are provided.

This package contains tests for Pluggable Authentication Utility.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

