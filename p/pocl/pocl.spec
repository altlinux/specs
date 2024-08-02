%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define llvm_ver 18.1
%define soname 2
%ifarch x86_64
%def_with cuda
# libcuda doesn't have debuginfo
%filter_from_requires /libcuda\.so\.1/d

%else
%def_without cuda
%endif
%ifarch x86_64 ppc64le aarch64
%def_with vulkan
# remote client/server
# http://portablecl.org/docs/html/remote.html
%def_enable remote
%def_with vsock
%def_with traffic_monitor
%else
%def_without vsock
%def_without traffic_monitor
%def_without vulkan
%def_disable remote
%endif
# RDMA used only by remote for HPC-like performance
%def_without rdma
# risc-v/loongarch64 might not supported
%def_with openmp

# pocl detects LTO automatically
%define optflags_lto %nil

Name: pocl
Version: 6.0
Release: alt0.2

# The entire code is under MIT
# include/utlist.h which is under BSD-1-Clause (unbundled)
# lib/kernel/vecmath which is under GPL-3.0-or-later OR LGPL-3.0-or-later
License: MIT AND BSD-1-Clause AND (GPL-3.0-or-later OR LGPL-3.0-or-later)
Summary: Portable Computing Language - an OpenCL implementation
Group: Development/Other
Url: https://github.com/%name/%name
Source0: %url/archive/v%version/%name-%version.tar
Patch0: 0001-vulkan-remove-unsupported-clspv-args.patch
# remote rely on some hidden rdma funcs
Patch1: pocl-5.0-alt-unhide-rdma.patch
Patch2: pocl-5.0-remote-fix-uthash.patch
# debian patches for GENERIC cpu target
Patch100: deb-generic-cpu.patch
Patch101: deb-blhc.patch
Patch102: deb-distro.patch

BuildRequires(pre): cmake ctest
BuildRequires: clang%{llvm_ver}
BuildRequires: clang%{llvm_ver}-devel
BuildRequires: libGLEW-devel
BuildRequires: libhwloc-devel
BuildRequires: libedit-devel
BuildRequires: llvm%{llvm_ver}-devel
BuildRequires: libGL-devel
BuildRequires: libEGL-devel
BuildRequires: ocl-icd-devel
BuildRequires: libuthash-devel
BuildRequires: zlib-devel
BuildRequires: ninja-build
BuildRequires: libstdc++-devel
BuildRequires: python3-module-sphinx
%if_with vulkan
BuildRequires: clspv glslang glslc libvulkan-devel
%endif
%if_with cuda
BuildRequires: nvidia-cuda-devel
%endif
%if_with rdma
BuildRequires: rdma-core-devel
%endif
%if_with openmp
BuildRequires: libomp%{llvm_ver}-devel
%endif

# https://bugzilla.redhat.com/show_bug.cgi?id=1082364
Requires: libstdc++-devel
# Runtime dependency, because libm.so is required for kernels
Requires: glibc-devel

%description
Pocl's goal is to become an efficient open source (MIT-licensed) implementation
of the OpenCL 1.2 (and soon OpenCL 2.0) standard.

In addition to producing an easily portable open-source OpenCL implementation,
another major goal of this project is improving performance portability of
OpenCL programs with compiler optimizations, reducing the need for
target-dependent manual optimizations.

At the core of pocl is the kernel compiler that consists of a set of LLVM
passes used to statically transform kernels into work-group functions with
multiple work-items, even in the presence of work-group barriers. These
functions are suitable for parallelization in multiple ways (SIMD, VLIW,
superscalar,...).

%package -n lib%name%{soname}
Summary: Portable Computing Language library
Group: System/Libraries

%description -n lib%name%{soname}
Pocl's goal is to become an efficient open source (MIT-licensed) implementation
of the OpenCL 1.2 (and soon OpenCL 2.0) standard.

In addition to producing an easily portable open-source OpenCL implementation,
another major goal of this project is improving performance portability of
OpenCL programs with compiler optimizations, reducing the need for
target-dependent manual optimizations.

At the core of pocl is the kernel compiler that consists of a set of LLVM
passes used to statically transform kernels into work-group functions with
multiple work-items, even in the presence of work-group barriers. These
functions are suitable for parallelization in multiple ways (SIMD, VLIW,
superscalar,...).

This package provides the core library of pocl.

%package devel
Summary: Portable Computing Language development files
Group: Development/Other
Requires: clang%{llvm_ver}
Requires: ocl-icd-devel
Requires: libuthash-devel

%description devel
Portable Computing Language development files.

%package opencl-icd
Summary: pocl OpenCL ICD
Group: System/X11
Requires: opencl-filesystem, lib%{name}%{soname} = %EVR
BuildArch: noarch

%description opencl-icd
Portable Computing Language OpenCL ICD

%package docs
Summary: pocl documentation
Group: Documentation
BuildArch: noarch

%description docs
pocl documentation

%if_with vulkan
%package devices-vulkan
Summary: pocl Vulkan OpenCL device
Group: System/Libraries
Requires: clspv

%description devices-vulkan
pocl Vulkan OpenCL device
%endif

%if_enabled remote
%package devices-remote
Summary: pocl remote client
Group: System/Libraries

%description devices-remote
pocl remote client

PoCL-Remote is an OpenCL driver which forwards OpenCL commands to a remote
server over network. The remote OpenCL devices are listed in the local OpenCL
platform device list and each each remote device can be used like it was a
local OpenCL device. The properties of a remote device as queried via
clGetDeviceInfo() mirror the remote physical device's properties etc.

%package -n pocld
Summary: pocl remote server
Group: System/Servers

%description -n pocld
pocl remote server

PoCL-Remote is an OpenCL driver which forwards OpenCL commands to a remote
server over network. The remote OpenCL devices are listed in the local OpenCL
platform device list and each each remote device can be used like it was a
local OpenCL device. The properties of a remote device as queried via
clGetDeviceInfo() mirror the remote physical device's properties etc.

%endif

%if_with cuda
%package devices-cuda
Summary: pocl NVPTX/CUDA OpenCL device
Group: System/Libraries
Requires: libcuda

%description devices-cuda
pocl NVPTX/CUDA OpenCL device

%package kernels-nvidia
Summary: %name bitcode for nvptx/CUDA
Requires: %name-devices-cuda = %EVR
Group: Graphics

%description kernels-nvidia
%name precompiled bitcode for NVPTX/CUDA targets.
%endif

%prep
%setup -q
%autopatch -p1
# Unbundle uthash/utlist
find . -depth -type f -regex '\.\/include\/\(uthash\|utlist\)\.h' -print -delete

%build
export ALTWRAP_LLVM_VERSION=%{llvm_ver}
# see README.PPC64le for details
export PPC_CXXFLAGS=$(llvm-config --cxxflags|sed -e "s/std=c/std=gnu/")
%if_enabled vulkan
export VULKAN_SDK=%_libdir
%endif
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DENABLE_ICD:BOOL=ON \
    -DENABLE_TESTS:BOOL=ON \
    -DPOCL_INSTALL_ICD_VENDORDIR=%_sysconfdir/OpenCL/vendors \
    -DEXTRA_KERNEL_CXX_FLAGS="%optflags" \
%ifarch riscv64
    -DLLC_HOST_CPU="generic-rv64" \
%endif
%ifarch %ix86 x86_64
    -DLLC_HOST_CPU=GENERIC \
    -DKERNELLIB_HOST_CPU_VARIANTS=distro \
%endif
%ifarch %ix86 %arm
    -DENABLE_EXAMPLES:BOOL=OFF \
%else
    -DENABLE_EXAMPLES:BOOL=ON \
%endif
%ifarch ppc64le
    -DLLVM_CXXFLAGS="$PPC_CXXFLAGS" \
%endif
%if_with cuda
    -DENABLE_CUDA=ON \
%endif
%if_with vulkan
    -DENABLE_VULKAN=1 \
    -DCLSPV_DIR=%_bindir \
%endif
%if_enabled remote
    -DENABLE_REMOTE_CLIENT=1 \
    -DENABLE_REMOTE_SERVER=1 \
    -DVISIBILITY_HIDDEN:BOOL=OFF \
%if_with vsock
    -DENABLE_VSOCK:BOOL=ON \
%endif #vsock
%if_with traffic_monitor
    -DENABLE_TRAFFIC_MONITOR:BOOL=ON \
%endif #traffic_monitor
%endif
%if_with rdma
    -DENABLE_RDMA=1 \
%endif
%if_with openmp
    -DENABLE_HOST_CPU_DEVICES_OPENMP:BOOL=ON \
%endif
    -DPOCL_ICD_ABSOLUTE_PATH:BOOL=OFF \
    -DENABLE_POCL_BUILDING:BOOL=ON
%cmake_build

%install
%cmake_install

# FIXME maybe we could just install it properly?
ln -s %name/libpocl-devices-basic.so %buildroot%_libdir/libpocl-devices-basic.so

sphinx-build-3 -N -b html doc/sphinx/source build-doc/html

# tests require sysfs access
#%%check
#mkdir -p build/kcache
#for k in $(sed -r -n '/KERNELLIB_HOST_CPU_VARIANTS/ { s/.*"(.*)".*/\1/; s/;/ /g; p }' %_cmake__builddir/config.h) ; \
#do
#echo TESTING $k ; \
#POCL_KERNELLIB_NAME=$k \
#POCL_CACHE_DIR=build/kcache \
#OCL_ICD_VENDORS=%_cmake__builddir/ocl-vendors/pocl-tests.icd \
#POCL_BUILDING=1 POCL_DEVICES=basic clinfo || touch build/stamp-failed-testsuite
#done

%files -n lib%{name}%{soname}
%doc CHANGES TODO README.md README.PPC64le README.packaging LICENSE COPYING
%_libdir/lib%name.so.2*
%dir %_libdir/%name
%_libdir/%name/lib%name-devices-basic.so
%_libdir/%name/lib%name-devices-pthread.so
%_libdir/lib%name-devices-basic.so
%dir %_datadir/%name
%_datadir/%name/include
%_datadir/%name/kernel-*-*-*-*-*.bc


%files opencl-icd
%_sysconfdir/OpenCL/vendors/%name.icd

%if_with cuda
%files devices-cuda
%_libdir/%name/lib%name-devices-cuda.so

%files kernels-nvidia
%_datadir/%name/cuda
%_datadir/%name/kernel-nvptx64-*.bc
%endif

%files devel
%_bindir/poclcc
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%files docs
%doc build-doc/html

%if_with vulkan
%files devices-vulkan
%_libdir/%name/lib%name-devices-vulkan.so
%endif

%if_enabled remote
%files devices-remote
%_libdir/%name/lib%name-devices-remote.so

%files -n pocld
%_bindir/pocld
%endif

%changelog
* Sun Jul 28 2024 L.A. Kostis <lakostis@altlinux.ru> 6.0-alt0.2
- remote: enable vsock.
- remote: enable traffic monitor.

* Sun Jul 28 2024 L.A. Kostis <lakostis@altlinux.ru> 6.0-alt0.1
- 6.0.
- Update patches.
- Remove lld dependency.
- cpu: enable OpenMP support.

* Thu Jan 04 2024 L.A. Kostis <lakostis@altlinux.ru> 5.0-alt0.2
- Enable remote client/server.
- Split CL devices to separate packages.

* Mon Jan 01 2024 L.A. Kostis <lakostis@altlinux.ru> 5.0-alt0.1
- 5.0.
- Update debian patches.
- BR: bump llvm version.

* Sat Dec 09 2023 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt0.7
- x86_64: Enable CUDA.

* Fri Sep 01 2023 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt0.6
- .spec: major rewrite:
  + split to subpackages like in debian (doc/lib/icd).
- fix requires.

* Fri Sep 01 2023 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt0.5
- Apply patches from Debian for generic cpu targets.
- armh: fix build (disable LTO).
- added CUDA support.
- ppc64le: apply CXXFLAGS hack as suggested in README.

* Thu Aug 31 2023 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt0.4
- Enable vulkan only on 64-bit (due clspv).
- Enable lld only on x86_64/ppc64le.
- aarch64: use real host CPU, not fake cortex-NN.
- Relax verify-elf on non-lld compiled builds.

* Thu Aug 31 2023 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt0.3
- Build with updated clspv.
- Remove HSA (unmaintained).

* Sun Jun 25 2023 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt0.2
- Build with vulkan.

* Thu Jun 22 2023 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt0.1
- Initial build for ALTLinux.

* Tue Apr 11 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1-1
- Updated to version 3.1.
- Fixed FTBFS on Fedora 37+.
- Performed major SPEC cleanup.
- Switched to SPDX license tag.
