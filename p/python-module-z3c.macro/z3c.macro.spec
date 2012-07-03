%define oname z3c.macro
Name: python-module-%oname
Version: 1.4.1
Release: alt1
Summary: Simpler definition of ZPT macros
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.macro/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.configuration zope.interface
%py_requires zope.pagetemplate zope.publisher zope.schema zope.tales
%py_requires z3c.ptcompat

%description
This package provides an adapter and a TALES expression for a more
explicit and more flexible macro handling using the adapter registry for
macros.

%package tests
Summary: Tests for Simpler definition of ZPT macros
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.template z3c.pt lxml zope.browserpage zope.app.testing
%py_requires zope.testing

%description tests
This package provides an adapter and a TALES expression for a more
explicit and more flexible macro handling using the adapter registry for
macros.

This package contains tests for Simpler definition of ZPT macros.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Version 1.4.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

