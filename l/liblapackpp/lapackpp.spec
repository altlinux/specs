%define        _unpackaged_files_terminate_build 1
%define        praenomen lapack
%define        nomen lapackpp
%def_enable    check

Name:          lib%nomen
Version:       2025.05.28
Release:       alt1
Summary:       LAPACK++ is a library for high performance linear algebra computations
License:       LGPL-2.1
Group:         Sciences/Mathematics
Url:           https://github.com/icl-utk-edu/lapackpp
Vcs:           https://github.com/icl-utk-edu/lapackpp.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
BuildRequires: /proc
BuildRequires: gcc-fortran
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: cmake(lapack)
BuildRequires: cmake(blaspp)

%description
LAPACK++ is a library for high performance linear algebra computations. This
version includes support for solving linear systems using LU, Cholesky, QR
matrix factorizations, for real and complex matrices.

This package contains shared libraries of LAPACK++.

%package       devel
Summary:       LAPACK++ the library for high performance linear algebra computations development files
Group:         Development/C++
Requires:      gcc-fortran
Requires:      gcc-c++
Requires:      cmake
Requires:      ctest
Requires:      cmake(lapack)
Requires:      cmake(blaspp)


%description   devel
LAPACK++ is a library for high performance linear algebra computations.
This version includes support for solving linear systems using LU,
Cholesky, QR matrix factorizations, for real and complex matrices.

This package contains development files of LAPACK++.

%prep
%setup

%build
%cmake \
   -Duse_cmake_find_lapack=ON

%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files
%doc README.md LICENSE INSTALL.md CHANGELOG.md
%_libdir/%{name}*.so.*

%files         devel
%_libdir/%{name}*.so
%_includedir/%{praenomen}*
%_cmakedir/%nomen/


%changelog
* Fri Apr 10 2026 Pavel Skrylev <majioa@altlinux.org> 2025.05.28-alt1
- ^ 2.5.4 -> 2025.05.28
- * renamed to liblapackpp

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.4-alt2.svn20110615
- Rebuilt with OpenBLAS instead of GotoBLAS2

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.4-alt1.svn20110615
- New snapshot

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.4-alt1.svn20101110.2
- Built with GotoBLAS2 instead of ATLAS

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.4-alt1.svn20101110.1
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.4-alt1.svn20101110
- Version 2.5.4

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.3-alt1.svn20100314.1
- Rebuilt for soname set-versions

* Fri Sep 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.3-alt1.svn20100314
- Initial build for Sisyphus
