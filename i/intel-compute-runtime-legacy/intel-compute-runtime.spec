%define soversion 1
%define llvmversion 16
%define prefix legacy1
%define optflags_lto %nil

Name: intel-compute-runtime-legacy
Version: 24.35.30872.45
Release: alt1
Summary: Intel(R) Graphics Compute Runtime for OpenCL(TM)
License: MIT
Group: System/Libraries
Url: https://github.com/intel/compute-runtime

Source: %name-%version.tar

Patch1: intel-compute-runtime-24.35.30872.18-alt-build.patch

BuildRequires(pre): cmake ninja-build
BuildRequires: gcc-c++ libstdc++-devel
BuildRequires: libintel-opencl-clang%llvmversion-devel
BuildRequires: libigdfcl-devel
BuildRequires: libigc-devel
BuildRequires: intel-gmmlib-devel
BuildRequires: libva-devel
BuildRequires: libdrm-devel
BuildRequires: libglvnd-devel
BuildRequires: ocl-icd-devel
BuildRequires: opencl-headers
BuildRequires: libze-devel

ExclusiveArch: x86_64

%description
The Intel(R) Graphics Compute Runtime for OpenCL(TM) is a open source project
to converge Intel's development efforts on OpenCL(TM) compute stacks supporting
the GEN graphics hardware architecture.

%package -n intel-opencl-%prefix
Summary: OpenCL support implementation for Intel GPUs (legacy version)
Group: System/Libraries
Provides: intel-opencl-icd-legacy = %EVR
Provides: intel-opencl-legacy = %EVR
Requires: libigdfcl2
Requires: libigc2
Requires: libigdgmm12

%description -n intel-opencl-%prefix
Implementation for the Intel GPUs of the OpenCL specification - a generic
compute oriented API. This code base contains the code to run OpenCL programs
on Intel GPUs which basically defines and implements the OpenCL host functions
required to initialize the device, create the command queues, the kernels and
the programs and run them on the GPU.

%package -n libze-intel-gpu-%prefix
Summary: oneAPI L0 support implementation for Intel GPUs (legacy version)
Group: System/Libraries
Requires: libigdfcl2
Requires: libigc2
Requires: libigdgmm12

%description -n libze-intel-gpu-%prefix
Implementation for the Intel GPUs of the oneAPI L0 specification -  which
provides direct-to-metal interfaces to offload accelerator devices. Its
programming interface can be tailored to any device needs and can be adapted to
support broader set of languages features such as function pointers, virtual
functions, unified memory, and I/O capabilities..

%prep
%setup
%patch1 -p1

%build
%cmake -G Ninja \
 -DCMAKE_INSTALL_PREFIX=%prefix \
 -DCMAKE_INSTALL_LIBDIR=%_libdir \
 -DNEO_ALLOW_LEGACY_PLATFORMS_SUPPORT:BOOL=TRUE \
 -DNEO_CURRENT_PLATFORMS_SUPPORT:BOOL=FALSE \
 -DCMAKE_BUILD_TYPE=RelwithDebInfo \
 -DSKIP_UNIT_TESTS=1

%cmake_build

%install
%cmake_install

%files -n intel-opencl-%prefix
%_libdir/intel-opencl/libigdrcl_%prefix.so
%_sysconfdir/OpenCL/vendors/intel_%prefix.icd

%files -n libze-intel-gpu-%prefix
%_libdir/libze_intel_gpu_%prefix.so.%soversion.*
%_libdir/libze_intel_gpu_%prefix.so.%soversion

%changelog
* Thu Mar 19 2026 L.A. Kostis <lakostis@altlinux.ru> 24.35.30872.45-alt1
- 24.35.30872.45.
- Build with gcc.

* Tue Mar 17 2026 L.A. Kostis <lakostis@altlinux.ru> 24.35.30872.36-alt1
- 24.35.30872.36.
- Rebuild w/ llvm16.

* Thu Jun 19 2025 L.A. Kostis <lakostis@altlinux.ru> 24.35.30872.32-alt3
- Rebuild w/ llvm15.

* Mon Feb 03 2025 L.A. Kostis <lakostis@altlinux.ru> 24.35.30872.32-alt2
- Rebuild w/ llvm14 and disable LTO.

* Thu Jan 30 2025 L.A. Kostis <lakostis@altlinux.ru> 24.35.30872.32-alt1
- Build legacy ICD.
