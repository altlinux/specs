%define oname chameleon
Name: python-module-%oname.html
Version: 1.0.b4
Release: alt1.bzr20090520.1
Summary: Dynamic HTML template compiler with XSS language support
License: BSD
Group: Development/Python
Url: http://chameleon.repoze.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch lp:chameleon.html
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
This package implements a template compiler for dynamic HTML
documents. In particular, it supports the XSS rule language which is
used to associate elements with dynamic content.

%package tests
Summary: Tests for Dynamic HTML template compiler
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package implements a template compiler for dynamic HTML
documents. In particular, it supports the XSS rule language which is
used to associate elements with dynamic content.

This package contains tests for Dynamic HTML template compiler.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/*/tests

%files tests
%python_sitelibdir/%oname/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.b4-alt1.bzr20090520.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.b4-alt1.bzr20090520
- Initial build for Sisyphus

