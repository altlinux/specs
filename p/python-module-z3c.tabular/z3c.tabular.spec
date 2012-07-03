%define oname z3c.tabular
Name: python-module-%oname
Version: 0.6.0
Release: alt2.1
Summary: Table with form support based on z3c.form and z3c.table for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.tabular/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.form z3c.formui z3c.table z3c.template
%py_requires zope.i18nmessageid zope.interface

%description
This package provides a table implementation including form support for
Zope3 based on z3c.form and z3c.table.

%package tests
Summary: Tests for z3c.tabular
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.form z3c.macro z3c.testing zope.app.publisher
%py_requires zope.app.testing zope.browserpage zope.publisher
%py_requires zope.testing

%description tests
This package provides a table implementation including form support for
Zope3 based on z3c.form and z3c.table.

This package contains tests for z3c.tabular.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

