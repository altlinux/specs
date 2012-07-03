%define oname zope.ucol
Name: python-module-%oname
Version: 1.0.2
Release: alt2.1.1
Summary: Python access to ICU text collation
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.ucol/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute libicu-devel

%py_requires zope

%description
This package provides a Python interface to the International Component
for Unicode (ICU).

%package tests
Summary: Tests for Python access to ICU text collation
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a Python interface to the International Component
for Unicode (ICU).

This package contains tests for Python access to ICU text collation.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/zope/__init__.*
%exclude %python_sitelibdir/zope/*/tests.*

%files tests
%python_sitelibdir/zope/*/tests.*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added necessary requirements

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

