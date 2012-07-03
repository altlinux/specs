%define oname z3c.multifieldindex
Name: python-module-%oname
Version: 3.4.0
Release: alt2.1
Summary: Multi-field index for zope catalog
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.multifieldindex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.catalog ZODB3 zope.app.catalog zope.app.container
%py_requires zope.component zope.index zope.interface zope.schema

%description
This package provides an index for zope catalog that can index multiple
fields. It is useful in cases when field set are dynamic (for example
with customizable persistent fields).

%package tests
Summary: Tests for Multi-field index for zope catalog
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package provides an index for zope catalog that can index multiple
fields. It is useful in cases when field set are dynamic (for example
with customizable persistent fields).

This package contains tests for Multi-field index for zope catalog.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

