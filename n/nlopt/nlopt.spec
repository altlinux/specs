Name: nlopt
Version: 2.7.1
Release: alt1

Summary: Library for nonlinear optimization

License: MIT and LGPLv2
Group: Sciences/Mathematics
Url: https://github.com/stevengj/nlopt

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: https://github.com/stevengj/nlopt/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ gcc-fortran python3-devel
BuildRequires: libnumpy-py3-devel swig

%description
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

%package -n lib%name
Summary: Shared libraries of NLopt
Group: System/Libraries

%description -n lib%name
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains shared libraries of NLopt.

%package -n lib%name-cxx
Summary: Shared libraries of NLopt (C++ interface)
Group: System/Libraries

%description -n lib%name-cxx
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains shared libraries of NLopt (C++ interface).

%package -n lib%name-devel
Summary: Development files of NLopt
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains development files of NLopt.

%package tests
Summary: Tests for NLopt
Group: Sciences/Mathematics
Requires: lib%name = %version-%release

%description tests
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains tests for NLopt.

%package -n python3-module-%name
Summary: Python wrapper for NLopt 
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python3-module-%name
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains python wrapper for NLopt.

%package docs
Summary: Documentation for NLopt
Group: Development/Documentation
BuildArch: noarch

%description docs
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains development documentation for NLopt.

%prep
%setup

%build
%cmake \
    -DNLOPT_OCTAVE=OFF \
    -DNLOPT_MATLAB=OFF \
    -DNLOPT_GUILE=OFF \
    %nil
%cmake_build

%install
%cmakeinstall_std

%files -n lib%name
%doc AUTHORS ChangeLog COPYING NEWS.md README.md TODO
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_libdir/cmake/nlopt/
%_man3dir/*

#%files tests
#%doc test/*.c* test/*.h
#%_bindir/*

%files docs
%doc doc/docs

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Mon Aug 07 2023 Vitaly Lipatov <lav@altlinux.ru> 2.7.1-alt1
- new version 2.7.1, switched to cmake build, rewrote spec
- no more separate libnlopt_cxx library (libnlopt-cxx subpackage)

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1
- Version 2.4.2

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1
- Version 2.4

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1
- Initial build for Sisyphus

