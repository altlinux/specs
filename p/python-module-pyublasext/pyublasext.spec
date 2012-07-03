%define oname pyublasext
Name: python-module-%oname
Version: 0.92.4
Release: alt3.git20100108
Summary: Added functionality for PyUblas
License: BSD
Group: Development/Python
Url: http://mathema.tician.de/software/pyublas/pyublasext
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://git.tiker.net/trees/pyublasext.git
Source: %oname-%version.tar

BuildPreReq: gcc-c++ boost-python-devel python-module-pyublas-devel
BuildPreReq: liblapack-devel libode-devel libnumpy-devel
BuildPreReq: libarpack-devel libsuitesparse-devel gcc-fortran
BuildPreReq: libmtl4-devel libdaskr-devel boost-numeric-bindings

%description
PyUblasExt is a companion to PyUblas and exposes a variety of useful
additions to it:

  * A cross-language "operator" class for building matrix-free
    algorithms
  * CG and BiCGSTAB linear solvers that use this operator class
  * An ARPACK interface that also uses this operator class
  * An UMFPACK interface for PyUblas's sparse matrices
  * An interface to the DASKR ODE solver.

%package devel
Summary: Development files of PyUblasExt
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release
Requires: python-module-pyublas-devel

%description devel
PyUblasExt is a companion to PyUblas and exposes a variety of useful
additions to it:

  * A cross-language "operator" class for building matrix-free
    algorithms
  * CG and BiCGSTAB linear solvers that use this operator class
  * An ARPACK interface that also uses this operator class
  * An UMFPACK interface for PyUblas's sparse matrices
  * An interface to the DASKR ODE solver.

This package contains development files of PyUblasExt.

%prep
%setup

%build
%add_optflags
%python_build_debug

%install
%python_install

%files
%python_sitelibdir/*

%files devel
%doc test/*
%_includedir/*

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt3.git20100108
- Rebuilt with Boost 1.49.0

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt2.git20100108
- Rebuilt with Boost 1.48.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.92.4-alt1.git20100108.3.1
- Rebuild with Python-2.7

* Mon Jul 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt1.git20100108.3
- Rebuilt with Boost 1.47.0

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt1.git20100108.2
- Built with GotoBLAS2 instead of ATLAS
- Added support of LAPACK, DASKR, ARPACK and UMFPACK

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt1.git20100108.1
- Rebuilt for debuginfo

* Tue Dec 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt1.git20100108
- Initial build for Sisyphus

