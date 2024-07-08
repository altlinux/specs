%define build_type RelWithDebInfo
%define optflags_lto %nil

Name: hipify-clang
Version: 6.1.2
Release: alt0.1
License: MIT
Summary: HIPIFY: Convert CUDA to Portable C++ Code
Url: https://github.com/ROCm/HIPIFY
Group: Development/C++

Source: %name-%version.tar
Patch: hipify-alt-remove-rpath.patch

BuildRequires(pre): cmake /proc
BuildRequires: llvm-rocm-devel = %version clang-rocm-devel = %version clang-rocm-tools = %version
BuildRequires: libstdc++-devel zlib-devel libtinfo-devel

Requires: llvm-rocm = %version clang-rocm = %version

ExclusiveArch: x86_64 ppc64le aarch64

%description
HIPIFY is a set of tools that you can use to automatically translate CUDA
source code into portable HIP C++.

%prep
%setup
%patch -p1

%build
export ALTWRAP_LLVM_VERSION=rocm
%cmake \
    -Wno-dev \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++
%cmake_build

%install
%cmake_install

# remove includes as they are part of clang already
rm -rf %buildroot%_includedir

%files
%doc README.md LICENSE.txt CHANGELOG.md
%_bindir/*

%changelog
* Mon Jul 08 2024 L.A. Kostis <lakostis@altlinux.ru> 6.1.2-alt0.1
- Initial build for ALTLinux.

