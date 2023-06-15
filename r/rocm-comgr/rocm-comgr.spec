%define llvm_ver 16.0
%define soname 2
%define bdir lib/comgr

%define optflags_lto %nil

Name: rocm-comgr
Version: 5.5.1
Release: alt0.2
License: NCSA
Summary: AMD Code Object Manager (Comgr)
Url: https://github.com/RadeonOpenCompute/ROCm-CompilerSupport
Group: Development/C++

Source: %name-%version.tar

# link llvm statically due collisions with Mesa
Patch0: %name-llvm-static.patch
# llvm16 compatible patches 
Patch1: 0001-None-std-nullopt.patch
Patch2: 0002-llvm-merge-add-include-of-lld-Common-CommonLinkerCon.patch
Patch3: 0003-llvm-move-to-inverted-OPT_mrelax_relocations_no.patch
Patch4: 0004-llvm-merge-Move-to-Expected-on-SubtargetFeatures.patch
Patch5: 0005-Remove-h-option-from-comgr-objdump.patch
Patch6: 0006-Replacing-deprecated-llvm-None-with-std-nullopt.patch

BuildRequires(pre): cmake
BuildRequires: llvm%{llvm_ver}-devel clang%{llvm_ver}-devel clang%{llvm_ver}-tools
BuildRequires: mlir%{llvm_ver}-tools lld%{llvm_ver}-devel
BuildRequires: zlib-devel libstdc++-devel rocm-cmake rocm-device-libs ncurses-devel
%ifarch %ix86
BuildRequires: gcc-c++
%endif

# clang segfaults on armh
# doesn't compile on ix86
ExclusiveArch: x86_64 aarch64 ppc64le

%description
The Comgr library provides APIs for compiling and inspecting AMDGPU code
objects.

%package -n libamd_comgr%{soname}
Summary: AMD Code Object Manager (Comgr) library
Group: System/Libraries
Provides: libamd_comgr = %EVR
Requires: clang%{llvm_ver}-libs-support

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
export ALTWRAP_LLVM_VERSION=%{llvm_ver}
%cmake \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DLLD_DIR=%_prefix/lib/llvm-%{llvm_ver}/%_lib/cmake/lld \
    -DCMAKE_SHARED_LINKER_FLAGS='-fuse-ld=lld' \
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
