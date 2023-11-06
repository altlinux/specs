%define soname 2
%define bdir lib/comgr

%define optflags_lto %nil

Name: rocm-comgr
Version: 5.7.1
Release: alt0.1
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

BuildRequires(pre): cmake
BuildRequires: llvm-rocm-devel = %version clang-rocm-devel = %version clang-rocm-tools = %version lld-rocm-devel = %version
BuildRequires: zlib-devel libstdc++-devel rocm-cmake = %version rocm-device-libs = %version ncurses-devel

# clang segfaults on armh
# doesn't compile on ix86
# and llvm-rocm exists only for x86_64
ExclusiveArch: x86_64

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
export ALTWRAP_LLVM_VERSION=rocm
%cmake \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DLLD_DIR=%_prefix/lib/llvm-rocm/%_lib/cmake/lld \
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
