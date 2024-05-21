%define _unpackaged_files_terminate_build 1
%define libamd_soname 3
%define libbtf_soname 2
%define _cmake__builddir BUILD

%define libamd_soname 3
%define libbtf_soname 2
%define libcamd_soname 3
%define libcolamd_soname 3
%define libccolamd_soname 3
%define libcholmod_soname 5
%define libcxsparse_soname 4
%define libklu_soname 2
%define libldl_soname 3
%define libumfpack_soname 6
%define librbio_soname 4
%define libspqr_soname 4
%define mongoose_soname 3
%define libspex_soname 3
%define libparu_soname 0
%define libsuitesparseconfig_soname 7


Name: libsuitesparse
Version: 7.7.0
Release: alt1

Summary: Shared libraries for sparse matrix calculations
License: BSD-3-Clause AND LGPL-2.1-or-later AND GPL-2.0-or-later
Group: Sciences/Mathematics

Url: https://people.engr.tamu.edu/davis/suitesparse.html
VCS: https://github.com/DrTimothyAldenDavis/SuiteSparse.git
Source0: %name-%version.tar
BuildRequires: libmetis-devel gcc-c++ libtbb-devel
BuildRequires: libblas-devel
BuildRequires: libgmp-devel
BuildRequires: libmpfr-devel

# Automatically added by buildreq on Sun Sep 14 2008
BuildRequires: gcc-fortran liblapack-devel texlive-latex-base
BuildRequires: libgomp-devel
BuildRequires: cmake

%description
Package contains a set of shared libraries to use efficient calculation
algorithms with sparse matricies.


%package devel
Summary: Development files of SuiteSparse
Group: Development/Other
Requires: libamd%libamd_soname = %EVR
Requires: libbtf%libbtf_soname = %EVR
Requires: libcamd%libcamd_soname = %EVR
Requires: libcolamd%libcolamd_soname = %EVR
Requires: libccolamd%libccolamd_soname = %EVR
Requires: libcholmod%libcholmod_soname = %EVR
Requires: libcxsparse%libcxsparse_soname = %EVR
Requires: libklu%libklu_soname = %EVR
Requires: libldl%libldl_soname = %EVR
Requires: libumfpack%libumfpack_soname = %EVR
Requires: librbio%librbio_soname = %EVR
Requires: libspqr%libspqr_soname = %EVR
Requires: libsuitesparse_mongoose%mongoose_soname = %EVR
Requires: libspex%libspex_soname = %EVR
Requires: libparu%libparu_soname = %EVR
Requires: libsuitesparseconfig%libsuitesparseconfig_soname = %EVR
Conflicts: libumfpack-devel UFconfig
%description devel
Package contains a set of development files to use efficient calculation
algorithms with sparse matricies in your programs.

%package tools
Summary: %name tools
Group: Sciences/Mathematics
%description tools
Package contains Mongoose executable.
Mongoose executable can read a Matrix Market file containing an adjacency
matrix and output timing and partitioning information to a plain-text file.
Simply call it with the following syntax:
mongoose <MM-input-file.mtx> [output-file]


%package -n libamd%libamd_soname
Group: Sciences/Mathematics
Summary: Approximate minimum degree ordering library for sparse matrices
%description -n libamd%libamd_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

The AMD library provides a set of routines for pre-ordering sparse matrices
prior to Cholesky or LU factorization, using the "Approximate Minimum Degree
ordering" algorithm.

%package -n libbtf%libbtf_soname
Group: Sciences/Mathematics
Summary: Permutation to block triangular form library for sparse matrices
%description -n libbtf%libbtf_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

The BTF library is a software package for permuting a matrix into Block upper
Triangular Form. It includes a maximum transversal algorithm, which finds a
permutation of a square or rectangular matrix so that it has a zero-free
diagonal (if one exists); otherwise, it finds a maximal matching which
maximizes the number of nonzeros on the diagonal. The package also includes a
method for finding the strongly connected components of a graph. These two
methods together give the permutation to block upper triangular form.

%package -n libcamd%libcamd_soname
Group: Sciences/Mathematics
Summary: Symmetric approximate minimum degree library for sparse matrices
%description -n libcamd%libcamd_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

The CAMD library provides a set of routines for pre-ordering sparse matrices
prior to Cholesky or LU factorization, using the approximate minimum degree
ordering algorithm with optional ordering constraints.

%package -n libcolamd%libcolamd_soname
Group: Sciences/Mathematics
Summary: Column approximate minimum degree ordering library for sparse matrices
%description -n libcolamd%libcolamd_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

The COLAMD library implements the "COLumn Approximate Minimum Degree ordering"
algorithm. It computes a permutation vector P such that the LU factorization
of A (:,P) tends to be sparser than that of A. The Cholesky factorization of
(A (:,P))'*(A (:,P)) will also tend to be sparser than that of A'*A.

%package -n libccolamd%libccolamd_soname
Group: Sciences/Mathematics
Summary: Constrained column approximate library for sparse matrices
%description -n libccolamd%libccolamd_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

The CCOLAMD library implements the "Constrained COLumn Approximate Minimum
Degree ordering" algorithm. It computes a permutation vector P such that the
LU factorization of A (:,P) tends to be sparser than that of A. The Cholesky
factorization of (A (:,P))'*(A (:,P)) will also tend to be sparser than that
of A'*A.

%package -n libcholmod%libcholmod_soname
Group: Sciences/Mathematics
Summary: Sparse Cholesky factorization library for sparse matrices
%description -n libcholmod%libcholmod_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

The CHOLMOD library provides a set of routines for factorizing sparse
symmetric positive definite matrices of the form A or AA', updating/downdating
a sparse Cholesky factorization, solving linear systems, updating/downdating
the solution to the triangular system Lx=b, and many other sparse matrix
functions for both symmetric and unsymmetric matrices. Its supernodal Cholesky
factorization relies on LAPACK and the Level-3 BLAS, and obtains a substantial
fraction of the peak performance of the BLAS.

%package -n libcxsparse%libcxsparse_soname
Group: Sciences/Mathematics
Summary: Concise sparse matrix library
%description -n libcxsparse%libcxsparse_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

The CXSparse library provides several matrix algorithms. The focus is on direct
methods; iterative methods and solvers for eigenvalue problems are beyond the
scope of this package.

The performance of the sparse factorization methods in CXSparse will not be
competitive with UMFPACK or CHOLMOD, but the codes are much more concise and
easy to understand. Other methods are competitive.

%package -n libklu%libklu_soname
Group: Sciences/Mathematics
Summary: Circuit simulation sparse LU factorization library
%description -n libklu%libklu_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

The KLU library provides routines for LU factorization, primarily for circuit
simulation.

%package -n libldl%libldl_soname
Group: Sciences/Mathematics
Summary: Simple LDL' factorization library for sparse matrices
%description -n libldl%libldl_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

The LDL library provides routines for sparse LDL' factorization and solving.
These routines are not terrifically fast (they do not use dense matrix
kernels), but the code is very short and concise. The purpose is to illustrate
the algorithms in a very concise and readable manner, primarily for
educational purposes.

%package -n libumfpack%libumfpack_soname
Group: Sciences/Mathematics
Summary: Sparse LU factorization library
%description -n libumfpack%libumfpack_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

The UMFPACK library provides a set of routines solving sparse linear systems
via LU factorization.

%package -n librbio%librbio_soname
Group: Sciences/Mathematics
Summary: Read/write sparse matrices in Rutherford/Boeing format
%description -n librbio%librbio_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

RBio is a library for reading/writing sparse matrices in the Rutherford/Boeing
format.

%package -n libspqr%libspqr_soname
Group: Sciences/Mathematics
Summary: Sparse QR factorization library
%description -n libspqr%libspqr_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

SuiteSparseQR (SPQR) is a multithreaded, multifrontal, rank-revealing sparse
QR factorization method.

%package -n libsuitesparse_mongoose%mongoose_soname
Group: Sciences/Mathematics
Summary: Graph partitioning tool that can quickly compute edge cuts (shared library)
%description -n libsuitesparse_mongoose%mongoose_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

Mongoose is a graph partitioning library that can quickly compute edge cuts in
arbitrary graph. Given a graph with a vertex set and edge set, an edge cut is
a partitioning of the graph into two subgraphs that are balanced (contain the
same number of vertices) and the connectivity between the subgraphs is
minimized (few edges are in the cut).

This package contains the shared C++ library.

%package -n libspex%libspex_soname
Group: Sciences/Mathematics
Summary: Solves sparse linear systems in exact arithmetic
%description -n libspex%libspex_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

SPEX Left LU is a software package designed to exactly solve unsymmetric sparse
linear systems, Ax = b, where A, b and x contain rational numbers. This
package performs a left-looking, roundoff-error-free (REF) LU factorization
PAQ = LDU, where L and U are integer, D is diagonal, and P and Q are row and
column permutations, respectively. Note that the matrix D is never explicitly
computed nor needed; thus this package uses only the matrices L and U.

This package relies on GNU GMP and MPRF for exact arithmetic computations.

%package -n libparu%libparu_soname
Group: Sciences/Mathematics
Summary: Unsymmetric multifrontal multithreaded sparse LU factorization
%description -n libparu%libparu_soname
Suitesparse is a collection of libraries for computations involving
sparse matrices.

ParU is an implementation of the multifrontal sparse LU factorization
method.  Parallelism is exploited both in the BLAS and across different frontal
matrices using OpenMP tasking, a shared-memory programming model for modern
multicore architectures. The package is written in C++ and real sparse matrices
are supported.

%package -n libsuitesparseconfig%libsuitesparseconfig_soname
Group: Sciences/Mathematics
Summary: Configuration routines for all SuiteSparse modules
%description -n libsuitesparseconfig%libsuitesparseconfig_soname 
Suitesparse is a collection of libraries for computations involving
sparse matrices.

The SuiteSparse_config library provides configuration routines that are common
to all SuiteSparse libraries.

%prep
%setup
%ifarch %e2k
# -fopenmp must also be set when linking
sed -i '/CF += $(CFOPENMP)/a LDFLAGS += $(CFOPENMP)' \
    SuiteSparse_config/SuiteSparse_config.mk
%endif

%build
%cmake \
	-DSUITESPARSE_ENABLE_PROJECTS="suitesparse_config;mongoose;amd;btf;camd;ccolamd;colamd;cholmod;cxsparse;ldl;klu;umfpack;paru;rbio;spqr;spex" \
	-DBLA_PREFER_PKGCONFIG=TRUE \
	-DSUITESPARSE_USE_CUDA=OFF \
	-DBUILD_STATIC_LIBS=OFF
%cmake_build

%install
%cmake_install

%files -n libamd%libamd_soname
%_libdir/libamd.so.%libamd_soname
%_libdir/libamd.so.%libamd_soname.*

%files -n libbtf%libbtf_soname
%_libdir/libbtf.so.%libbtf_soname
%_libdir/libbtf.so.%libbtf_soname.*

%files -n libcamd%libcamd_soname
%_libdir/libcamd.so.%libcamd_soname
%_libdir/libcamd.so.%libcamd_soname.*

%files -n libcolamd%libcolamd_soname
%_libdir/libcolamd.so.%libcolamd_soname
%_libdir/libcolamd.so.%libcolamd_soname.*

%files -n libccolamd%libccolamd_soname
%_libdir/libccolamd.so.%libccolamd_soname
%_libdir/libccolamd.so.%libccolamd_soname.*

%files -n libcholmod%libcholmod_soname
%_libdir/libcholmod.so.%libcholmod_soname
%_libdir/libcholmod.so.%libcholmod_soname.*

%files -n libcxsparse%libcxsparse_soname
%_libdir/libcxsparse.so.%libcxsparse_soname
%_libdir/libcxsparse.so.%libcxsparse_soname.*

%files -n libklu%libklu_soname
%_libdir/libklu.so.%libklu_soname
%_libdir/libklu.so.%libklu_soname.*
%_libdir/libklu_cholmod.so.%libklu_soname
%_libdir/libklu_cholmod.so.%libklu_soname.*

%files -n libldl%libldl_soname
%_libdir/libldl.so.%libldl_soname
%_libdir/libldl.so.%libldl_soname.*

%files -n libumfpack%libumfpack_soname
%_libdir/libumfpack.so.%libumfpack_soname
%_libdir/libumfpack.so.%libumfpack_soname.*

%files -n librbio%librbio_soname
%_libdir/librbio.so.%librbio_soname
%_libdir/librbio.so.%librbio_soname.*

%files -n libspqr%libspqr_soname
%_libdir/libspqr.so.*%libspqr_soname
%_libdir/libspqr.so.*%libspqr_soname.*

%files -n libsuitesparse_mongoose%mongoose_soname
%_libdir/libsuitesparse_mongoose.so.%mongoose_soname

%files -n libspex%libspex_soname
%_libdir/libspexpython.so.%libspex_soname
%_libdir/libspexpython.so.%libspex_soname.*
%_libdir/libspex.so.%libspex_soname
%_libdir/libspex.so.%libspex_soname.*


%files -n libparu%libparu_soname
%_libdir/libparu.so.%libparu_soname
%_libdir/libparu.so.%libparu_soname.*

%files -n libsuitesparseconfig%libsuitesparseconfig_soname
%_libdir/libsuitesparseconfig.so.%libsuitesparseconfig_soname
%_libdir/libsuitesparseconfig.so.%libsuitesparseconfig_soname.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_libdir/cmake/*

%files tools
%_bindir/suitesparse_mongoose

%changelog
* Sun May 12 2024 Anton Farygin <rider@altlinux.ru> 7.7.0-alt1
- 5.10.1 -> 7.7.0
- split package according shared libs policy

* Tue Apr 11 2023 Michael Shigorin <mike@altlinux.org> 5.10.1-alt2
- Dropped patch for Elbrus (unneeded with lcc 1.26);
  fixed linking against openmp (ilyakurdyukov@).
- Minor spec cleanup.

* Wed Jul 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.10.1-alt1
- Updated to upstream version 5.10.1.

* Mon Jul 19 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 5.8.1-alt4
- Added patch for Elbrus.

* Thu Jun 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.8.1-alt3
- Fixed build with new cmake macros.

* Fri Mar 19 2021 Ivan A. Melnikov <iv@altlinux.org> 5.8.1-alt2
- Link with -latomic on mipsel.

* Thu Sep 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.8.1-alt1
- Updated to upstream version 5.8.1.

* Tue Jun 04 2019 Slava Aseev <ptrnine@altlinux.org> 5.4.0-alt1
- Updated to stable upstream version 5.4.0.

* Fri Nov 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.2-alt2
- Fixed build with new gcc.

* Wed Feb 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.2-alt1
- Updated to stable upstream version 5.1.2.

* Wed Jul 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5.5-alt1
- Updated to upstream version 4.5.5

* Thu Nov 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1
- Version 4.2.1

* Mon Sep 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2
- Rebuilt with libmetis instead of libmetis0

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt5
- Built with OpenBLAS instead of GotoBLAS2

* Sun Jul 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt4
- Added cs.h for CXSparse as cx_cs.h

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt3
- Rebuilt with libmetis0 4.0.3-alt3

* Fri Sep 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Rebuilt with libmetis0 instead of libmetis

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt3
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Built with lapack-goto instead of lapack

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Version 3.6.0

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt7
- Rebuilt with metis 4.0.1-alt9

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt6
- Rebuilt for debuginfo

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt5
- Rebuilt for soname set-versions

* Fri Oct 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt4
- Fixed underlinking of libraries

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt3
- Rebuilt with reformed Metis

* Mon Dec 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Rebuilt with texlive instead of tetex

* Fri Aug 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Version 3.4.0
- Added:
    + pkg-config files (ALT #21192)
    + shared libraries
    + examples

* Tue Nov 18 2008 Paul Wolneykien <manowar@altlinux.ru> 3.1-alt3
- Generate position independent code (PIC).

* Sat Nov 01 2008 Paul Wolneykien <manowar@altlinux.ru> 3.1-alt2
- Architacture independent documentation package.

* Mon Sep 08 2008 Paul Wolneykien <manowar@altlinux.ru> 3.1-alt1
- Initial release for ALTLinux.
