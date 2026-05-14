%ifarch x86_64 aarch64
%def_with cuda
%filter_from_requires /libcuda\.so\.1/d
%else
%def_without cuda
%endif

Name: clpeak
Version: 2.0.6
Release: alt1
Summary: A tool which profiles OpenCL devices to find their peak capacities
License: Apache-2.0
Group: System/Configuration/Hardware
Url: https://github.com/krrishnarraj/clpeak

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: opencl-cpp-headers ocl-icd-devel gcc-c++ libvulkan-devel glslc
%if_with cuda
BuildRequires: nvidia-cuda-devel
%endif

%description
A synthetic micro-benchmark that measures the peak achievable performance of
GPU compute devices. It exercises tight vector / MAD / MMA loops and vendor-SDK
GEMM libraries (cuBLASLt on NVIDIA, MPS on Apple) to expose what the hardware
is capable of - from raw ALU peaks to near-vendor-advertised matrix
throughput.

clpeak began as an OpenCL-only tool. It now ships four interchangeable
backends - OpenCL, Vulkan, CUDA, and Metal. Rrunning back-to-back on the same
hardware, so cross-stack differences (driver lowering, instruction scheduling,
extension exposure) become visible alongside the raw peak numbers.

%package cuda
Summary: %name with CUDA support
Group: System/Configuration/Hardware
Requires: libcuda

%description cuda
%name with CUDA support.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	%nil
%cmake_build
%if_with cuda
mv %_cmake__builddir/%name /tmp/%name-cuda
make -C %_cmake__builddir clean
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCLPEAK_ENABLE_CUDA=OFF \
	%nil
%cmake_build
%endif

%install
%cmake_install
rm -rf %buildroot%_datadir
%if_with cuda
install -pm755 /tmp/%name-cuda %buildroot%_bindir/
%endif

%files
%doc LICENSE README.md
%_bindir/%name

%if_with cuda
%files cuda
%_bindir/%name-cuda
%endif

%changelog
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
