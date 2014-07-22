%define oname z3c.listjs

%def_with python3

Name: python-module-%oname
Version: 1.0b1
Release: alt3
Summary: A formlib list widget that uses Javascript
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.listjs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.schema zope.app.form grokcore.component
%py_requires hurry.resource

%description
z3c.listjs contains a widget called ListJsWidget that is a drop-in
replacement for the zope.app.form.browser.ListSequenceWidget. It allows
users to add and remove list items without the need for server
interaction, using Javascript.

Note: This package only works with zope.formlib (zope.app.form) and is
not compatible with z3c.form.

%package -n python3-module-%oname
Summary: A formlib list widget that uses Javascript
Group: Development/Python3
%py3_requires zope.schema zope.app.form grokcore.component
%py3_requires hurry.resource

%description -n python3-module-%oname
z3c.listjs contains a widget called ListJsWidget that is a drop-in
replacement for the zope.app.form.browser.ListSequenceWidget. It allows
users to add and remove list items without the need for server
interaction, using Javascript.

Note: This package only works with zope.formlib (zope.app.form) and is
not compatible with z3c.form.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.listjs
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
z3c.listjs contains a widget called ListJsWidget that is a drop-in
replacement for the zope.app.form.browser.ListSequenceWidget. It allows
users to add and remove list items without the need for server
interaction, using Javascript.

Note: This package only works with zope.formlib (zope.app.form) and is
not compatible with z3c.form.

This package contains tests for z3c.listjs.

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

%if_with python3
cp -fR . ../python3
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
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*
%endif

%changelog
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1
- Initial build for Sisyphus

