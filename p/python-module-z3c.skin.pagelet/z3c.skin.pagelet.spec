%define oname z3c.skin.pagelet
Name: python-module-%oname
Version: 1.0.2
Release: alt2.1
Summary: A base skin for pagelet-based UIs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.skin.pagelet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.component zope.app.pagetemplate zope.app.publisher
%py_requires zope.app.container zope.app.securitypolicy zope.app.testing
%py_requires zope.app.twisted zope.app.zapi zope.contentprovider
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.schema
%py_requires zope.security zope.testing zope.traversing zope.viewlet
%py_requires z3c.i18n z3c.layer z3c.macro z3c.macroviewlet
%py_requires z3c.pagelet z3c.template z3c.viewlet z3c.zrtresource
%py_requires z3c.menu.simple

%description
This package provides a base skin for people wanting to develop
pagelet-based applications.

%package tests
Summary: Tests for a base skin for pagelet-based UIs
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage z3c.etestbrowser zope.app.testing

%description tests
This package provides a base skin for people wanting to develop
pagelet-based applications.

This package contains tests for a base skin for pagelet-based UIs.

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

touch %buildroot%python_sitelibdir/z3c/skin/__init__.py

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

