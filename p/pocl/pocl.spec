%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define llvm_ver 16.0
%define soname 2
%ifarch x86_64 ppc64le
%def_with lld
%else
%def_without lld
%endif
# needs CUDA SDK
%def_without cuda
%ifarch x86_64 ppc64le aarch64
%def_with vulkan
%else
%def_without vulkan
%endif
%if_with lld
%set_verify_elf_method skip
%endif

# pocl detects LTO automatically
%define optflags_lto %nil

Name: pocl
Version: 4.0
Release: alt0.6

# The entire code is under MIT
# include/utlist.h which is under BSD-1-Clause (unbundled)
# lib/kernel/vecmath which is under GPL-3.0-or-later OR LGPL-3.0-or-later
License: MIT AND BSD-1-Clause AND (GPL-3.0-or-later OR LGPL-3.0-or-later)
Summary: Portable Computing Language - an OpenCL implementation
Group: Development/Other
Url: https://github.com/%name/%name
Source0: %url/archive/v%version/%name-%version.tar
Patch0: 0001-vulkan-remove-unsupported-clspv-args.patch
# debian patches for GENERIC cpu target
Patch100: deb-0001-rename-bitcode_is_triple-to-pocl_bitcode_is_triple.patch
Patch101: deb-0002-rename-opencl_image_type_to_index-to-pocl_opencl_ima.patch
Patch102: deb-0028-add-llvm_cpu-to-the-long-device-name.patch
Patch103: deb-0035-rename-getX86KernelLibName-to-pocl_get_distro_kernel.patch
Patch104: deb-0036-use-a-more-generic-solution-for-pocl_get_distro_kern.patch
Patch105: deb-0037-add-pocl_get_distro_cpu_name.patch
Patch106: deb-0038-_cl_device_id-add-const-char-kernellib_name.patch
Patch107: deb-0039-allow-overriding-kernellib_name-for-distro-builds-wi.patch
Patch108: deb-0040-support-overriding-the-runtime-cpu-detection-with-PO.patch
Patch109: deb-0041-disable-the-device-if-kernellib-or-cpu-detection-fai.patch
Patch110: deb-distro.patch
Patch111: deb-generic-cpu.patch

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
%if_with lld
BuildRequires: lld%{llvm_ver} /proc
%endif
%if_with vulkan
BuildRequires: clspv glslang glslc libvulkan-devel
%endif

# https://bugzilla.redhat.com/show_bug.cgi?id=1082364
Requires: libstdc++-devel
# Runtime dependency, because libm.so is required for kernels
Requires: glibc-devel

%add_findreq_skiplist %_libdir/%name/libpocl-devices-pthread.so

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
%if_with vulkan
Requires: clspv
%endif

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

%package -n %name-opencl-icd
Summary: pocl OpenCL ICD
Group: System/X11
Requires: opencl-filesystem, lib%{name}%{soname} = %EVR
BuildArch: noarch

%description -n %name-opencl-icd
Portable Computing Language OpenCL ICD

%package docs
Summary: pocl documentation
Group: Documentation
BuildArch: noarch

%description docs
pocl documentation

%prep
%setup -q
%autopatch -p1

# Unbundle uthash
find . -depth -name utlist* -print -delete

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
    -DENABLE_EXAMPLES:BOOL=ON \
    -DPOCL_INSTALL_ICD_VENDORDIR=%_sysconfdir/OpenCL/vendors \
    -DCMAKE_EXE_LINKER_FLAGS="%optflags %{?_with_lld:-fuse-ld=lld -Wl,--build-id=sha1}" \
    -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS %{?_with_lld:-fuse-ld=lld -Wl,--build-id=sha1}" \
    -DEXTRA_KERNEL_CXX_FLAGS="%optflags" \
%ifarch x86_64
    -DCMAKE_C_FLAGS="-Wno-error=int-conversion" \
%endif
%ifarch riscv64
    -DLLC_HOST_CPU="generic-rv64" \
%endif
%ifarch %ix86 x86_64
    -DLLC_HOST_CPU=GENERIC \
    -DKERNELLIB_HOST_CPU_VARIANTS=distro \
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
    -DPOCL_ICD_ABSOLUTE_PATH:BOOL=OFF \
    -DENABLE_POCL_BUILDING:BOOL=ON \
    || cat %_cmake__builddir/CMakeFiles/CMakeOutput.log
%cmake_build

%install
%cmake_install
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
%doc CHANGES TODO README.md README.ARM README.PPC64le README.packaging LICENSE COPYING
%_libdir/lib%name.so.2*
%_libdir/%name
%dir %_datadir/%name
%_datadir/%name/include
%_datadir/%name/kernel-*-*-*-*-*.bc

%files -n %name-opencl-icd
%_sysconfdir/OpenCL/vendors/%name.icd

%files devel
%_bindir/poclcc
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%files docs
%doc build-doc/html

%changelog
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
