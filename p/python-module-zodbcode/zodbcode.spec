%define oname zodbcode
Name: python-module-%oname
Version: 3.4.0
Release: alt2.1
Summary: Allows Python code to live in the ZODB
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zodbcode/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.interface

%description
The package seeks to allow Python code to be stored in the ZODB. The
main benefits are that this code can then be easily transferred to other
servers and be changed at run time.

%package tests
Summary: Tests for zodbcode
Group: Development/Python
Requires: %name = %version-%release

%description tests
The package seeks to allow Python code to be stored in the ZODB. The
main benefits are that this code can then be easily transferred to other
servers and be changed at run time.

This package contains tests for zodbcode.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

