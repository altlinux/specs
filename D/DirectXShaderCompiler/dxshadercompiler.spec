%define sover 3
%define git 6f204c7
%define rname dxcompiler

Name: DirectXShaderCompiler
Version: 1.6.2112
Release: alt0.1.g%{git}

Summary: DirectX Shader Compiler
Group: Development/C++
License: Apache-2.0 with LLVM-exception

URL: https://github.com/microsoft/DirectXShaderCompiler
Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %name-%version.tar
Patch: alt-spirv-tools-shared.patch

# same as AMDVLK
# anyway ppc64le doesn't compile
ExclusiveArch: %ix86 x86_64

BuildRequires(pre): cmake
BuildRequires: gcc-c++ ninja-build spirv-headers libspirv-tools-devel python3-devel git-core

%description
The DirectX Shader Compiler project includes a compiler and related tools used
to compile High-Level Shader Language (HLSL) programs into DirectX Intermediate
Language (DXIL) representation. Applications that make use of DirectX for
graphics, games, and computation can use it to generate shader programs.

%package -n lib%{rname}-devel
Summary: %name devel libraries and headers
Group: Development/C++
Requires: lib%{rname}%{sover} = %EVR

%description -n lib%{rname}-devel
%name development libraries

%package -n lib%{rname}%{sover}
Summary: %name support libraries
Group: System/Libraries
Provides: lib%{rname} = %EVR

%description -n lib%{rname}%{sover}
%name support libraries

%prep
%setup -n %name-%version
%patch -p1

%build
%cmake \
  -GNinja \
  -DCMAKE_C_COMPILER=gcc \
  -DCMAKE_CXX_COMPILER=c++ \
  -DSPIRV-Headers_SOURCE_DIR=%_prefix \
  -DSPIRV_BUILD_TESTS=OFF \
  -C ./cmake/caches/PredefinedParams.cmake
%cmake_build

%install
mkdir -p %buildroot{%_libdir,%_bindir}
cp -ar %_cmake__builddir/lib/lib%{rname}.so* %buildroot%_libdir/
cp -ar %_cmake__builddir/bin/dxc* %buildroot%_bindir/

%files -n lib%{rname}%{sover}
%_libdir/lib%{rname}.so.*

%files -n lib%{rname}-devel
%_bindir/*
%_libdir/lib%{rname}.so

%changelog
* Sat Oct 15 2022 L.A. Kostis <lakostis@altlinux.ru> 1.6.2112-alt0.1.g6f204c7
- initial build for ALTLinux.
- Compile only library and dxc tool (as required by AMDVLK driver).
