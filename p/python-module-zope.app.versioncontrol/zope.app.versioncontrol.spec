%define oname zope.app.versioncontrol
Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: A framework for managing multiple versions of objects within a ZODB database
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.versioncontrol/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app ZODB3 zope.datetime zope.location zope.security

%description
This package provides a framework for managing multiple versions of
objects within a ZODB database.

%package tests
Summary: Tests for zope.app.versioncontrol
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.event zope.traversing zope.annotation zope.component

%description tests
This package provides a framework for managing multiple versions of
objects within a ZODB database.

This package contains tests for zope.app.versioncontrol.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

