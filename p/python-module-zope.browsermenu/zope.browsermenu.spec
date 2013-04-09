%define oname zope.browsermenu
Name: python-module-%oname
Version: 4.1.0
Release: alt1.a1
Summary: Browser menu implementation for Zope
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.browsermenu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.browser zope.component zope.configuration
%py_requires zope.i18nmessageid zope.interface zope.pagetemplate
%py_requires zope.publisher zope.schema zope.security zope.traversing

%description
This package provides an implementation of browser menus and ZCML
directives for configuring them.

%package tests
Summary: Tests for zope.browsermenu
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package provides an implementation of browser menus and ZCML
directives for configuring them.

This package contains tests for zope.browsermenu.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.a1
- Version 4.1.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1
- Initial build for Sisyphus

