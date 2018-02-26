%define oname z3c.baseregistry
Name: python-module-%oname
Version: 1.3.0
Release: alt2.1
Summary: Manage IComponents instances using Python code and ZCML
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.baseregistry/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.configuration zope.i18nmessageid
%py_requires zope.interface zope.schema zope.site zope.formlib
%py_requires zope.app.zcmlfiles

%description
The purpose of this package is to define, populate and use multiple
IComponents instances using filesystem-based development -- in other
words, Python code and ZCML.

%package tests
Summary: Tests for z3c.baseregistry
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing

%description tests
The purpose of this package is to define, populate and use multiple
IComponents instances using filesystem-based development -- in other
words, Python code and ZCML.

This package contains tests for z3c.baseregistry.

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
%exclude %python_sitelibdir/*/*/*tests*
%exclude %python_sitelibdir/*/*/*/*tests*

%files tests
%python_sitelibdir/*/*/*tests*
%python_sitelibdir/*/*/*/*tests*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Added necessary requirements
- Excludes *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

