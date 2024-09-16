%define soversion 1
%define llvmversion 14

Name: intel-compute-runtime
Version: 24.35.30872.18
Release: alt2
Summary: Intel(R) Graphics Compute Runtime for OpenCL(TM)
License: MIT
Group: System/Libraries
URL: https://github.com/intel/compute-runtime

Source: %name-%version.tar

Patch1: intel-compute-runtime-2.35.30872.18-alt-build.patch

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libintel-opencl-clang%llvmversion-devel
BuildRequires: libigdfcl-devel
BuildRequires: libigc-devel
BuildRequires: intel-gmmlib-devel
BuildRequires: libva-devel
BuildRequires: libdrm-devel
BuildRequires: libglvnd-devel
BuildRequires: ocl-icd-devel
BuildRequires: opencl-headers
BuildRequires: liboneapi-level-zero1-devel

Requires: intel-ocloc = %{version}-%{release}
Requires: intel-opencl = %{version}-%{release}
Requires: libze-intel-gpu%soversion = %{version}-%{release}

ExclusiveArch: x86_64

%description
The Intel(R) Graphics Compute Runtime for OpenCL(TM) is a open source project to
converge Intel's development efforts on OpenCL(TM) compute stacks supporting
the GEN graphics hardware architecture.
 
%package -n intel-ocloc
Summary: Tool for managing Intel Compute GPU device binary format
Group: Development/Tools
 
%description -n intel-ocloc
ocloc is a tool for managing Intel Compute GPU device binary format (a format used by Intel Compute GPU runtime).
It can be used for generation (as part of 'compile' command) as well as
manipulation (decoding/modifying - as part of 'disasm'/'asm' commands) of such binary files.
 
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
Requires: libigdfcl1
Requires: libigc1
Requires: libigdgmm12

%description -n intel-opencl
Implementation for the Intel GPUs of the OpenCL specification - a generic
compute oriented API. This code base contains the code to run OpenCL programs
on Intel GPUs which basically defines and implements the OpenCL host functions
required to initialize the device, create the command queues, the kernels and
the programs and run them on the GPU.

%package -n libze-intel-gpu%soversion
Summary: oneAPI L0 support implementation for Intel GPUs
Group: System/Libraries
Requires: libigdfcl1
Requires: libigc1
Requires: libigdgmm12

%description -n libze-intel-gpu%soversion
Implementation for the Intel GPUs of the oneAPI L0 specification -  which provides direct-to-metal
interfaces to offload accelerator devices. Its programming interface can be tailored to any device
needs and can be adapted to support broader set of languages features such as function pointers,
virtual functions, unified memory, and I/O capabilities..

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
mkdir -p build
pushd build
cmake .. \
 -DCMAKE_INSTALL_PREFIX=%_prefix \
 -DCMAKE_INSTALL_LIBDIR=%_libdir \
 -DCMAKE_BUILD_TYPE=Release \
 -DSKIP_UNIT_TESTS=1

%make_build
popd

%install
pushd build
%makeinstall_std
popd

mv %buildroot%_bindir/ocloc-24.35.1 %buildroot%_bindir/ocloc

%files -n intel-opencl
%_libdir/intel-opencl/libigdrcl.so
%_sysconfdir/OpenCL/vendors/intel.icd
 
%files -n libze-intel-gpu%soversion
%_libdir/libze_intel_gpu.so.%soversion.*
%_libdir/libze_intel_gpu.so.%soversion

%files -n libze-intel-gpu-devel
%_includedir/level_zero/zet_intel_gpu_debug.h
 
%files -n intel-ocloc
%_bindir/ocloc
%_libdir/libocloc.so
 
%files -n intel-ocloc-devel
%_includedir/ocloc_api.h

%changelog
* Mon Sep 16 2024 Andrey Kovalev <ded@altlinux.org> 24.35.30872.18-alt2
- Added provides intel-opencl-icd for intel-opencl.

* Fri Sep 13 2024 Andrey Kovalev <ded@altlinux.org> 24.35.30872.18-alt1
- Intial build for Sisyphus.

