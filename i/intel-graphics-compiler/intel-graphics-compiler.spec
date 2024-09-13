%define soversion 1
%define llvmversion 14

Name: intel-graphics-compiler
Version: 1.0.17384.11
Release: alt1
Summary: Intel Graphics Compiler for OpenCL
License: MIT
Group: Development/C++
URL: https://github.com/intel/intel-graphics-compiler

Source: %name-%version.tar

Patch1: %name-1.0.17384.11-alt-build.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: flex
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-module-mako
BuildRequires: python3-module-yaml
BuildRequires: spirv-headers
BuildRequires: spirv-tools
BuildRequires: clang%llvmversion.0
BuildRequires: lld%llvmversion.0-devel
BuildRequires: libspirv-tools-devel
BuildRequires: libspirv-llvm%llvmversion.0-translator-devel
BuildRequires: llvm%llvmversion-spirv
BuildRequires: llvm%llvmversion.0-devel
BuildRequires: llvm%llvmversion.0-polly
BuildRequires: libpolly%llvmversion.0-devel
BuildRequires: mlir%llvmversion.0-tools
BuildRequires: libmlir%llvmversion.0-devel
BuildRequires: libvc-intrinsics-devel
BuildRequires: libvc-intrinsics-devel-static
BuildRequires: libintel-opencl-clang%llvmversion-devel
BuildRequires: zlib-devel

ExclusiveArch: x86_64

%description
Intel Graphics Compiler for OpenCL.

%package -n libigc%soversion
Summary: Library for Intel Graphics Compiler
Group: System/Libraries

%description -n libigc%soversion
An LLVM based compiler for OpenCL targeting Intel Gen graphics hardware architecture.

%package -n libigc-devel
Summary: Headers for the Intel Graphics Compiler library
Group: System/Libraries
Requires: libigc%soversion = %EVR

%description -n libigc-devel
This package contains development files for libigc.

%package -n libigc-tools
Summary:  Tools for the Intel Graphics Compiler library
Group: Development/Tools
Requires: libigc%soversion = %EVR

%description -n libigc-tools
This package includes tools for the media driver.

%package -n libigdfcl%soversion
Summary: Intel Graphics Frontend Compiler library
Group: System/Libraries

%description -n libigdfcl%soversion
Library files for the Intel Graphics Frontend Compiler.

%package -n libigdfcl-devel
Summary: Headers for the Intel Graphics Frontend Compiler library
Group: System/Libraries
Requires: libigdfcl%soversion = %EVR

%description -n libigdfcl-devel
This package contains development files for libigdfcl.

%prep
%setup
%patch1 -p1


%build
mkdir -p build
pushd build
cmake ../IGC -DLLVM_DIR=/usr/lib/llvm-%llvmversion.0/lib64/cmake/llvm/ \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DIGC_OPTION__LLDELF_LIB_DIR=/usr/lib/llvm-%llvmversion.0/lib64/ \
  -DIGC_OPTION__LLD_BIN_DIR=/usr/bin/llvm-%llvmversion.0/bin/ \
  -DCMAKE_BUILD_TYPE=Release \
  -DIGC_OPTION__ARCHITECTURE_TARGET='Linux64' \
  -DIGC_OPTION__SPIRV_TOOLS_MODE=Prebuilds \
  -DIGC_OPTION__VC_INTRINSICS_MODE=Prebuilds

%make_build
popd

%install
pushd build
%makeinstall_std
popd


%files -n libigc%soversion
%_libdir/libigc.so.%soversion
%_libdir/libigc.so.%soversion.*
%_libdir/libiga64.so.%soversion
%_libdir/libiga64.so.%soversion.*
%_libdir/igc/NOTICES.txt

%files -n libigc-devel
%_libdir/libigc.so
%_includedir/igc
%_libdir/libiga64.so
%_includedir/iga

%files -n libigc-tools
%_bindir/GenX_IR
%_bindir/iga64

%files -n libigdfcl%soversion
%_libdir/libigdfcl.so.%soversion
%_libdir/libigdfcl.so.%soversion.*

%files -n libigdfcl-devel
%_libdir/libigdfcl.so
%_includedir/visa
%_libdir/pkgconfig/igc-opencl.pc

%changelog
* Mon Sep 09 2024 Andrey Kovalev <ded@altlinux.org> 1.0.17384.11-alt1
- Initial build for Sisyphus.
