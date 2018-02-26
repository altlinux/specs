%define oname pyramid_restler
Name: python-module-%oname
Version: 0.1a3
Release: alt1
Summary: RESTful views for Pyramid
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_restler/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid

%description
pyramid_restler is a somewhat-opinionated toolkit for building RESTful
Web services and applications on top of the Pyramid framework.
Essentially, it routes HTTP requests to Pyramid views. These views
interact with model entities via a uniform context interface, and then
respond with appropriate status codes and entity representations.

%package tests
Summary: Tests for pyramid_restler
Group: Development/Python
Requires: %name = %version-%release

%description tests
pyramid_restler is a somewhat-opinionated toolkit for building RESTful
Web services and applications on top of the Pyramid framework.
Essentially, it routes HTTP requests to Pyramid views. These views
interact with model entities via a uniform context interface, and then
respond with appropriate status codes and entity representations.

This package contains tests for pyramid_restler.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1a3-alt1
- Version 0.1a3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1a1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1a1-alt1
- Initial build for Sisyphus

