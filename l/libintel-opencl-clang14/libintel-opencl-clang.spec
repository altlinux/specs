Name: libintel-opencl-clang14
Version: 14.0.0
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
BuildRequires: llvm14.0-devel
BuildRequires: clang14.0-devel
BuildRequires: zlib-devel
BuildRequires: libspirv-llvm14.0-translator-devel
BuildRequires: mlir14.0-tools
BuildRequires: libmlir14.0-devel
BuildRequires: libpolly14.0-devel
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
%__subst 's/$<TARGET_FILE:clang>/$<TARGET_FILE:clang14.0>/' cl_headers/CMakeLists.txt

%build
%cmake \
    -DLLVM_DIR=%_libexecdir/llvm-14.0/lib64/cmake/llvm/
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
* Thu Aug 29 2024 Boris Yumankulov <boria138@altlinux.org> 14.0.0-alt1
- initial build for ALT Sisyphus


