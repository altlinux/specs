%define oname pyramid_simpleform
Name: python-module-%oname
Version: 0.6.1
Release: alt1.1
Summary: Simple form utilities for using Pyramid with Formencode and webhelpers
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_simpleform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid webhelpers formencode

%description
Simple form utilities for using Pyramid with Formencode and webhelpers.

%package tests
Summary: Tests for pyramid_simpleform
Group: Development/Python
Requires: %name = %version-%release

%description tests
Simple form utilities for using Pyramid with Formencode and webhelpers.

This package contains tests for pyramid_simpleform.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

