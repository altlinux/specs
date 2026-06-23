%define soname 0

Name: shader-slang
Version: 2026.11
Release: alt1

Summary: Slang shading language compiler

License: Apache-2.0 WITH LLVM-exception
Group: Development/Tools
Url: https://github.com/shader-slang/slang

# Source-url: https://github.com/shader-slang/slang.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: glslang-devel libspirv-tools-devel spirv-headers
BuildRequires: vulkan-headers libunordered_dense-devel
BuildRequires: python3

%description
Slang is a shading language that extends HLSL with modern features such
as generics, interfaces, modules and automatic differentiation. It can
compile shaders to a variety of targets including SPIR-V, HLSL, GLSL,
Metal and CUDA.

This package provides the standalone slangc compiler.

# The library subpackages are named after the source package (libshader-slang*)
# rather than after the on-disk soname (libslang-compiler.so.0) on purpose: the
# libslang* namespace is already taken in ALT by the unrelated S-Lang extension
# language (libslang2). Naming them libshader-slang0/-devel keeps both stacks
# co-installable.
%package -n lib%name%soname
Summary: Slang runtime libraries
Group: System/Libraries

%description -n lib%name%soname
Slang is a shading language that extends HLSL with modern features.

This package provides the shared libraries needed to run slangc and to
embed the Slang compiler into applications.

%package -n lib%name-devel
Summary: Development files for Slang
Group: Development/C++
Requires: lib%name%soname = %EVR

%description -n lib%name-devel
Slang is a shading language that extends HLSL with modern features.

This package provides headers, CMake configuration and pkgconfig files
for developing applications that use the Slang compiler library.

%prep
%setup

# Upstream hardcodes the shared library install dir (and the runtime RPATH),
# the standard module dir and the pkgconfig dir to "lib"; make them follow the
# system libdir so everything lands in %_lib.
sed -i 's|^set(library_subdir lib)|set(library_subdir %_lib)|' \
    cmake/SlangTarget.cmake
sed -i 's|set(slang_library_dir "lib")|set(slang_library_dir "%_lib")|' \
    source/standard-modules/CMakeLists.txt
sed -i 's|DESTINATION "lib/pkgconfig"|DESTINATION "%_lib/pkgconfig"|' \
    CMakeLists.txt
sed -i 's|^        DESTINATION lib$|        DESTINATION %_lib|' \
    source/slang/CMakeLists.txt

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DSLANG_VERSION=%version \
    -DSLANG_ENABLE_SLANGC=ON \
    -DSLANG_ENABLE_SLANGD=OFF \
    -DSLANG_ENABLE_SLANGI=OFF \
    -DSLANG_ENABLE_SLANGRT=ON \
    -DSLANG_ENABLE_GFX=OFF \
    -DSLANG_ENABLE_SLANG_RHI=OFF \
    -DSLANG_ENABLE_TESTS=OFF \
    -DSLANG_ENABLE_EXAMPLES=OFF \
    -DSLANG_ENABLE_REPLAYER=OFF \
    -DSLANG_ENABLE_DXIL=OFF \
    -DSLANG_SLANG_LLVM_FLAVOR=DISABLE \
    -DSLANG_ENABLE_SLANG_GLSLANG=ON \
    -DSLANG_USE_SYSTEM_GLSLANG=ON \
    -DSLANG_USE_SYSTEM_SPIRV_TOOLS=ON \
    -DSLANG_USE_SYSTEM_SPIRV_HEADERS=ON \
    -DSLANG_USE_SYSTEM_VULKAN_HEADERS=ON \
    -DSLANG_USE_SYSTEM_UNORDERED_DENSE=ON \
    -DSLANG_USE_SYSTEM_LZ4=OFF \
    -DSLANG_USE_SYSTEM_MINIZ=OFF \
    %nil
# slang-bootstrap and slangc are run at build time (to embed the core module
# and to precompile the standard modules); they link against libraries in the
# build output dirs, which are not on the loader path during the build.
# The per-arch output dir is named <cpu>-alt-linux (x86_64/i586/aarch64/...),
# so resolve it with a glob to stay architecture-independent (exactly one such
# dir exists during the build).
archdir=$(echo $PWD/*-alt-linux)
export LD_LIBRARY_PATH=$archdir/Release/%_lib:$archdir/generators/Release/%_lib
%cmake_build

%install
%cmake_install

# The generated pkgconfig file hardcodes libdir=${prefix}/lib regardless of the
# system libdir; point it at %_lib so pkg-config --libs returns the right path.
sed -i 's|^libdir=${prefix}/lib$|libdir=${prefix}/%_lib|' \
    %buildroot%_pkgconfigdir/slang-compiler.pc

# Drop the documentation source tree that upstream installs via CPack
# (duplicates %doc and pulls in build scripts and assets).
# Upstream uses the literal project name "slang" for this path.
rm -rv %buildroot%_datadir/doc/slang

# Drop the deprecated backward-compatibility symlink libslang.so -> libslang-compiler.so.
# It collides with /usr/lib64/libslang.so from libslang2-devel (the unrelated S-Lang
# extension language). Modern consumers link via the CMake config (slang::slang) or
# the slang-compiler.pc pkgconfig file, both pointing at libslang-compiler.so.
rm -v %buildroot%_libdir/libslang.so

%files
%doc README.md
%_bindir/slang
%_bindir/slangc

%files -n lib%name%soname
%_libdir/libslang-compiler.so.*
%_libdir/libslang-rt.so.*
%_libdir/libslang-glslang-*.so
%_libdir/libslang-glsl-module-*.so
%_libdir/slang-standard-module-*/

%files -n lib%name-devel
%_includedir/*
%_libdir/libslang-compiler.so
%_libdir/libslang-rt.so
# Upstream uses the literal project name "slang" for the CMake config dir.
%_libdir/cmake/slang/
%_pkgconfigdir/*.pc

%changelog
* Wed Jun 17 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.11-alt1
- initial build for ALT Sisyphus (2026.11)
- named the package shader-slang to match other distributions and to avoid
  clashing with the unrelated S-Lang library (libslang2)

