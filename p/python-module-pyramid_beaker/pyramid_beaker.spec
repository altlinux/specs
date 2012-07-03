%define oname pyramid_beaker
Name: python-module-%oname
Version: 0.6.1
Release: alt1
Summary: Beaker session factory backend for Pyramid
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_beaker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid beaker

%description
Provides a session factory for the Pyramid web framework backed by the
Beaker sessioning system.

%package tests
Summary: Tests for pyramid_beaker
Group: Development/Python
Requires: %name = %version-%release

%description tests
Provides a session factory for the Pyramid web framework backed by the
Beaker sessioning system.

This package contains tests for pyramid_beaker.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Version 0.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

