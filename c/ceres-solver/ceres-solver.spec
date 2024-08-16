%ifarch %ix86
%define check_relax ||:
%else
%define check_relax %nil
%endif
%define ceres_soname 4
Name: ceres-solver
Version: 2.2.0
Release: alt2
Summary: A non-linear least squares minimizer
Group: Development/Other
License: BSD
Url: https://ceres-solver.org/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: gcc-c++
BuildRequires(pre): rpm-macros-cmake
BuildRequires: python3-devel rpm-build-python3 cmake ctest
BuildRequires: libglog-devel
BuildRequires: eigen3 >= 3.2.1
BuildRequires: libsuitesparse-devel >= 7.7.0
BuildRequires: tbb-devel
BuildRequires: libflexiblas-devel
BuildRequires: libgflags-devel >= 2.2.1

%description
Ceres Solver is an open source C++ library for modeling and solving
large, complicated optimization problems. It is a feature rich, mature
and performant library which has been used in production at Google
since 2010. Notable use of Ceres Solver is for the image alignment in
Google Maps and for vehicle pose in Google Street View. Ceres Solver
can solve two kinds of problems.

  1. Non-linear Least Squares problems with bounds constraints.
  2. General unconstrained optimization problems.

Features include:

  - A friendly API: build your objective function one term at a time
  - Automatic and numeric differentiation
  - Robust loss functions
  - Local parameterizations
  - Threaded Jacobian evaluators and linear solvers
  - Trust region solvers with non-monotonic steps (Levenberg-Marquardt and
    Dogleg (Powell & Subspace))
  - Line search solvers (L-BFGS and Nonlinear CG)
  - Dense QR and Cholesky factorization (using Eigen) for small problems
  - Sparse Cholesky factorization (using SuiteSparse) for large sparse problems
  - Specialized solvers for bundle adjustment problems in computer vision
  - Iterative linear solvers for general sparse and bundle adjustment problems
  - Runs on Linux, Windows, Mac OS X, Android, and iOS

%package -n libceres%ceres_soname
Summary: A non-linear least squares minimizer (Shared library)
Group: Sciences/Computer science
%description -n libceres%ceres_soname
Ceres Solver is an open source C++ library for modeling and solving large,
complicated optimization problems.
It is a feature rich, mature and performant library which has been used
in production at Google since 2010.

Ceres Solver can solve two kinds of problems.
 - Non-linear Least Squares problems with bounds constraints.
 - General unconstrained optimization problems.

This package contains the shared library.

%package devel
Group: Development/Other
Summary: A non-linear least squares minimizer
Requires: libceres%ceres_soname = %EVR
Requires: eigen3
Requires: libgflags-devel
Requires: libsuitesparse-devel
Provides: libsolver-devel = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%cmake \
  -DCMAKE_CXX_FLAGS="-DGLOG_USE_GLOG_EXPORT" \
  -DCXSPARSE_INCLUDE_DIR:PATH=%_includedir/suitesparse \
  -DBLA_VENDOR=FlexiBLAS \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=ON \
  -DBUILD_SHARED_LIBS=ON \
  -DGFLAGS_INCLUDE_DIR=%_includedir
%cmake_build

%install
%cmake_install
rm -f %buildroot%_libdir/cmake/Ceres/FindGlog.cmake

%check
%ctest %check_relax

%files -n libceres%ceres_soname
%doc README.md
%doc LICENSE
%_libdir/*.so.%ceres_soname
%_libdir/*.so.%version

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/Ceres

%changelog
* Tue Jun 04 2024 Anton Farygin <rider@altlinux.ru> 2.2.0-alt2
- fixed the build against glog 0.7.0

* Tue May 21 2024 Anton Farygin <rider@altlinux.ru> 2.2.0-alt1
- 2.1.0 -> 2.2.0
- package with shared library was renamed according shared libs policy

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 2.1.0-alt1_4
- update to new release by fcimport

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 2.1.0-alt1_1
- update to new release by fcimport

* Fri Jan 28 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt2_6
- Rebuilt with new TBB.

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt1_6
- update to new release by fcimport

* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt1_4
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_2
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_1
- update to new release by fcimport

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.13.0-alt1_8
- update to new release by fcimport

* Tue Jan 30 2018 Igor Vlasenko <viy@altlinux.ru> 1.13.0-alt1_1
- new version

