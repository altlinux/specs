%define _unpackaged_files_terminate_build 1
%def_enable check
%def_without fabric
%def_with ndctl
%def_without pmemcheck

Name: pmdk
Version: 1.12.1
Release: alt1
Summary: Persistent Memory Development Kit (formerly NVML)
Group: System/Base
License: BSD-3-Clause
Url: http://pmem.io/pmdk

Source: %name-%version.tar

BuildRequires: python3
BuildRequires: pandoc
BuildRequires: groff
# for build deps/miniasync
BuildRequires: cmake

%{?_with_ndctl:BuildRequires: libndctl-devel >= 60.1 libdaxctl-devel >= 60.1}
%{?_with_fabric:BuildRequires: libfabric-devel >= 1.4.2}

# for tests
%if_enabled check
BuildRequires: /proc
BuildRequires: gdb
BuildRequires: bc
BuildRequires: libunwind-devel
BuildRequires: ndctl
#BuildRequires: valgrind
%endif

# By design, PMDK does not support any 32-bit architecture.
# Due to dependency on some inline assembly, PMDK can be compiled only
# on these architectures:
# - x86_64
# - ppc64le (experimental)
# - aarch64 (unmaintained, supporting hardware doesn't exist?)
#
# Other 64-bit architectures could also be supported, if only there is
# a request for that, and if somebody provides the arch-specific
# implementation of the low-level routines for flushing to persistent
# memory.

# ExclusiveArch: x86_64 ppc64le aarch64
ExcludeArch: %ix86 %arm %mips32 ppc

%description
The Persistent Memory Development Kit is a collection of libraries for
using memory-mapped persistence, optimized specifically for persistent memory.

%package -n libpmem
Summary: Low-level persistent memory support library
Group: System/Libraries

%description -n libpmem
The libpmem provides low level persistent memory support. In particular,
support for the persistent memory instructions for flushing changes
to pmem is provided.  This package provides the v1 API.

%package -n libpmem-devel
Summary: Development files for the low-level persistent memory library
Group: Development/C
Requires: libpmem = %EVR

%description -n libpmem-devel
The libpmem provides low level persistent memory support. In particular,
support for the persistent memory instructions for flushing changes
to pmem is provided. This package provides the v1 API.

This library is provided for software which tracks every store to
pmem and needs to flush those changes to durability. Most developers
will find higher level libraries like libpmemobj to be much more
convenient.

%package -n libpmem2
Summary: Low-level persistent memory support library
Group: System/Libraries

%description -n libpmem2
The libpmem provides low level persistent memory support. In particular,
support for the persistent memory instructions for flushing changes
to pmem is provided. This package provides the v2 API.

%package -n libpmem2-devel
Summary: Development files for the low-level persistent memory library
Group: Development/C
Requires: libpmem2 = %EVR

%description -n libpmem2-devel
The libpmem provides low level persistent memory support. In particular,
support for the persistent memory instructions for flushing changes
to pmem is provided. This package provides the v2 API.

This library is provided for software which tracks every store to
pmem and needs to flush those changes to durability. Most developers
will find higher level libraries like libpmemobj to be much more
convenient.

%package -n libpmemblk
Summary: Persistent Memory Resident Array of Blocks library
Group: System/Libraries

%description -n libpmemblk
The libpmemblk implements a pmem-resident array of blocks, all the same
size, where a block is updated atomically with respect to power
failure or program interruption (no torn blocks).

%package -n libpmemblk-devel
Summary: Development files for the Persistent Memory Resident Array of Blocks library
Group: Development/C
Requires: libpmemblk = %EVR
Requires: libpmem-devel = %EVR

%description -n libpmemblk-devel
The libpmemblk implements a pmem-resident array of blocks, all the same
size, where a block is updated atomically with respect to power
failure or program interruption (no torn blocks).

For example, a program keeping a cache of fixed-size objects in pmem
might find this library useful. This library is provided for cases
requiring large arrays of objects at least 512 bytes each. Most
developers will find higher level libraries like libpmemobj to be
more generally useful.

%package -n libpmemlog
Summary: Persistent Memory Resident Log File library
Group: System/Libraries

%description -n libpmemlog
The libpmemlog library provides a pmem-resident log file. This is
useful for programs like databases that append frequently to a log
file.

%package -n libpmemlog-devel
Summary: Development files for the Persistent Memory Resident Log File library
Group: Development/C
Requires: libpmemlog = %EVR
Requires: libpmem-devel = %EVR

%description -n libpmemlog-devel
The libpmemlog library provides a pmem-resident log file. This
library is provided for cases requiring an append-mostly file to
record variable length entries. Most developers will find higher
level libraries like libpmemobj to be more generally useful.

%package -n libpmemobj
Summary: Persistent Memory Transactional Object Store library
Group: System/Libraries

%description -n libpmemobj
The libpmemobj library provides a transactional object store,
providing memory allocation, transactions, and general facilities for
persistent memory programming.

%package -n libpmemobj-devel
Summary: Development files for the Persistent Memory Transactional Object Store library
Group: Development/C
Requires: libpmemobj = %EVR
Requires: libpmem-devel = %EVR

%description -n libpmemobj-devel
The libpmemobj library provides a transactional object store,
providing memory allocation, transactions, and general facilities for
persistent memory programming. Developers new to persistent memory
probably want to start with this library.

%package -n libpmempool
Summary: Persistent Memory pool management library
Group: System/Libraries

%description -n libpmempool
The libpmempool library provides a set of utilities for off-line
administration, analysis, diagnostics and repair of persistent memory
pools created by libpmemlog, libpmemblk and libpmemobj libraries.

%package -n libpmempool-devel
Summary: Development files for Persistent Memory pool management library
Group: Development/C
Requires: libpmempool = %EVR
Requires: libpmem-devel = %EVR

%description -n libpmempool-devel
The libpmempool library provides a set of utilities for off-line
administration, analysis, diagnostics and repair of persistent memory
pools created by libpmemlog, libpmemblk and libpmemobj libraries.

%package -n librpmem
Summary: Remote Access to Persistent Memory library
Group: System/Libraries
Requires: libfabric
Requires: openssh-clients

%description -n librpmem
The librpmem library provides low-level support for remote access
to persistent memory utilizing RDMA-capable NICs. It can be used
to replicate persistent memory regions over RDMA protocol.

%package -n librpmem-devel
Summary: Development files for the Remote Access to Persistent Memory library
Group: Development/C
Requires: librpmem = %EVR

%description -n librpmem-devel
The librpmem library provides low-level support for remote access
to persistent memory utilizing RDMA-capable NICs. It can be used
to replicate persistent memory regions over RDMA protocol.

This sub-package contains libraries and header files for developing
applications that want to specifically make use of librpmem.

%package -n rpmemd
Summary: Target node process executed by librpmem
Group: System/Base
Requires: libfabric

%description -n rpmemd
The rpmemd process is executed on a target node by librpmem library
and facilitates access to persistent memory over RDMA.

%package -n pmempool
Summary: Utilities for Persistent Memory
Group: System/Base
Requires: libpmem >= %EVR
Requires: libpmemlog >= %EVR
Requires: libpmemblk >= %EVR
Requires: libpmemobj >= %EVR
Requires: libpmempool >= %EVR

%description -n pmempool
The pmempool is a standalone utility for management and off-line analysis
of Persistent Memory pools created by PMDK libraries. It provides a set
of utilities for administration and diagnostics of Persistent Memory pools.
The pmempool may be useful for troubleshooting by system administrators
and users of the applications based on PMDK libraries.

%package -n daxio
Summary: Perform I/O on Device DAX devices or zero a Device DAX device
Group: System/Base
Requires: libpmem >= %EVR

%description -n daxio
The daxio utility performs I/O on Device DAX devices or zero
a Device DAX device.  Since the standard I/O APIs (read/write) cannot be used
with Device DAX, data transfer is performed on a memory-mapped device.
The daxio may be used to dump Device DAX data to a file, restore data from
a backup copy, move/copy data to another device or to erase data from
a device.

%package -n pmreorder
Group: System/Base
Summary: Consistency Checker for Persistent Memory

%description -n pmreorder
The pmreorder tool is a collection of python scripts designed to parse
and replay operations logged by pmemcheck - a persistent memory checking tool.
Pmreorder performs the store reordering between persistent memory barriers -
a sequence of flush-fence operations. It uses a consistency checking routine
provided in the command line options to check whether files are in a consistent state.

%prep
%setup

%build
# This package calls binutils components directly and would need to pass
# in flags to enable the LTO plugins
# Disable LTO
%global optflags_lto %nil

# For debug build default flags may be overriden to disable compiler
# optimizations.
CFLAGS="%optflags" \
%make_build NORPATH=1 %{?_without_ndctl:NDCTL_ENABLE=n}

# Override LIB_AR with empty string to skip installation of static libraries
%install
%makeinstall_std \
	%{?_without_ndctl:NDCTL_ENABLE=n} \
	LIB_AR= \
	prefix=%prefix \
	libdir=%_libdir \
	includedir=%_includedir \
	mandir=%_mandir \
	bindir=%_bindir \
	sysconfdir=%_sysconfdir \
	docdir=%_docdir
mkdir -p %buildroot%_datadir/pmdk
cp utils/pmdk.magic %buildroot%_datadir/pmdk/
mkdir -p %buildroot%_datadir/bash-completion/completions
mv %buildroot%_sysconfdir/bash_completion.d/pmempool %buildroot%_datadir/bash-completion/completions/pmempool

# delete debug build
rm -rf %buildroot%_libdir/pmdk_debug

%check
echo "PMEM_FS_DIR=/tmp"                  > src/test/testconfig.sh
echo "PMEM_FS_DIR_FORCE_PMEM=1"         >> src/test/testconfig.sh
echo 'TEST_BUILD="debug nondebug"'      >> src/test/testconfig.sh
echo "TM=1"                             >> src/test/testconfig.sh

echo "config = {"                        > src/test/testconfig.py
echo "  'pmem_fs_dir': '/tmp',"         >> src/test/testconfig.py
echo "  'fs_dir_force_pmem': 1,"        >> src/test/testconfig.py
echo "  'build': ['debug', 'release']," >> src/test/testconfig.py
echo "  'tm': 1,"                       >> src/test/testconfig.py
echo "  'test_type': 'check',"          >> src/test/testconfig.py
echo "  'fs': 'all',"                   >> src/test/testconfig.py
echo "  'unittest_log_level': 1,"       >> src/test/testconfig.py
echo "  'keep_going': False,"           >> src/test/testconfig.py
echo "  'timeout': '30m',"              >> src/test/testconfig.py
echo "  'dump_lines': 30,"              >> src/test/testconfig.py
echo "  'force_enable': None,"          >> src/test/testconfig.py
echo "  'device_dax_path': [],"         >> src/test/testconfig.py
echo "  'granularity': 'cacheline',"    >> src/test/testconfig.py
echo "  'enable_admin_tests': False,"   >> src/test/testconfig.py
echo "  'fail_on_skip': False,"         >> src/test/testconfig.py
echo "  'cacheline_fs_dir': '/tmp',"    >> src/test/testconfig.py
echo "  'force_cacheline': True,"       >> src/test/testconfig.py
echo "  'granularity': 'cacheline',"    >> src/test/testconfig.py
echo "}"                                >> src/test/testconfig.py

rm -f src/test/obj_sync/TEST7
rm -f src/test/pmemset*/TEST*
rm -f src/test/ex_libpmemobj/TESTS.py
%ifarch ppc64le
rm -f src/test/pmem2_future/TESTS.py
%endif
make pycheck
make check

%files -n libpmem
%dir %_datadir/pmdk
%_libdir/libpmem.so.*
%_datadir/pmdk/pmdk.magic

%files -n libpmem-devel
%doc LICENSE ChangeLog CONTRIBUTING.md README.md
%_libdir/libpmem.so
%_pkgconfigdir/libpmem.pc
%_includedir/libpmem.h
%_man7dir/libpmem.*
%_man3dir/pmem_*
%_man5dir/pmem_ctl.*

%files -n libpmem2
%_libdir/libpmem2.so.*

%files -n libpmem2-devel
%doc LICENSE ChangeLog CONTRIBUTING.md README.md
%_libdir/libpmem2.so
%_pkgconfigdir/libpmem2.pc
%_includedir/libpmem2.h
%_includedir/libpmem2
%_man7dir/libpmem2*
%_man3dir/pmem2_*

%files -n libpmemblk
%_libdir/libpmemblk.so.*

%files -n libpmemblk-devel
%doc LICENSE ChangeLog CONTRIBUTING.md README.md
%_libdir/libpmemblk.so
%_pkgconfigdir/libpmemblk.pc
%_includedir/libpmemblk.h
%_man7dir/libpmemblk.*
%_man3dir/pmemblk_*

%files -n libpmemlog
%_libdir/libpmemlog.so.*

%files -n libpmemlog-devel
%doc LICENSE ChangeLog CONTRIBUTING.md README.md
%_libdir/libpmemlog.so
%_pkgconfigdir/libpmemlog.pc
%_includedir/libpmemlog.h
%_man7dir/libpmemlog.*
%_man3dir/pmemlog_*

%files -n libpmemobj
%_libdir/libpmemobj.so.*

%files -n libpmemobj-devel
%doc LICENSE ChangeLog CONTRIBUTING.md README.md
%_libdir/libpmemobj.so
%_pkgconfigdir/libpmemobj.pc
%_includedir/libpmemobj.h
%_includedir/libpmemobj
%_man7dir/libpmemobj.*
%_man3dir/pmemobj_*
%_man3dir/pobj_*
%_man3dir/oid_*
%_man3dir/toid*
%_man3dir/direct_*
%_man3dir/d_r*
%_man3dir/tx_*

%files -n libpmempool
%_libdir/libpmempool.so.*

%files -n libpmempool-devel
%doc LICENSE ChangeLog CONTRIBUTING.md README.md
%_libdir/libpmempool.so
%_pkgconfigdir/libpmempool.pc
%_includedir/libpmempool.h
%_man7dir/libpmempool.*
%_man5dir/poolset.*
%_man3dir/pmempool_*

%files -n pmempool
%_bindir/pmempool
%_man1dir/pmempool*
%_datadir/bash-completion/completions/pmempool

%if_with fabric
%files -n librpmem
%_libdir/librpmem.so.*

%files -n librpmem-devel
%doc LICENSE ChangeLog CONTRIBUTING.md README.md
%_libdir/librpmem.so
%_pkgconfigdir/librpmem.pc
%_includedir/librpmem.h
%_man7dir/librpmem.*
%_man3dir/rpmem_*

%files -n rpmemd
%_bindir/rpmemd
%_man1dir/rpmemd.*
%endif

%if_with ndctl
%files -n daxio
%_bindir/daxio
%_man1dir/daxio.*
%endif

%if_with pmemcheck
%files -n pmreorder
%_bindir/pmreorder
%_datadir/pmreorder
%_man1dir/pmreorder*
%else
%exclude %_bindir/pmreorder
%exclude %_datadir/pmreorder
%exclude %_man1dir/pmreorder*
%endif

%changelog
* Fri Dec 16 2022 Alexey Shabalin <shaba@altlinux.org> 1.12.1-alt1
- new version 1.12.1

* Sun Jun 12 2022 Alexey Shabalin <shaba@altlinux.org> 1.12.0-alt1
- new version 1.12.0

* Wed Oct 06 2021 Alexey Shabalin <shaba@altlinux.org> 1.11.1-alt1
- Initial build.

