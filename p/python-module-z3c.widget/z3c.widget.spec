%define oname z3c.widget
Name: python-module-%oname
Version: 0.3.0
Release: alt2.1
Summary: Additional zope.formlib Widgets
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.widget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 z3c.i18n z3c.javascript z3c.schema zc.resourcelibrary
%py_requires zope.app.cache zope.app.container zope.app.file
%py_requires zope.app.i18n zope.app.pagetemplate zope.component
%py_requires zope.event zope.filerepresentation zope.formlib zope.i18n
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.publisher zope.schema zope.security zope.traversing

%description
Additional zope.formlib Widgets.

%package tests
Summary: Tests for Additional zope.formlib Widgets
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing zope.app.securitypolicy
%py_requires zope.app.zcmlfiles zope.testbrowser

%description tests
Additional zope.formlib Widgets.

This package contains tests for Additional zope.formlib Widgets.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2
- Added necesssary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

