%define _unpackaged_files_terminate_build 1

%def_with clang

%ifnarch ppc64le
%def_with jemalloc
%else
%def_without jemalloc
%endif

%if_with clang
# LTO support for clang
%ifnarch aarch64
%global optflags_lto -flto=thin
%else
%global optflags_lto %nil
%endif
ExclusiveArch: aarch64 x86_64
%else
# LTO causes random crashes, disable it
%global optflags_lto %nil
ExclusiveArch: aarch64 x86_64 ppc64le
%endif

Name: clickhouse-lts
Version: 21.8.15.7
Release: alt1
Summary: Open-source distributed column-oriented DBMS
License: Apache-2.0
Group: Databases
Url: https://clickhouse.yandex/

# https://github.com/ClickHouse/ClickHouse.git
Source: %name-%version.tar

Source1:  %name-%version-contrib-abseil-cpp.tar
Source2:  %name-%version-contrib-AMQP-CPP.tar
Source3:  %name-%version-contrib-avro.tar
Source4:  %name-%version-contrib-aws.tar
Source5:  %name-%version-contrib-aws-c-common.tar
Source6:  %name-%version-contrib-aws-c-event-stream.tar
Source7:  %name-%version-contrib-aws-checksums.tar
Source8:  %name-%version-contrib-base64.tar
Source9:  %name-%version-contrib-boost.tar
Source10: %name-%version-contrib-boringssl.tar
Source11: %name-%version-contrib-cassandra.tar
Source12: %name-%version-contrib-cctz.tar
Source13: %name-%version-contrib-cppkafka.tar
Source14: %name-%version-contrib-cppkafka-third_party-Catch2.tar
Source15: %name-%version-contrib-croaring.tar
Source16: %name-%version-contrib-datasketches-cpp.tar
Source17: %name-%version-contrib-dragonbox.tar
Source18: %name-%version-contrib-fast_float.tar
Source19: %name-%version-contrib-fastops.tar
Source20: %name-%version-contrib-fmtlib.tar
Source21: %name-%version-contrib-gcem.tar
Source22: %name-%version-contrib-googletest.tar
Source23: %name-%version-contrib-grpc.tar
Source24: %name-%version-contrib-h3.tar
Source25: %name-%version-contrib-libcxx.tar
Source26: %name-%version-contrib-libcxxabi.tar
Source27: %name-%version-contrib-libhdfs3.tar
Source28: %name-%version-contrib-libpq.tar
Source29: %name-%version-contrib-libpqxx.tar
Source30: %name-%version-contrib-llvm.tar
Source31: %name-%version-contrib-miniselect.tar
Source32: %name-%version-contrib-nanodbc.tar
Source33: %name-%version-contrib-NuRaft.tar
Source34: %name-%version-contrib-poco.tar
Source35: %name-%version-contrib-protobuf.tar
Source36: %name-%version-contrib-re2.tar
Source37: %name-%version-contrib-replxx.tar
Source38: %name-%version-contrib-rocksdb.tar
Source39: %name-%version-contrib-sentry-native.tar
Source40: %name-%version-contrib-simdjson.tar
Source41: %name-%version-contrib-sparsehash-c11.tar
Source42: %name-%version-contrib-stats.tar
Source43: %name-%version-contrib-thrift.tar
Source44: %name-%version-contrib-yaml-cpp.tar
Source45: %name-%version-contrib-zlib-ng.tar

Source1000: clickhouse.watch

Patch0: %name-%version-%release.patch
Patch1: clickhouse-base64-ppc64le.patch
Patch2: clickhouse-avro-gcc10-compat.patch
Patch3: clickhouse-grpc-abseil-cxx17-compat.patch
Patch4: clickhouse-system-libuv.patch
Patch5: clickhouse-fastops-gcc-compat.patch
Patch6: clickhouse-nanodbc-compat.patch
Patch7: clickhouse-llvm-compat.patch

BuildRequires(pre): rpm-build-python3
%if_with clang
BuildRequires: clang lld
%else
BuildRequires: gcc-c++
BuildRequires: libabseil-cpp-devel
BuildRequires: boost-complete
BuildRequires: cctz-devel
BuildRequires: libcppkafka-devel
BuildRequires: libfmt-devel
BuildRequires: libprotobuf-devel protobuf-compiler protobuf-c-compiler
BuildRequires: libre2-devel
BuildRequires: librocksdb-devel
BuildRequires: libyaml-cpp-devel
%endif
BuildRequires: cmake libicu-devel libreadline-devel python3 gperf tzdata
BuildRequires: rpm-macros-cmake liblz4-devel /proc libzstd-devel
BuildRequires: libmysqlclient-devel
BuildRequires: libssl-devel
BuildRequires: farmhash-devel metrohash-devel libdouble-conversion-devel librdkafka-devel
BuildRequires: libgsasl-devel libcap-ng-devel libxxhash-devel libunixODBC-devel libgperftools-devel
BuildRequires: libbrotli-devel capnproto-devel libxml2-devel liblzma-devel
# TODO: try unbundling poco when new version is released
#BuildRequires: libpoco-devel
BuildRequires: libtinfo-devel
BuildRequires: perl-JSON-XS libb64-devel libasan-devel-static
BuildRequires: libstdc++-devel-static
BuildRequires: rapidjson-devel
%ifarch x86_64
BuildRequires: libhyperscan-devel
%endif
BuildRequires: libcurl-devel
BuildRequires: libflatbuffers-devel
# TODO: try unbundling googletest when new version is released
#BuildRequires: libgtest-devel
%ifnarch aarch64
BuildRequires: libunwind-devel
%endif
%ifarch x86_64
BuildRequires: libcpuid-devel
%endif
BuildRequires: libuv-devel
BuildRequires: libmsgpack-devel
BuildRequires: libsasl2-devel
BuildRequires: libsnappy-devel
BuildRequires: libltdl-devel
BuildRequires: bzlib-devel libgflags-devel
BuildRequires: liblzma-devel

%if_with jemalloc
BuildRequires: libjemalloc-devel
%endif

%add_python3_path %_datadir/clickhouse-test

Conflicts: clickhouse

%filter_from_requires /^python3(queries) = .*/d
%filter_from_requires /^python3(queries\.conftest) = .*/d
%filter_from_requires /^python3(queries\.query_test) = .*/d
%filter_from_requires /^python3(queries\.server) = .*/d

%filter_from_provides /^python3(queries) = .*/d
%filter_from_provides /^python3(queries\.conftest) = .*/d
%filter_from_provides /^python3(queries\.query_test) = .*/d
%filter_from_provides /^python3(queries\.server) = .*/d

%description
ClickHouse is an open-source column-oriented database management system that
allows generating analytical data reports in real time.

%package common-static
Group: Databases
Summary: Common files for %name
Provides: libclickhouse = %EVR
Conflicts: libclickhouse < %EVR
Obsoletes: libclickhouse < %EVR
Conflicts: clickhouse-common-static

%description common-static
This package provides common files for both clickhouse server and client.

%package server
Summary: Server binary for ClickHouse
Group: Databases
Requires: %name-common-static = %EVR
Conflicts: clickhouse-server

%description server
This package contains server binaries for ClickHouse DBMS.

%package client
Summary: Client binary for ClickHouse
Group: Databases
Requires: %name-common-static = %EVR
Conflicts: clickhouse-client

%description client
This package contains clickhouse-client, clickhouse-local and clickhouse-benchmark

%package test
Summary: ClickHouse tests
Group: Databases
Requires: %name-client = %EVR
Conflicts: clickhouse-test

%description test
ClickHouse tests

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39 -a40 -a41 -a42 -a43 -a44 -a45

%if_without clang
# remove unneeded bundles
rm -rf contrib/{abseil-cpp,boost,cctz,cppkafka,fmtlib,libcxx,libcxxabi,protobuf,re2,rocksdb,yaml-cpp}
%endif

%patch0 -p1

pushd contrib/base64
%patch1 -p1
popd

pushd contrib/avro
%patch2 -p1
popd

pushd contrib/grpc
%patch3 -p1
popd

pushd contrib/cassandra
%patch4 -p1
popd

pushd contrib/fastops
%patch5 -p1
popd

pushd contrib/nanodbc
%patch6 -p1
popd

pushd contrib/llvm
%patch7 -p1
popd

# remove third-party headers which must not be used
rm -rf contrib/jemalloc-cmake/include*

%build
if [ %__nprocs -gt 6 ] ; then
	export NPROCS=6
else
	export NPROCS=%__nprocs
fi

# strip debuginfo: with bundled llvm debuginfo takes too much space
%define optflags_debug -g0

%cmake \
%if_with clang
	-DCMAKE_C_COMPILER=clang \
	-DCMAKE_CXX_COMPILER=clang++ \
	-DUSE_LIBCXX:BOOL=ON \
	-DUSE_INTERNAL_BOOST_LIBRARY:BOOL=ON \
	-DUSE_INTERNAL_CCTZ_LIBRARY:BOOL=ON \
	-DUSE_INTERNAL_LIBCXX_LIBRARY:BOOL=ON \
	-DUSE_INTERNAL_PROTOBUF_LIBRARY:BOOL=ON \
	-DUSE_INTERNAL_RE2_LIBRARY:BOOL=ON \
	-DUSE_INTERNAL_ROCKSDB_LIBRARY:BOOL=ON \
	-DUSE_INTERNAL_ZLIB_LIBRARY:BOOL=ON \
	-DUSE_SYSTEM_ABSEIL_CPP:BOOL=OFF \
	-DUSE_SYSTEM_BOOST:BOOL=OFF \
	-DUSE_SYSTEM_CPPKAFKA:BOOL=OFF \
	-DUSE_SYSTEM_FMTLIB:BOOL=OFF \
	-DUSE_SYSTEM_YAML_CPP:BOOL=OFF \
	-DPARALLEL_COMPILE_JOBS=$NPROCS \
	-DPARALLEL_LINK_JOBS=1 \
%else
	-DUSE_LIBCXX:BOOL=OFF \
	-DUSE_INTERNAL_BOOST_LIBRARY:BOOL=OFF \
	-DUSE_INTERNAL_CCTZ_LIBRARY:BOOL=OFF \
	-DUSE_INTERNAL_LIBCXX_LIBRARY:BOOL=OFF \
	-DUSE_INTERNAL_PROTOBUF_LIBRARY:BOOL=OFF \
	-DUSE_INTERNAL_RE2_LIBRARY:BOOL=OFF \
	-DUSE_INTERNAL_ROCKSDB_LIBRARY:BOOL=OFF \
	-DUSE_INTERNAL_ZLIB_LIBRARY:BOOL=OFF \
	-DUSE_SYSTEM_ABSEIL_CPP:BOOL=ON \
	-DUSE_SYSTEM_BOOST:BOOL=ON \
	-DUSE_SYSTEM_CPPKAFKA:BOOL=ON \
	-DUSE_SYSTEM_FMTLIB:BOOL=ON \
	-DUSE_SYSTEM_YAML_CPP:BOOL=ON \
	-DPARALLEL_COMPILE_JOBS=$NPROCS \
	-DPARALLEL_LINK_JOBS=$NPROCS \
%endif
	-DCLICKHOUSE_SPLIT_BINARY:BOOL=OFF \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=OFF \
%ifarch x86_64
	-DENABLE_CPUID:BOOL=ON \
%else
	-DENABLE_CPUID:BOOL=OFF \
	-DENABLE_FASTOPS:BOOL=OFF \
	-DENABLE_HDFS:BOOL=OFF \
	-DUSE_INTERNAL_HDFS3_LIBRARY:BOOL=OFF \
%endif
%if_with jemalloc
	-DENABLE_JEMALLOC:BOOL=ON \
%else
	-DENABLE_JEMALLOC:BOOL=OFF \
%endif
	-DENABLE_PARQUET:BOOL=OFF \
	-DENABLE_S3:BOOL=OFF \
	-DENABLE_UTILS:BOOL=OFF \
	-DUNBUNDLED:BOOL=ON \
	-DUSE_INTERNAL_AWS_S3_LIBRARY:BOOL=OFF \
	-DUSE_INTERNAL_BROTLI_LIBRARY:BOOL=OFF \
	-DUSE_INTERNAL_GRPC_LIBRARY:BOOL=ON \
	-DUSE_INTERNAL_GTEST_LIBRARY:BOOL=ON \
	-DUSE_INTERNAL_LIBGSASL_LIBRARY:BOOL=OFF \
%ifarch x86_64
	-DUSE_INTERNAL_LLVM_LIBRARY:BOOL=ON \
%else
	-DUSE_INTERNAL_LLVM_LIBRARY:BOOL=OFF \
%endif
	-DUSE_INTERNAL_POCO_LIBRARY:BOOL=ON \
	-DUSE_INTERNAL_RDKAFKA_LIBRARY:BOOL=OFF \
	-DUSE_INTERNAL_REPLXX:BOOL=ON \
	-DUSE_INTERNAL_XZ_LIBRARY:BOOL=OFF \
	-DUSE_STATIC_LIBRARIES:BOOL=ON \
%ifnarch aarch64
	-DUSE_UNWIND:BOOL=ON \
%else
	-DUSE_UNWIND:BOOL=OFF \
%endif
	%nil

%cmake_build

%install
%cmake_install
install -Dm0644 debian/clickhouse-server.cron.d %buildroot%_sysconfdir/cron.d/clickhouse-server
install -Dm0644 debian/clickhouse-server.service %buildroot%_unitdir/clickhouse-server.service
mkdir -p %buildroot%_localstatedir/clickhouse
mkdir -p %buildroot%_logdir/clickhouse-server

# remove unpackaged files
rm -rfv %buildroot%_prefix/cmake
rm -fv %buildroot%_prefix/lib/*.a

%check
./%_cmake__builddir/src/unit_tests_dbms --gtest_filter='-CoordinationTest.TestRotateIntervalChanges:ReadBufferAIOTest.TestReadAfterAIO:WeakHash32.*'

%pre server
%_sbindir/groupadd -r -f _clickhouse 2> /dev/null ||:
%_sbindir/useradd -r -g _clickhouse -d %_localstatedir/lib/clickhouse -s /dev/null -c "ClickHouse User" _clickhouse 2> /dev/null ||:

%post server
%post_service clickhouse-server

%preun server
%preun_service clickhouse-server

%post common-static
# CAP_IPC_LOCK capability is needed for binary mlock
# CAP_SYS_NICE capability is needef for os_thread_priority feature
setcap -q cap_ipc_lock,cap_sys_nice=+ep %_bindir/clickhouse 2>/dev/null ||:

if [ -f /proc/cpuinfo ] ; then
	grep -sq sse4_2 /proc/cpuinfo || echo "Warning: No SSE4.2 detected on this CPU, clickhouse may fail." >&2
fi

%files common-static
%_bindir/clickhouse
%_bindir/clickhouse-odbc-bridge
%_bindir/clickhouse-library-bridge
%_datadir/bash-completion/completions/clickhouse
%_datadir/bash-completion/completions/clickhouse-bootstrap

%files server
%dir %_sysconfdir/clickhouse-server
%dir %_sysconfdir/clickhouse-keeper
%config(noreplace) %_sysconfdir/cron.d/clickhouse-server
%config(noreplace) %_sysconfdir/clickhouse-server/config.xml
%config(noreplace) %_sysconfdir/clickhouse-server/users.xml
%config(noreplace) %_sysconfdir/clickhouse-keeper/keeper_config.xml
%_bindir/clickhouse-server
%_bindir/clickhouse-report
%_bindir/clickhouse-copier
%_bindir/clickhouse-keeper
%_bindir/clickhouse-keeper-converter
%_unitdir/clickhouse-server.service
%dir %attr(0750,_clickhouse,_clickhouse) %_logdir/clickhouse-server
%dir %attr(0750,_clickhouse,_clickhouse) %_localstatedir/clickhouse

%files client
%dir %_sysconfdir/clickhouse-client
%config(noreplace) %_sysconfdir/clickhouse-client/config.xml
%_bindir/clickhouse-client
%_bindir/clickhouse-local
%_bindir/clickhouse-compressor
%_bindir/clickhouse-benchmark
%_bindir/clickhouse-obfuscator
%_bindir/clickhouse-format
%_bindir/clickhouse-extract-from-config
%_bindir/clickhouse-git-import
%_datadir/bash-completion/completions/clickhouse-benchmark
%_datadir/bash-completion/completions/clickhouse-client
%_datadir/bash-completion/completions/clickhouse-local

%files test
%_bindir/clickhouse-test
%_datadir/clickhouse-test

%changelog
* Wed Mar 09 2022 Anton Farygin <rider@altlinux.ru> 21.8.15.7-alt1
- 21.8.14.5 -> 21.8.15.7

* Thu Feb 17 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.14.5-alt2
- Renamed to clickhouse-lts.

* Mon Feb 14 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.14.5-alt1
- Updated to lts upstream version 21.8.14.5.

* Mon Jan 10 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.13.6-alt1
- Updated to lts upstream version 21.8.13.6.

* Mon Dec 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.12.29-alt1
- Updated to lts upstream version 21.8.12.29.

* Mon Nov 22 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.11.4-alt1
- Updated to lts upstream version 21.8.11.4.

* Fri Oct 29 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.10.19-alt2
- Rebuilt with clang.
- Rebuilt with mysql instead of mariadb.
- Disabled build for ppc64le when clang is used.
- Enabled tests.

* Mon Oct 25 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.10.19-alt1
- Updated to lts upstream version 21.8.10.19.
- Disabled thread fuzzer since it's not compatible with glibc-2.34 yet (GH issue 30462).

* Mon Oct 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.8.29-alt1
- Updated to lts upstream version 21.8.8.29.

* Tue Sep 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.7.22-alt1
- Updated to lts upstream version 21.8.7.22.
- Disabled LTO which caused random crashes.

* Tue Sep 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.5.7-alt2
- Updated generated version information.

* Mon Sep 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.5.7-alt1
- Updated to lts upstream version 21.8.5.7.

* Fri Aug 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.8.3.44-alt1
- Updated to lts upstream version 21.8.3.44.

* Wed Jul 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.3.14.1-alt1
- Updated to lts upstream version 21.3.14.1.

* Fri Jun 25 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.3.13.9-alt1
- Updated to lts upstream version 21.3.13.9.

* Wed Jun 02 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.3.12.2-alt2
- Rebuilt with jemalloc.
- Added capabilities to clickhouse executable.

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 21.3.12.2-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu May 27 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.3.12.2-alt1
- Updated to lts upstream version 21.3.12.2.

* Mon May 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.3.11.5-alt1
- Updated to lts upstream version 21.3.11.5.

* Tue May 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.3.10.1-alt1
- Updated to lts upstream version 21.3.10.1.

* Thu Apr 29 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.3.8.76-alt1
- Updated to lts upstream version 21.3.8.76.

* Thu Apr 22 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.3.6.55-alt1
- Updated to lts upstream version 21.3.6.55.

* Thu Apr 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.3.4.25-alt1
- Updated to lts upstream version 21.3.4.25.

* Thu Mar 25 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.3.3.14-alt1
- Updated to lts upstream version 21.3.3.14.
- Added watch file for upstream lts releases.

* Tue Mar 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 21.3.2.5-alt1
- Updated to lts upstream version 21.3.2.5.

* Wed Jan 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 20.8.11.17-alt1
- Updated to lts upstream version 20.8.11.17.

* Fri Sep 25 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20.3.19.4-alt1
- Updated to lts upstream version 20.3.19.4.

* Fri Sep 18 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20.3.18.10-alt1
- Updated to lts upstream version 20.3.18.10.
- Enabled libunwind dependency.

* Wed Sep 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20.3.17.173-alt1
- Updated to lts upstream version 20.3.17.173.

* Thu Aug 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20.3.15.133-alt1
- Updated to lts upstream version 20.3.15.133.

* Tue Jun 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20.3.11.97-alt1
- Updated to lts upstream version 20.3.11.97.

* Tue Mar 17 2020 Anton Farygin <rider@altlinux.ru> 19.17.9.60-alt1
-  19.17.8.54 -> 19.17.9.60

* Fri Feb 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 19.17.8.54-alt1
- Updated to stable upstream version 19.17.8.54.

* Thu Dec 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 19.16.2.2-alt2
- Rebuilt with boost-1.71.0.

* Wed Nov 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 19.16.2.2-alt1
- Updated to stable upstream version 19.16.2.2.
- Used bundled zlib-ng instead of system zlib library.
- Disabled building shared clickhouse library.
- Built single clickhouse binary.

* Thu Oct 03 2019 Anton Farygin <rider@altlinux.ru> 19.13.6.51-alt1
- 19.13.6.51

* Wed Sep 25 2019 Anton Farygin <rider@altlinux.ru> 19.13.5.44-alt1
- 19.13.5.44

* Tue Sep 10 2019 Anton Farygin <rider@altlinux.ru> 19.13.4.32-alt1
- 19.13.4.32

* Thu Aug 22 2019 Anton Farygin <rider@altlinux.ru> 19.13.3.26-alt1
- 19.13.3.26

* Wed Aug 14 2019 Anton Farygin <rider@altlinux.ru> 19.13.2.19-alt1
- 19.13.2.19

* Mon Aug 12 2019 Anton Farygin <rider@altlinux.ru> 19.13.1.11-alt1
- 19.13.1.11

* Wed Aug 07 2019 Anton Farygin <rider@altlinux.ru> 19.11.6.31-alt1
- 19.11.6.31-alt1

* Tue Aug 06 2019 Anton Farygin <rider@altlinux.ru> 19.11.5.28-alt2
- 19.11.5.28
- fixed build on aarch64 and ppc (thanx to Sergey Bolshakov)
- enabled rapidjson
- build by gcc

* Mon Jul 22 2019 Anton Farygin <rider@altlinux.ru> 19.9.5.36-alt1
- new version
- build without jemalloc

* Mon Jul 01 2019 Anton Farygin <rider@altlinux.ru> 19.9.2.4-alt2
- config files was marked for prevent rewrite during an update

* Tue Jun 25 2019 Anton Farygin <rider@altlinux.ru> 19.9.2.4-alt1
- updated to 19.9.2.4

* Wed Jun 19 2019 Anton Farygin <rider@altlinux.ru> 19.8.3.8-alt1
- first build for ALT

