Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: python3-devel rpm-build-python3
# END SourceDeps(oneline)
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ceres-solver
Version:        2.1.0
# Release candidate versions are messy. Give them a release of
# e.g. "0.1.0%%{?dist}" for RC1 (and remember to adjust the Source0
# URL). Non-RC releases go back to incrementing integers starting at 1.
Release:        alt1_4
Summary:        A non-linear least squares minimizer

License:        BSD

URL:            http://ceres-solver.org/
Source0:        http://%{name}.org/%{name}-%{version}.tar.gz

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global cmake_blas_flags -DBLA_VENDOR=FlexiBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif

%if 0%{?rhel} > 0 && 0%{?rhel} < 7
# Exclude ppc64 because suitesparse is not available on ppc64
# https://lists.fedoraproject.org/pipermail/epel-devel/2015-May/011193.html
ExcludeArch: ppc64
%endif

%if 0%{?rhel} == 9
# Workaround a build error with eigen3 on rhel 9
%ifarch ppc64le
%undefine _lto_cflags
%endif
%endif

%if (0%{?rhel} && 0%{?rhel} <= 7)
BuildRequires:  ccmake cmake ctest
%else
BuildRequires:  ctest cmake
%endif
BuildRequires:  gcc-c++

# Need -static package per guidelines for handling dependencies on header-only
# libraries.
# http://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_Header_Only_Libraries
BuildRequires:  eigen3 >= 3.2.1

# suitesparse < 3.4.0-9 ships without *.hpp C++ headers
# https://bugzilla.redhat.com/show_bug.cgi?id=1001869
BuildRequires:  libsuitesparse-devel >= 3.4.0

# If the suitesparse package was built with TBB then we need TBB too
BuildRequires:  tbb-devel

# Use FlexiBLAS or OpenBLAS for BLAS
BuildRequires:  libopenblas-devel
BuildRequires:  libgflags-devel >= 2.2.1
# Build against miniglog on RHEL6 until glog package is added to EPEL6
%if (0%{?rhel} != 06)
BuildRequires:  libglog-devel >= 0.3.1
%endif
Source44: import.info

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


%package        devel
Group: Development/Other
Summary:        A non-linear least squares minimizer
Requires:       %{name} = %{version}-%{release}
Requires:       eigen3

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%{fedora_v2_cmake} \
  -DCXSPARSE_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
  %{cmake_blas_flags} \
  -DGFLAGS_INCLUDE_DIR=%{_includedir}
%fedora_v2_cmake_build


%install
%fedora_v2_cmake_install


%check
# FIXME: Some tests fail on these arches
%ifarch aarch64 ppc64le s390x
%fedora_v2_ctest || :
%else
%fedora_v2_ctest
%endif





%files
%if (0%{?rhel} == 06)
%doc README.md LICENSE
%else
%doc README.md
%doc --no-dereference LICENSE
%endif
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/Ceres


%changelog
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

