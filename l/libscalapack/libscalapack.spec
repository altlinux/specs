%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%def_enable bootstrap

%define soname 2.2
Name: libscalapack
Version: 2.2.2
Release: alt1
Summary: Scalable LAPACK library
License: BSD-3-Clause
Group: Sciences/Mathematics
Url: http://www.netlib.org/scalapack/

Source: %name-%version.tar
Source1: manpages.tar

Patch0: scalapack-2.2.2-alt-lib-version.patch
Patch1: scalapack-2.2.2-alt-fix-pkgconfig.patch
Patch2: scalapack-2.2.2-alt-cmake-compat.patch
Patch3: scalapack-2.2.2-alt-cmake-install-path.patch

BuildRequires: %mpiimpl-devel
BuildRequires: cmake
BuildRequires: gcc-fortran
BuildRequires: libopenblas-devel
BuildRequires: liblapack-devel
%if_disabled bootstrap
# circular build deps with arpack
BuildRequires: libarpack-devel
%endif

%description
The ScaLAPACK (or Scalable LAPACK) library includes a subset of LAPACK routines
redesigned for distributed memory MIMD parallel computers. It is currently
written in a Single-Program-Multiple-Data style using explicit message passing
for interprocessor communication. It assumes matrices are laid out in a
two-dimensional block cyclic decomposition.

ScaLAPACK is designed for heterogeneous computing and is portable on any
computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on block-partitioned algorithms in
order to minimize the frequency of data movement between different levels of the
memory hierarchy. (For such machines, the memory hierarchy includes the
off-processor memory of other processors, in addition to the hierarchy of
registers, cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS) of the
Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra Communication
Subprograms (BLACS) for communication tasks that arise frequently in parallel
linear algebra computations. In the ScaLAPACK routines, all interprocessor
communication occurs within the PBLAS and the BLACS. One of the design goals of
ScaLAPACK was to have the ScaLAPACK routines resemble their LAPACK equivalents
as much as possible.

If You need man pages, install libscalapack-manpages.

%package -n libscalapack%soname
Summary: Common files for scalapack
Group: Sciences/Mathematics

%description -n libscalapack%soname
The ScaLAPACK (or Scalable LAPACK) library includes a subset of LAPACK routines
redesigned for distributed memory MIMD parallel computers. It is currently
written in a Single-Program-Multiple-Data style using explicit message passing
for interprocessor communication. It assumes matrices are laid out in a
two-dimensional block cyclic decomposition.

ScaLAPACK is designed for heterogeneous computing and is portable on any
computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on block-partitioned algorithms in
order to minimize the frequency of data movement between different levels of the
memory hierarchy. (For such machines, the memory hierarchy includes the
off-processor memory of other processors, in addition to the hierarchy of
registers, cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS) of the
Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra Communication
Subprograms (BLACS) for communication tasks that arise frequently in parallel
linear algebra computations. In the ScaLAPACK routines, all interprocessor
communication occurs within the PBLAS and the BLACS. One of the design goals of
ScaLAPACK was to have the ScaLAPACK routines resemble their LAPACK equivalents
as much as possible.

%package devel
Summary: Development files of ScaLAPACK
Group: Development/Other
Requires: %mpiimpl-devel
%if_disabled bootstrap
Requires: libarpack-devel
%endif

%description devel
Development files of ScaLAPACK.

%package manpages
Summary: Man pages of ScaLAPACK
Group: Sciences/Mathematics
BuildArch: noarch

%description manpages
Man pages of ScaLAPACK.

%prep
%setup -a1
%autopatch -p1

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_STATIC_LIBS:BOOL=OFF \
	-DLAPACK_LIBRARIES="$(pkg-config --libs lapack)" \
	-DBLAS_LIBRARIES="$(pkg-config --libs openblas)" \
	-DCMAKE_C_STANDARD="90" \
	#

%cmake_build

%install
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%cmakeinstall_std

install -Dm 644 BLACS/SRC/*.h -t %buildroot%_includedir/blacs/

install -Dm 644 PBLAS/SRC/*.h -t %buildroot%_includedir/scalapack/

install -Dm 644 MANPAGES/man/manl/* -t %buildroot%_man1dir/

%files -n libscalapack%soname
%doc LICENSE
%doc README
%_libdir/libscalapack.so.%soname
%_libdir/libscalapack.so.%version

%files devel
%_libdir/libscalapack.so
%_includedir/*
%_libdir/cmake/*
%_pkgconfigdir/*

%files manpages
%_man1dir/*

%changelog
* Tue Jul 22 2025 Ilya Muhamadeev <nicourced@altlinux.org> 2.2.2-alt1
- New version.
- Correct license.

* Tue Aug 31 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt3
- Disabled static libraries.

* Fri Apr 23 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt2
- Fixed build dependencies.

* Tue Apr 20 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Updated to upstream version 2.1.0.
- Cleaned up spec.

* Thu Sep 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.0-alt20
- Updated conflicts and obsoletes.

* Mon Jul 08 2019 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt19
- build without arpack

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.0-alt18
- Rebuilt with new mpi and toolchain

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt17
- Built with OpenBLAS instead of GotoBLAS2

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt16
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt15
- Fixed RPATH

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt14
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt13
- Rebuilt with GotoBLAS2 instead of ATLAS
- Disabled static and *-full packages

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt12
- Rebuilt for debuginfo

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt11
- Rebuilt

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt10
- Rebuilt for soname set-versions

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt9
- Fixed overlinking of libraries

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt8
- Rebuilt without udapl support

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt7
- Added missing requirements for devel package

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt6
- Added simple shared library
- Disabled strict aliasing rules

* Sat Aug 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt5
- Added all-in-one shared library

* Thu Jun 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt4
- Rebuild with PIC

* Mon Jun 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt3
- Add requirement on libblacs-devel

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt2
- Rebuild with OpenMPI

* Sun Feb 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus

