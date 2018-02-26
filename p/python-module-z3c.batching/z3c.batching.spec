%define oname z3c.batching
Name: python-module-%oname
Version: 1.1.0
Release: alt2.1
Summary: This package provides simple sequence batching
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.batching/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface zope.schema

%description
This module implements a simple batching mechanism that allows you to
split a large sequence into smaller batches.

%package tests
Summary: Tests for z3c.batching
Group: Development/Python
Requires: %name = %version-%release

%description tests
This module implements a simple batching mechanism that allows you to
split a large sequence into smaller batches.

This package contains tests for z3c.batching.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

