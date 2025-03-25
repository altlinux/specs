%define _unpackaged_files_terminate_build 1
%define soname 1
%define llvm_ver 18.0

%def_with llvm_rocm

# LTO causes segfaults (
%define optflags_lto %nil

Name: rocr-runtime
Version: 6.3.2
Release: alt0.2
License: MIT
Summary: HSA Runtime API and runtime for ROCm
Url: https://github.com/RadeonOpenCompute/ROCR-Runtime
Group: System/Libraries

Source: %name-%version.tar
Patch0: rocr-image-bitcode-path.patch
# https://bugs.gentoo.org/716948
Patch1: rocr-runtime-4.3.0_no-aqlprofiler.patch
Patch2: rocr-alt-mm-pause.patch
Patch3: rocr-alt-extra-arches-support.patch
Patch4: libhsakmt-alt-shared.patch
Patch5: libhsakmt-add-extra-symbols.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libelf-devel rocm-device-libs >= %version xxd
BuildRequires: libnuma-devel libdrm-devel
%ifarch aarch64
BuildRequires: sse2neon-devel
%endif
%if_with llvm_rocm
BuildRequires: clang-rocm-devel >= %version clang-rocm-tools >= %version llvm-rocm-devel >= %version lld-rocm >= %version
%else
BuildRequires: clang%{llvm_ver}-devel llvm%{llvm_ver}-devel lld%{llvm_ver}
%endif

ExclusiveArch: x86_64 ppc64le aarch64 loongarch64

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

%package -n libhsakmt%{soname}
Summary: Thunk libraries for AMD KFD
Group: System/Libraries
Provides: hsakmt-roct = %EVR

%description -n libhsakmt%{soname}
This package includes the libhsakmt (Thunk) libraries for AMD KFD.

%package -n hsakmt-rocm-devel
Summary: Development headers for AMD KFD thunk libraries
Group: Development/C

%description -n hsakmt-rocm-devel
Development headers for AMD KFD thunk libraries.

%prep
%setup
pushd runtime/hsa-runtime
%patch0 -p2
%patch1 -p1
%patch2 -p2
popd
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%if_with llvm_rocm
export ALTWRAP_LLVM_VERSION=rocm
%else
export ALTWRAP_LLVM_VERSION=%{llvm_ver}
%endif
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DINCLUDE_PATH_COMPATIBILITY=OFF \
	-DCMAKE_INSTALL_LIBDIR=%_lib \
	%nil
%cmake_build

%install
%cmake_install

rm -f %buildroot%_datadir/doc/hsa-runtime64/LICENSE.md

%files -n libhsa-runtime%{soname}
%doc LICENSE.txt README.md
%_libdir/libhsa-runtime64.so.%{soname}*

%files -n hsa-rocr-devel
%_includedir/hsa
%_libdir/libhsa-runtime64.so
%_libdir/cmake/hsa-runtime64

%files -n libhsakmt%{soname}
%doc libhsakmt/README.md libhsakmt/LICENSE.md
%_libdir/libhsakmt.so.%{soname}*

%files -n hsakmt-rocm-devel
%_includedir/hsakmt
%_pkgconfigdir/*.pc
%_libdir/cmake/hsakmt
%_libdir/libhsakmt.so

%changelog
* Fri Feb 14 2025 L.A. Kostis <lakostis@altlinux.ru> 6.3.2-alt0.2
- aarch64/ppc64le: re-added experimental support (UNTESTED!).

* Tue Feb 11 2025 L.A. Kostis <lakostis@altlinux.ru> 6.3.2-alt0.1
- rocm-6.3.2.
- combine with -trunk package.

* Sat Jul 06 2024 L.A. Kostis <lakostis@altlinux.ru> 6.1.2-alt0.1
- rocm-6.1.2.

* Fri Mar 22 2024 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.4
- Rebuild with llvm-rocm.

* Mon Mar 18 2024 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.3
- BR: relax rocm components version requires.
- Bootstrap with llvm.
- Try to enable all 64-bit arches.

* Thu Dec 28 2023 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.2
- Added loongarch support (upstream PR #168).

* Sun Dec 24 2023 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.1
- rocm-6.0.0.

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
