%define oname z3c.listjs
Name: python-module-%oname
Version: 1.0b1
Release: alt2.1
Summary: A formlib list widget that uses Javascript
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.listjs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.schema zope.app.form grokcore.component
%py_requires hurry.resource

%description
z3c.listjs contains a widget called ListJsWidget that is a drop-in
replacement for the zope.app.form.browser.ListSequenceWidget. It allows
users to add and remove list items without the need for server
interaction, using Javascript.

Note: This package only works with zope.formlib (zope.app.form) and is
not compatible with z3c.form.

%package tests
Summary: Tests for z3c.listjs
Group: Development/Python
Requires: %name = %version-%release

%description tests
z3c.listjs contains a widget called ListJsWidget that is a drop-in
replacement for the zope.app.form.browser.ListSequenceWidget. It allows
users to add and remove list items without the need for server
interaction, using Javascript.

Note: This package only works with zope.formlib (zope.app.form) and is
not compatible with z3c.form.

This package contains tests for z3c.listjs.

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
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1
- Initial build for Sisyphus

