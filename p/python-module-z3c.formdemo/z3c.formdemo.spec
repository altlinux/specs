%define oname z3c.formdemo
Name: python-module-%oname
Version: 2.1.1
Release: alt2.1
Summary: A set of demo applications for z3c.form and z3c.formui
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.formdemo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.csvvocabulary z3c.form z3c.formui z3c.layer.pagelet
%py_requires z3c.pagelet z3c.template z3c.zrtresource zc.resourcelibrary
%py_requires zc.table zope.annotation zope.app.container zope.app.folder
%py_requires zope.app.pagetemplate zope.app.session zope.component
%py_requires zope.interface zope.location zope.pagetemplate
%py_requires zope.publisher zope.rdb zope.schema zope.traversing
%py_requires zope.viewlet

%description
This package contains several small demo applications for the z3c.form
and z3c.formui packages.

* TABLE- versus DIV-based layout of all widgets.
* A simple Hello World message application demonstrating the easiest way
  to write add, edit and display forms.
* A simple calculator showing the flexibility of the new action
  declaration framework by declaring different classes of buttons.
* A linear wizard shows off the sub-form capabilities of z3c.form. It
  also demonstrates how one can overcome the short-coming of an object
  widget.
* A simple table/spreadsheet that allows adding and editing as simple
  content object. This demo also shows the usage of forms and zc.table
  at the same time.

%package tests
Summary: Tests for z3c.formdemo
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage z3c.etestbrowser zope.app.testing

%description tests
This package contains several small demo applications for the z3c.form
and z3c.formui packages.

This package contains tests for z3c.formdemo.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus

