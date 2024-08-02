%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: libvc-intrinsics
Version: 0.19.0
Release: alt1

Summary: Set of new intrinsics on top of core LLVM IR instructions that represent SIMD semantics of a program targeting GPU
License: MIT
Group: Development/C++

Url: https://github.com/intel/vc-intrinsics
# Source-url: https://github.com/intel/vc-intrinsics/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: llvm-devel
BuildRequires: llvm-devel-static

%description
VC Intrinsics project contains a set of new intrinsics on top of core LLVM IR instructions
that represent SIMD semantics of a program targeting GPU.

%package devel
Summary: Development files for LLVM  VC Intrinsics
Group: Development/C++
Requires: %name-devel-static = %EVR

%description devel
This package contains libraries and header files for
developing against vc-intrinsics built against LLVM.

%package devel-static
Summary: The static library for %name
Group: Development/C++

%description devel-static
%summary

%prep
%setup

%build
%cmake -DLLVM_DIR=%_libdir/cmake/llvm -DCMAKE_BUILD_TYPE=Release -DLLVM_INCLUDE_TESTS=OFF -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files devel
%doc LICENSE.md
%_libdir/cmake/VCIntrinsics*/
%_libdir/cmake/LLVMGenXIntrinsics/
%_includedir/llvm/GenXIntrinsics/

%files devel-static
%_libdir/libLLVMGenXIntrinsics.a

%changelog
* Wed Jul 31 2024 Boris Yumankulov <boria138@altlinux.org> 0.19.0-alt1
- initial build for ALT Sisyphus

