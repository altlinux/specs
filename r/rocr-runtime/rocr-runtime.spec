%define soname 1
%define llvm_ver 16.0

%def_with llvm_rocm

# LTO causes segfaults (
%define optflags_lto %nil

Name: rocr-runtime
Version: 5.7.1
Release: alt0.1
License: MIT
Summary: HSA Runtime API and runtime for ROCm
Url: https://github.com/RadeonOpenCompute/ROCR-Runtime
Group: System/Libraries

Source: %name-%version.tar
Patch0: rocr-image-bitcode-path.patch
# https://bugs.gentoo.org/716948
Patch1: rocr-runtime-4.3.0_no-aqlprofiler.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libelf-devel libdrm-devel hsakmt-rocm-devel = %version rocm-device-libs = %version xxd
%if_with llvm_rocm
BuildRequires: clang-rocm-devel = %version clang-rocm-tools = %version llvm-rocm-devel = %version lld-rocm = %version
%else
BuildRequires: clang%{llvm_ver}-devel llvm%{llvm_ver}-devel lld%{llvm_ver} libmlir%{llvm_ver}-devel mlir%{llvm_ver}-tools libpolly%{llvm_ver}-devel clang%{llvm_ver}-tools clangd%{llvm_ver}
%endif

# only x86_64 due cpuid.h requirement
ExclusiveArch: x86_64

%description
AMD's implementation of the core HSA Runtime API's.

%package -n libhsa-runtime%{soname}
Summary: HSA Runtime API and runtime for ROCm
Provides: libhsa-runtime64 = %EVR, hsa-rocr = %EVR
Group: System/Libraries

%description -n libhsa-runtime%{soname}
AMD's implementation of the core HSA Runtime API's.

%package -n hsa-rocr-devel
Summary: HSA Runtime API and runtime for ROCm development
Group: Development/C++

%description -n hsa-rocr-devel
HSA Runtime API and runtime for ROCm development headers and library.

%prep
%setup
%patch0 -p1
%patch1 -p0

%build
%if_with llvm_rocm
export ALTWRAP_LLVM_VERSION=rocm
%else
export ALTWRAP_LLVM_VERSION=%{llvm_ver}
%endif
pushd src
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=ON \
	-DINCLUDE_PATH_COMPATIBILITY=OFF \
	-DCMAKE_INSTALL_LIBDIR=%_lib
%cmake_build

%install
pushd src
%cmake_install

%files -n libhsa-runtime%{soname}
%doc src/LICENSE.md src/README.md
%_libdir/libhsa-runtime64.so.%{soname}*

%files -n hsa-rocr-devel
%_includedir/hsa
%_libdir/libhsa-runtime64.so
%_libdir/cmake/hsa-runtime64

%changelog
* Mon Nov 06 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.1-alt0.1
- rocm-5.7.1.

* Tue Sep 19 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.0-alt0.1
- rocm-5.7.0.
- BR: strict dependencies.

* Thu Aug 31 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.1-alt0.2
- Rebuild w/ llvm-rocm-5.6.1.
- fix llvm-rocm knob.

* Wed Aug 30 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.1-alt0.1
- rocm-5.6.1.
- No code changes, just version bump.
- Relax device-libs requires.
- Bootstrap with llvm-16.

* Wed Jul 05 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.4
- Rebuild with llvm-rocm.

* Tue Jul 04 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.3
- Added bootstrap knob.
- Limit build to x86_64 only due strict requirement to cpuid.h.

* Tue Jul 04 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.2
- Rebuild with llvm-rocm.

* Mon Jul 03 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.1
- rocm-5.6.0.

* Thu Jun 15 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.2
- Disable 32-bit completely.

* Sun May 28 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.1
- rocm-5.5.1.
- llvm15->llvm16.

* Wed Jan 04 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.2
- Restrict build to 64-bit.

* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- First build for ALTLinux.
