%define _unpackaged_files_terminate_build 1

%def_with devel

Name:    fxdiv
Epoch:   1
Version: 0
Release: alt0.git63058ef

Summary: C99/C++ header-only library for division via fixed-point multiplication by inverse
License: MIT
Group:   Development/C
Url:     https://github.com/Maratyszcza/FXdiv

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
Header-only library for division via fixed-point multiplication by inverse

On modern CPUs and GPUs integer division is several times slower
than multiplication. FXdiv implements an algorithm to replace an
integer division with a multiplication and two shifts. This
algorithm improves performance when an application performs repeated
divisions by the same divisor.

Features
  * Integer division for uint32_t, uint64_t, and size_t
  * Header-only library, no installation or build required
  * Compatible with C99, C++, OpenCL, and CUDA
  * Uses platform-specific compiler intrinsics for optimal performance
  * Covered with unit tests and microbenchmarks

%if_with devel
%package devel
Summary: Header for division via fixed-point math
Group: Development/C
Provides: %name = %EVR

%description devel
Header-only library for division via fixed-point multiplication by inverse

On modern CPUs and GPUs integer division is several times slower
than multiplication. FXdiv implements an algorithm to replace an
integer division with a multiplication and two shifts. This
algorithm improves performance when an application performs repeated
divisions by the same divisor.

Features
  * Integer division for uint32_t, uint64_t, and size_t
  * Header-only library, no installation or build required
  * Compatible with C99, C++, OpenCL, and CUDA
  * Uses platform-specific compiler intrinsics for optimal performance
  * Covered with unit tests and microbenchmarks
%endif

%prep
%setup -n %name-%version

%build
%cmake \
  -DFXDIV_BUILD_TESTS=OFF \
  -DFXDIV_BUILD_BENCHMARKS=OFF \

%cmake_build

%install
%cmake_install

%if_with devel
%files devel
%doc LICENSE *.md
%_includedir/fxdiv.h
%endif

%changelog
* Tue Jun 02 2026 Nikita Shmatko <nash@altlinux.org> 1:0-alt0.git63058ef
- Fixed git snapshot versioning to keep future upstream releases upgradeable.

* Mon Oct 13 2025 Nikita Shmatko <nash@altlinux.org> 1.0.git63058ef-alt1
- Initial build for Sisyphus.
