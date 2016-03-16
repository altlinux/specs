%define oname z3c.formwidget.ckeditor

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.a1.1
Summary: A CKEditor widget for text fields using z3c.form
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.formwidget.ckeditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires simplejson z3c.form zope.viewlet
Requires: python-module-z3c.formwidget = %EVR

%description
This package provides a CKEditor widget for the z3c.form library. It
also provides a RichText schema field, which makes the usage of CKEditor
completely transparent.

%package -n python3-module-%oname
Summary: A CKEditor widget for text fields using z3c.form
Group: Development/Python3
%py3_requires simplejson z3c.form zope.viewlet
Requires: python3-module-z3c.formwidget = %EVR

%description -n python3-module-%oname
This package provides a CKEditor widget for the z3c.form library. It
also provides a RichText schema field, which makes the usage of CKEditor
completely transparent.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.formwidget.ckeditor
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing z3c.coverage z3c.form

%description -n python3-module-%oname-tests
This package provides a CKEditor widget for the z3c.form library. It
also provides a RichText schema field, which makes the usage of CKEditor
completely transparent.

This package contains tests for z3c.formwidget.ckeditor.

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

%package -n python3-module-z3c.formwidget
Summary: Core package for z3c.formwidget
Group: Development/Python3

%description -n python3-module-z3c.formwidget
Core package for z3c.formwidget.

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
touch %buildroot%python_sitelibdir/z3c/formwidget/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/z3c/formwidget/__init__.py
%endif

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

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/z3c/formwidget/__init__.py
%exclude %python3_sitelibdir/z3c/formwidget/__pycache__/__init__.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-z3c.formwidget
%python3_sitelibdir/z3c/formwidget/__init__.py
%python3_sitelibdir/z3c/formwidget/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Fixed requirements

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

