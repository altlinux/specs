%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define git 28f7cd9216

# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%ifarch %ix86 %arm mipsel
%define optflags_debug -g0
#define __nprocs 1
%else
%define optflags_debug -g1
%endif

# LTO-related flags are set by CMake.
# LTO causes LLVM to break badly on %%ix86 see
# https://github.com/llvm/llvm-project/issues/57740
# will enable it conditionally per platform
%global optflags_lto %nil

Name: clspv
Version: 0.1
Release: alt0.8.g%{git}
License: Apache-2.0
Summary: Clspv is a prototype compiler for a subset of OpenCL C to Vulkan compute shaders
Group: Development/Other
Url: https://github.com/google/clspv
Source: %name-%version.tar
Patch0: clspv-spirv-tools-link.patch

BuildRequires(pre): cmake ninja-build
BuildRequires: gcc-c++ zlib-devel libtinfo-devel spirv-headers libspirv-tools-devel python3-base

%description
Clspv is a prototype compiler for a subset of OpenCL C to Vulkan compute
shaders.

It consists of:

 - A set of LLVM Module passes to transform a dialect of LLVM IR into a SPIR-V
   module containing Vulkan compute shaders.
 - A command line compiler tool called 'clspv' to compile a subset of OpenCL C
   into a Vulkan compute shader.

%prep
%setup
%autopatch -p1

%build
export NPROCS="%__nprocs"
if [ "$NPROCS" -gt 64 ]; then
	export NPROCS=64
fi
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DSPIRV_HEADERS_SOURCE_DIR=%_prefix \
    -DSPIRV_TOOLS_SOURCE_DIR=%_prefix \
    -DSPIRV_TOOLS_BINARY_DIR=%_prefix \
    -DCLSPV_BUILD_SPIRV_DIS=OFF \
    -DCLSPV_BUILD_TESTS=OFF \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    %nil
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_libdir/*.a

#%%check
#cmake --build "%_cmake__builddir" --target check-spirv

%files
%doc README.md LICENSE CONTRIBUTING.md CONTRIBUTORS AUTHORS docs
%_bindir/*
%_includedir/%name

%changelog
* Mon Jul 29 2024 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.8.g28f7cd9216
- GIT 28f7cd9216.

* Tue Jan 09 2024 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.7.g3617a5d662
- GIT 3617a5d662.

* Wed Nov 08 2023 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.6.gd9d9172be7
- GIT d9d9172be7.
- Try to enable all arches again (with some build tweaks applied).

* Sat Nov 04 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.1-alt0.5.g2c1e7c4a42
- spec: build on LoongArch too.

* Thu Sep 21 2023 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.5.gf43601e423
- Rebuild with updated spirv-tools/headers.

* Thu Aug 31 2023 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.4.g2c1e7c4a42
- .spec: limit build arches to 64-bit only.

* Thu Aug 31 2023 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.3.g2c1e7c4a42
- GIT 2c1e7c4a42.

* Wed Jul 26 2023 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.2.ga6873b627b
- GIT a6873b627b.

* Fri Jun 23 2023 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.1.gd1b618bf
- Initial build for ALTLinux.
