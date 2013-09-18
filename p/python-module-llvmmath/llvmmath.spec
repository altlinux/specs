%define oname llvmmath

Name: python-module-%oname
Version: 0.1.1
Release: alt1
Summary: LLVM math library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/llvmmath
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel libnumpy-devel python-module-llvm
BuildPreReq: python-module-sphinx-devel python-module-sphinxjp.themecore
BuildPreReq: python-module-sphinxjp.themes.basicstrap

%description
The purpose of this project is to provide portable math functions, many
of which are in C99 and not available on all platforms. It is based on
NumPy's umath and tries to support all floating point and complex types.

%package tests
Summary: Tests for llvmmath
Group: Development/Python
Requires: %name = %EVR

%description tests
The purpose of this project is to provide portable math functions, many
of which are in C99 and not available on all platforms. It is based on
NumPy's umath and tries to support all floating point and complex types.

This package contains tests for llvmmath.

%package pickles
Summary: Pickles for llvmmath
Group: Development/Python

%description pickles
The purpose of this project is to provide portable math functions, many
of which are in C99 and not available on all platforms. It is based on
NumPy's umath and tries to support all floating point and complex types.

This package contains pickles for llvmmath.

%package docs
Summary: Documentation for llvmmath
Group: Development/Documentation

%description docs
The purpose of this project is to provide portable math functions, many
of which are in C99 and not available on all platforms. It is based on
NumPy's umath and tries to support all floating point and complex types.

This package contains documentation for llvmmath.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%make -C docs pickle
%make -C docs html

%install
%python_install

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc README.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

