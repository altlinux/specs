%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_without jemalloc
%def_without java
%def_with snappy
%def_with lz4
%def_with zlib
%def_with bzip2
%def_with zstd
%def_with tbb
%def_with numa
%def_without rocksdb_lite
%def_with liburing
%def_disable static

Name: rocksdb
Version: 7.9.3
Release: alt1.1
Summary: A Persistent Key-Value Store for Flash and RAM Storage
Group: Databases
# License is changed from "BSD-plus-Patents" (BSD-3-Clause) to GPL-2.0 AND Apache-2.0 in 2017.
License: GPL-2.0-only AND Apache-2.0
Url: https://rocksdb.org/
Vcs: https://github.com/facebook/rocksdb.git

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: libgtest-devel libgflags-devel cmake >= 3.10
%{?_with_jemalloc:BuildRequires: libjemalloc-devel}
%{?_with_java:BuildRequires: java-devel}
%{?_with_snappy:BuildRequires: libsnappy-devel}
%{?_with_lz4:BuildRequires: liblz4-devel}
%{?_with_zlib:BuildRequires: zlib-devel}
%{?_with_bzip2:BuildRequires: bzlib-devel}
%{?_with_zstd:BuildRequires: libzstd-devel}
%{?_with_tbb:BuildRequires: tbb-devel}
%{?_with_numa:BuildRequires: libnuma-devel}
%{?_with_liburing:BuildRequires: liburing-devel}

%description
Rocksdb is a library that forms the core building block for a fast key value
server, especially suited for storing data on flash drives. It has a
Log-Structured-Merge-Database (LSM) design with flexible trade offs between
Write-Amplification-Factor (WAF), Read-Amplification-Factor (RAF) and
Space-Amplification-Factor (SAF). It has multithreaded compaction, making it
specially suitable for storing multiple terabytes of data in a single database.

%package -n %name-tools
Summary: A Persistent Key-Value Store for Flash and RAM Storage (tools)
Group: System/Libraries

%description -n %name-tools
Administration and Data Access Tools

- The ldb command line tool offers multiple data access and database admin
  commands.
- sst_dump tool can be used to gain insights about a specific SST file.

%package -n lib%name
Summary: A Persistent Key-Value Store for Flash and RAM Storage
Group: System/Libraries

%description -n lib%name
Rocksdb is a library that forms the core building block for a fast key value
server, especially suited for storing data on flash drives. It has a
Log-Structured-Merge-Database (LSM) design with flexible trade offs between
Write-Amplification-Factor (WAF), Read-Amplification-Factor (RAF) and
Space-Amplification-Factor (SAF). It has multithreaded compaction, making it
specially suitable for storing multiple terabytes of data in a single database.

%package -n lib%name-devel
Summary: Development files for rocksdb
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Development files for rocksdb

%package -n lib%name-devel-static
Summary: Static library for rocksdb
Group: Development/C
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
Static library for rocksdb

%prep
%setup
%patch -p1
%ifarch %e2k
sed -i 's/#error No timer .*/return __rdtsc();/;1i #include <x86intrin.h>' \
	utilities/transactions/lock/range/range_tree/lib/portability/toku_time.h
%add_optflags -mno-sse4.2
sed -i 's/-msse4.2/-mno-sse4.2/' CMakeLists.txt
%endif

#rm -rf third-party/gtest-1.7.0
#rm java/benchmark/src/main/java/org/rocksdb/benchmark/DbBenchmark.java
rm build_tools/gnu_parallel

%build
%cmake \
    -DROCKSDB_BUILD_SHARED:BOOL=ON \
    %{?_with_jemalloc:-DWITH_JEMALLOC:BOOL=ON} \
    %{?_with_java:-DWITH_JNI:BOOL=ON} \
    %{?_with_snappy:-DWITH_SNAPPY:BOOL=ON} \
    %{?_with_zlib:-DWITH_ZLIB:BOOL=ON} \
    %{?_with_lz4:-DWITH_LZ4:BOOL=ON} \
    %{?_with_bzip2:-DWITH_BZ2:BOOL=ON} \
    %{?_with_zstd:-DWITH_ZSTD:BOOL=ON} \
    %{?_with_rocksdb_lite:-DROCKSDB_LITE:BOOL=ON} \
    %{?_without_liburing:-DWITH_LIBURING:BOOL=OFF} \
    -DWITH_CORE_TOOLS:BOOL=ON \
    -DWITH_BENCHMARK_TOOLS:BOOL=ON \
    -DWITH_TOOLS:BOOL=ON \
    -DUSE_RTTI=ON \
    -DFAIL_ON_WARNINGS=OFF \
%ifnarch %e2k
    -DPORTABLE:BOOL=ON \
%endif
    -DWITH_TESTS=ON

%cmake_build

%install
%cmake_install

%if_disabled static
rm -f %buildroot%_libdir/*.a
%endif

%files -n %name-tools
%_bindir/ldb
%_bindir/sst_dump

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_libdir/cmake/%name
%_pkgconfigdir/%name.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Fri Sep 22 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 7.9.3-alt1.1
- Fixed build for Elbrus.

* Thu Aug 03 2023 Alexey Shabalin <shaba@altlinux.org> 7.9.3-alt1
- 7.9.3

* Thu Apr 13 2023 Alexey Shabalin <shaba@altlinux.org> 7.9.2-alt1
- 7.9.2
- build for all arches

* Mon Oct 25 2021 Alexey Shabalin <shaba@altlinux.org> 6.25.3-alt1
- 6.25.3
- Exclude build on ix86.

* Fri Oct 08 2021 Alexey Shabalin <shaba@altlinux.org> 6.22.1-alt1
- 6.22.1
- Build with liburing.
- Disable package static lib.
- Add patches for arm, mips and riscv from openembedded.

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 6.14.6-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sun Jan 17 2021 Alexey Shabalin <shaba@altlinux.org> 6.14.6-alt1
- 6.14.6

* Tue Nov 24 2020 Alexey Shabalin <shaba@altlinux.org> 6.14.5-alt1
- 6.14.5

* Mon Oct 26 2020 Vitaly Chikunov <vt@altlinux.org> 6.1.2-alt3
- spec: Fix License, Url, add Vcs tags.
- Package cmake rules into librocksdb-devel.
- Package rocksdb-tools (administration and data access tools).

* Wed Apr 08 2020 Alexey Shabalin <shaba@altlinux.org> 6.1.2-alt2
- fixed build with gcc-9

* Mon Oct 07 2019 Alexey Shabalin <shaba@altlinux.org> 6.1.2-alt1
- 6.1.2

* Thu Feb 28 2019 Alexey Shabalin <shaba@altlinux.org> 5.17.2-alt1
- 5.17.2

* Fri Oct 26 2018 Alexey Shabalin <shaba@altlinux.org> 5.14.3-alt1
- 5.14.3
- build with PORTABLE=ON

* Wed Jun 13 2018 Alexey Shabalin <shaba@altlinux.ru> 5.13.3-alt1
- 5.13.3

* Wed Jun 06 2018 Alexey Shabalin <shaba@altlinux.ru> 5.8.8-alt1
- 5.8.8

* Thu Dec 07 2017 Alexey Shabalin <shaba@altlinux.ru> 5.7.5-alt1
- 5.7.5

* Mon Sep 25 2017 Alexey Shabalin <shaba@altlinux.ru> 5.7.4-alt1
- 5.7.4

* Wed Sep 20 2017 Alexey Shabalin <shaba@altlinux.ru> 5.7.3-alt1
- Initial build
