%define        _unpackaged_files_terminate_build 1
%def_enable    check
%define        nomen blaspp

Name:          lib%nomen
Version:       2025.05.28
Release:       alt1.1
Summary:       BLAS++ the C++ wrapper around CPU and GPU BLAS library
License:       BSD-3-Clause
Group:         Sciences/Mathematics
Url:           https://github.com/icl-utk-edu/blaspp
Vcs:           https://github.com/icl-utk-edu/blaspp.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libgomp-devel
BuildRequires: cmake(lapack)
# BuildRequires: libsycl-devel
# BuildRequires: libmkl-devel
# BuildRequires: hip-devel
# BuildRequires: rocblas-devel
%{?_enable_check:BuildRequires: ctest}
%{?_enable_check:BuildRequires: cmake(testsweeper)}

%description
BLAS++ is a C++ wrapper around CPU and GPU BLAS (basic linear algebra
subroutines), developed as part of the SLATE project

The Basic Linear Algebra Subprograms (BLAS) have been around for many decades
and serve as the de facto standard for performance-portable and numerically
robust implementation of essential linear algebra functionality. Originally,
they were written in Fortran, and later furnished with a C API (CBLAS).

The objective of BLAS++ is to provide a convenient, performance oriented API for
development in the C++ language, that, for the most part, preserves established
conventions, while, at the same time, takes advantages of modern C++ features,
such as: namespaces, templates, exceptions, etc.

BLAS++ is part of the SLATE project (Software for Linear Algebra Targeting
Exascale), which is funded by the Department of Energy as part of its Exascale
Computing Initiative (ECP). Closely related to BLAS++ is the LAPACK++ project,
which provides a C++ API for LAPACK.


%package       devel
Summary:       C++ wrapper around CPU and GPU BLAS library development files
Group:         Development/C++

Requires:      gcc-c++
Requires:      cmake
Requires:      libgomp-devel
Requires:      liblapack-devel
%{?_enable_check:Requires: ctest}
%{?_enable_check:Requires: libtestsweeper-devel}

%description   devel
BLAS++ is a C++ wrapper around CPU and GPU BLAS (basic linear algebra
subroutines), developed as part of the SLATE project

The Basic Linear Algebra Subprograms (BLAS) have been around for many decades
and serve as the de facto standard for performance-portable and numerically
robust implementation of essential linear algebra functionality. Originally,
they were written in Fortran, and later furnished with a C API (CBLAS).

The objective of BLAS++ is to provide a convenient, performance oriented API for
development in the C++ language, that, for the most part, preserves established
conventions, while, at the same time, takes advantages of modern C++ features,
such as: namespaces, templates, exceptions, etc.

BLAS++ is part of the SLATE project (Software for Linear Algebra Targeting
Exascale), which is funded by the Department of Energy as part of its Exascale
Computing Initiative (ECP). Closely related to BLAS++ is the LAPACK++ project,
which provides a C++ API for LAPACK.

This package contains development files of BLAS++.


%prep
%setup

%build
%cmake \
%{?!_enable_check:-DBUILD_TESTING=OFF} \
   -Duse_cmake_find_blas=ON \
   %nil

%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files
%doc README.md CHANGELOG.md INSTALL.md LICENSE
%_libdir/lib%{nomen}*.so.*


%files         devel
%doc README.md CHANGELOG.md INSTALL.md LICENSE
%_libdir/lib%{nomen}*.so
%_includedir/blas.hh
%_includedir/blas/*
%_cmakedir/%nomen/


%changelog
* Mon Apr 13 2026 Pavel Skrylev <majioa@altlinux.org> 2025.05.28-alt1.1
- ! replaced direct dep to devel with cmake-like oblique dep

* Fri Apr 10 2026 Pavel Skrylev <majioa@altlinux.org> 2025.05.28-alt1
- initial build for Sisyphus
