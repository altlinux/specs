%define oname zope.annotation
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: Object annotation mechanism
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.annotation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface zope.component zope.location zope.proxy ZODB3

%description
This package provides a mechanism to store additional information about
objects without need to modify object class.

%package tests
Summary: Tests for zope.annotation
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package provides a mechanism to store additional information about
objects without need to modify object class.

This package contains tests for zope.annotation.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

