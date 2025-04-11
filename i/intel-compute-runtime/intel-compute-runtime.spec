%define soversion 1
%define llvmversion 19.1
%define oclocversion 25.09.1
# LTO will be checked during configuration
%define optflags_lto %nil

Name: intel-compute-runtime
Version: 25.09.32961.8
Release: alt1.1
Summary: Intel(R) Graphics Compute Runtime for OpenCL(TM)
License: MIT
Group: System/Libraries
Url: https://github.com/intel/compute-runtime

Source: %name-%version.tar

Patch1: intel-compute-runtime-24.35.30872.18-alt-build.patch

BuildRequires(pre): rpm-build-cmake ninja-build
BuildRequires: clang%llvmversion libstdc++-devel
BuildRequires: libintel-opencl-clang-devel
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
The Intel(R) Graphics Compute Runtime for OpenCL(TM) is a open source project to
converge Intel's development efforts on OpenCL(TM) compute stacks supporting
the GEN graphics hardware architecture.

%package -n intel-ocloc
Summary: Tool for managing Intel Compute GPU device binary format
Group: Development/Tools

%description -n intel-ocloc
ocloc is a tool for managing Intel Compute GPU device binary format (a format
used by Intel Compute GPU runtime).  It can be used for generation (as part of
'compile' command) as well as manipulation (decoding/modifying - as part of
'disasm'/'asm' commands) of such binary files.

%package -n intel-ocloc-devel
Summary: Tool for managing Intel Compute GPU device binary format - Devel Files
Group: System/Libraries
Requires: intel-ocloc

%description -n intel-ocloc-devel
Devel files (headers and libraries) for developing against
intel-ocloc (a tool for managing Intel Compute GPU device binary format).

%package -n intel-opencl
Summary: OpenCL support implementation for Intel GPUs
Group: System/Libraries
Provides: intel-opencl-icd
Requires: libigdfcl2
Requires: libigc2
Requires: libigdgmm12
Requires: opencl-filesystem

%description -n intel-opencl
Implementation for the Intel GPUs of the OpenCL specification - a generic
compute oriented API. This code base contains the code to run OpenCL programs
on Intel GPUs which basically defines and implements the OpenCL host functions
required to initialize the device, create the command queues, the kernels and
the programs and run them on the GPU.

%package -n libze-intel-gpu%soversion
Summary: oneAPI L0 support implementation for Intel GPUs
Group: System/Libraries
Requires: libigdfcl2
Requires: libigc2
Requires: libigdgmm12

%description -n libze-intel-gpu%soversion
Implementation for the Intel GPUs of the oneAPI L0 specification -  which
provides direct-to-metal interfaces to offload accelerator devices. Its
programming interface can be tailored to any device needs and can be adapted to
support broader set of languages features such as function pointers, virtual
functions, unified memory, and I/O capabilities..

%package -n libze-intel-gpu-devel
Summary: oneAPI L0 support implementation for Intel GPUs - Devel Files
Group: System/Libraries
Requires: libze-intel-gpu%soversion

%description -n libze-intel-gpu-devel
Devel files (headers and libraries) for developing against libze-intel-gpu.

%prep
%setup
%patch1 -p1

%build
export ALTWRAP_LLVM_VERSION=%llvmversion
%cmake -G Ninja \
 -DCMAKE_C_COMPILER=/usr/bin/clang \
 -DCMAKE_CXX_COMPILER=/usr/bin/clang++ \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DSKIP_UNIT_TESTS=1

%cmake_build

%install
%cmake_install

mv %buildroot%_bindir/ocloc-%oclocversion %buildroot%_bindir/ocloc

%files -n intel-opencl
%_libdir/intel-opencl
%_sysconfdir/OpenCL/vendors/intel.icd

%files -n libze-intel-gpu%soversion
%_libdir/libze_intel_gpu.so.%soversion.*
%_libdir/libze_intel_gpu.so.%soversion

%files -n libze-intel-gpu-devel
%_includedir/level_zero

%files -n intel-ocloc
%_bindir/ocloc
%_libdir/libocloc.so

%files -n intel-ocloc-devel
%_includedir/ocloc_api.h

%changelog
* Fri Apr 11 2025 L.A. Kostis <lakostis@altlinux.ru> 25.09.32961.8-alt1.1
- NMU:
  - spec: cleanup.
  - Use ninja-build.
  - Use cmake macros (to have consistent build flags and debuginfo).
  - Compile with clang19 (should fix luxmark segfaults).
  - optflags: disable LTO (will be checked during configuration).

* Thu Apr 10 2025 Andrey Kovalev <ded@altlinux.org> 25.09.32961.8-alt1
- Updated to upstream version 25.09.32961.8.

* Tue Mar 11 2025 Andrey Kovalev <ded@altlinux.org> 25.05.32567.18-alt1
- Updated to upstream version 25.05.32567.18.

* Mon Jan 20 2025 Andrey Kovalev <ded@altlinux.org> 24.52.32224.7-alt1
- Updated to upstream version 24.52.32224.7.

* Thu Dec 12 2024 Andrey Kovalev <ded@altlinux.org> 24.48.31907.6-alt1
- Updated to upstream version 24.48.31907.6.

* Mon Nov 11 2024 Andrey Kovalev <ded@altlinux.org> 24.39.31294.12-alt1
- Updated to upstream version 24.39.31294.12.
- Added patch for fix error in Davinci Resolve (closes: #51702).

* Mon Sep 16 2024 Andrey Kovalev <ded@altlinux.org> 24.35.30872.18-alt2
- Added provides intel-opencl-icd for intel-opencl.

* Fri Sep 13 2024 Andrey Kovalev <ded@altlinux.org> 24.35.30872.18-alt1
- Intial build for Sisyphus.

