%define llvm_ver 15.0
%define optflags_lto %nil
%define bits 64

Name: rocclr
Version: 5.4.3
Release: alt0.1
License: MIT
Summary: Radeon Open Compute Common Language Runtime
Url: https://github.com/ROCm-Developer-Tools/ROCclr
Group: System/Libraries

Source0: %name-%version.tar
# https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime.git
Source1: opencl.tar

BuildRequires(pre): cmake
BuildRequires: llvm%{llvm_ver}-devel clang%{llvm_ver}-devel clang%{llvm_ver}-tools mlir%{llvm_ver}-tools lld%{llvm_ver}
BuildRequires: zlib-devel libstdc++-devel rocm-cmake rocm-comgr-devel hsa-rocr-devel
BuildRequires: libX11-devel libnuma-devel libGL-devel

ExclusiveArch: x86_64 aarch64 ppc64le

%description
ROCclr is a virtual device interface that compute runtimes interact with to
different backends such as ROCr or PAL This abstraction allows runtimes to work
on Windows as well as on Linux without much effort.

%package -n rocm-opencl-runtime
Summary: ROCm OpenCL Compatible Runtime
Group: System/Libraries
Requires: opencl-filesystem

%description -n rocm-opencl-runtime
ROCm OpenCL Compatible Runtime:

- OpenCL 2.0 compatible language runtime
- Supports offline and in-process/in-memory compilation

%prep
%setup -n %name-%version -a1

%build
export ALTWRAP_LLVM_VERSION=%{llvm_ver}
%cmake \
    -Wno-dev \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_EXE_LINKER_FLAGS='-fuse-ld=lld'
%cmake_build
pushd opencl
%cmake \
    -Wno-dev \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_EXE_LINKER_FLAGS='-fuse-ld=lld' \
    -DUSE_COMGR_LIBRARY=ON \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
    -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DCMAKE_PREFIX_PATH="../../" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
pushd opencl
%cmake_install
install -pD -m644 config/amdocl%{bits}.icd %buildroot%_sysconfdir/OpenCL/vendors/amdocl%{bits}.icd

%files -n rocm-opencl-runtime
%_libdir/libamdocl%{bits}.so
%_libdir/libcltrace.so
%_sysconfdir/OpenCL/vendors/amdocl%{bits}.icd

%changelog
* Tue Mar 21 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.3-alt0.1
- rocclr: updated to ccd065214094837dd59a45aa5111d860aff38ecf (rocm-5.4.3).

* Wed Jan 04 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.2
- Restrict build to 64-bit.

* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- First build for ALTLinux.
