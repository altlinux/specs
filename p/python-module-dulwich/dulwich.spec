%define _unpackaged_files_terminate_build 1
%define oname dulwich
Name: python-module-%oname
Version: 0.16.3
Release: alt1
Summary: Python Git Library
License: GPLv2+
Group: Development/Python
Url: http://pypi.python.org/pypi/dulwich/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/9e/d7/8fb5b952ad14f27f7ab1bbe17db7860fe99c3c3e5d08de0bea3a161389a0/%{oname}-%{version}.tar.gz

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
%setup -q -n %{oname}-%{version}

%build
%python_build

%install
%python_install

%files
%doc AUTHORS COPYING NEWS README.md docs/*.txt docs/tutorial PKG-INFO examples
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.16.3-alt1
- automated PyPI update

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.a
- Version 0.10.1a

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1
- Version 0.9.7

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1
- Version 0.9.3

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Version 0.9.0

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.7-alt1
- Version 0.8.7

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

