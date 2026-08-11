%define        _unpackaged_files_terminate_build 1

Name:          hypre
Version:       3.1.0
Release:       alt1
Summary:       Scalable algorithms for solving linear systems of equations
License:       LGPLv2.1
Group:         Sciences/Mathematics
Url:           http://www.llnl.gov/casc/hypre/
Vcs:           https://github.com/hypre-space/hypre.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake /proc
BuildRequires: gcc-fortran
BuildRequires: gcc-c++
BuildRequires: openmpi-devel
BuildRequires: liblapack-devel
BuildRequires: libgomp-devel
BuildRequires: libsuperlu-devel
# BuildRequires: hip-devel
# BuildRequires: llvm-rocm-devel

%description
Livermore's hypre library of linear solvers makes possible larger, more detailed
simulations by solving problems faster than traditional methods at large scales.
It offers a comprehensive suite of scalable solvers for large-scale scientific
simulations, featuring parallel multigrid methods for both structured and
unstructured grid problems. The open-source hypre library is highly portable and
supports a number of languages.

Work on hypre began in the late 1990s. It has since been used by research
institutions and private companies to simulate groundwater flow, magnetic fusion
energy plasmas in tokamaks and stellarators, blood flow through the heart, fluid
flow in steam generators for nuclear power plants, and pumping activity in oil
reservoirs, to name just a few application areas. In 2007, hypre won an R&D100
Award from R&D Magazine as one of the year's most significant technological
breakthroughs.

The hypre team was one of the first to develop algebraic multigrid algorithms
and software for extreme-scale parallel supercomputers, including LLNL's El
Capitan system. The team maintains an active role in the multigrid research
community and is recognized for its leadership in both algorithm and software
development.

The goal of the Scalable Linear Solvers project is to develop scalable
algorithms and software for solving large, sparse linear systems of equations on
parallel computers. The primary software product is Hypre, a library of high
performance preconditioners that features parallel multigrid methods for both
structured and unstructured grid problems. The problems of interest arise in the
simulation codes being developed at LLNL and elsewhere to study physical
phenomena in the defense, environmental, energy, and biological sciences.


%package       -n lib%name
Summary:       Scalable algorithms for solving linear systems of equations shared library files
Group:         System/Libraries

%description -n lib%name
Scalable algorithms for solving linear systems of equations shared library files

Livermore's hypre library of linear solvers makes possible larger, more detailed
simulations by solving problems faster than traditional methods at large scales.
It offers a comprehensive suite of scalable solvers for large-scale scientific
simulations, featuring parallel multigrid methods for both structured and
unstructured grid problems. The open-source hypre library is highly portable and
supports a number of languages.

Work on hypre began in the late 1990s. It has since been used by research
institutions and private companies to simulate groundwater flow, magnetic fusion
energy plasmas in tokamaks and stellarators, blood flow through the heart, fluid
flow in steam generators for nuclear power plants, and pumping activity in oil
reservoirs, to name just a few application areas. In 2007, hypre won an R&D100
Award from R&D Magazine as one of the year's most significant technological
breakthroughs.

The hypre team was one of the first to develop algebraic multigrid algorithms
and software for extreme-scale parallel supercomputers, including LLNL's El
Capitan system. The team maintains an active role in the multigrid research
community and is recognized for its leadership in both algorithm and software
development.

The goal of the Scalable Linear Solvers project is to develop scalable
algorithms and software for solving large, sparse linear systems of equations on
parallel computers. The primary software product is Hypre, a library of high
performance preconditioners that features parallel multigrid methods for both
structured and unstructured grid problems. The problems of interest arise in the
simulation codes being developed at LLNL and elsewhere to study physical
phenomena in the defense, environmental, energy, and biological sciences.


%package       -n lib%name-devel
Summary:       Development files of Hypre
Group:         Development/C
Provides:      %name = %EVR
Obsoletes:     %name < %EVR

%description -n lib%name-devel
Scalable algorithms for solving linear systems of equations development files.

Livermore's hypre library of linear solvers makes possible larger, more detailed
simulations by solving problems faster than traditional methods at large scales.
It offers a comprehensive suite of scalable solvers for large-scale scientific
simulations, featuring parallel multigrid methods for both structured and
unstructured grid problems. The open-source hypre library is highly portable and
supports a number of languages.

Work on hypre began in the late 1990s. It has since been used by research
institutions and private companies to simulate groundwater flow, magnetic fusion
energy plasmas in tokamaks and stellarators, blood flow through the heart, fluid
flow in steam generators for nuclear power plants, and pumping activity in oil
reservoirs, to name just a few application areas. In 2007, hypre won an R&D100
Award from R&D Magazine as one of the year's most significant technological
breakthroughs.

The hypre team was one of the first to develop algebraic multigrid algorithms
and software for extreme-scale parallel supercomputers, including LLNL's El
Capitan system. The team maintains an active role in the multigrid research
community and is recognized for its leadership in both algorithm and software
development.

The goal of the Scalable Linear Solvers project is to develop scalable
algorithms and software for solving large, sparse linear systems of equations on
parallel computers. The primary software product is Hypre, a library of high
performance preconditioners that features parallel multigrid methods for both
structured and unstructured grid problems. The problems of interest arise in the
simulation codes being developed at LLNL and elsewhere to study physical
phenomena in the defense, environmental, energy, and biological sciences.


%prep
%setup

%build
cd src

%cmake \
   -DBUILD_SHARED_LIBS=ON \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   -DHYPRE_USING_HYPRE_BLAS=OFF \
   -DHYPRE_USING_HYPRE_LAPACK=OFF \
   -DHYPRE_ENABLE_OPENMP=ON \
   -DHYPRE_ENABLE_LTO=ON \
   -DHYPRE_ENABLE_COMPLEX=OFF \
   -DHYPRE_ENABLE_MIXED_PRECISION=OFF \
   -DHYPRE_ENABLE_FORTRAN=ON \
   -DHYPRE_ENABLE_HIP=OFF \
   -DHYPRE_ENABLE_GPU_AWARE_MPI=ON \
   -DHYPRE_ENABLE_UNIFIED_MEMORY=ON \
   -DHYPRE_ENABLE_DEVICE_MALLOC_ASYNC=ON \
   -DHYPRE_ENABLE_THRUST_NOSYNC=ON \
   -DHYPRE_ENABLE_GPU_PROFILING=OFF \
   -DHYPRE_ENABLE_UMPIRE=OFF \
   -DHYPRE_ENABLE_UMPIRE_HOST=OFF \
   -DHYPRE_ENABLE_UMPIRE_PINNED=OFF \
   -DHYPRE_ENABLE_UMPIRE_DEVICE=OFF \
   -DHYPRE_ENABLE_UMPIRE_UM=OFF \
   -DHYPRE_ENABLE_SUPERLU=ON \
   -DHYPRE_ENABLE_DSUPERLU=OFF \
   -DHYPRE_ENABLE_MAGMA=OFF \
   -DHYPRE_ENABLE_CALIPER=OFF \
   %nil

%cmake_build

%install
cd src
%cmake_install

%files         -n lib%name
%_libdir/lib*.so.*

%files         -n lib%name-devel
%doc README.md SUPPORT.md CHANGELOG NOTICE LICENSE* COPYRIGHT
%_libdir/lib*.so
%_includedir/_hypre*
%_includedir/HYPRE*
%_libdir/cmake/HYPRE/


%changelog
* Sun Aug 09 2026 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 2.20.0 -> 3.1.0
- > rebased to upstream

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt2
- cleanup BR

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 2.20.0-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt1
- new version (2.20.0) with rpmgs script
- cleanup spec, build from tarball, don't pack empty hypre package
- temp. disable docs packing (needs checking)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 2.15.1-alt3
- NMU: update github repo url and add upstream/remotes
- NMU: fix license name, fix the package obsoletes itself error

* Mon Apr 27 2020 Anton Midyukov <antohami@altlinux.org> 2.15.1-alt2
- clean buidrequires doc++

* Fri Feb 22 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.15.1-alt1
- Update to latest release

* Fri Jul 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13.0-alt2
- Updated build dependencies.

* Mon Jan 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13.0-alt1
- Updated to upstream version 2.13.0.

* Thu Feb 21 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0b-alt1
- Version 2.9.0b

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt5
- Built with OpenBLAS instead of GotoBLAS2

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt4
- Rebuilt with emacs 24.1

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt3
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt2
- Fixed build

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt1
- Version 2.8.0b

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0b-alt3
- Rebuilt with GotoBLAS2 1.13-alt3

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0b-alt2
- Rebuilt with GotoBLAS2 instead of ATLAS

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0b-alt1
- Version 2.7.0b
- Disabled static package

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt6
- Added -g into compiler flags

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt5
- Rebuilt for debuginfo

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt4
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt3
- Fixed overlinking of libraries

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt2
- Rebuilt without python-module-Numeric

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt1
- Version 2.6.0b

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt9
- Rebuilt with SuperLU 4.0 and emacs23

* Sun Nov 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt8
- Removed unnecessary headers

* Tue Sep 1 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt7
- Added shared libraries

* Sun Jul 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt6
- Fixed MPI check

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt5
- Rebuild with PIC

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt4
- Rebuild with OpenMPI

* Wed Apr 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt3
- Move headers into hypre subdirectory

* Tue Apr 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt2
- Remove files owned by other packages

* Sat Apr 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt1
- Initial build for Sisyphus

