%define oname numba

Name: python-module-%oname
Version: 0.11
Release: alt1.git20130917
Summary: NumPy aware dynamic compiler for Python
License: BSD-like
Group: Development/Python
Url: http://numba.pydata.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildPreReq: libnumpy-devel python-module-Cython

%description
numba is a NumPy aware dynamic compiler for Python. It creates LLVM
bit-code from Python syntax and then creates a wrapper around that
bitcode to call from Python.

%package tests
Summary: Tests for numba
Group: Development/Python
Requires: %name = %EVR

%description tests
numba is a NumPy aware dynamic compiler for Python. It creates LLVM
bit-code from Python syntax and then creates a wrapper around that
bitcode to call from Python.

This package contains tests for numba.

%package docs
Summary: Documentation for numba
Group: Development/Documentation
BuildArch: noarch

%description docs
numba is a NumPy aware dynamic compiler for Python. It creates LLVM
bit-code from Python syntax and then creates a wrapper around that
bitcode to call from Python.

This package contains documentation for numba.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc AUTHORS CHANGE_LOG LICENSE README.md
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%if 0
%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%endif

%files docs
%doc docs/*.pdf docs/*.txt docs/ams_presentation/*.pdf

%changelog
* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.git20130917
- Version 0.11

* Wed Mar 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20130304
- Initial build for Sisyphus

