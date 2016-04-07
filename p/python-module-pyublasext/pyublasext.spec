%define oname pyublasext

%def_without python3

Name: python-module-%oname
Version: 0.92.4
Release: alt6.git20140527.qa2
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
BuildPreReq: python-module-py python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-pyublas-devel
BuildPreReq: libnumpy-py3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
PyUblasExt is a companion to PyUblas and exposes a variety of useful
additions to it:

  * A cross-language "operator" class for building matrix-free
    algorithms
  * CG and BiCGSTAB linear solvers that use this operator class
  * An ARPACK interface that also uses this operator class
  * An UMFPACK interface for PyUblas's sparse matrices
  * An interface to the DASKR ODE solver.

%package -n python3-module-%oname
Summary: Added functionality for PyUblas
Group: Development/Python3

%description -n python3-module-%oname
PyUblasExt is a companion to PyUblas and exposes a variety of useful
additions to it:

  * A cross-language "operator" class for building matrix-free
    algorithms
  * CG and BiCGSTAB linear solvers that use this operator class
  * An ARPACK interface that also uses this operator class
  * An UMFPACK interface for PyUblas's sparse matrices
  * An interface to the DASKR ODE solver.

%package -n python3-module-%oname-devel
Summary: Development files of PyUblasExt
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-%oname = %version-%release
Requires: python3-module-pyublas-devel

%description -n python3-module-%oname-devel
PyUblasExt is a companion to PyUblas and exposes a variety of useful
additions to it:

  * A cross-language "operator" class for building matrix-free
    algorithms
  * CG and BiCGSTAB linear solvers that use this operator class
  * An ARPACK interface that also uses this operator class
  * An UMFPACK interface for PyUblas's sparse matrices
  * An interface to the DASKR ODE solver.

This package contains development files of PyUblasExt.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_build_debug
popd
exit 1
%endif

%python_install

%files
%python_sitelibdir/*

%files devel
%doc test/*
%_includedir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*

%files -n python3-module-%oname-devel
%doc test/*
%_includedir/*
%endif

%changelog
* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.92.4-alt6.git20140527.qa2
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.92.4-alt6.git20140527.1
- rebuild with boost 1.57.0

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt6.git20140527
- New snapshot

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt6.git20130722
- New snapshot

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt6.git20130314
- New snapshot

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt6.git20120406
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt5.git20120406
- Rebuilt with Boost 1.52.0

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt4.git20120406
- Rebuilt with Boost 1.51.0

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.4-alt3.git20120406
- New snapshot

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

