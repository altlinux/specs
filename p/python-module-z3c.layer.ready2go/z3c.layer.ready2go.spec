%define oname z3c.layer.ready2go
Name: python-module-%oname
Version: 0.6.0
Release: alt2.1
Summary: A ready to go layer for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.layer.ready2go/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.form z3c.formui z3c.layer.pagelet zope.viewlet

%description
This package provides a layer based on z3c.form and z3c.pagelet. This
layer can be used in custom skins.

%package tests
Summary: Tests for z3c.layer.ready2go
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testbrowser zope.app.authentication zope.app.testing
%py_requires zope.browserresource zope.principalregistry zope.publisher
%py_requires zope.security zope.securitypolicy zope.testing

%description tests
This package provides a layer based on z3c.form and z3c.pagelet. This
layer can be used in custom skins.

This package contains tests for z3c.layer.ready2go.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

