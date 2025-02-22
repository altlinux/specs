Name: libintel-opencl-clang
Version: 19.1.0
Release: alt1

Summary: Library to compile OpenCL C kernels to SPIR-V modules
License: NCSA
Group: Development/C++

Url: https://github.com/intel/opencl-clang
# Source-url: https://github.com/intel/opencl-clang/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

ExcludeArch: i586

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: llvm19.1-devel
BuildRequires: clang19.1-devel
BuildRequires: zlib-devel
BuildRequires: libLLVMSPIRVLib-devel
BuildRequires: libstdc++-devel

%description
opencl-clang is a thin wrapper library around clang. The library has OpenCL-oriented API and
is capable to compile OpenCL C kernels to SPIR-V modules.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
This package contains libraries and header files for
developing against %name

%prep
%setup
%__subst 's/$<TARGET_FILE:clang>/$<TARGET_FILE:clang18.1>/' cl_headers/CMakeLists.txt

%build
%cmake \
    -DLLVM_DIR=%_libexecdir/llvm-19.1/lib64/cmake/llvm/
%cmake_build

%install
%cmake_install

%files
%doc LICENSE
%_libdir/libopencl-clang.so.*

%files devel
%_libdir/libopencl-clang.so
%_includedir/cclang/

%changelog
* Tue Dec 24 2024 Boris Yumankulov <boria138@altlinux.org> 19.1.0-alt1
- new version 19.1.0 (ALT bug: 52502)

* Sat Aug 03 2024 Boris Yumankulov <boria138@altlinux.org> 18.1.0-alt1.1
- pack forget common_clang.h

* Thu Aug 01 2024 Boris Yumankulov <boria138@altlinux.org> 18.1.0-alt1
- initial build for ALT Sisyphus

