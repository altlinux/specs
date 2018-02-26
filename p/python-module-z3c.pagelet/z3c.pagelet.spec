%define oname z3c.pagelet
Name: python-module-%oname
Version: 1.3.0
Release: alt1
Summary: Pagelets are way to specify a template without the O-wrap
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.pagelet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.template z3c.ptcompat zope.browserpage zope.component
%py_requires zope.configuration zope.contentprovider zope.interface
%py_requires zope.publisher zope.schema zope.security

%description
Pagelets are Zope 3 UI components. In particular they allow the
developer to specify content templates without worrying about the UI
O-wrap.

%package tests
Summary: Tests for z3c.pagelet
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.form zope.testing zope.traversing
%py_requires lxml z3c.pt z3c.ptcompat zope.formlib

%description tests
Pagelets are Zope 3 UI components. In particular they allow the
developer to specify content templates without worrying about the UI
O-wrap.

This package contains tests for z3c.pagelet.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

