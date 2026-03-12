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
Version: 1.19.0
Release: alt2

Summary: Unified Communication X  (mailing list - https://elist.ornl.gov/mailman/listinfo/ucx-group)
License: BSD-3-Clause
Group:   System/Libraries 
Url:     https://openucx.org/
Vcs:     https://github.com/openucx/ucx.git

Source: %name-%version.tar
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
%if_with mkx5
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

%description
UCX is an optimized communication framework for high-performance distributed
applications. UCX utilizes high-speed networks, such as RDMA (InfiniBand, RoCE,
etc), Cray Gemini or Aries, for inter-node communication. If no such network is
available, TCP is used instead. UCX supports efficient transfer of data in
either main memory (RAM) or GPU memory (through CUDA and ROCm libraries). In
addition, UCX provides efficient intra-node communication, by leveraging the
following shared memory mechanisms: posix, sysv, cma, knem, and xpmem.
The acronym UCX stands for "Unified Communication X".

%package -n lib%name%abiversion
Summary: %summary
Group: System/Libraries

%description -n lib%name%abiversion
UCX is an optimized communication framework for high-performance distributed
applications. UCX utilizes high-speed networks, such as RDMA (InfiniBand, RoCE,
etc), Cray Gemini or Aries, for inter-node communication. If no such network is
available, TCP is used instead. UCX supports efficient transfer of data in
either main memory (RAM) or GPU memory (through CUDA and ROCm libraries). In
addition, UCX provides efficient intra-node communication, by leveraging the
following shared memory mechanisms: posix, sysv, cma, knem, and xpmem.
The acronym UCX stands for "Unified Communication X".

%package -n lib%name-devel
Requires: lib%name%abiversion = %EVR
Group: Development/C
Summary: Header files required for developing with UCX.

%description -n lib%name-devel
Provides header files and examples for developing with UCX.

%if_with cma
%package -n lib%name-cma
Requires: lib%name%abiversion = %EVR
Group: System/Libraries
Summary: UCX CMA support.

%description -n lib%name-cma
Provides CMA (Linux cross-memory-attach) transport for UCX. It utilizes the
system calls process_vm_readv/writev() for one-shot memory copy from another
process.
%endif

%if_with cuda
%package -n lib%name-cuda
Requires: lib%name%abiversion = %EVR
Summary: UCX CUDA support.
Group: System/Libraries

%description -n lib%name-cuda
Provide CUDA (NVIDIA GPU) support for UCX. Enables passing GPU memory pointers
to UCX communication routines, and transports taking advantage of GPU-Direct
technology for direct data transfer between GPU and RDMA devices.
%endif

%if_with gdrcopy
%package -n lib%name-gdrcopy
Requires: lib%name-cuda = %EVR
Summary: UCX GDRCopy support.
Group: System/Libraries

%description -n lib%name-gdrcopy
Provide GDRCopy support for UCX. GDRCopy is a low-latency GPU memory copy
library, built on top of the NVIDIA GPUDirect RDMA technology.
%endif

%if_with ib
%package -n lib%name-ib
Requires: lib%name%abiversion = %EVR
Summary: UCX RDMA support.
Group: System/Libraries

%description -n lib%name-ib
Provides support for IBTA-compliant transports for UCX. This includes RoCE,
InfiniBand, OmniPath, and any other transport supported by IB Verbs API.
Typically these transports provide RDMA support, which enables a fast and
hardware-offloaded data transfer.
%endif

%package -n lib%name-ib-efa
Requires: lib%name-ib = %EVR
Summary: UCX IB EFA provider support.
Group: System/Libraries

%description -n lib%name-ib-efa
Provides UCX InfiniBad EFA transport.

%if_with knem
%package -n lib%name-knem
Requires: lib%name%abiversion = %EVR
Summary: UCX KNEM transport support.
Group: System/Libraries

%description -n lib%name-knem 
Provides KNEM (fast inter-process copy) transport for UCX. KNEM is a Linux
kernel module that enables high-performance intra-node MPI communication
for large messages.
%endif

%if_with rdmacm
%package -n lib%name-rdmacm
Requires: lib%name-ib = %EVR
Group: System/Libraries
Summary: UCX RDMA connection manager support.

%description -n lib%name-rdmacm
Provides RDMA connection-manager support to UCX, which enables client/server
based connection establishment for RDMA-capable transports.
%endif

%if_with ugni
%package -n lib%name-ugni
Requires: lib%name%abiversion = %EVR
Summary: UCX Gemini/Aries transport support.
Group: System/Libraries

%description -n lib%name-ugni
Provides Gemini/Aries transport for UCX.
%endif

%if_with xpmem
%package -n lib%name-xpmem
Requires: lib%name%abiversion = %EVR
Group: System/Libraries
Summary: UCX XPMEM transport support.

%description -n lib%name-xpmem
Provieds XPMEM transport for UCX. XPMEM is a Linux kernel module that enables a
process to map the memory of another process into its virtual address space.
%endif

%if_with vfs
%package -n lib%name-vfs
Requires: lib%name%abiversion = %EVR
Group: System/Libraries
Summary: UCX Virtual Filesystem support.

%description -n lib%name-vfs
Provides a virtual filesystem over FUSE which allows real-time
monitoring of UCX library internals, protocol objects, transports
status, and more.
%endif

%if_with mlx5
%package -n lib%name-ib-mlx5
Requires: lib%name%abiversion = %EVR
Summary: UCX IB MLX5 RDMA provider support.
Group: System/Libraries

%description -n lib%name-ib-mlx5
Provides support for DevX, Direct Verbs and DC transports for Infiniband
devices
%endif

%if_with mad
%package -n lib%name-mad
Requires: lib%name%abiversion = %EVR
Summary: UCX Infiniband MAD support
Group: System/Libraries

%description -n lib%name-mad
Provide Infiniband mad support for UCX. Enables running perftest using
Infiniband datagrams for out-of-band communications.
%endif

%prep
%setup -a1

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
install -d %{buildroot}%{_includedir}/ucs/sys
install -m644 src/ucs/sys/sys.h %{buildroot}%{_includedir}/ucs/sys/

%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/%name/*.la
rm -f %{buildroot}%{_libdir}/%name/lib*.so
rm -f %{buildroot}%{_libdir}/%name/lib*.a

%files -n lib%name%abiversion
%doc LICENSE README AUTHORS NEWS
%_libdir/lib*.so.%{abiversion}*
%_bindir/%{name}_info
%_bindir/%{name}_perftest
%_bindir/%{name}_perftest_daemon
%_bindir/%{name}_read_profile
%_bindir/io_demo
%_datadir/%name
%dir %_sysconfdir/%name
%_sysconfdir/%name/%name.conf
%exclude %_datadir/%name/examples

%files -n lib%name-devel
%_includedir/uc*
%_libdir/lib*.so
%_pkgconfigdir/%{name}*.pc
%dir %_cmakedir/%name
%_cmakedir/%name/*.cmake
%_datadir/%name/examples

%if_with cma
%files -n lib%name-cma
%dir %_libdir/%name
%_libdir/%name/libuct_cma.so.%{abiversion}*
%endif

%if_with cuda
%files -n lib%name-cuda
%dir %_libdir/%name
%_libdir/%name/libucx_perftest_cuda.so.%{abiversion}*
%_libdir/%name/libucm_cuda.so.%{abiversion}*
%_libdir/%name/libuct_cuda.so.%{abiversion}*
%endif

%if_with gdrcopy
%files -n lib%name-gdrcopy
%dir %_libdir/%name
%_libdir/%name/libuct_cuda_gdrcopy.so.%{abiversion}*
%endif

%if_with ib
%files -n lib%name-ib
%dir %_libdir/%name
%_libdir/%name/libuct_ib.so.%{abiversion}*
%endif

%files -n lib%name-ib-efa
%_libdir/%name/libuct_ib_efa.so.%{abiversion}*

%if_with knem
%files -n lib%name-knem
%dir %_libdir/%name
%_libdir/%name/libuct_knem.so.%{abiversion}*
%endif

%if_with rdmacm
%files -n lib%name-rdmacm
%dir %_libdir/%name
%_libdir/%name/libuct_rdmacm.so.%{abiversion}*
%endif

%if_with ugni
%files -n lib%name-ugni
%dir %_libdir/%name
%_libdir/%name/libuct_ugni.so.%{abiversion}*
%endif

%if_with xpmem
%files -n lib%name-xpmem
%dir %_libdir/%name
%_libdir/%name/libuct_xpmem.so.%{abiversion}*
%endif

%if_with vfs
%files -n lib%name-vfs
%dir %_libdir/%name
%_libdir/%name/libucs_fuse.so.%{abiversion}*
%_bindir/%{name}_vfs
%endif

%if_with mlx5
%files -n lib%name-ib-mlx5
%_libdir/%name/libuct_ib_mlx5.so.%{abiversion}*
%endif

%if_with mad
%files -n lib%name-mad
%_libdir/%name/lib%name/perftest_mad.so.%{abiversion}*
%endif

%changelog
* Wed Mar 11 2026 Nikita Shmatko <nash@altlinux.org> 1.19.0-alt2
- Minor specfile fixes.

* Mon Oct 13 2025 Nikita Shmatko <nash@altlinux.org> 1.19.0-alt1
- Initial build for Sisyphus.
