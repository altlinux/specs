%define oname zope.securitypolicy
Name: python-module-%oname
Version: 3.7.0
Release: alt2.1
Summary: Default security policy for Zope3
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.securitypolicy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

Requires: python-module-zope.i18nmessageid
%py_requires ZODB3 zope.annotation zope.authentication zope.component
%py_requires zope.configuration zope.interface zope.location
%py_requires zope.schema zope.security

%description
This package provides an useful security policy for Zope3. It's the
default security policy used in "zope3 the application" and many other
zope-based projects.

%package tests
Summary: Tests for Default security policy for Zope3
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides an useful security policy for Zope3. It's the
default security policy used in "zope3 the application" and many other
zope-based projects.

This package contains tests for Default security policy for Zope3.

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
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

