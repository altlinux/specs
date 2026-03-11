%define oname eigen
%def_without docs

Name: %{oname}3
Version: 5.0.1
Release: alt1

Summary: A lightweight C++ template library for vector and matrix math
License: Apache-2.0 AND MPL-2.0 AND BSD-3-Clause AND Minpack
Group: Development/C++

Url: https://libeigen.gitlab.io/
VCS: https://gitlab.com/libeigen/eigen.git
Source: %name-%version.tar

# Fix/workaround doc build failures
Patch0: eigen3_docs.patch
# Fix lib install dir
Patch1: eigen3_libinstalldir.patch
# Avoid SSE4.2/AVX on e2k
Patch3: eigen3-3.4.0-alt-e2k.patch
# Temporarily disable EIGEN_ALTIVEC_DISABLE_MMA on PPC64le
Patch4: eigen_mma.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: libsuitesparse-devel libscotch-devel libgoogle-sparsehash
BuildRequires: gcc-c++
BuildRequires: gcc-fortran
%if_with docs
BuildRequires: doxygen graphviz
%endif
BuildRequires: libsuperlu-devel libmpfr-devel libgmp-devel
BuildRequires: libfftw3-devel libGLU-devel libgsl-devel gcc-fortran
BuildRequires: liblapack-devel libglew-devel libGLUT-devel libXi-devel
BuildRequires: libXmu-devel libmetis-devel libXres-devel
BuildRequires: libXcomposite-devel libXdamage-devel libXdmcp-devel
BuildRequires: libXft-devel libxkbfile-devel libXpm-devel
BuildRequires: libXScrnSaver-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: boost-devel
BuildRequires: libopenblas-devel

%description
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%package devel
Summary: A lightweight C++ template library for vector and matrix math
Group: Development/C++
Provides: %{oname}-devel = %EVR
Provides: %name = %EVR
Obsoletes: %name < %EVR
 
%description devel
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%package blas
Summary: BLAS library built on top of eigen3
Group: Development/C++

%description blas
%{summary}.

%package lapack
Summary: LAPACK library built on top of eigen3
Group: Development/C++

%description lapack
%{summary}.

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
%patch0 -p1
%patch1 -p1
%ifarch %e2k
%patch3 -p2 -b .e2k
# crashes with a bus error
rm -f unsupported/doc/examples/BVH_Example.cpp
%endif
%ifarch ppc64le
%patch4 -p1
%endif

%build
export PATH=$PATH:%_libdir/pastix/bin

%cmake -GNinja \
	-Wno-dev \
        -DEIGEN_BUILD_SHARED_LIBS=ON \
        -DEIGEN_BUILD_BLAS=ON \
        -DEIGEN_BUILD_LAPACK=ON \
	-DINCLUDE_INSTALL_DIR=%_includedir/%name \
	-DPKGCONFIG_INSTALL_DIR=%_libdir/pkgconfig \
	-DCMAKEPACKAGE_INSTALL_DIR=%_libdir/cmake/%name \
	-DOpenGL_GL_PREFERENCE=GLVND \
	-DCHOLMOD_INCLUDES=%_includedir/suitesparse \
	-DUMFPACK_INCLUDES=%_includedir/suitesparse \
	-DEIGEN_TEST_NOQT=ON \
	-DSUPERLU_LIBRARIES=-lsuperlu_4.0 \
	-DCMAKE_STRIP="/bin/echo" \
	-DGOOGLEHASH_INCLUDES="%_includedir/google" \
	-DGOOGLEHASH_COMPILE="g++ %optflags" \
	-DMETIS_INCLUDE_DIRS=%_includedir/metis

%cmake_build
%if_with docs
%cmake_build -t doc
%endif

%install
%cmake_install
rm %buildroot%_libdir/*.a
%if_with docs
install -d %buildroot%_bindir
cd %_cmake__builddir
rm -fR doc/examples/CMakeFiles doc/examples/*.out \
	doc/examples/*.cmake
install -m755 doc/examples/* %buildroot%_bindir
cd -
%endif

%files devel
%_includedir/*
%_pkgconfigdir/*
%_libdir/cmake/%name

%files blas
%_libdir/libeigen_blas.so

%files lapack
%_libdir/libeigen_lapack.so

%if_with docs
%files examples
%_bindir/*
%doc doc/examples/*

%files docs
%doc %_cmake__builddir/doc/html/*
%endif

%changelog
* Wed Mar 11 2026 Anton Farygin <rider@altlinux.org> 5.0.1-alt1
- 5.0.0 -> 5.0.1

* Wed Mar 04 2026 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt2
- Really build without documentation (due doxygen errors).

* Tue Oct 14 2025 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.
- Build without documentation.

* Fri Mar 28 2025 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt3
- Fixed path to includes in pkgconfig file (ALT #53643).

* Wed Jan 12 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.4.0-alt2.1
- E2K: updated patch, enabled build of docs and examples

* Tue Aug 31 2021 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt2
- Temporarily disable EIGEN_ALTIVEC_DISABLE_MMA on ppc64le (ALT #40833).

* Mon Aug 23 2021 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Wed Jun 30 2021 Andrey Cherepanov <cas@altlinux.org> 3.3.9-alt2
- FTBFS: completely remove qt4 and phonon support.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 3.3.9-alt1.1
- NMU: spec: adapted to new cmake macros.

* Fri Dec 11 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.9-alt1
- New version.

* Thu Oct 22 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.8-alt3
- Move cmake files to %_libdir/cmake/eigen3 (ALT #39109).
- Spec cleanup.

* Fri Oct 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.8-alt2
- Applied upstream fix for eigen.

* Sun Oct 11 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.8-alt1
- New version.
- Use ninja for build.

* Fri Jun 26 2020 Michael Shigorin <mike@altlinux.org> 3.3.7-alt5
- E2K: lcc 1.24 workaround

* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 3.3.7-alt4
- build without Qt4

* Sat Feb 02 2019 Michael Shigorin <mike@altlinux.org> 3.3.7-alt3
- E2K: avoid SSE4.2/AVX in installed headers too.

* Fri Feb 01 2019 Michael Shigorin <mike@altlinux.org> 3.3.7-alt2
- E2K: avoid building too much for now.

* Fri Dec 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.7-alt1
- New version.

* Mon Oct 22 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.5-alt2
- Fix prototype (see https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=908336) (ALT #35537).

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.5-alt1.qa1
- NMU: applied repocop patch

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.5-alt1
- New version.

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

