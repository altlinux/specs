%define _unpackaged_files_terminate_build 1

%def_with devel

Name:    FP16
Epoch: 	 1
Version: 0
Release: alt0.git98b0a46

Summary: Conversion to/from half-precision floating point formats
License: MIT
Group:   Development/C++
Url:     https://github.com/Maratyszcza/FP16

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
Header-only library for conversion to/from half-precision floating point formats

* Supports IEEE and ARM alternative half-precision floating-point format
  *  Property converts infinities and NaNs
  *  Properly converts denormal numbers, even on systems without denormal
     support
* Header-only library, no installation or build required
* Compatible with C99 and C++11
* Fully covered with unit tests and microbenchmarks

%if_with devel
%package devel
Summary: Conversion to/from half-precision floating point format
Group: Other
Provides: %name-static = %EVR

%description devel
Header-only library for conversion to/from half-precision floating point formats

* Supports IEEE and ARM alternative half-precision floating-point format
  *  Property converts infinities and NaNs
  *  Properly converts denormal numbers, even on systems without denormal
     support
* Header-only library, no installation or build required
* Compatible with C99 and C++11
* Fully covered with unit tests and microbenchmarks
%endif

%prep
%setup

%build
%cmake \
  -DFP16_BUILD_TESTS=OFF \
  -DFP16_BUILD_BENCHMARKS=OFF
%cmake_build

%install
%cmake_install

%if_with devel
%files devel
%doc LICENSE *.md
%_includedir/fp16.h
%_includedir/fp16/
%endif

%changelog
* Mon Jun 01 2026 Nikita Shmatko <nash@altlinux.org> 1:0-alt0.git98b0a46
- Fixed git snapshot versioning to keep future upstream releases upgradeable.

* Wed Sep 17 2025 Nikita Shmatko <nash@altlinux.org> 1.0.git98b0a46-alt1
- Initial build for Sisyphus.
