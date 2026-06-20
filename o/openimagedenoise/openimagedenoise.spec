%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define build_type RelWithDebInfo
%set_verify_elf_method strict

%ifarch x86_64
%def_with cuda
%def_without oneapi
%filter_from_requires /libcudart\.so\.12/d
%else
%def_without cuda
%endif

%def_with hip

%define oname oidn
%define soname 2

Name: openimagedenoise
Version: 2.3.3
Release: alt6
Summary: Intel Open Image Denoise library
Group: Development/Other
License: Apache-2.0
URL: https://www.openimagedenoise.org/

ExclusiveArch: x86_64 aarch64

# https://github.com/OpenImageDenoise/oidn/releases/download/v%version/oidn-%version.src.tar.gz
Source: %oname-%version.tar
Patch: oidn-alt-aarch64-cuda-glibc-fix.patch
Patch1: blender-sycl-add-more-ids.patch
# introduced in https://github.com/intel/llvm/pull/15798
Patch2: sycl-fix-deprecated-warning.patch
# gfx1031 is identical to gfx1030
Patch3: oidn-alt-rocm-add-gfx1031.patch
Patch4: oidn-alt-no-fortify-again.patch

BuildRequires: cmake gcc-c++
BuildRequires: python3
BuildRequires: tbb-devel
BuildRequires: ispc
BuildRequires: libopenimageio-devel chrpath
%if_with hip
BuildRequires: hip-devel hip-runtime-amd rocm-comgr-devel rocm-device-libs hsa-rocr-devel
%endif
%if_with oneapi
# FIXME  sycl code doesn't support LTO?
%define optflags_lto %nil
BuildRequires: llvm-dpcpp-devel clang-dpcpp-devel clang-dpcpp-tools intel-ocloc libze-devel libigc-devel opencl-headers
%endif
%if_with cuda
# nvcc 12.9 rejects gcc > 14 (crt/host_config.h), use gcc14 as CUDA host compiler
BuildRequires: nvidia-cuda-devel >= 12.8 nvidia-cuda-devel-static gcc14-c++
%endif

%description
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.
Intel Open Image Denoise is part of the Intel oneAPI Rendering Toolkit
and is released under the permissive Apache 2.0 license.

%package -n lib%name%soname
Summary: Intel Open Image Denoise library
Group: System/Libraries

%description -n lib%name%soname
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.
Intel Open Image Denoise is part of the Intel oneAPI Rendering Toolkit
and is released under the permissive Apache 2.0 license.

%package devel
Summary: Intel Open Image Denoise library
Group: Development/C++
Requires: %name = %EVR
Requires: lib%name%soname = %EVR

%description devel
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.
Intel Open Image Denoise is part of the Intel oneAPI Rendering Toolkit
and is released under the permissive Apache 2.0 license.

This package contains development files for Intel Open Image Denoise.

%package hip
Summary: Intel Open Image Denoise library with HIP support
Group: System/Libraries
Requires: lib%{name}%{soname} = %EVR

%description hip
Intel Open Image Denoise library with HIP support

%package cuda
Summary: Intel Open Image Denoise library with CUDA support
Group: System/Libraries
Requires: lib%{name}%{soname} = %EVR, libcudart

%description cuda
Intel Open Image Denoise library with CUDA support

%package sycl
Summary: Intel Open Image Denoise library with oneAPI/SYCL support
Group: System/Libraries
Requires: lib%{name}%{soname} = %EVR

%description sycl
Intel Open Image Denoise library with oneAPI/SYCL support

%prep
%setup -n %oname-%version
%ifarch aarch64
# see https://github.com/OE4T/meta-tegra/pull/1445
%patch -p2
mkdir -p /tmp/bits
cat >/tmp/bits/math-vector.h <<EOF
#include <bits/libm-simd-decl-stubs.h>
#undef __ADVSIMD_VEC_MATH_SUPPORTED
#undef __SVE_VEC_MATH_SUPPORTED
EOF
%endif
%patch1 -p1
%patch2 -p2
#%%patch3 -p2
%patch4 -p2

%build
%if_with hip
export ROCM_PATH=/usr
export ALTWRAP_LLVM_VERSION=rocm
# co-installed CUDA puts nvcc in PATH, so `hipconfig --platform` autodetects
# nvidia and hip::device becomes an empty stub; force the AMD HIP platform
export HIP_PLATFORM=amd
%endif
%if_with cuda
# nvcc 12.9 rejects gcc > 14 (crt/host_config.h); pin nvcc host compiler to gcc14
export CUDAHOSTCXX=g++-14
%endif
%cmake \
	-DOIDN_STATIC_LIB:BOOL=OFF \
	%if_with hip
	-DLLD_DIR=%_prefix/lib/llvm-rocm/%_lib/cmake/lld \
	-DOIDN_DEVICE_HIP:BOOL=ON \
	%endif
	%if_with cuda
	-DOIDN_DEVICE_CUDA:BOOL=ON \
	-DOIDN_DEVICE_CUDA_API=RuntimeShared \
	-DCUDAToolkit_ROOT=%_prefix \
	%endif
	%if_with oneapi
	-DOIDN_DEVICE_SYCL:BOOL=ON \
	-DCMAKE_C_COMPILER=%prefix/lib/llvm-dpcpp/bin/clang \
	-DCMAKE_CXX_COMPILER=%prefix/lib/llvm-dpcpp/bin/clang++ \
	%endif
	-DCMAKE_BUILD_TYPE=%build_type \
	-DCMAKE_STRIP:STRING=""
	%nil
%cmake_build

%install
%cmake_install

# Remove duplicated documentation
rm -rf %buildroot%_defaultdocdir/OpenImageDenoise
%if_with hip
chrpath -d %buildroot%_libdir/libOpenImageDenoise_device_hip.so.%{version}
%endif
%if_with cuda
chrpath -d %buildroot%_libdir/libOpenImageDenoise_device_cuda.so.%{version}
%endif

%files
%_bindir/%{oname}*

%files -n lib%name%soname
%doc LICENSE.txt
%doc CHANGELOG.md README.md readme.pdf
%_libdir/lib*.so.%{soname}
%_libdir/lib*.so.%{soname}.*
%if_with hip
%exclude %_libdir/libOpenImageDenoise_device_hip.so.%{version}
%endif
%if_with cuda
%exclude %_libdir/libOpenImageDenoise_device_cuda.so.%{version}
%endif
%if_with oneapi
%exclude %_libdir/libOpenImageDenoise_device_sycl.so.%{version}
%endif

%if_with hip
%files hip
%_libdir/libOpenImageDenoise_device_hip.so.%{version}
%endif

%if_with cuda
%files cuda
%_libdir/libOpenImageDenoise_device_cuda.so.%{version}
%endif

%if_with oneapi
%files sycl
%_libdir/libOpenImageDenoise_device_sycl.so.%{version}
%endif

%files devel
%_includedir/*
%_libdir/lib*.so
%_libdir/cmake/*

%changelog
* Sat Jun 20 2026 Anton Farygin <rider@altlinux.org> 2.3.3-alt6
- Fixed CUDA build against nvidia-cuda-devel 12.9:
  + set CUDAToolkit_ROOT (new scattered toolkit layout broke nvcc autodetect);
  + build CUDA device with gcc14 (nvcc 12.9 rejects gcc > 14).
- Force HIP_PLATFORM=amd (co-installed CUDA made hipconfig pick nvidia,
  turning hip::device into an empty stub).

* Wed Aug 27 2025 L.A. Kostis <lakostis@altlinux.ru> 2.3.3-alt5
- Disable sycl (can't reliably compile).
- Added patch to fix already enabled FORTIFY_SOURCE warning.

* Fri Jul 18 2025 L.A. Kostis <lakostis@altlinux.ru> 2.3.3-alt4
- (WIP) hip/device: enabled gfx1031.

* Wed Jun 18 2025 L.A. Kostis <lakostis@altlinux.ru> 2.3.3-alt3
- oneapi: limit nprocs to 4 to fix intermittent build failures
  (closes #54416).

* Thu May 22 2025 L.A. Kostis <lakostis@altlinux.ru> 2.3.3-alt2
- sycl: add more Xe2HPG devices (patch from blender).
- sycl: fix deprecated warning.

* Tue Apr 08 2025 L.A. Kostis <lakostis@altlinux.ru> 2.3.3-alt1
- Updated to upstream version 2.3.3.
- Remove .watch file (doesn't work anyway, as we need archives
  from releases not from tags).
- cuda: build with default gcc.

* Tue Jan 28 2025 L.A. Kostis <lakostis@altlinux.ru> 2.3.2-alt1
- Updated to upstream version 2.3.2.
- x86_64: Enabled oneAPI/SYCL.

* Mon Jul 29 2024 L.A. Kostis <lakostis@altlinux.ru> 2.3.0-alt1
- Updated to upstream version 2.3.0.

* Thu Apr 04 2024 L.A. Kostis <lakostis@altlinux.ru> 2.2.2-alt3
- Enable HIP back.
- aarch64: added build workaround.

* Thu Mar 21 2024 L.A. Kostis <lakostis@altlinux.ru> 2.2.2-alt2
- Apply rocm6 patch.
- Disable HIP for ROCm version upgrade.

* Sat Mar 16 2024 L.A. Kostis <lakostis@altlinux.ru> 2.2.2-alt1
- Updated to upstream version 2.2.2.
- aarch64: enable build (officially supported now).
- x86_64: use shared cudart.
- x86_64: disable rocm6 patch for now.

* Sun Dec 24 2023 L.A. Kostis <lakostis@altlinux.ru> 2.1.0-alt3
- Added patch for rocm-6.0.0.

* Sun Dec 10 2023 L.A. Kostis <lakostis@altlinux.ru> 2.1.0-alt2
- Enabled CUDA support (and downgrade to gcc12 on arches where
  CUDA packaged).
- Split HIP/CUDA support libs to separate pkgs.

* Wed Oct 25 2023 L.A. Kostis <lakostis@altlinux.ru> 2.1.0-alt1
- Updated to upstream version 2.1.0.

* Wed Jul 05 2023 L.A. Kostis <lakostis@altlinux.ru> 2.0.1-alt1
- Updated to upstream version 2.0.1.
- Rebuild with HIP rocm-5.6.0.

* Tue Jun 20 2023 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt1
- Updated to upstream version 2.0.0.
- Built with HIP.

* Mon Sep 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt1
- Updated to upstream version 1.4.1.

* Wed Jun 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt1
- Initial build for ALT.
