%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%define origname scalapack

%def_enable bootstrap

%define sover 2
Name: lib%origname
Version: 2.1.0
Release: alt3
Summary: Scalable LAPACK library
License: BSD-style
Group: Sciences/Mathematics
Url: http://www.netlib.org/scalapack/

Source: %origname-%version.tar
Source1: manpages.tar

# Patches from Fedora
Patch1: scalapack-2.1-fix-version.patch

# Patches from Gentoo
Patch2: scalapack-upstream-gcc10-compat.patch

# Patches from ALT
Patch3: scalapack-2.1.0-alt-pkgconfig.patch

BuildRequires(pre): %mpiimpl-devel
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

%package common
Summary: Common files for scalapack
Group: Sciences/Mathematics

%description common
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

This package contains common files which are not specific
to any MPI implementation.

%package devel
Summary: Development files of ScaLAPACK
Group: Development/Other
Requires: %mpiimpl-devel
%if_disabled bootstrap
Requires: libarpack-devel
%endif
Requires: %name = %EVR

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
%patch1 -p2
%patch2 -p1
%patch3 -p2

%build
%define build_fflags %(echo %build_fflags -fallow-argument-mismatch| sed 's|-Werror=format-security||g')

mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_STATIC_LIBS:BOOL=OFF \
	-DLAPACK_LIBRARIES="$(pkg-config --libs lapack)" \
	-DBLAS_LIBRARIES="$(pkg-config --libs openblas)" \
	%nil

%cmake_build

%install
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%cmakeinstall_std

install -d %buildroot%_includedir/blacs
install -m644 BLACS/SRC/*.h %buildroot%_includedir/blacs/

install -d %buildroot%_includedir/scalapack
install -m644 PBLAS/SRC/*.h %buildroot%_includedir/scalapack/

install -d %buildroot%_mandir/manl
install -m644 MANPAGES/man/manl/* %buildroot%_mandir/manl/

%files
%doc LICENSE
%doc README
%_libdir/*.so.%sover
%_libdir/*.so.%sover.*

%files devel
%_libdir/*.so
%_includedir/*
%_libdir/cmake/*
%_pkgconfigdir/*

%files manpages
%_mandir/manl/*

%changelog
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

