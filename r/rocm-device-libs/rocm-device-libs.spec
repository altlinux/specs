%define llvm_ver 15.0
%define optflags_lto %nil

Name: rocm-device-libs
Version: 5.4.1
Release: alt0.1
License: NCSA
Summary: AMD specific device-side language runtime libraries
Url: https://github.com/RadeonOpenCompute/ROCm-Device-Libs
Group: System/Libraries

Source: %name-%version.tar
# https://salsa.debian.org/rocm-team/rocm-device-libs/-/blob/master/debian/patches/cmake-amdgcn-bitcode.patch
Patch0: cmake-amdgcn-bitcode.patch
Patch1: cmake-alt-install-prefix.patch

BuildRequires(pre): cmake
BuildRequires: llvm%{llvm_ver}-devel clang%{llvm_ver}-devel clang%{llvm_ver}-tools mlir%{llvm_ver}-tools lld%{llvm_ver}
BuildRequires: zlib-devel libstdc++-devel rocm-cmake ncurses-devel libffi-devel libxml2-devel

# bitcode itself is arch-agnostic
BuildArch: noarch

%description
Set of AMD specific device-side language runtime libraries, specifically: the
Open Compute library controls, the Open Compute Math library, the Open Compute
Kernel library, the OpenCL built-in library, the HIP built-in library, and the
Heterogeneous Compute built-in library.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
export ALTWRAP_LLVM_VERSION=%{llvm_ver}
%cmake \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_EXE_LINKER_FLAGS='-fuse-ld=lld'
%cmake_build

%install
%cmake_install

%files
%doc LICENSE.TXT README.md
%_datadir/amdgcn/bitcode
%_datadir/cmake/AMDDeviceLibs

%changelog
* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- First build for ALTLinux.
