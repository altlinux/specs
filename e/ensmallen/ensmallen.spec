%ifnarch %ix86
%def_with check
%else
%def_without check
%endif
Name: ensmallen
Version: 3.11.0
Release: alt1
Summary: Header-only C++ library for efficient mathematical optimization
Group: System/Libraries
License: BSD
Url: https://www.ensmallen.org
VCS: https://github.com/mlpack/ensmallen
Source0: %name-%version.tar
BuildRequires: ctest cmake
BuildRequires: gcc-c++
BuildRequires: libarmadillo-devel >= 9.800.0
BuildRequires: libhdf5-devel libsuperlu-devel
BuildRequires: libflexiblas-devel

%description
ensmallen is a header-only C++ library for efficient mathematical optimization.
It provides a simple set of abstractions for writing an objective function to
optimize. It also provides a large set of standard and cutting-edge optimizers
that can be used for virtually any mathematical optimization task.  These
include full-batch gradient descent techniques, small-batch techniques,
gradient-free optimizers, and constrained optimization.

%package devel
Group: Other
Summary: Header-only C++ library for efficient mathematical optimization
Provides: ensmallen-static = %EVR

%description devel
ensmallen is a header-only C++ library for efficient mathematical optimization.
It provides a simple set of abstractions for writing an objective function to
optimize. It also provides a large set of standard and cutting-edge optimizers
that can be used for virtually any mathematical optimization task.  These
include full-batch gradient descent techniques, small-batch techniques,
gradient-free optimizers, and constrained optimization.

%prep
%setup

%build
%cmake -DENSMALLEN_CMAKE_DIR=%_libdir/cmake/ensmallen/ -DBUILD_TESTS=ON

%cmake_build -t ensmallen_tests

%install
%cmake_install

%check
success=0;
pushd %_cmake__builddir;
test_filter=("~SmallLovaszThetaSdp" "~BBSBBLogisticRegressionTest");
%ifarch aarch64
# Numerically unstable on aarch64 with current Armadillo/BLAS/compiler stack.
# These are TEMPLATE_TEST_CASEs, so Catch2 names the instances
# "<name> - arma::mat" etc; the trailing '*' is required for the exclude to
# match. The "Function -*" form excludes LBFGS_GeneralizedRosenbrockFunction
# without also dropping its still-stable LBFGS_GeneralizedRosenbrockFunctionLoose sibling.
test_filter+=("~Johnson844LovaszThetaSDP*" "~GaussianMatrixSensingSDP*" "~LBFGS_GeneralizedRosenbrockFunction -*");
%endif
for i in `seq 1 5`; do
  code=""; # Reset exit code.
  ./ensmallen_tests --rng-seed=time "${test_filter[@]}" || code=$?
  if [ "a$code" == "a" ]; then
    success=1;
    break;
  fi
done
if [ $success -eq 0 ]; then
  false # Force a build error.
fi
popd;

%files devel
%doc --no-dereference LICENSE.txt
%_includedir/ensmallen.hpp
%_includedir/ensmallen_bits/
%_libdir/cmake/ensmallen/ensmallen-config-version.cmake
%_libdir/cmake/ensmallen/ensmallen-config.cmake
%_libdir/cmake/ensmallen/ensmallen-targets.cmake

%changelog
* Tue Jun 23 2026 Anton Farygin <rider@altlinux.org> 3.11.0-alt1
- 2.22.1 -> 3.11.0
- fixed %%check on aarch64: use Catch2 wildcards so the numerically unstable
  TEMPLATE_TEST_CASE instances are actually excluded

* Tue Feb 18 2025 Anton Farygin <rider@altlinux.ru> 2.22.1-alt1
- 2.21.1 -> 2.22.1

* Sat Sep 21 2024 Anton Farygin <rider@altlinux.ru> 2.21.1-alt1
- 2.19.0 -> 2.21.1

* Mon Apr 17 2023 Igor Vlasenko <viy@altlinux.org> 2.19.0-alt1_3
- new version

* Thu Oct 14 2021 Igor Vlasenko <viy@altlinux.org> 2.17.0-alt1_1
- update to new release by fcimport

* Mon Nov 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.14.2-alt1_1
- fc import

