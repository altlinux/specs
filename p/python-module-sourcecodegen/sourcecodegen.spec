%define oname sourcecodegen
Name: python-module-%oname
Version: 0.6.14
Release: alt1.git20110519
Summary: A Python source-code generator based on the compiler.ast abstract syntax tree
License: BSD
Group: Development/Python
Url: http://chameleon.repoze.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch lp:sourcecodegen
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
This package provides a module-level source-code generator which
operates on the AST from the built-in ``compiler.ast`` module.

Note that this AST is not compatible with the new ``ast`` module in
Python 2.6.

%package tests
Summary: Tests for sourcecodegen
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a module-level source-code generator which
operates on the AST from the built-in ``compiler.ast`` module.

Note that this AST is not compatible with the new ``ast`` module in
Python 2.6.

This package contains tests for sourcecodegen.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.14-alt1.git20110519
- Version 0.6.14

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.13-alt1.bzr20110501.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.13-alt1.bzr20110501
- Initial build for Sisyphus

