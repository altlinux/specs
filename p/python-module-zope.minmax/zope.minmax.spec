%define oname zope.minmax
Name: python-module-%oname
Version: 1.1.2
Release: alt2.1
Summary: Homogeneous values favoring maximum or minimum for ZODB conflict resolution
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.minmax/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope ZODB3 zope.interface

%description
This package provides support for homogeneous values favoring maximum or
minimum for ZODB conflict resolution.

%package tests
Summary: Tests for zope.minmax
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides support for homogeneous values favoring maximum or
minimum for ZODB conflict resolution.

This package contains tests for zope.minmax.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus

