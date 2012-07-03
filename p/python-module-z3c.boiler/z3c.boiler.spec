%define oname z3c.boiler
Name: python-module-%oname
Version: 0.1.1
Release: alt2.1
Summary: A utility to help jump start Zope 3 projects
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.boiler/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.buildout z3c.builder.core z3c.feature.core
%py_requires z3c.feature.zope

%description
This package provides the ZBoiler Zope Features.

The ZBoiler package provides a small script to generate the boilerplate
of a project from a simple, high-level feature XML file.

%package tests
Summary: Tests for ZBoiler Zope Features
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing z3c.coverage

%description tests
This package provides the ZBoiler Zope Features.

The ZBoiler package provides a small script to generate the boilerplate
of a project from a simple, high-level feature XML file.

This package contains tests for ZBoiler Zope Features.

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

