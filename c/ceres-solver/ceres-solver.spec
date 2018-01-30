# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ liblapack-devel openmpi-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ceres-solver
Version:        1.13.0
# Release candidate versions are messy. Give them a release of
# e.g. "0.1.0%{?dist}" for RC1 (and remember to adjust the Source0
# URL). Non-RC releases go back to incrementing integers starting at 1.
Release:        alt1_1
Summary:        A non-linear least squares minimizer

Group:          Development/Other
License:        BSD

URL:            http://ceres-solver.org/
Source0:        http://%{name}.org/%{name}-%{version}.tar.gz
# Temporary workaround for bogus gflags-config.cmake, see #1359776
Patch1:         ceres-solver_gflags.patch
%if 0%{?rhel} > 0 && 0%{?rhel} < 7
# Exclude ppc64 because suitesparse is not available on ppc64
# https://lists.fedoraproject.org/pipermail/epel-devel/2015-May/011193.html
ExcludeArch: ppc64
%endif

%if (0%{?rhel} && 0%{?rhel} <= 7)
BuildRequires:  ccmake cmake ctest
%else
BuildRequires:  ctest cmake
%endif

# Need -static package per guidelines for handling dependencies on header-only
# libraries.
# http://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_Header_Only_Libraries
BuildRequires:  eigen3-devel >= 3.2.1

# suitesparse < 3.4.0-9 ships without *.hpp C++ headers
# https://bugzilla.redhat.com/show_bug.cgi?id=1001869
BuildRequires:  libsuitesparse-devel >= 3.4.0

# If the suitesparse package was built with TBB then we need TBB too
BuildRequires:  tbb-devel

# Use atlas for BLAS and LAPACK
BuildRequires:  libatlas-devel
BuildRequires:  libgflags-devel
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
Summary:        A non-linear least squares minimizer
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       eigen3

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch1 -p1

%build
mkdir build
pushd build

%if (0%{?rhel} == 06)
%{cmake28} .. -DMINIGLOG:BOOL=ON \
%else
%{fedora_cmake} .. \
%endif
  -DCXSPARSE_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
  -DBLAS_LIBRARIES:PATH=%{_libdir}/atlas/libsatlas.so \
  -DGFLAGS_INCLUDE_DIR=%{_includedir}
%make_build


%install
make -C build install DESTDIR=$RPM_BUILD_ROOT


%check
CTEST_OUTPUT_ON_FAILURE=1 make -C build test


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
* Tue Jan 30 2018 Igor Vlasenko <viy@altlinux.ru> 1.13.0-alt1_1
- new version

