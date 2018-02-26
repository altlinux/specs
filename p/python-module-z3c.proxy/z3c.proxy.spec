%define oname z3c.proxy
Name: python-module-%oname
Version: 0.6.1
Release: alt2.1
Summary: Container proxy implementation for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.proxy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.container zope.copypastemove zope.interface
%py_requires zope.location zope.proxy

%description
This package provides a proxy container implementation for Zope3.

%package tests
Summary: Tests for Container proxy implementation for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage z3c.testing zope.app.testing zope.testing

%description tests
This package provides a proxy container implementation for Zope3.

This package contains tests for Container proxy implementation for Zope3.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

