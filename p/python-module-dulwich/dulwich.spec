%define oname dulwich
Name: python-module-%oname
Version: 0.8.5
Release: alt1
Summary: Python Git Library
License: GPLv2+
Group: Development/Python
Url: http://pypi.python.org/pypi/dulwich/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_provides %oname

%description
Simple Python implementation of the Git file formats and protocols.
Dulwich is the place where Mr. and Mrs. Git live in one of the Monty
Python sketches.

All functionality is available in pure Python, but (optional) C
extensions are also available for better performance.

%package tests
Summary: Tests for dulwich
Group: Development/Python
Requires: %name = %version-%release

%description tests
Simple Python implementation of the Git file formats and protocols.
Dulwich is the place where Mr. and Mrs. Git live in one of the Monty
Python sketches.

All functionality is available in pure Python, but (optional) C
extensions are also available for better performance.

This package contains tests for dulwich.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS COPYING HACKING NEWS README docs/*.txt docs/tutorial
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.5-alt1
- Version 0.8.5

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.2-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1
- Version 0.8.2

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1
- Version 0.8.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus

