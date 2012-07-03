%define oname z3c.menu.ready2go
Name: python-module-%oname
Version: 0.8.0
Release: alt2.1
Summary: A ready to go menu for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.menu.ready2go/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.template zope.browserpage zope.component
%py_requires zope.configuration zope.interface zope.proxy zope.publisher
%py_requires zope.schema zope.security zope.site zope.traversing
%py_requires zope.viewlet

%description
This package provides a ready 2 go menu implementation based on viewlets
for Zope3.

%package tests
Summary: Tests for z3c.menu.ready2go
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.testing zope.browserpage zope.app.testing
%py_requires zope.container zope.contentprovider zope.component
%py_requires zope.traversing

%description tests
This package provides a ready 2 go menu implementation based on viewlets
for Zope3.

This package contains tests for z3c.menu.ready2go.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus

