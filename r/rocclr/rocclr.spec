%define llvm_ver 16.0
%define build_type RelWithDebInfo
%define builddir %_cmake__builddir
%def_with mold
%define _cmake %cmake -G Ninja -S . -Wno-dev -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ %{?_with_mold:-DCMAKE_EXE_LINKER_FLAGS='-fuse-ld=mold' -DCMAKE_SHARED_LINKER_FLAGS='-fuse-ld=mold'} -DCMAKE_BUILD_TYPE=%build_type -DCMAKE_STRIP:STRING=""
%define _ninja_build ninja -vvv -j %__nprocs -C %builddir
%define optflags_lto %nil
%define bits 64
# HIP requires some components which are not built
# yet to ALT (cuda as example)
%def_with HIP

Name: rocclr
Version: 5.5.1
Release: alt0.5
License: MIT
Summary: Radeon Open Compute Common Language Runtime
# FIXME! migrate to https://github.com/ROCm-Developer-Tools/clr
Url: https://github.com/ROCm-Developer-Tools/ROCclr
Group: System/Libraries

Source0: %name-%version.tar
# https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime.git
Source1: opencl.tar
# https://github.com/ROCm-Developer-Tools/hipamd.git
Source2: hipamd.tar
# https://github.com/ROCm-Developer-Tools/HIP.git
Source3: hip.tar
# sane defaults for HIP
Source4: hip.sh

Patch0: hipcc-alt-paths.patch
Patch1: hipamd-alt-bitcode-path.patch
Patch2: rocclr-gcc-13-fixes.patch
Patch3: opencl-gcc-13-fixes.patch

BuildRequires(pre): cmake /proc ninja-build
BuildRequires: llvm%{llvm_ver}-devel clang%{llvm_ver}-devel clang%{llvm_ver}-tools mlir%{llvm_ver}-tools
BuildRequires: zlib-devel libstdc++-devel rocm-cmake = %version rocm-comgr-devel = %version hsa-rocr-devel = %version
BuildRequires: libX11-devel libnuma-devel libGL-devel
%if_with mold
BuildRequires: mold
%else
BuildRequires: lld%{llvm_ver}
%endif
%if_with HIP
BuildRequires: python3-module-CppHeaderParser
%endif

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

%package -n hip-devel
Summary: HIP:Heterogenous-computing Interface for Portability
Group: Development/Other
# as hip scripts are noarch
# perl scripts rely on runtime envs
AutoReq: yes, noperl
Requires: clang%{llvm_ver} clang%{llvm_ver}-tools clang%{llvm_ver}-libs-support llvm%{llvm_ver} lld%{llvm_ver} glibc-devel gcc
Requires: rocm-device-libs = %version rocminfo = %version hip-runtime-amd = %EVR

%description -n hip-devel
HIP: Heterogenous-computing Interface for Portability development libraries and
headers.

%package -n hip-devel-samples
Summary: HIP development sample code and cookbook
Group: Documentation
BuildArch: noarch

%description -n hip-devel-samples
HIP development sample code and cookbook

%package -n hip-runtime-amd
Summary: HIP implementation specifically for AMD platform.
Group: Development/Other

%description -n hip-runtime-amd
HIP is a C++ Runtime API and Kernel Language that allows developers to create
portable applications for AMD and NVIDIA GPUs from single source code.

This package provides the HIP implementation specifically for AMD platform.

%prep
%setup -n %name-%version -a1 -a2 -a3
%patch0 -p1 -b .hipcc-alt-paths
%patch1 -p1 -b .hipamd-bitcode-paths
%patch2 -p1 -b .rocclr-gcc13-fixes
%patch3 -p1 -b .opencl-gcc13-fixes

%build
export ALTWRAP_LLVM_VERSION=%{llvm_ver}
%_cmake
%_ninja_build
pushd opencl
%_cmake \
    -DUSE_COMGR_LIBRARY=ON \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
    -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DCMAKE_PREFIX_PATH="../../"
%_ninja_build
%if_with HIP
popd
pushd hipamd
%_cmake \
    -DHIP_COMMON_DIR=%_builddir/%name-%version/hip \
    -DAMD_OPENCL_PATH=../opencl \
    -DROCCLR_PATH=../../ \
    -DCMAKE_MODULE_PATH=%_libdir/cmake \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DHIP_PLATFORM=amd
%_ninja_build
%endif

%install
pushd opencl
%cmake_install
install -pD -m644 config/amdocl%{bits}.icd %buildroot%_sysconfdir/OpenCL/vendors/amdocl%{bits}.icd
# rocm clinfo expose more information than third-party clinfo
mv %buildroot%_bindir/clinfo %buildroot%_bindir/rocm-clinfo

%if_with HIP
popd
pushd hipamd
%cmake_install

# hip cmake scripts are noarch
mkdir -p %buildroot%_datadir/cmake/hip
mv %buildroot%_libdir/cmake/hip/FindHIP.cmake %buildroot%_datadir/cmake/hip/
mv %buildroot%_libdir/cmake/hip/FindHIP %buildroot%_datadir/cmake/hip

mkdir -p %buildroot%_sysconfdir/profile.d
install -p -m 755 %SOURCE4 %buildroot%_sysconfdir/profile.d/
%endif

%files -n rocm-opencl-runtime
%_bindir/rocm-clinfo
%_libdir/libamdocl%{bits}.so
%_libdir/libcltrace.so
%_sysconfdir/OpenCL/vendors/amdocl%{bits}.icd

%if_with HIP
%files -n hip-devel
%doc hip/README.md hip/RELEASE.md hip/LICENSE.txt
%_sysconfdir/profile.d/hip.sh
%_bindir/*
%_bindir/.hipVersion
%exclude %_bindir/rocm-clinfo
%_includedir/hip
%_includedir/hip_prof_str.h
%_datadir/cmake/hip

%files -n hip-runtime-amd
%doc hipamd/README.md hipamd/LICENSE.txt
%_libdir/cmake/hip
%_libdir/cmake/hip-lang
%_libdir/cmake/hiprtc
%_libdir/libamdhip%{bits}*.so*
%_libdir/libhiprtc-builtins*.so*
%_libdir/libhiprtc*.so*

%files -n hip-devel-samples
%_datadir/hip/samples
%endif

%changelog
* Wed Jun 21 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.5
- hipamd: update bitcode search paths.
- hipamd: fix symlinks.
- rocclr: apply fixes for gcc-13.
- opencl: apply fixes for gcc-13.
- hip-devel: fix unmet requires.

* Mon Jun 19 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.4
- Enable HIP again:
  + hip-devel: update dependencies.
  + hipcc.pl: update search paths and options.
  + hip: setup env.

* Sat Jun 17 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.3
- ppc64le: use mold for linking.

* Wed Jun 14 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.2
- Added HIP packages (disabled by default).
- Use ninja build and mold for linking.

* Sun May 28 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.1
- rocm-5.5.1.
- llvm15->llvm16.

* Tue Mar 21 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.3-alt0.1
- rocclr: updated to ccd065214094837dd59a45aa5111d860aff38ecf (rocm-5.4.3).

* Wed Jan 04 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.2
- Restrict build to 64-bit.

* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- First build for ALTLinux.
