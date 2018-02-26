%define oname z3c.etestbrowser
Name: python-module-%oname
Version: 2.0.0
Release: alt1
Summary: Extensions for zope.testbrowser
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.etestbrowser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires lxml zope.testbrowser zope.app.wsgi

%description
This package is intended to provide extended versions of the Zope 3
testbrowser. Especially those extensions that introduce dependencies to
more external products, like lxml.

%package tests
Summary: Tests for Extensions for zope.testbrowser
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles
%py_requires zope.app.securitypolicy zope.app.server zope.testbrowser

%description tests
This package is intended to provide extended versions of the Zope 3
testbrowser. Especially those extensions that introduce dependencies to
more external products, like lxml.

This package contains tests for Extensions for zope.testbrowser.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Added necessary requirements
- Excludes *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus

