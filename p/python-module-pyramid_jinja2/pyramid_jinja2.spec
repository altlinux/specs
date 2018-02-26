%define oname pyramid_jinja2
Name: python-module-%oname
Version: 1.2
Release: alt1
Summary: Jinja2 template bindings for the Pyramid web framework
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_jinja2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid

%description
These are bindings for the Jinja2 templating system for the Pyramid web
framework.

%package tests
Summary: Tests for pyramid_jinja2
Group: Development/Python
Requires: %name = %version-%release
%py_requires webtest

%description tests
These are bindings for the Jinja2 templating system for the Pyramid web
framework.

This package contains tests for pyramid_jinja2.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/demo

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/demo

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

