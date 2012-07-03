%define oname zope.app.localpermission
Name: python-module-%oname
Version: 3.7.2
Release: alt3.1
Summary: Local Persistent Permissions for zope.security
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.localpermission/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app ZODB3 zope.component zope.i18nmessageid
%py_requires zope.interface zope.location zope.security

%description
This package implements local persistent permissions for zope.security
that can be added and registered per site.

This is a part of "Through The Web" development pattern that is not used
much by zope community and not really supported in zope framework
anymore nowadays, so it can be considered as deprecated.

%package tests
Summary: Tests for zope.app.localpermission
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package implements local persistent permissions for zope.security
that can be added and registered per site.

This is a part of "Through The Web" development pattern that is not used
much by zope community and not really supported in zope framework
anymore nowadays, so it can be considered as deprecated.

This package contains tests for zope.app.localpermission.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.2-alt3.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt3
- Really added necessary requirements

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt1
- Initial build for Sisyphus

