%define soversion 2
%define llvmversion 14
%define optflags_lto %nil

Name: intel-graphics-compiler
Version: 2.10.5
Release: alt1.1
Summary: Intel Graphics Compiler for OpenCL
License: MIT
Group: Development/C++
URL: https://github.com/intel/intel-graphics-compiler

Source: %name-%version.tar

Patch1: %name-2.3.1-alt-build.patch
Patch2: ffdcbc033c0ad140b898a7ccb431f2dabd5dedab.patch
Patch3: c5c2623610f37abdd9f3b12efcc4a6d42ac55773.patch
# our -Wall triggers -Werror for everything
Patch4: %name-alt-disable-werror.patch

BuildRequires(pre): rpm-build-cmake ninja-build

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
An LLVM based compiler for OpenCL targeting Intel Gen graphics hardware
architecture.

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
%autopatch1 -p1

%build
export ALTWRAP_LLVM_VERSION=%llvmversion.0
%cmake -GNinja \
  -DLLVM_DIR=%_prefix/lib/llvm-%llvmversion.0/%_lib/cmake/llvm \
  -DIGC_OPTION__LLDELF_LIB_DIR=%_prefix/lib/llvm-%llvmversion.0/%_lib/ \
  -DLLD_INCLUDE_DIR=%_prefix/lib/llvm-%llvmversion.0/include/lld \
  -DCMAKE_BUILD_TYPE=Release \
  -Wno-dev \
  -DIGC_OPTION__ARCHITECTURE_TARGET='Linux64' \
  -DIGC_OPTION__SPIRV_TOOLS_MODE=Prebuilds \
  -DIGC_OPTION__VC_INTRINSICS_MODE=Prebuilds
%cmake_build

%install
%cmake_install

pushd %buildroot%_libdir
ln -sf libigc.so.%soversion libigc.so
ln -sf libiga64.so.%soversion libiga64.so
ln -sf libigdfcl.so.%soversion libigdfcl.so
popd

%files -n libigc%soversion
%_libdir/libigc.so.%soversion
%_libdir/libigc.so.%soversion.*
%_libdir/libiga64.so.%soversion
%_libdir/libiga64.so.%soversion.*
%_libdir/igc2/NOTICES.txt

%files -n libigc-devel
%_libdir/libigc.so
%_includedir/igc
%_libdir/libiga64.so
%_includedir/iga

%files -n libigc-tools
%_bindir/iga64

%files -n libigdfcl%soversion
%_libdir/libigdfcl.so.%soversion
%_libdir/libigdfcl.so.%soversion.*

%files -n libigdfcl-devel
%_libdir/libigdfcl.so
%_includedir/visa
%_libdir/pkgconfig/igc-opencl.pc

%changelog
* Fri Apr 11 2025 L.A. Kostis <lakostis@altlinux.ru> 2.10.5-alt1.1
- NMU:
  - Explicitly disable LTO (not supported).
  - Use cmake macros. This also makes build flags consistent.
  - Use ninja-build.
  - Disable -Werror (due enabled -Wall).
  - Apply some fixes from master:
    + Fix crashes encountered during the compilation of Blender
      kernels utilizing the `SPV_INTEL_bindless_images` extension
    + Fix crash in `ProgramScopeConstantAnalysis` during
      recompilation

* Thu Apr 10 2025 Andrey Kovalev <ded@altlinux.org> 2.10.5-alt1
- Updated to upstream version 2.10.5.
- Fixed FTBFS with cmake4.

* Tue Mar 11 2025 Andrey Kovalev <ded@altlinux.org> 2.9.0-alt1
- Updated to upstream version 2.9.0.

* Mon Jan 20 2025 Andrey Kovalev <ded@altlinux.org> 2.5.9-alt1
- Updated to upstream version 2.5.9.

* Thu Dec 12 2024 Andrey Kovalev <ded@altlinux.org> 2.3.1-alt1
- Updated to upstream version 2.3.1.

* Mon Nov 11 2024 Andrey Kovalev <ded@altlinux.org> 1.0.17791.9-alt1
- Updated to upstream version 1.0.17791.9.

* Mon Sep 09 2024 Andrey Kovalev <ded@altlinux.org> 1.0.17384.11-alt1
- Initial build for Sisyphus.
