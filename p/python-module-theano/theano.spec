%define oname theano

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt3.2.1
Summary: Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Theano
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
#BuildPreReq: libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel libnumpy-py3-devel python-tools-2to3
BuildRequires: python-tools-2to3
%endif

%add_python_req_skip lazylinker_ext pycuda scan_perform gnumpy pygpu

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-numpy python-module-pyparsing python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-docutils python-module-html5lib python-module-matplotlib rpm-build-python3 time
BuildRequires: python-dev

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

%package -n python3-module-%oname
Summary: Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs
Group: Development/Python3
%add_python3_req_skip lazylinker_ext pycuda scan_perform gnumpy pygpu

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for Theano
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip multinomial neighbours theano_object

%description -n python3-module-%oname-tests
Theano is a Python library that allows you to define, optimize, and
efficiently evaluate mathematical expressions involving
multi-dimensional arrays. It is built on top of NumPy.

This package contains tests for Theano.

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

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	$(find ./ -name '*.py')
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
	$(find ./ -name '*.py')
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%filter_from_requires /python\-base/d

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
%if_with python3
%exclude %_bindir/*.py3
%endif
%exclude %_bindir/theano-cache
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/test_*
%python_sitelibdir/*/*/*/test_*

%files docs
%doc doc/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/theano-cache.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests
%exclude %python3_sitelibdir/*/*/test_*
%exclude %python3_sitelibdir/*/*/*/test_*

%files -n python3-module-%oname-tests
%_bindir/*.py3
%exclude %_bindir/theano-cache.py3
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests
%python3_sitelibdir/*/*/test_*
%python3_sitelibdir/*/*/*/test_*
%endif

%changelog
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

