%define oname z3c.rest
Name: python-module-%oname
Version: 0.4.0
Release: alt2.1
Summary: A REST Framework for Zope 3 Applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.rest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires lxml z3c.traverser zope.publisher zope.app.http

%description
This package provides a framework to build REST APIs on top of Zope 3.

%package tests
Summary: Tests for z3c.rest
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage z3c.etestbrowser zope.app.container
%py_requires zope.app.testing

%description tests
This package provides a framework to build REST APIs on top of Zope 3.

This package contains tests for z3c.rest.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

