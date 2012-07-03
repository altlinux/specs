%define oname z3c.currency
Name: python-module-%oname
Version: 0.1.0
Release: alt2.1
Summary: A currency field and support for ``z3c.form``.
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.currency/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.i18n zope.i18nmessageid zope.interface zope.schema

%description
A package implementing a currency field for zope.schema and support for
using the field with z3c.form.

%package tests
Summary: Tests for z3c.currency
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.form zope.testing

%description tests
A package implementing a currency field for zope.schema and support for
using the field with z3c.form.

This package contains tests for z3c.currency.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

