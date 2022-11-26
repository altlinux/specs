%define sover 3
%define git 6f204c7
%define rname dxcompiler
%define llvm_ver 13.0
%define gcc_ver 9

%define optflags_lto %nil

%def_without clang
%def_with gcc

Name: DirectXShaderCompiler
Version: 1.6.2112
Release: alt0.4.g%{git}

Summary: DirectX Shader Compiler
Group: Development/C++
License: Apache-2.0 with LLVM-exception

URL: https://github.com/microsoft/DirectXShaderCompiler
Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %name-%version.tar
Patch0: alt-spirv-tools-shared.patch

ExclusiveArch: %ix86 x86_64 aarch64

BuildRequires(pre): cmake
BuildRequires: ninja-build spirv-headers libspirv-tools-devel python3-devel git-core
%if_with clang
BuildRequires: clang%{llvm_ver} llvm%{llvm_ver}-devel libstdc++-devel
%else
BuildRequires: gcc%{gcc_ver}-c++ libstdc++%{gcc_ver}-devel
%endif

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
%autopatch -p1

%build
%if_with gcc
export GCC_VERSION=%{gcc_ver} \
%endif
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
%if_with clang
  -DCMAKE_C_COMPILER=clang \
  -DCMAKE_CXX_COMPILER=clang++ \
%else
  -DCMAKE_C_COMPILER=gcc \
  -DCMAKE_CXX_COMPILER=c++ \
%endif
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
* Fri Nov 25 2022 L.A. Kostis <lakostis@altlinux.ru> 1.6.2112-alt0.4.g6f204c7
- Compile w/ gcc9.
- Add clang support (still doesn't compile).

* Fri Nov 25 2022 L.A. Kostis <lakostis@altlinux.ru> 1.6.2112-alt0.3.g6f204c7
- Added some fixes from upstream:
  + Fix-incorrect-REGDB_E_CLASSNOTREG-value
  + DxbcConverter-Fix-corruption-of-ICB-integer-values
- Enable aarch64.

* Wed Nov 23 2022 L.A. Kostis <lakostis@altlinux.ru> 1.6.2112-alt0.2.g6f204c7
- Disable LTO (cause problems on ix86).
- Set cmake release target.

* Sat Oct 15 2022 L.A. Kostis <lakostis@altlinux.ru> 1.6.2112-alt0.1.g6f204c7
- initial build for ALTLinux.
- Compile only library and dxc tool (as required by AMDVLK driver).
