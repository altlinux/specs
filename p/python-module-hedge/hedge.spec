%define oname hedge
Name: python-module-%oname
Version: 0.91
Release: alt1.git20140528.1
Summary: Hybrid and Easy Discontinuous Galerkin Environment
License: MIT
Group: Development/Python
Url: http://mathema.tician.de/software/hedge/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel boost-numeric-bindings libopenblas-devel
BuildPreReq: python-module-pyublas-devel boost-python-devel
BuildPreReq: python-module-pyvisfile libsilo-devel gcc-c++
BuildPreReq: python-module-pymetis libnumpy-devel
BuildPreReq: python-module-py python-module-pytest
BuildPreReq: python-module-epydoc python-module-sphinx-devel
BuildPreReq: python-module-pytools

%add_python_req_skip pycuda

%description
hedge is an unstructured, high-order, parallel Discontinuous Galerkin
(DG) code that I am developing as part my PhD project. hedge's design is
focused on two things: being fast and easy to use. While the need for
speed dictates implementation in a low level language, these same
low-level languages become quite cumbersome at a higher level of
abstraction. This is where the "h" in hedge comes from; it takes a
hybrid approach. While a small core is written in C++ for speed, all
user-visible functionality is driven from Python.

%package pickles
Summary: Pickles for hedge
Group: Development/Python

%description pickles
hedge is an unstructured, high-order, parallel Discontinuous Galerkin
(DG) code that I am developing as part my PhD project. hedge's design is
focused on two things: being fast and easy to use. While the need for
speed dictates implementation in a low level language, these same
low-level languages become quite cumbersome at a higher level of
abstraction. This is where the "h" in hedge comes from; it takes a
hybrid approach. While a small core is written in C++ for speed, all
user-visible functionality is driven from Python.

This package contains pickles for hedge.

%package docs
Summary: Documentation for hedge
Group: Development/Documentation
BuildArch: noarch

%description docs
hedge is an unstructured, high-order, parallel Discontinuous Galerkin
(DG) code that I am developing as part my PhD project. hedge's design is
focused on two things: being fast and easy to use. While the need for
speed dictates implementation in a low level language, these same
low-level languages become quite cumbersome at a higher level of
abstraction. This is where the "h" in hedge comes from; it takes a
hybrid approach. While a small core is written in C++ for speed, all
user-visible functionality is driven from Python.

This package contains documentation for hedge.

%prep
%setup

%prepare_sphinx doc/manual
ln -s ../objects.inv doc/manual/source/

%build
./configure.py \
	--boost-compiler=g++ \
	--boost-python-libname=boost_python \
	--boost-bindings-inc-dir=/usr/include \
	--have-blas \
	--blas-libname=openblas \
	--cxxflags="-g"
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc/manual pickle
%make -C doc/manual html
%make userdoc
%make devdoc

cp -fR doc/manual/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc HACKING README README.rst TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/dev-reference
%doc doc/user-reference
%doc examples
%doc doc/manual/build/html

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.91-alt1.git20140528.1
- rebuild with boost 1.57.0

* Thu Jun 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91-alt1.git20140528
- Initial build for Sisyphus

