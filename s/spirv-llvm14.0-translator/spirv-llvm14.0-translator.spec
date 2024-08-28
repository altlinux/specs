Name: spirv-llvm14.0-translator
Version: 14.0.3
Release: alt1

Summary: LLVM 14 to SPIRV Translator
License: NCSA
Group: Development/C++

Url: https://github.com/KhronosGroup/SPIRV-LLVM-Translator
# Source-url: https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: llvm14.0-devel
BuildRequires: spirv-headers
BuildRequires: libspirv-tools-devel
BuildRequires: libstdc++-devel
BuildRequires: zlib-devel
BuildRequires: mlir14.0-tools
BuildRequires: libmlir14.0-devel
BuildRequires: libpolly14.0-devel

Patch: spirv-llvm14.0-translator-14.0.3-alt-rename-pc-file.patch

%description
Khronos LLVM 14 to SPIRV Translator. This is a library
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

%description -n lib%name-devel
%name development headers.

%package -n llvm14-spirv
Summary: %name translator CLI
Group: Development/C++
Requires: lib%name = %EVR
Conflicts: llvm-spirv

%description -n llvm14-spirv
command line utility for translating between LLVM bitcode and SPIR-V binary.

%prep
%setup
%patch -p1

%build
%cmake \
  -DLLVM_DIR=%_libexecdir/llvm-14.0/%_lib/cmake/llvm \
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

%files -n llvm14-spirv
%_bindir/llvm-spirv

%changelog
* Fri Aug 09 2024 Boris Yumankulov <boria138@altlinux.org> 14.0.3-alt1
- initial build for ALT Sisyphus (ALT bug: 51109)

