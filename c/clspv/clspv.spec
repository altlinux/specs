%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define git 2c1e7c4a42
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%define optflags_debug -g1

Name: clspv
Version: 0.1
Release: alt0.5.g%{git}
License: Apache-2.0
Summary: Clspv is a prototype compiler for a subset of OpenCL C to Vulkan compute shaders
Group: Development/Other
Url: https://github.com/google/clspv
Source: %name-%version.tar
Patch0: clspv-spirv-tools-link.patch

# armh doesn't compile due memory limits
# i586 fails with error: stat(lib/libclspv_combined.a): Value too large for defined data type.
ExclusiveArch: x86_64 aarch64 ppc64le loongarch64

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
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
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
* Sat Nov 04 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.1-alt0.5.g2c1e7c4a42
- spec: build on LoongArch too.

* Thu Aug 31 2023 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.4.g2c1e7c4a42
- .spec: limit build arches to 64-bit only.

* Thu Aug 31 2023 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.3.g2c1e7c4a42
- GIT 2c1e7c4a42.

* Wed Jul 26 2023 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.2.ga6873b627b
- GIT a6873b627b.

* Fri Jun 23 2023 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt0.1.gd1b618bf
- Initial build for ALTLinux.
