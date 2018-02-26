%define oname eigen
Name: %{oname}3
Version: 3.0.5
Release: alt1
Summary: C++ template library for linear algebra
License: LGPLv3+ or GPLv2+
Group: Development/C++
Url: http://eigen.tuxfamily.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake doxygen libqt4-devel libsuitesparse-devel
BuildPreReq: libsuperlu-devel libadolc-devel libmpfr-devel libgmp-devel
BuildPreReq: libfftw3-devel libGLU-devel libgsl-devel gcc-fortran
BuildPreReq: liblapack-devel libglew-devel libGLUT-devel libXi-devel
BuildPreReq: libXmu-devel libmetis-devel phonon-devel libXres-devel
BuildPreReq: libXcomposite-devel libXdamage-devel libXdmcp-devel
BuildPreReq: libXft-devel libxkbfile-devel libXpm-devel
BuildPreReq: libXScrnSaver-devel libXxf86misc-devel libXxf86vm-devel

%description
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%package docs
Summary: Documentation for Eigen3
Group: Development/Documentation
BuildArch: noarch

%description docs
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

This package contains development documentation for Eigen.

%package examples
Summary: Examples for Eigen3
Group: Development/Documentation

%description examples
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

This package contains examples for Eigen.

%prep
%setup

%build
mkdir BUILD
pushd BUILD

%add_optflags -I%_includedir/metis

cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_C_FLAGS="%optflags" \
	-DCMAKE_CXX_FLAGS="%optflags" \
	-DCMAKE_Fortran_FLAGS="%optflags" \
	-DADOLC_INCLUDES:PATH=%_includedir/adolc \
	-DCHOLMOD_INCLUDES:PATH=%_includedir/suitesparse \
	-DUMFPACK_INCLUDES:PATH=%_includedir/suitesparse \
	-DSUPERLU_LIBRARIES:STRING=-lsuperlu_4.0 \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DEIGEN_INCLUDE_INSTALL_DIR:PATH=%_includedir/%name \
	..
popd

%make_build -C BUILD
%make_build -C BUILD doc

%install
%makeinstall_std -C BUILD

install -d %buildroot%_bindir
rm -fR BUILD/doc/examples/CMakeFiles BUILD/doc/examples/*.out \
	BUILD/doc/examples/*.cmake
install -m755 BUILD/doc/examples/* %buildroot%_bindir

%files
%_includedir/*
%_pkgconfigdir/*

%files examples
%_bindir/*
%doc doc/examples/*

%files docs
%doc BUILD/doc/html/*

%changelog
* Tue Mar 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1
- Initial build for Sisyphus

