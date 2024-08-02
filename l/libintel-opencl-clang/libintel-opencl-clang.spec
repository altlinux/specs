Name: libintel-opencl-clang
Version: 18.1.0
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
BuildRequires: llvm18.1-devel
BuildRequires: clang18.1-devel
BuildRequires: zlib-devel
BuildRequires: libLLVMSPIRVLib-devel

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

%build
%cmake \
    -DLLVM_DIR=%_libexecdir/llvm-18.1/lib64/cmake/llvm/
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
* Thu Aug 01 2024 Boris Yumankulov <boria138@altlinux.org> 18.1.0-alt1
- initial build for ALT Sisyphus

