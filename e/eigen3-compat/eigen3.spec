%define        nomen eigen

Name:          %{nomen}3-compat
Version:       3.4.1
Release:       alt1
Summary:       A lightweight C++ template library for vector and matrix math
License:       Apache-2.0 AND MPL-2.0 AND BSD-3-Clause AND Minpack
Group:         Development/C++
Url:           http://eigen.tuxfamily.org/
Vcs:           https://gitlab.com/libeigen/eigen.git
Source:        %name-%version.tar

# Avoid SSE4.2/AVX on e2k
Patch:         eigen3-3.4.0-alt-e2k.patch
Patch1:        cmake.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: libsuitesparse-devel libscotch-devel libgoogle-sparsehash
BuildRequires: gcc-c++
BuildRequires: gcc-fortran
BuildRequires: libsuperlu-devel libmpfr-devel libgmp-devel
BuildRequires: libfftw3-devel libGLU-devel libgsl-devel gcc-fortran
BuildRequires: liblapack-devel libglew-devel libGLUT-devel libXi-devel
BuildRequires: libXmu-devel libmetis-devel libXres-devel
BuildRequires: libXcomposite-devel libXdamage-devel libXdmcp-devel
BuildRequires: libXft-devel libxkbfile-devel libXpm-devel
BuildRequires: libXScrnSaver-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: boost-devel
BuildRequires: libopenblas-devel

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Conflicts:     eigen3-lapack eigen3-blas

%description
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%package       devel
Summary:       A lightweight C++ template library for vector and matrix math
Group:         Development/C++
 
%description   devel
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.


%prep
%setup
%ifarch %e2k
%patch -p2 -b .e2k
%endif
%patch1

%build
export PATH=$PATH:%_libdir/pastix/bin

%cmake \
   -Wno-dev \
   -DEIGEN_BUILD_SHARED_LIBS=ON \
   -DEIGEN_BUILD_BLAS=OFF \
   -DEIGEN_BUILD_LAPACK=OFF \
   -DEIGEN_BUILD_BTL=ON \
   -DEIGEN_BUILD_SPBENCH=ON \
   -DEIGEN_BUILD_AOCL_BENCH=ON \
   -DEIGEN_BUILD_DOC=OFF \
   -DEIGEN_TEST_NOQT=ON \
   -DINCLUDE_INSTALL_DIR=%_includedir/%name \
   -DPKGCONFIG_INSTALL_DIR=%_libdir/pkgconfig \
   -DCMAKEPACKAGE_INSTALL_DIR=%_libdir/cmake/%name \
   -DOpenGL_GL_PREFERENCE=GLVND \
   -DCHOLMOD_INCLUDES=%_includedir/suitesparse \
   -DUMFPACK_INCLUDES=%_includedir/suitesparse \
   -DSUPERLU_LIBRARIES=-lsuperlu_4.0 \
   -DCMAKE_STRIP="/bin/echo" \
   -DGOOGLEHASH_INCLUDES="%_includedir/google" \
   -DGOOGLEHASH_COMPILE="g++ %optflags" \
   -DMETIS_INCLUDE_DIRS=%_includedir/metis

%cmake_build

%install
%cmake_install

%files
#%_libdir/libeigen_blas.so
#%_libdir/libeigen_lapack.so

%files         devel
%_includedir/*
%_pkgconfigdir/*
%_libdir/cmake/%name


%changelog
* Tue Jan 13 2026 Andrey Cherepanov <majioa@altlinux.org> 3.4.1-alt1
- initial build for Sisyphus to remove FTBFS
