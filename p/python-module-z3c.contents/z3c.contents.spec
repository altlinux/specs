%define oname z3c.contents
Name: python-module-%oname
Version: 0.6.0
Release: alt3.1
Summary: Container management page based on z3c.form and z3c.table for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.contents/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.form z3c.formui z3c.table z3c.template
%py_requires zope.annotation zope.component zope.container
%py_requires zope.copypastemove zope.exceptions zope.i18n
%py_requires zope.i18nmessageid zope.index zope.interface zope.publisher
%py_requires zope.schema zope.security zope.traversing

%description
This package provides a contents.html page replacement for Zope3 based
on z3c.form and z3c.table.

%package tests
Summary: Tests for z3c.contents
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.macro z3c.layer.ready2go z3c.macro z3c.table
%py_requires z3c.etestbrowser zope.app.component zope.app.pagetemplate
%py_requires zope.app.securitypolicy zope.app.testing zope.testing

%description tests
This package provides a contents.html page replacement for Zope3 based
on z3c.form and z3c.table.

This package contains tests for z3c.contents.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt3
- Removed setuptools from requirements

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

