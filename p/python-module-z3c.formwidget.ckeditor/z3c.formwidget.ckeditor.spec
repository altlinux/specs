%define oname z3c.formwidget.ckeditor
Name: python-module-%oname
Version: 1.1.0
Release: alt3.1
Summary: A CKEditor widget for text fields using z3c.form
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.formwidget.ckeditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.formwidget simplejson z3c.form zope.viewlet

%description
This package provides a CKEditor widget for the z3c.form library. It
also provides a RichText schema field, which makes the usage of CKEditor
completely transparent.

%package tests
Summary: Tests for z3c.formwidget.ckeditor
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing z3c.coverage z3c.form

%description tests
This package provides a CKEditor widget for the z3c.form library. It
also provides a RichText schema field, which makes the usage of CKEditor
completely transparent.

This package contains tests for z3c.formwidget.ckeditor.

%package -n python-module-z3c.formwidget
Summary: Core package for z3c.formwidget
Group: Development/Python

%description -n python-module-z3c.formwidget
Core package for z3c.formwidget.

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

touch %buildroot%python_sitelibdir/z3c/formwidget/__init__.py

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/z3c/formwidget/__init__.py*
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%files -n python-module-z3c.formwidget
%python_sitelibdir/z3c/formwidget/__init__.py*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Fixed requirements

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

