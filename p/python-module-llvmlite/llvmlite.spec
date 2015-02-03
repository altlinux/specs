%define oname llvmlite

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt1.git20150129
Summary: Lightweight wrapper around basic LLVM functionality
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/llvmlite/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/numba/llvmlite.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ clang-devel llvm-devel-static libffi-devel
BuildPreReq: libstdc++-devel-static
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-enum34
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-enum34
%endif

%py_provides %oname
Requires: python-module-enum34

%description
Old llvmpy binding exposes a lot of LLVM but the mapping of C++ style
memory management to python is error prone. Numba and many JIT compiler
does not need a full LLVM API. Only the IR builder, optimizer, and JIT
compiler APIs are necessary.

llvmlite is a project originally tailored for Numba's needs, using the
following approach:

* A small C wrapper around the parts of the LLVM C++ API we need that
  are not already exposed by the LLVM C API.
* A ctypes Python wrapper around the C API.
* A pure Python implementation of the subset of the LLVM IR builder that
  we need for Numba.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Lightweight wrapper around basic LLVM functionality.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Lightweight wrapper around basic LLVM functionality
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-enum34

%description -n python3-module-%oname
Old llvmpy binding exposes a lot of LLVM but the mapping of C++ style
memory management to python is error prone. Numba and many JIT compiler
does not need a full LLVM API. Only the IR builder, optimizer, and JIT
compiler APIs are necessary.

llvmlite is a project originally tailored for Numba's needs, using the
following approach:

* A small C wrapper around the parts of the LLVM C++ API we need that
  are not already exposed by the LLVM C API.
* A ctypes Python wrapper around the C API.
* A pure Python implementation of the subset of the LLVM IR builder that
  we need for Numba.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Lightweight wrapper around basic LLVM functionality.

This package contains tests for %oname.

%prep
%setup

sed -i 's|@VERSION@|%version|' %oname/_version.py

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
python runtests.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150129
- Version 0.2.2

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141218
- Version 0.2.0

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141208
- Initial build for Sisyphus

