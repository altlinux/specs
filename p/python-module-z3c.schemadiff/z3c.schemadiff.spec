%define oname z3c.schemadiff
Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: Zope Diff Tool
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.schemadiff/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface zope.schema zope.component
%py_requires zope.pagetemplate

%description
A diff tool that bridges zope.schema with difflib.

It allows you to take two objects and retrieve a field-by-field diff;
fields are chosen based on all implemented interfaces, unless explicitly
specified.

A browser view is included to easily display a diff between two objects
using difflib's HtmlDiff-class.

%package tests
Summary: Tests for Zope Diff Tool
Group: Development/Python
Requires: %name = %version-%release

%description tests
A diff tool that bridges zope.schema with difflib.

It allows you to take two objects and retrieve a field-by-field diff;
fields are chosen based on all implemented interfaces, unless explicitly
specified.

A browser view is included to easily display a diff between two objects
using difflib's HtmlDiff-class.

This package contains tests for Zope Diff Tool.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

