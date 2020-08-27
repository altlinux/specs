%define _unpackaged_files_terminate_build 1
%define oname theano

%def_with bootstrap

Name:       python3-module-%oname
Version:    1.0.5
Release:    alt1

Summary:    Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs
License:    BSD
Group:      Development/Python3
Url:        https://pypi.org/project/Theano/

BuildArch:  noarch

Source:     %name-%version.tar

Patch1: %oname-alt-numpy-compat.patch
Patch2: %oname-alt-python3-compat.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%add_python3_req_skip lazylinker_ext pycuda scan_perform gnumpy pygpu
%if_with bootstrap
%add_python3_req_skip lazylinker_ext.lazylinker_ext pycuda.compiler
%add_python3_req_skip pycuda.elementwise pycuda.tools
%add_python3_req_skip scan_perform.scan_perform theano.compat.six.moves
%endif


%description
Theano is a Python library that allows you to define, optimize, and efficiently
evaluate mathematical expressions involving multi-dimensional arrays. It is
built on top of NumPy. Theano features:

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
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip multinomial neighbours theano_object
%if_with bootstrap
%add_python3_req_skip pycuda.driver pycuda.gpuarray pygpu.array
%endif

%description tests
Theano is a Python library that allows you to define, optimize, and efficiently
evaluate mathematical expressions involving multi-dimensional arrays. It is
built on top of NumPy.

This package contains tests for Theano.

%package docs
Summary: Documentation for Theano
Group: Development/Documentation

%description docs
Theano is a Python library that allows you to define, optimize, and efficiently
evaluate mathematical expressions involving multi-dimensional arrays. It is
built on top of NumPy.

This package contains documentation for Theano.

%prep
%setup
%patch1 -p2
%patch2 -p2

%build
export LC_ALL=en_US.UTF-8

sed -i \
	-e 's|#!/usr/bin/env python$|#!/usr/bin/env python3|' \
	-e 's|#! /usr/bin/env python$|#! /usr/bin/env python3|' \
	-e 's|#!/usr/bin/python$|#!/usr/bin/python3|' \
	$(find ./ -name '*.py')

%python3_build_debug

%install
export LC_ALL=en_US.UTF-8

%python3_install

%files
%doc *.txt
%_bindir/theano-*
%exclude %_bindir/theano-nose
%python3_sitelibdir/*
%exclude %python3_sitelibdir/bin/theano_nose.py
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files tests
%_bindir/theano-nose
%python3_sitelibdir/bin/theano_nose.py
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests

%files docs
%doc doc/*

%changelog
* Wed Aug 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1
- Updated to upstream version 1.0.5.

* Tue Oct 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.4-alt1
- Version updated to 1.0.4
- disable python2

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt4.qa1
- NMU: applied repocop patch

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.0-alt4
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt3.2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 07 2016 Denis Medvedev <nbr@altlinux.org> 0.6.0-alt3.2
- Added missing dependence on python-dev

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt3.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt3
- Disabled version check for numpy & scipy

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Version 0.6.0
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.rc5
- Version 0.6.0rc5

* Wed Mar 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.rc3
- Initial build for Sisyphus

