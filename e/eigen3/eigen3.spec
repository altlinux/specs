%define oname eigen
Name: %{oname}3
Version: 3.3.4
Release: alt4
Summary: C++ template library for linear algebra
License: LGPLv3+ or GPLv2+
Group: Development/C++
Url: http://eigen.tuxfamily.org/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

# Install FindEigen3.cmake
# Adapted from Debian eigen3 package
Patch0:         01_install_FindEigen3.patch
# Fix pkg-config file
Patch1:         eigen_pkgconfig.patch
# Fix the include paths in the new Eigen3Config.cmake file
Patch2:         eigen3-3.3.1-fixcmake.patch

BuildPreReq: gcc-c++ cmake doxygen libqt4-devel libsuitesparse-devel
BuildPreReq: libsuperlu-devel libmpfr-devel libgmp-devel
BuildPreReq: libfftw3-devel libGLU-devel libgsl-devel gcc-fortran
BuildPreReq: liblapack-devel libglew-devel libGLUT-devel libXi-devel
BuildPreReq: libXmu-devel libmetis-devel phonon-devel libXres-devel
BuildPreReq: libXcomposite-devel libXdamage-devel libXdmcp-devel
BuildPreReq: libXft-devel libxkbfile-devel libXpm-devel
BuildPreReq: libXScrnSaver-devel libXxf86misc-devel libXxf86vm-devel
BuildPreReq: libscotch-devel libgoogle-sparsehash

# TODO: add devel subpackage and move stuff
Provides: %{name}-devel = %EVR
Provides: %{oname}-devel = %EVR

%description
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%package docs
Summary: Documentation for Eigen3
Group: Development/Documentation
#BuildArch: noarch

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
%patch0 -p1
%patch1 -p1
%patch2 -p0 -b .fixcmake

%build
mkdir -p BUILD
pushd BUILD

%add_optflags -I%_includedir/metis
export PATH=$PATH:%_libdir/pastix/bin

cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_C_FLAGS="%optflags" \
	-DCMAKE_CXX_FLAGS="%optflags" \
	-DCMAKE_Fortran_FLAGS="%optflags" \
	-DCHOLMOD_INCLUDES:PATH=%_includedir/suitesparse \
	-DUMFPACK_INCLUDES:PATH=%_includedir/suitesparse \
	-DSUPERLU_LIBRARIES:STRING=-lsuperlu_4.0 \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DEIGEN_INCLUDE_INSTALL_DIR:PATH=%_includedir/%name \
	-DPASTIX_INCLUDES:STRING="$(pastix-conf --incs)" \
	-DPASTIX_LIBRARIES:STRING="$(pastix-conf --libs)" \
	-DSCOTCH_INCLUDES:STRING="$(pkg-config scotch --cflags)" \
	-DSCOTCH_LIBRARIES:STRING="$(pkg-config scotch --libs)" \
	-DGOOGLEHASH_INCLUDES:PATH="%_includedir/google" \
	-DGOOGLEHASH_COMPILE:STRING="g++ %optflags" \
	-DPKGCONFIG_INSTALL_DIR=%_pkgconfigdir \
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
%_datadir/cmake/Modules/FindEigen3.cmake
%_datadir/%name/cmake/*.cmake

%files examples
%_bindir/*
%doc doc/examples/*

%files docs
%doc BUILD/doc/html/*

%changelog
* Wed Jan 31 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.4-alt4
- NMU: fixed FindEigen3.cmake (added fedora patches)
- added -devel provides (TODO: eigen3 should be renamed to eigen3-devel)

* Fri Nov 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.4-alt3
- Updated build dependencies.

* Tue Oct 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.4-alt2
- Rebuilt without libadolc.

* Mon Jun 26 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.4-alt1
- Version 3.3.4

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.3-alt1
- Version 3.3.3

* Fri Mar 18 2016 Sergey V Turchin <zerg@altlinux.org> 3.2.8-alt1
- new version

* Wed May 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Tue Nov 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1
- Version 3.2.0

* Wed Jun 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1
- Version 3.1.3

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1
- Version 3.1.2

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1
- Version 3.1.1

* Tue Mar 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1
- Initial build for Sisyphus

