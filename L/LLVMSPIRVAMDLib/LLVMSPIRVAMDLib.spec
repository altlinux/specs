%define _unpackaged_files_terminate_build 1
%define llvm_ver_major 22.1
%define rocm_ver 7.2.1

# FIXME!
%define optflags_lto %nil

Name:    LLVMSPIRVAMDLib
Version: %rocm_ver
Release: alt1
Summary: A tool and a library for bi-directional translation between SPIR-V and LLVM IR
Group:   Development/C++
License: MIT
URL:     https://github.com/ROCm/SPIRV-LLVM-Translator
Vcs:	 https://github.com/ROCm/SPIRV-LLVM-Translator

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: %name-alt-inc.patch
Patch2: 15a4c73b0ae57e66f18d11ff23211bfcd44ebb01.patch
Patch3: 1892e566b544c9fe444e84c0c3dd097b102f7a31.patch
Patch4: fa34c816bb283f0357af35d0e55514f5b600cfb9.patch

BuildRequires(pre): cmake
BuildRequires: llvm%{llvm_ver_major}-devel gcc-c++ libstdc++-devel zlib-devel
BuildRequires: libspirv-tools-devel spirv-headers >= 1.5.5-alt20

%description
LLVM/SPIR-V Bi-Directional Translator, a library and tool for translation
between LLVM IR and SPIR-V.

This repository contains a temporary fork which includes changes that are
currently necessary for the generation and subsequent consumption of AMDGCN
flavoured SPIR-V. These changes will be upstreamed, where feasible, or
superseded by generic alternatives, and hence should be regarded as ephemeral
(please do not form any dependencies on anything but superficial semantics).

%package -n lib%name
Summary: %name translator library
Group: System/Libraries

%description -n lib%name
LLVM/SPIR-V Bi-Directional Translator, a library and tool for translation
between LLVM IR and SPIR-V.

This is the AMD-maintained fork of the SPIRV-LLVM_Translator.

%package -n lib%name-devel
Summary: %name static libraries
Group: Development/C++
Requires: lib%name = %EVR, llvm%{llvm_ver_major}-devel

%description -n lib%name-devel
%name development headers.

%package -n amd-llvm-spirv
Summary: %name translator CLI
Group: Development/C++
Requires: lib%name = %EVR

%description -n amd-llvm-spirv
command line utility for translating between LLVM bitcode and SPIR-V binary.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%cmake \
  -DLLVM_DIR=%_libexecdir/llvm-%{llvm_ver_major}/%_lib/cmake/llvm \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_STATIC_LIBS:BOOL=OFF \
  -DBASE_LLVM_VERSION=%{llvm_ver_major}.1 \
  -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=%_includedir \
  -DLLVM_SPIRV_BUILD_EXTERNAL=YES
%cmake_build

%install
%cmake_install

%files -n lib%name
%doc LICENSE.TXT
%doc *.md
%_libdir/*%name.so.*

%files -n lib%name-devel
%doc docs/*
%_includedir/%name
%_pkgconfigdir/%name.pc
%_libdir/*.so

%files -n amd-llvm-spirv
%_bindir/amd-llvm-spirv

%changelog
* Sun Apr 26 2026 L.A. Kostis <lakostis@altlinux.ru> 7.2.1-alt1
- Initial build for ALTLinux.
