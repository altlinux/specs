%define optflags_lto %nil
%define llvm_ver 17.0

%ifarch x86_64
%def_without llvm_rocm
%else
%def_without llvm_rocm
%endif

Name: rocm-device-libs
Version: 6.0.0
Release: alt0.2
License: NCSA
Summary: AMD specific device-side language runtime libraries
Url: https://github.com/RadeonOpenCompute/ROCm-Device-Libs
Group: System/Libraries

Source: %name-%version.tar
# https://salsa.debian.org/rocm-team/rocm-device-libs/-/blob/master/debian/patches/cmake-amdgcn-bitcode.patch
Patch0: cmake-amdgcn-bitcode.patch
Patch1: cmake-alt-install-prefix.patch

BuildRequires(pre): cmake
%if_with llvm_rocm
BuildRequires: clang-rocm-devel >= %version clang-rocm-tools >= %version llvm-rocm-devel >= %version lld-rocm >= %version
%else
BuildRequires: clang%{llvm_ver}-devel llvm%{llvm_ver}-devel lld%{llvm_ver}
%endif
BuildRequires: zlib-devel libstdc++-devel rocm-cmake ncurses-devel libffi-devel libxml2-devel

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
%if_with llvm_rocm
export ALTWRAP_LLVM_VERSION=rocm
%else
export ALTWRAP_LLVM_VERSION=%{llvm_ver}
%endif
%cmake \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_EXE_LINKER_FLAGS='-fuse-ld=lld'
%cmake_build

%install
%cmake_install

%files
%doc LICENSE.TXT README.md
%dir %_datadir/amdgcn
%_datadir/amdgcn/bitcode
%_datadir/cmake/AMDDeviceLibs

%changelog
* Mon Mar 18 2024 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.2
- Boostrap with llvm.
- x86_64: relax llvm-rocm version requires.

* Sun Dec 24 2023 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.1
- rocm-6.0.0.

* Mon Nov 06 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.1-alt0.1
- rocm-5.7.1.

* Wed Sep 20 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.0-alt0.1
- rocm-5.7.0.

* Wed Aug 30 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.1-alt0.1
- rocm-5.6.1 (no code change, just version bump).
- Rebuild w/ llvm-rocm-5.6.1.

* Tue Jul 04 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.2
- Rebuild with llvm-rocm.
- Set ExclusiveArch due llvm-rocm.

* Sat Jul 01 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.1
- rocm-5.6.0.

* Thu May 25 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.1
- rocm-5.5.1.
- llvm15->llvm16.

* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- First build for ALTLinux.
