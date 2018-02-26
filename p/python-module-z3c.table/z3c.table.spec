%define oname z3c.table
Name: python-module-%oname
Version: 0.9.1
Release: alt1
Summary: Modular table rendering implementation for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.table/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.batching zope.component zope.contentprovider
%py_requires zope.dublincore zope.i18nmessageid zope.i18n zope.interface
%py_requires zope.location zope.schema zope.security zope.traversing

%description
This package provides a modular table rendering implementation for
Zope3.

%package tests
Summary: Tests for z3c.table
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.testing zope.app.testing zope.publisher zope.security
%py_requires zope.testing

%description tests
This package provides a modular table rendering implementation for
Zope3.

This package contains tests for z3c.table.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1
- Version 0.9.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus

