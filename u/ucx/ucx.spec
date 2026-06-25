%define _unpackaged_files_terminate_build 1

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define abiversion 0

%def_with cma
%def_without cuda
%def_without gdrcopy
%def_with ib
%def_without knem
%def_with rdmacm
%def_without ugni
%def_without xpmem
%def_without vfs
%def_without mad
%def_with mlx5

Name:    ucx
Version: 1.20.1
Release: alt1

Summary: Unified Communication X  (mailing list - https://elist.ornl.gov/mailman/listinfo/ucx-group)
License: BSD-3-Clause
Group:   Networking/Other 
Url:     https://openucx.org/
Vcs:     https://github.com/openucx/ucx.git

Source: ucx-%version.tar
Source1: ucg.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: libnuma-devel
%if_with cma
BuildRequires: glibc-devel
%endif
%if_with gdrcopy
BuildRequires: gdrcopy
%endif
%if_with ib
BuildRequires: libibverbs-devel
%endif
%if_with mlx5
BuildRequires: rdma-core-devel
%endif
%if_with knem
BuildRequires: knem-devel
%endif
%if_with rdmacm
BuildRequires: librdmacm-devel
%endif
%if_with xpmem
BuildRequires: xpmem-devel
%endif
%if_with vfs
BuildRequires: libfuse3-devel
%endif
%if_with mad
BuildRequires: libibmad libibumad
%endif

#error "Unsupported architecture" avoid
ExcludeArch: %ix86

Requires: libucx%abiversion = %EVR

%description
UCX is an optimized communication framework for high-performance distributed
applications. UCX utilizes high-speed networks, such as RDMA (InfiniBand, RoCE,
etc), Cray Gemini or Aries, for inter-node communication. If no such network is
available, TCP is used instead. UCX supports efficient transfer of data in
either main memory (RAM) or GPU memory (through CUDA and ROCm libraries). In
addition, UCX provides efficient intra-node communication, by leveraging the
following shared memory mechanisms: posix, sysv, cma, knem, and xpmem.
The acronym UCX stands for "Unified Communication X".

%package -n libucx%abiversion
Summary: Runtime library for UCX.
Group: System/Libraries

%description -n libucx%abiversion
This package contains the shared runtime library for ucx.

%package -n libucx-devel
Requires: libucx%abiversion = %EVR
Group: Development/C
Summary: Header files required for developing with UCX.

%description -n libucx-devel
Provides header files and examples for developing with UCX.

%if_with cma
%package -n libucx%abiversion-cma
Requires: libucx%abiversion = %EVR
Obsoletes: libucx-cma < %EVR
Group: System/Libraries
Summary: UCX CMA support.

%description -n libucx%abiversion-cma
Provides CMA (Linux cross-memory-attach) transport for UCX. It utilizes the
system calls process_vm_readv/writev() for one-shot memory copy from another
process.
%endif

%if_with cuda
%package -n libucx%abiversion-cuda
Requires: libucx%abiversion = %EVR
Obsoletes: libucx-cuda < %EVR
Summary: UCX CUDA support.
Group: System/Libraries

%description -n libucx%abiversion-cuda
Provide CUDA (NVIDIA GPU) support for UCX. Enables passing GPU memory pointers
to UCX communication routines, and transports taking advantage of GPU-Direct
technology for direct data transfer between GPU and RDMA devices.
%endif

%if_with gdrcopy
%package -n libucx%abiversion-gdrcopy
Requires: libucx%abiversion-cuda = %EVR
Obsoletes: libucx-gdrcopy < %EVR
Summary: UCX GDRCopy support.
Group: System/Libraries

%description -n libucx%abiversion-gdrcopy
Provide GDRCopy support for UCX. GDRCopy is a low-latency GPU memory copy
library, built on top of the NVIDIA GPUDirect RDMA technology.
%endif

%if_with ib
%package -n libucx%abiversion-ib
Requires: libucx%abiversion = %EVR
Obsoletes: libucx-ib < %EVR
Summary: UCX RDMA support.
Group: System/Libraries

%description -n libucx%abiversion-ib
Provides support for IBTA-compliant transports for UCX. This includes RoCE,
InfiniBand, OmniPath, and any other transport supported by IB Verbs API.
Typically these transports provide RDMA support, which enables a fast and
hardware-offloaded data transfer.
%endif

%package -n libucx%abiversion-ib-efa
Requires: libucx%abiversion-ib = %EVR
Obsoletes: libucx-ib-efa < %EVR
Summary: UCX IB EFA provider support.
Group: System/Libraries

%description -n libucx%abiversion-ib-efa
Provides UCX InfiniBad EFA transport.

%if_with knem
%package -n libucx%abiversion-knem
Requires: libucx%abiversion = %EVR
Obsoletes: libucx-knem < %EVR
Summary: UCX KNEM transport support.
Group: System/Libraries

%description -n libucx%abiversion-knem 
Provides KNEM (fast inter-process copy) transport for UCX. KNEM is a Linux
kernel module that enables high-performance intra-node MPI communication
for large messages.
%endif

%if_with rdmacm
%package -n libucx%abiversion-rdmacm
Requires: libucx%abiversion-ib = %EVR
Obsoletes: libucx-rdmacm < %EVR
Group: System/Libraries
Summary: UCX RDMA connection manager support.

%description -n libucx%abiversion-rdmacm
Provides RDMA connection-manager support to UCX, which enables client/server
based connection establishment for RDMA-capable transports.
%endif

%if_with ugni
%package -n libucx%abiversion-ugni
Requires: libucx%abiversion = %EVR
Obsoletes: libucx-ugni < %EVR
Summary: UCX Gemini/Aries transport support.
Group: System/Libraries

%description -n libucx%abiversion-ugni
Provides Gemini/Aries transport for UCX.
%endif

%if_with xpmem
%package -n libucx%abiversion-xpmem
Requires: libucx%abiversion = %EVR
Obsoletes: libucx-xpmem < %EVR
Group: System/Libraries
Summary: UCX XPMEM transport support.

%description -n libucx%abiversion-xpmem
Provieds XPMEM transport for UCX. XPMEM is a Linux kernel module that enables a
process to map the memory of another process into its virtual address space.
%endif

%if_with vfs
%package -n ucx-vfs
Summary: UCX virtual filesystem tool
Group: Monitoring
Requires: libucx%abiversion-vfs = %EVR

%description -n ucx-vfs
Provides the ucx_vfs command-line tool that mounts a FUSE-based virtual
filesystem exposing UCX library internals - protocol objects, transport
status, and other runtime state - for real-time monitoring.

%package -n libucx%abiversion-vfs
Requires: libucx%abiversion = %EVR
Obsoletes: libucx-vfs < %EVR
Group: System/Libraries
Summary: UCX Virtual Filesystem support.

%description -n libucx%abiversion-vfs
Provides a virtual filesystem over FUSE which allows real-time
monitoring of UCX library internals, protocol objects, transports
status, and more.
%endif

%if_with mlx5
%package -n libucx%abiversion-ib-mlx5
Requires: libucx%abiversion = %EVR
Obsoletes: libucx-ib-mlx5 < %EVR
Summary: UCX IB MLX5 RDMA provider support.
Group: System/Libraries

%description -n libucx%abiversion-ib-mlx5
Provides support for DevX, Direct Verbs and DC transports for Infiniband
devices
%endif

%if_with mad
%package -n libucx%abiversion-mad
Requires: libucx%abiversion = %EVR
Obsoletes: libucx-mad < %EVR
Summary: UCX Infiniband MAD support
Group: System/Libraries

%description -n libucx%abiversion-mad
Provide Infiniband mad support for UCX. Enables running perftest using
Infiniband datagrams for out-of-band communications.
%endif

%prep
%setup -a1 -n ucx-%version

%build
%autoreconf
%configure \
    --disable-optimizations \
    --disable-logging \
    --disable-debug \
    --disable-rpath \
    --disable-assertions \
    --disable-static \
    --disable-params-check \
    --without-java \
    --without-rocm \
%if_with cma
    --enable-cma \
%else
    --disable-cma \
%endif
%if_with cuda
    --with-cuda \
%else
    --without-cuda \
%endif
%if_with gdrcopy
    --with-gdrcopy \
%else
    --without-gdrcopy \
%endif
%if_with ib
    --with-verbs \
%else
    --without-verbs \
%endif
%if_with mlx5
    --with-mlx5 \
%else
    --without-mlx5 \
%endif
%if_with knem
    --with-knem \
%else
    --without-knem \
%endif
%if_with rdmacm
    --with-rdmacm \
%else
    --without-rdmacm \
%endif
%if_with xpmem
    --with-xpmem \
%else
    --without-xpmem \
%endif
%if_with vfs
    --with-fuse3 \
%else
    --without-fuse3 \
%endif
%if_with ugni
    --with-ugni \
%else
    --without-ugni \
%endif
%if_with mad
    --with-mad \
%else
    --without-mad \
%endif

%make_build V=1

%install
%set_verify_elf_method relaxed
install -d %buildroot%_includedir/ucs/sys
install -m644 src/ucs/sys/sys.h %buildroot%_includedir/ucs/sys/

%makeinstall_std

rm -f %buildroot%_libdir/*.la
rm -f %buildroot%_libdir/*.a
rm -f %buildroot%_libdir/ucx/*.la
rm -f %buildroot%_libdir/ucx/lib*.so
rm -f %buildroot%_libdir/ucx/lib*.a

%files
%doc LICENSE README AUTHORS NEWS
%_bindir/ucx_info
%_bindir/ucx_perftest
%_bindir/ucx_perftest_daemon
%_bindir/ucx_read_profile
%_bindir/io_demo
%_datadir/ucx
%dir %_sysconfdir/ucx
%config(noreplace) %_sysconfdir/ucx/ucx.conf
%exclude %_datadir/ucx/examples

%files -n libucx%abiversion
%dir %_libdir/ucx
%_libdir/lib*.so.%{abiversion}*

%files -n libucx-devel
%_includedir/uc*
%_libdir/lib*.so
%_pkgconfigdir/ucx*.pc
%dir %_cmakedir/ucx
%_cmakedir/ucx/*.cmake
%_datadir/ucx/examples

%if_with cma
%files -n libucx%abiversion-cma
%dir %_libdir/ucx
%_libdir/ucx/libuct_cma.so.%{abiversion}*
%endif

%if_with cuda
%files -n libucx%abiversion-cuda
%dir %_libdir/ucx
%_libdir/ucx/libucx_perftest_cuda.so.%{abiversion}*
%_libdir/ucx/libucm_cuda.so.%{abiversion}*
%_libdir/ucx/libuct_cuda.so.%{abiversion}*
%endif

%if_with gdrcopy
%files -n libucx%abiversion-gdrcopy
%dir %_libdir/ucx
%_libdir/ucx/libuct_cuda_gdrcopy.so.%{abiversion}*
%endif

%if_with ib
%files -n libucx%abiversion-ib
%dir %_libdir/ucx
%_libdir/ucx/libuct_ib.so.%{abiversion}*
%endif

%files -n libucx%abiversion-ib-efa
%_libdir/ucx/libuct_ib_efa.so.%{abiversion}*

%if_with knem
%files -n libucx%abiversion-knem
%dir %_libdir/ucx
%_libdir/ucx/libuct_knem.so.%{abiversion}*
%endif

%if_with rdmacm
%files -n libucx%abiversion-rdmacm
%dir %_libdir/ucx
%_libdir/ucx/libuct_rdmacm.so.%{abiversion}*
%endif

%if_with ugni
%files -n libucx%abiversion-ugni
%dir %_libdir/ucx
%_libdir/ucx/libuct_ugni.so.%{abiversion}*
%endif

%if_with xpmem
%files -n libucx%abiversion-xpmem
%dir %_libdir/ucx
%_libdir/ucx/libuct_xpmem.so.%{abiversion}*
%endif

%if_with vfs
%files -n ucx-vfs
%_bindir/ucx_vfs

%files -n libucx%abiversion-vfs
%dir %_libdir/ucx
%_libdir/ucx/libucs_fuse.so.%{abiversion}*
%endif

%if_with mlx5
%files -n libucx%abiversion-ib-mlx5
%_libdir/ucx/libuct_ib_mlx5.so.%{abiversion}*
%endif

%if_with mad
%files -n libucx%abiversion-mad
%_libdir/ucx/libucx/perftest_mad.so.%{abiversion}*
%endif

%changelog
* Wed Jun 17 2026 Nikita Shmatko <nash@altlinux.org> 1.20.1-alt1
- New version 1.20.1.
- Reworked subpackages per Shared Libs Policy.

* Mon Apr 20 2026 Nikita Shmatko <nash@altlinux.org> 1.20.0-alt1
- New version 1.20.0.

* Wed Mar 11 2026 Nikita Shmatko <nash@altlinux.org> 1.19.0-alt2
- Minor specfile fixes.

* Mon Oct 13 2025 Nikita Shmatko <nash@altlinux.org> 1.19.0-alt1
- Initial build for Sisyphus.
