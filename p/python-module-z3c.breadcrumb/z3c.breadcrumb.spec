%define oname z3c.breadcrumb
Name: python-module-%oname
Version: 1.1.1
Release: alt2.1
Summary: A pluggable breadcrumbs implementation based on adapters
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.breadcrumb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.interface zope.location
%py_requires zope.publisher zope.schema zope.traversing

%description
The z3c.breadcrumb package provides base classes for breadcrumb
implementations. It allows you to write adapters for each content object
which provides it's own rules for providing the breadcrumb name, url and
selection.

%package tests
Summary: Tests for z3c.breadcrumb
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.container

%description tests
The z3c.breadcrumb package provides base classes for breadcrumb
implementations. It allows you to write adapters for each content object
which provides it's own rules for providing the breadcrumb name, url and
selection.

This package contains tests for z3c.breadcrumb.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

