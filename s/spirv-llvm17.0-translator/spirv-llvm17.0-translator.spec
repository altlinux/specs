%define _unpackaged_files_terminate_build 1
%define llvmversion 17
%define llvmrel 17.0.6-alt7
%define git %nil

Name: spirv-llvm%llvmversion.0-translator
Version: 17.0.27
Release: alt1

Summary: LLVM %llvmversion tool and a library for bi-directional translation between SPIR-V and LLVM IR
License: NCSA
Group: Development/C++

Url: https://github.com/KhronosGroup/SPIRV-LLVM-Translator
# Source-url: https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: llvm%llvmversion.0-devel >= %llvmrel
BuildRequires: spirv-headers >= 1.5.5-alt26
BuildRequires: libspirv-tools-devel >= 2026.3-alt0.1
BuildRequires: libstdc++-devel
BuildRequires: zlib-devel
BuildRequires: mlir%llvmversion.0-tools >= %llvmrel
BuildRequires: libmlir%llvmversion.0-devel >= %llvmrel
BuildRequires: libpolly%llvmversion.0-devel >= %llvmrel

Patch: spirv-llvm17.0-translator-alt-rename-pc-file.patch

# due strict dependency to llvm17.0 patches
ExclusiveArch: x86_64

%description
Khronos LLVM %llvmversion to SPIRV Translator. This is a library
to be used by Mesa for OpenCL support. It translate
LLVM IR to Khronos SPIR-V. It also includes a
standalone tool used for building libclc.

%package -n lib%name
Summary: %name translator library
Group: System/Libraries

%description -n lib%name
LLVM/SPIR-V Bi-Directional Translator, a library and tool for translation
between LLVM IR and SPIR-V.

%package -n lib%name-devel
Summary: %name static libraries
Group: Development/C++
Requires: lib%name = %EVR
Conflicts: libLLVMSPIRVLib
Conflicts: libspirv-llvm14.0-translator-devel, libspirv-llvm15.0-translator-devel libspirv-llvm16.0-translator-devel

%description -n lib%name-devel
%name development headers.

%package -n llvm%llvmversion-spirv
Summary: %name translator CLI
Group: Development/C++
Requires: lib%name = %EVR
Conflicts: llvm-spirv
Conflicts: llvm14-spirv, llvm15-spirv, llvm16-spirv

%description -n llvm%llvmversion-spirv
command line utility for translating between LLVM bitcode and SPIR-V binary.

%prep
%setup
%patch -p1

%build
%cmake \
  -DLLVM_DIR=%_libexecdir/llvm-%llvmversion.0/%_lib/cmake/llvm \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_STATIC_LIBS:BOOL=OFF \
  -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=%_includedir \
  -DLLVM_SPIRV_BUILD_EXTERNAL=YES
%cmake_build

%install
%cmake_install

%files -n lib%name
%doc LICENSE.TXT
%doc *.md
%_libdir/libLLVMSPIRVLib.so.*

%files -n lib%name-devel
%doc docs/*
%_includedir/*
%_pkgconfigdir/*.pc
%_libdir/*.so

%files -n llvm%llvmversion-spirv
%_bindir/llvm-spirv

%changelog
* Mon Sep 14 2026 L.A. Kostis <lakostis@altlinux.ru> 17.0.27-alt1
- Updated to v17.0.27.

* Sat Mar 09 2024 L.A. Kostis <lakostis@altlinux.ru> 17.0.0-alt3.g6c1910a9
- GIT 6c1910a9 (fixes FTBFS with new spirv-headers).
- disable OpenSYCL patch (needs refactoring).

* Mon Jan 08 2024 L.A. Kostis <lakostis@altlinux.ru> 17.0.0-alt2
- llvm-spirv: apply patch from OpenSYCL.

* Tue Oct 03 2023 L.A. Kostis <lakostis@altlinux.ru> 17.0.0-alt1
- Rebased to v17.0.0.

* Wed Sep 06 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.0-alt4.g322fca5d
- GIT 322fca5d.

* Mon Jul 31 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.0-alt3.g44eda7be
- GIT 44eda7be from llvm_release_160 branch.

* Sun Jun 11 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.0-alt2.g39969a5c
- Built as spirv-llvm-translator replacement.
- Enable shared libs/disable static build.

* Wed Jun 07 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.0-alt1.g39969a5c
- GIT 39969a5c.
- Rebased to v16.0.0.

* Mon Jan 09 2023 L.A. Kostis <lakostis@altlinux.ru> 15.0.0-alt2.g78ad93b9
- GIT 78ad93b9.

* Thu Oct 06 2022 L.A. Kostis <lakostis@altlinux.ru> 15.0.0-alt1
- Rebased to v15.0.0.
- Added CLI utility.

* Wed Jun 16 2021 L.A. Kostis <lakostis@altlinux.ru> 12.0.0-alt1
- Initial build for ALTLinux.
