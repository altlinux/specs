%ifarch x86_64 aarch64
%def_with cuda
%define gcc_ver 14
%filter_from_requires /libcuda\.so\.1/d
%else
%def_without cuda
%endif
%ifarch x86_64
# rocm in sisyphus is too old
# update blocked by https://bugzilla.altlinux.org/56361
%def_without rocm
%def_with oneapi
%else
%def_without rocm
%def_without oneapi
%endif

Name: clpeak
Version: 2.0.19
Release: alt1
Summary: A synthetic micro-benchmark that measures the peak achievable performance of GPU compute devices
License: Apache-2.0
Group: System/Configuration/Hardware
Url: https://github.com/krrishnarraj/clpeak
Vcs: https://github.com/krrishnarraj/clpeak

Source0: %name-%version.tar
# https://github.com/IntelPython/dpctl/blob/master/cmake/IntelSYCLConfig.cmake
Source1: IntelSYCLConfig.cmake
Patch0: %name-alt-rocm-paths.patch
Patch1: %name-alt-cmake.patch
Patch2: %name-sycl.patch

BuildRequires(pre): cmake
BuildRequires: opencl-cpp-headers ocl-icd-devel gcc-c++ libvulkan-devel glslc
%if_with cuda
BuildRequires: gcc%gcc_ver-c++ libstdc++%gcc_ver-devel nvidia-cuda-devel
%endif
%if_with rocm
BuildRequires: hip-devel rocm-comgr-devel hsa-rocr-devel hipblas-common librocwmma-devel rocblas-devel hipblaslt-devel
%endif
%if_with oneapi
BuildRequires: libsycl-devel llvm-spirv llvm-dpcpp clang-dpcpp clang-dpcpp-tools clang-dpcpp-devel chrpath
%endif

%description
clpeak "Compute Latency PEAK". A synthetic micro-benchmark for
measuring the peak achievable compute performance of CPUs and GPUs. It
exercises tight vector, MAD, and MMA kernels, together with vendor-optimized
GEMM libraries, to expose peak hardware throughput.

Originally an OpenCL benchmark, clpeak now supports OpenCL, Vulkan, CUDA,
ROCm/HIP, Metal, oneAPI/SYCL, and native CPU execution, enabling direct
cross-backend comparisons on the same hardware.

This package supports only bare minimum - OpenCL and Vulkan, for extra install
respective -<tech> package to get CUDA/ROCm/oneAPI instead.

%package cuda
Summary: %name with CUDA support
Group: System/Configuration/Hardware
Requires: libcuda

%description cuda
%name with CUDA support.

%package rocm
Summary: %name with ROCm/HIP support
Group: System/Configuration/Hardware

%description rocm
%name with ROCm/HIP support.

%package oneapi
Summary: %name with oneAPI/SYCL support
Group: System/Configuration/Hardware

%description oneapi
%name with oneAPI/SYCL support.

%prep
%setup
%autopatch -p1
mkdir -p cmake
install -pm644 %SOURCE1 cmake/

%build
%if_with cuda
export GCC_VERSION=%gcc_ver
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCLPEAK_ENABLE_ROCM=OFF \
	-DCLPEAK_ENABLE_ONEAPI=OFF \
	%nil
%cmake_build
mv %_cmake__builddir/%name /tmp/%name-cuda
rm -rf %_cmake__builddir
%endif
%if_with rocm
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCLPEAK_ENABLE_CUDA=OFF \
	-DCLPEAK_ENABLE_ONEAPI=OFF \
	%nil
%cmake_build
mv %_cmake__builddir/%name /tmp/%name-rocm
rm -rf %_cmake__builddir
%endif
%if_with oneapi
# DPCPP is not compatible with LTO
%define optflags_lto %nil
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_CXX_COMPILER=%_prefix/lib/llvm-dpcpp/bin/clang++ \
	-DCLPEAK_ENABLE_CUDA=OFF \
	-DCLPEAK_ENABLE_ROCM=OFF \
	%nil
%cmake_build
mv %_cmake__builddir/%name /tmp/%name-oneapi
rm -rf %_cmake__builddir
%endif
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCLPEAK_ENABLE_ROCM=OFF \
	-DCLPEAK_ENABLE_CUDA=OFF \
	-DCLPEAK_ENABLE_ONEAPI=OFF \
	%nil
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_datadir
%{?_with_cuda:install -pm755 /tmp/%name-cuda %buildroot%_bindir/}
%{?_with_rocm:install -pm755 /tmp/%name-rocm %buildroot%_bindir/} 
%{?_with_oneapi:chrpath -d /tmp/%name-oneapi; install -pm755 /tmp/%name-oneapi %buildroot%_bindir/}

%files
%doc LICENSE README.md
%_bindir/%name

%if_with cuda
%files cuda
%_bindir/%name-cuda
%endif

%if_with rocm
%files rocm
%_bindir/%name-rocm
%endif

%if_with oneapi
%files oneapi
%_bindir/%name-oneapi
%endif

%changelog
* Tue Aug 18 2026 L.A. Kostis <lakostis@altlinux.ru> 2.0.19-alt1
- 2.0.19.

* Thu Jul 30 2026 L.A. Kostis <lakostis@altlinux.ru> 2.0.18-alt1
- 2.0.18.
- split out cuda/rocm/oneapi to separate subpkgs.

* Wed May 27 2026 L.A. Kostis <lakostis@altlinux.ru> 2.0.9-alt1
- 2.0.9.

* Thu May 14 2026 L.A. Kostis <lakostis@altlinux.ru> 2.0.6-alt1
- 2.0.6.
- Enable vulkan.
- Enable CUDA on x86_64/aarch64.

* Sat Mar 21 2026 L.A. Kostis <lakostis@altlinux.ru> 1.1.7-alt1
- 1.1.7.

* Mon Jun 16 2025 L.A. Kostis <lakostis@altlinux.ru> 1.1.5-alt1
- 1.1.5.

* Mon Feb 17 2025 L.A. Kostis <lakostis@altlinux.ru> 1.1.4-alt1
- Initial build for ALTLinux.
