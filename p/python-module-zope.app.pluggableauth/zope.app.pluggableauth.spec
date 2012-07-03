%define oname zope.app.pluggableauth
Name: python-module-%oname
Version: 3.4.0
Release: alt2.1
Summary: Pluggable Authenticatin Mechanism (Obselete)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.pluggableauth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.app.component zope.app.container
%py_requires zope.app.security zope.app.zapi zope.component
%py_requires zope.deprecation zope.interface zope.location
%py_requires zope.publisher zope.schema zope.traversing

%description
This package provides the original implementation of the pluggable
authentication utility. It has been superceded by
zope.app.authentication.

%package tests
Summary: Tests for zope.app.pluggableauth 
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package provides the original implementation of the pluggable
authentication utility. It has been superceded by
zope.app.authentication.

This package contains tests for zope.app.pluggableauth.

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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

