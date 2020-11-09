%define _unpackaged_files_terminate_build 1

%define sover 5

Name: superlu
Version: 5.2.2
Release: alt1
Summary: A set of subroutines to solve a sparse linear system A*X=B
License: BSD-like
Group: Sciences/Mathematics
Url: https://github.com/xiaoyeli/superlu

# https://github.com/xiaoyeli/superlu.git
Source: %name-%version.tar

# Patch from Gentoo
Patch1: superlu-5.2.2-no-internal-blas.patch

# ALT Patch
Patch10: superlu-5.2.2-respect-flags.patch

Provides: %name = %EVR
Requires: lib%name%sover = %EVR

BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-fortran gcc-c++ liblapack-devel
BuildRequires: csh doxygen graphviz ghostscript-utils

%description
SuperLU contains a set of subroutines to solve a sparse linear system
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP).
The columns of A may be preordered before factorization; the
preordering for sparsity is completely separate from the factorization.
SuperLU provides functionality for both real and complex matrices, in both
single and double precision.

%package -n lib%name%sover
Summary: Shared libraries of SuperLU
Group: System/Libraries

%description -n lib%name%sover
SuperLU contains a set of subroutines to solve a sparse linear system
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP).
The columns of A may be preordered before factorization; the
preordering for sparsity is completely separate from the factorization.
SuperLU provides functionality for both real and complex matrices, in both
single and double precision.

This package contains shared libraries of SuperLU.

%package -n lib%name-devel
Summary: Development files of SuperLU
Group: Development/C
Requires: lib%name%sover = %EVR

%description -n lib%name-devel
SuperLU contains a set of subroutines to solve a sparse linear system
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP).
The columns of A may be preordered before factorization; the
preordering for sparsity is completely separate from the factorization.
SuperLU provides functionality for both real and complex matrices, in both
single and double precision.

This package contains development files of SuperLU.

%package -n lib%name-devel-doc
Summary: Documentation for SuperLU
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
SuperLU contains a set of subroutines to solve a sparse linear system
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP).
The columns of A may be preordered before factorization; the
preordering for sparsity is completely separate from the factorization.
SuperLU provides functionality for both real and complex matrices, in both
single and double precision.

This package contains documentation for SuperLU.

%prep
%setup
%patch1 -p1
%patch10 -p1

%build
%cmake \
	-DCMAKE_INSTALL_INCLUDEDIR="include/superlu" \
	-DBUILD_SHARED_LIBS=ON \
	-Denable_internal_blaslib=OFF \
	-Denable_tests=ON \
	%nil

%cmake_build

%install
%cmakeinstall_std

%check
cd BUILD
ctest

%files -n lib%name%sover
%doc License.txt
%doc README
%_libdir/*.so.%{sover}
%_libdir/*.so.%{sover}.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_libdir/cmake/*

%files -n lib%name-devel-doc
%doc DOC/html
%doc EXAMPLE
%doc FORTRAN

%changelog
* Mon Nov 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.2.2-alt1
- Updated to upstream version 5.2.2 (Closes: #39217).

* Thu Jul 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3-alt9
- Added devel symlink libsuperlu.so -> libsuperlu_%%over.so.

* Thu Feb 14 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.3-alt8
- exclude %%arm from crippled arches

* Tue Feb 12 2019 Nikita Ermakov <arei@altlinux.org> 4.3-alt7
- liblapack is built with libblas.so on riscv64, not libopenblas.so
- Minor spec changes

* Sun Jun 10 2018 Michael Shigorin <mike@altlinux.org> 4.3-alt6
- support e2kv4 through %%e2k macro
- gear: avoid tarball compression
- minor spec cleanup

* Mon Nov 20 2017 Andrew Savchenko <bircoph@altlinux.org> 4.3-alt5
- Fix build on e2k.

* Thu Nov 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3-alt4
- Fixed build with gcc-6.

* Tue Mar 12 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.3-alt3
- on %arm liblapack is built with libblas, not libopenblas

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3-alt2
- Built with OpenBLAS instead of GotoBLAS2

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3-alt1
- Version 4.3

* Wed Oct 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1
- Version 4.2

* Tue May 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1
- Version 4.1
- Disabled devel-static package

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt6
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt5
- Built with GotoBLAS2 instead of ATLAS

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt4
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt3
- Rebuilt for debuginfo

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt2
- Fixed underlinking of libraries

* Mon Dec 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1
- Version 4.0 (soname changed)
- Rebuilt with texlive instead of tetex

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt7
- Added shared libraries and additional documentation

* Thu Jun 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt6
- Resolved conflicts with ctest and dapl*-utils

* Sun Jun 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt5
- Rebuild with PIC

* Fri Jun 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt4
- Added examples

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt3
- Resolve conflict with superlu_dist

* Tue May 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt2
- Added explicit conflict with superlu_dist

* Fri Apr 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Initial build for Sisyphus
