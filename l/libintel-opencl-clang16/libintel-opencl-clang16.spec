%define llvmversion 16

Name: libintel-opencl-clang%llvmversion
Version: 16.0.9
Release: alt1

Summary: Library to compile OpenCL C kernels to SPIR-V modules
License: NCSA
Group: Development/C++

Url: https://github.com/intel/opencl-clang
# Source-url: https://github.com/intel/opencl-clang/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch: opencl-clang-alt-libspirv-inc.patch

ExcludeArch: i586

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: llvm%llvmversion.0
BuildRequires: llvm%llvmversion.0-devel
BuildRequires: clang%llvmversion.0-devel
BuildRequires: zlib-devel
BuildRequires: libspirv-llvm%llvmversion.0-translator-devel
BuildRequires: mlir%llvmversion.0-tools
BuildRequires: libmlir%llvmversion.0-devel
BuildRequires: libpolly%llvmversion.0-devel
BuildRequires: libstdc++-devel
BuildRequires: libxml2-devel
BuildRequires: liblzma-devel

%description
opencl-clang is a thin wrapper library around clang. The library has OpenCL-oriented API and
is capable to compile OpenCL C kernels to SPIR-V modules.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR
Conflicts: libintel-opencl-clang14-devel, libintel-opencl-clang15-devel

%description devel
This package contains libraries and header files for
developing against %name

%prep
%setup
%patch -p1

%build
%cmake \
    -Wno-dev \
    -DLLVMSPIRV_INCLUDED_IN_LLVM=OFF \
    -DSPIRV_TRANSLATOR_DIR=%_prefix \
    -DLLVM_TABLEGEN_EXE:FILEPATH=%_libexecdir/llvm-%llvmversion.0/bin/llvm-tblgen \
    -DLLVM_DIR=%_libexecdir/llvm-%llvmversion.0/lib64/cmake/llvm/
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
* Mon Mar 16 2026 L.A. Kostis <lakostis@altlinux.ru> 16.0.9-alt1
- 16.0.9.

* Mon Mar 16 2026 L.A. Kostis <lakostis@altlinux.ru> 16.0.8-alt1
- 16.0.8.

* Fri Dec 19 2025 L.A. Kostis <lakostis@altlinux.ru> 15.0.5-alt1
- 15.0.5.

* Mon Nov 03 2025 L.A. Kostis <lakostis@altlinux.ru> 15.0.4-alt1
- 15.0.4.

* Sat Sep 13 2025 L.A. Kostis <lakostis@altlinux.ru> 15.0.3-alt1
- 15.0.3.

* Tue May 13 2025 Andrey Kovalev <ded@altlinux.org> 15.0.1-alt1
- initial build for ALT Sisyphus
