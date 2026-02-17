%define _unpackaged_files_terminate_build 1

%define soversion 2

%define oname nccl

Name:    nvidia-%oname
Version: 2.28.3
Release: alt1

Summary: Optimized primitives for collective multi-GPU communication
License: NVIDIA
Group:   System/Libraries
URL: 	 https://developer.nvidia.com/nccl
Vcs:     https://github.com/NVIDIA/nccl.git

Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

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

%package 	-n lib%oname%soversion
Group: System/Libraries
Summary: Optimized primitives for collective multi-GPU communication

%description 	-n lib%oname%soversion
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

%package 	-n lib%oname-devel
Summary: Development files for lib%name
Group: Development/Other
Requires: lib%oname%soversion = %EVR

%description 	-n lib%oname-devel
%summary.

%package 	-n lib%oname-static
Summary: Static libraries for lib%name
Group: Development/Other

%description 	-n lib%oname-static
%summary.

%prep
%setup

%build
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

%files 		-n lib%oname%soversion
%doc *.md LICENSE.txt
%_libdir/lib%oname.so.*

%files 		-n lib%oname-devel
%_bindir/ncclras
%_includedir/*
%_pkgconfigdir/%oname.pc
%_libdir/lib%oname.so

%files 		-n lib%oname-static
%_libdir/lib%{oname}_static.a

%changelog
* Wed Feb 04 2026 Nikita Shmatko <nash@altlinux.org> 2.28.3-alt1
- Initial build for Sisyphus.
