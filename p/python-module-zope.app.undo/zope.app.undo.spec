%define oname zope.app.undo
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: Transaction Undo API and UI
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.undo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.app.security zope.component zope.interface
%py_requires zope.location zope.publisher zope.security zope.traversing

%description
This package implements transaction undo capabilities in Zope 3
applications and specifically the Zope 3 ZMI.

%package tests
Summary: Tests for zope.app.undo
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.component zope.site zope.testing

%description tests
This package implements transaction undo capabilities in Zope 3
applications and specifically the Zope 3 ZMI.

This package contains tests for zope.app.undo.

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
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

