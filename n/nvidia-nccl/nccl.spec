%define _unpackaged_files_terminate_build 1

%define soversion 2

# NVCC is incompatible with GCC 15, use GCC 14 as host compiler.
%define nvcc_host_gcc_version 14
%define nvcc_host_cc  %_bindir/gcc-%nvcc_host_gcc_version
%define nvcc_host_cxx %_bindir/g++-%nvcc_host_gcc_version

Name:    nvidia-nccl
Version: 2.30.3
Release: alt1

Summary: Optimized primitives for collective multi-GPU communication
License: Apache-2.0 AND BSD-3-Clause
Group:   System/Libraries
URL: 	 https://developer.nvidia.com/nccl
Vcs:     https://github.com/NVIDIA/nccl.git

Source: nvidia-nccl-%version.tar

ExclusiveArch: x86_64 aarch64

BuildRequires: gcc%nvcc_host_gcc_version-c++
BuildRequires: nvidia-cuda-devel
BuildRequires: libcudart
BuildRequires: python3

%description
NCCL (pronounced "Nickel") is a stand-alone library
of standard communication routines for GPUs, implementing all-reduce,
all-gather, reduce, broadcast, reduce-scatter,
as well as any send/receive based communication pattern.
It has been optimized to achieve high bandwidth on platforms using PCIe,
NVLink, NVswitch, as well as networking using InfiniBand Verbs
or TCP/IP sockets. NCCL supports an arbitrary number of GPUs installed
in a single node or across multiple nodes, and can be used in either
single- or multi-process (e.g., MPI) applications.

For more information on NCCL usage, please refer to the NCCL documentation.

%package 	-n libnccl%soversion
Group: System/Libraries
Summary: Optimized primitives for collective multi-GPU communication

%description 	-n libnccl%soversion
NCCL (pronounced "Nickel") is a stand-alone library
of standard communication routines for GPUs, implementing all-reduce,
all-gather, reduce, broadcast, reduce-scatter,
as well as any send/receive based communication pattern.
It has been optimized to achieve high bandwidth on platforms using PCIe,
NVLink, NVswitch, as well as networking using InfiniBand Verbs
or TCP/IP sockets. NCCL supports an arbitrary number of GPUs installed
in a single node or across multiple nodes, and can be used in either
single- or multi-process (e.g., MPI) applications.

For more information on NCCL usage, please refer to the NCCL documentation.

%package 	-n libnccl-devel
Summary: Development files for libnccl
Group: Development/Other
Requires: libnccl%soversion = %EVR

%description 	-n libnccl-devel
%summary.

%prep
%setup

%build
export CC=%nvcc_host_cc
export CXX=%nvcc_host_cxx
export NVCC_CCBIN=%nvcc_host_cxx

export CUDARTLIB=cudart
export CUDA_HOME=%_usr
%make_build src.build

%install
export CUDARTLIB=cudart
export CUDA_HOME=%_usr
export PREFIX=%buildroot/%_prefix
%makeinstall_std

install -d %buildroot%_libdir
install -d %buildroot%_pkgconfigdir

mv %buildroot%_libexecdir/* %buildroot%_libdir/

# Delete static library
rm -rv %buildroot/%_libdir/libnccl_static.a

%files 		-n libnccl%soversion
%doc *.md LICENSE.txt
%_libdir/libnccl.so.%{soversion}*

%files 		-n libnccl-devel
%_bindir/ncclras
%_bindir/ncclparam
%_includedir/*
%_pkgconfigdir/nccl.pc
%_libdir/libnccl.so

%changelog
* Mon Jun 29 2026 Nikita Shmatko <nash@altlinux.org> 2.30.3-alt1
- New version 2.30.3.
- Used gcc 14 as NVCC host compiler to avoid gcc 15 incompatibility.
- Dropped the unused static library subpackage.

* Mon Apr 13 2026 Nikita Shmatko <nash@altlinux.org> 2.29.7-alt1
- New version 2.29.7.
- Changed license to relevant.

* Wed Feb 04 2026 Nikita Shmatko <nash@altlinux.org> 2.28.3-alt1
- Initial build for Sisyphus.
