%define oname z3c.pt.compat
Name: python-module-%oname
Version: 0.3
Release: alt2.1
Summary: Compatibility-layer for Zope Page Template engines
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.pt.compat/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.pt

%description
This package implements a compatibility-layer between the following Zope
Page Template engines:

* z3c.pt
* zope.pagetemplate

%package tests
Summary: Tests for z3c.pt.compat
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package implements a compatibility-layer between the following Zope
Page Template engines:

* z3c.pt
* zope.pagetemplate

This package contains tests for z3c.pt.compat.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

