%define llvmversion 16
%define git %nil

Name: spirv-llvm%llvmversion.0-translator
Version: 16.0.22
Release: alt1

Summary: LLVM %llvmversion to SPIRV Translator
License: NCSA
Group: Development/C++

Url: https://github.com/KhronosGroup/SPIRV-LLVM-Translator
# Source-url: https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: llvm%llvmversion.0-devel
BuildRequires: spirv-headers
BuildRequires: libspirv-tools-devel
BuildRequires: libstdc++-devel
BuildRequires: zlib-devel
BuildRequires: mlir%llvmversion.0-tools
BuildRequires: libmlir%llvmversion.0-devel
BuildRequires: libpolly%llvmversion.0-devel

Patch: spirv-llvm16.0-translator-16.0.22-alt-rename-pc-file.patch

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
Conflicts: libspirv-llvm14.0-translator-devel, libspirv-llvm15.0-translator-devel

%description -n lib%name-devel
%name development headers.

%package -n llvm%llvmversion-spirv
Summary: %name translator CLI
Group: Development/C++
Requires: lib%name = %EVR
Conflicts: llvm-spirv
Conflicts: llvm14-spirv, llvm15-spirv

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
* Mon Mar 16 2026 L.A. Kostis <lakostis@altlinux.ru> 16.0.22-alt1
- 16.0.22.

* Fri Dec 19 2025 L.A. Kostis <lakostis@altlinux.ru> 15.0.19-alt1
- 15.0.19.

* Wed Oct 22 2025 L.A. Kostis <lakostis@altlinux.ru> 15.0.15-alt2.g9c47ecad
- 15.0.15 GIT 9c47ecad.

* Wed Aug 27 2025 L.A. Kostis <lakostis@altlinux.ru> 15.0.15-alt1.gbef3fbc4
- 15.0.15 GIT bef3fbc4 (for latest IGC).

* Tue May 13 2025 Andrey Kovalev <ded@altlinux.org> 15.0.12-alt1
- initial build for ALT Sisyphus
