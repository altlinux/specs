%define soname 2
%define bdir lib/comgr
%define llvm_ver 17.0

%def_with llvm_rocm

%define optflags_lto %nil

Name: rocm-comgr
Version: 6.0.2
Release: alt0.3
License: NCSA
Summary: AMD Code Object Manager (Comgr)
Url: https://github.com/RadeonOpenCompute/ROCm-CompilerSupport
Group: Development/C++

Source: %name-%version.tar

# link llvm statically due collisions with Mesa
Patch0: %name-llvm-static.patch
# device libs path
Patch1: rocm-alt-device-libs-path.patch
# use llvm-rocm commands
Patch2: rocm-comgr-use-llvm-rocm.patch
# get rid of obsoleted llvm::Optional
Patch3: 0001-llvm-change-from-Optional-to-std-optional-in-support.patch

BuildRequires(pre): cmake
%if_with llvm_rocm
BuildRequires: clang-rocm-devel >= %version clang-rocm-tools >= %version llvm-rocm-devel >= %version lld-rocm-devel >= %version
%else
BuildRequires: clang%{llvm_ver}-devel llvm%{llvm_ver}-devel lld%{llvm_ver}-devel
%endif
BuildRequires: zlib-devel libstdc++-devel rocm-cmake >= 6.0.0 rocm-device-libs >= 6.0.0 ncurses-devel

ExclusiveArch: x86_64 ppc64le aarch64

%description
The Comgr library provides APIs for compiling and inspecting AMDGPU code
objects.

%package -n libamd_comgr%{soname}
Summary: AMD Code Object Manager (Comgr) library
Group: System/Libraries
Provides: libamd_comgr = %EVR
Requires: clang-rocm-libs-support = %version, lld-rocm = %version

%description -n libamd_comgr%{soname}
The Comgr library provides APIs for compiling and inspecting AMDGPU code
objects.

%package devel
Summary: AMD Code Object Manager (Comgr) headers
Group: Development/C++

%description devel
AMD Code Object Manager (Comgr) develpment library and headers

%prep
%setup
%autopatch -p1

%build
pushd %{bdir}
%if_with llvm_rocm
export ALTWRAP_LLVM_VERSION=rocm
%else
export ALTWRAP_LLVM_VERSION=%{llvm_ver}
%endif
%cmake \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
%if_with llvm_rocm
    -DLLD_DIR=%_prefix/lib/llvm-rocm/%_lib/cmake/lld \
%else
    -DLLD_DIR=%_prefix/lib/llvm-%{llvm_ver}/%_lib/cmake/lld \
%endif
    -DCMAKE_CXX_LINKER_FLAGS='-fuse-ld=lld -Wl,--build-id=sha1' \
    -DCMAKE_SHARED_LINKER_FLAGS='-fuse-ld=lld -Wl,--build-id=sha1' \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
pushd %{bdir}
%cmake_install

%files -n libamd_comgr%{soname}
%doc %{bdir}/README.md %{bdir}/LICENSE.txt %{bdir}/NOTICES.txt
%_libdir/libamd_comgr.so.%{soname}*

%files devel
%_includedir/*
%_libdir/libamd_comgr.so
%_libdir/cmake/amd_comgr

%changelog
* Tue Mar 19 2024 L.A. Kostis <lakostis@altlinux.ru> 6.0.2-alt0.3
- Build with llvm-rocm for all 64-bit arches.

* Mon Mar 18 2024 L.A. Kostis <lakostis@altlinux.ru> 6.0.2-alt0.2
- Build on all 64-bit arches.
- Added patch from amd-stg-open:
  + [PATCH] [llvm] change from Optional to std::optional

* Mon Mar 18 2024 L.A. Kostis <lakostis@altlinux.ru> 6.0.2-alt0.1
- rocm-6.0.2.

* Sun Dec 24 2023 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.1
- rocm-6.0.0.

* Mon Nov 06 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.1-alt0.1
- rocm-5.7.1.
- use sha1 for build-id.

* Wed Sep 20 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.0-alt0.1
- rocm-5.7.0.

* Wed Aug 30 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.1-alt0.1
- rocm-5.6.1 (no code change, just version bump).
- rebuild w/ llvm-rocm-5.6.1.

* Wed Jul 05 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.3
- Invoke llvm-rocm command explicitly.
- .spec: cleanup deps/requires.

* Mon Jul 03 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.2
- Use llvm-rocm.
- Built x86_64 only.

* Sat Jul 01 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.1
- rocm-5.6.0.
- remove merged patches.

* Thu Jun 29 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.3
- Fix amd device libs path.
- Rebuild with llvm-16.0.6.

* Thu Jun 15 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.2
- Disable 32-bit build.

* Thu May 25 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.1
- rocm-5.5.1.
- llvm15->llvm16.

* Thu Jan 05 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.5
- Link LLVM statically.

* Thu Jan 05 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.4
- Add dependency to clang-libs-support (due opencl-c-base.h).

* Wed Jan 04 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.3
- Fix compile on 32-bit.
- Exclude armh from build (clang segfaults).

* Wed Jan 04 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.2
- Enable LTO and debuginfo.

* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- First build for ALTLinux.
