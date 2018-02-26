%define oname pyramid_tm
Name: python-module-%oname
Version: 0.3
Release: alt1
Summary: A package which allows Pyramid requests to join the active transaction
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_tm/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid transaction

%description
pyramid_tm is a package which allows Pyramid requests to join the active
transaction as provided by the transaction package.

%package tests
Summary: Tests for pyramid_tm
Group: Development/Python
Requires: %name = %version-%release

%description tests
pyramid_tm is a package which allows Pyramid requests to join the active
transaction as provided by the transaction package.

This package contains tests for pyramid_tm.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

