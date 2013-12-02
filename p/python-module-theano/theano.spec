%define oname theano

Name: python-module-%oname
Version: 0.6.0
Release: alt1.rc5
Summary: Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Theano
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: libnumpy-devel

%add_python_req_skip lazylinker_ext pycuda scan_perform gnumpy pygpu

%description
Theano is a Python library that allows you to define, optimize, and
efficiently evaluate mathematical expressions involving
multi-dimensional arrays. It is built on top of NumPy. Theano features:

* **tight integration with NumPy:** a similar interface to NumPy's.
  numpy.ndarrays are also used internally in Theano-compiled functions.
* **transparent use of a GPU:** perform data-intensive computations up
  to 140x faster than on a CPU (support for float32 only).
* **efficient symbolic differentiation:** Theano can compute derivatives
  for functions of one or many inputs.
* **speed and stability optimizations:** avoid nasty bugs when computing
  expressions such as log(1 + exp(x)) for large values of x.
* **dynamic C code generation:** evaluate expressions faster.
* **extensive unit-testing and self-verification:** includes tools for
  detecting and diagnosing bugs and/or potential problems.

%package tests
Summary: Tests for Theano
Group: Development/Documentation
Requires: %name = %EVR
%add_python_req_skip multinomial neighbours theano_object

%description tests
Theano is a Python library that allows you to define, optimize, and
efficiently evaluate mathematical expressions involving
multi-dimensional arrays. It is built on top of NumPy.

This package contains tests for Theano.

%package docs
Summary: Documentation for Theano
Group: Development/Documentation

%description docs
Theano is a Python library that allows you to define, optimize, and
efficiently evaluate mathematical expressions involving
multi-dimensional arrays. It is built on top of NumPy.

This package contains documentation for Theano.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt
%_bindir/theano-cache
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/test_*
%exclude %python_sitelibdir/*/*/*/test_*

%files tests
%_bindir/*
%exclude %_bindir/theano-cache
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/test_*
%python_sitelibdir/*/*/*/test_*

%files docs
%doc doc/*

%changelog
* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.rc5
- Version 0.6.0rc5

* Wed Mar 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.rc3
- Initial build for Sisyphus

