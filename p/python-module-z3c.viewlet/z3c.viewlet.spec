%define oname z3c.viewlet
Name: python-module-%oname
Version: 1.1.0
Release: alt1.1
Summary: DEPRECATED: Collection of Viewlet Extensions
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.viewlet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c zope.viewlet zope.deferredimport

%description
This package is deprecated. All its functionality moved to zope.viewlet.

%package tests
Summary: Tests for z3c.viewlet
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package is deprecated. All its functionality moved to zope.viewlet.

This package contains tests for z3c.viewlet.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

