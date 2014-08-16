%define oname llvmmath

%def_with python3

Name: python-module-%oname
Version: 0.1.2
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
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel python3-module-llvm
%endif

%description
The purpose of this project is to provide portable math functions, many
of which are in C99 and not available on all platforms. It is based on
NumPy's umath and tries to support all floating point and complex types.

%package -n python3-module-%oname
Summary: LLVM math library
Group: Development/Python3

%description -n python3-module-%oname
The purpose of this project is to provide portable math functions, many
of which are in C99 and not available on all platforms. It is based on
NumPy's umath and tries to support all floating point and complex types.

%package -n python3-module-%oname-tests
Summary: Tests for llvmmath
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The purpose of this project is to provide portable math functions, many
of which are in C99 and not available on all platforms. It is based on
NumPy's umath and tries to support all floating point and complex types.

This package contains tests for llvmmath.

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
BuildArch: noarch

%description docs
The purpose of this project is to provide portable math functions, many
of which are in C99 and not available on all platforms. It is based on
NumPy's umath and tries to support all floating point and complex types.

This package contains documentation for llvmmath.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%make -C docs pickle
%make -C docs html

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

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

%if_with python3
%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Version 0.1.2
- Added module for Python 3

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

