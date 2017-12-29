%define oname z3c.formdemo

%def_without python3

Name: python-module-%oname
Version: 2.1.1
Release: alt4
Summary: A set of demo applications for z3c.form and z3c.formui
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.formdemo/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python-tools-2to3
%endif

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

%if_with python3
%package -n python3-module-%oname
Summary: A set of demo applications for z3c.form and z3c.formui
Group: Development/Python3
%py3_requires z3c.csvvocabulary z3c.form z3c.formui z3c.layer.pagelet
%py3_requires z3c.pagelet z3c.template z3c.zrtresource zc.resourcelibrary
%py3_requires zc.table zope.annotation zope.app.container zope.app.folder
%py3_requires zope.app.pagetemplate zope.app.session zope.component
%py3_requires zope.interface zope.location zope.pagetemplate
%py3_requires zope.publisher zope.rdb zope.schema zope.traversing
%py3_requires zope.viewlet

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for z3c.formdemo
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.coverage z3c.etestbrowser zope.app.testing

%description -n python3-module-%oname-tests
This package contains several small demo applications for the z3c.form
and z3c.formui packages.

This package contains tests for z3c.formdemo.
%endif

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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Fri Dec 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt4
- Rebuilt without python-3.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus

