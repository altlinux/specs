%define oname z3c.formui
Name: python-module-%oname
Version: 2.2.0
Release: alt2.1
Summary: A set of initial UI components for z3c.form
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.formui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.form z3c.macro z3c.template zope.component
%py_requires zope.publisher zope.viewlet

%description
This package provides a set of default layouts for the z3c.form
framework. In particular it provides a DIV-based and a TABLE-based
layout. The developer can use either layout by inheriting from a
different base layer.

The package also has some support for layout/pagelet templates.

%package tests
Summary: Tests for z3c.formui
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing z3c.form

%description tests
This package provides a set of default layouts for the z3c.form
framework. In particular it provides a DIV-based and a TABLE-based
layout. The developer can use either layout by inheriting from a
different base layer.

The package also has some support for layout/pagelet templates.

This package contains tests for z3c.formui.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus

