%define _unpackaged_files_terminate_build 1

%ifnarch ppc64le
%def_with jemalloc
%else
%def_without jemalloc
%global optflags_lto %nil
%endif

Name: clickhouse
Version: 21.8.5.7
Release: alt1
Summary: Open-source distributed column-oriented DBMS
License: Apache-2.0
Group: Databases
Url: https://clickhouse.yandex/

# https://github.com/ClickHouse/ClickHouse.git
Source: %name-%version.tar

Source1:  %name-%version-contrib-AMQP-CPP.tar
Source2:  %name-%version-contrib-avro.tar
Source3:  %name-%version-contrib-aws.tar
Source4:  %name-%version-contrib-aws-c-common.tar
Source5:  %name-%version-contrib-aws-c-event-stream.tar
Source6:  %name-%version-contrib-aws-checksums.tar
Source7:  %name-%version-contrib-base64.tar
Source8:  %name-%version-contrib-boringssl.tar
Source9:  %name-%version-contrib-cassandra.tar
Source10: %name-%version-contrib-croaring.tar
Source11: %name-%version-contrib-datasketches-cpp.tar
Source12: %name-%version-contrib-dragonbox.tar
Source13: %name-%version-contrib-fast_float.tar
Source14: %name-%version-contrib-fastops.tar
Source15: %name-%version-contrib-gcem.tar
Source16: %name-%version-contrib-googletest.tar
Source17: %name-%version-contrib-grpc.tar
Source18: %name-%version-contrib-grpc-third_party-cares-cares.tar
Source19: %name-%version-contrib-h3.tar
Source20: %name-%version-contrib-libhdfs3.tar
Source21: %name-%version-contrib-libpq.tar
Source22: %name-%version-contrib-libpqxx.tar
Source23: %name-%version-contrib-llvm.tar
Source24: %name-%version-contrib-miniselect.tar
Source25: %name-%version-contrib-nanodbc.tar
Source26: %name-%version-contrib-NuRaft.tar
Source27: %name-%version-contrib-poco.tar
Source28: %name-%version-contrib-replxx.tar
Source29: %name-%version-contrib-sentry-native.tar
Source30: %name-%version-contrib-simdjson.tar
Source31: %name-%version-contrib-sparsehash-c11.tar
Source32: %name-%version-contrib-stats.tar
Source33: %name-%version-contrib-thrift.tar
Source34: %name-%version-contrib-zlib-ng.tar

Source1000: %name.watch

Patch0: %name-%version-%release.patch
Patch1: %name-base64-ppc64le.patch
Patch2: %name-avro-gcc10-compat.patch
Patch3: %name-grpc-abseil-cxx17-compat.patch
Patch4: %name-system-libuv.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: cmake libicu-devel libreadline-devel python3 gperf tzdata cctz-devel
BuildRequires: rpm-macros-cmake liblz4-devel /proc libzstd-devel libmariadb-devel
BuildRequires: farmhash-devel metrohash-devel libdouble-conversion-devel librdkafka-devel libre2-devel
BuildRequires: libgsasl-devel libcap-ng-devel libxxhash-devel boost-complete libunixODBC-devel libgperftools-devel
BuildRequires: libbrotli-devel capnproto-devel libxml2-devel liblzma-devel libcppkafka-devel
# TODO: try unbundling poco when new version is released
#BuildRequires: libpoco-devel
BuildRequires: libtinfo-devel
BuildRequires: gcc-c++ perl-JSON-XS libb64-devel libasan-devel-static
BuildRequires: libprotobuf-devel protobuf-compiler protobuf-c-compiler
BuildRequires: libstdc++-devel-static
BuildRequires: rapidjson-devel
%ifarch x86_64
BuildRequires: libhyperscan-devel
%endif
BuildRequires: libcurl-devel
BuildRequires: libflatbuffers-devel
# TODO: try unbundling googletest when new version is released
#BuildRequires: libgtest-devel
BuildRequires: libfmt-devel
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
BuildRequires: libabseil-cpp-devel
BuildRequires: librocksdb-devel librocksdb-devel-static bzlib-devel libgflags-devel
BuildRequires: liblzma-devel
BuildRequires: libyaml-cpp-devel

%if_with jemalloc
BuildRequires: libjemalloc-devel
%endif

ExclusiveArch: aarch64 x86_64 ppc64le

%add_python3_path %_datadir/clickhouse-test

%description
ClickHouse is an open-source column-oriented database management system that
allows generating analytical data reports in real time.

%package common-static
Group: Databases
Summary: Common files for %name
Provides: libclickhouse = %EVR
Conflicts: libclickhouse < %EVR
Obsoletes: libclickhouse < %EVR

%description common-static
This package provides common files for both clickhouse server and client.

%package server
Summary: Server binary for ClickHouse
Group: Databases
Requires: %name-common-static = %EVR

%description server
This package contains server binaries for ClickHouse DBMS.

%package client
Summary: Client binary for ClickHouse
Group: Databases
Requires: %name-common-static = %EVR

%description client
This package contains clickhouse-client, clickhouse-local and clickhouse-benchmark

%package test
Summary: ClickHouse tests
Group: Databases
Requires: %name-client = %EVR

%description test
ClickHouse tests

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34
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
	-DPARALLEL_COMPILE_JOBS=$NPROCS \
	-DPARALLEL_LINK_JOBS=$NPROCS \
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
	-DUSE_INTERNAL_PROTOBUF_LIBRARY:BOOL=OFF \
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

%pre server
%_sbindir/groupadd -r -f _clickhouse 2> /dev/null ||:
%_sbindir/useradd -r -g _clickhouse -d %_localstatedir/lib/%name -s /dev/null -c "ClickHouse User" _clickhouse 2> /dev/null ||:

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

