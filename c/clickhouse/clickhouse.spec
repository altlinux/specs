%define _unpackaged_files_terminate_build 1
%global llvm_version 15.0
%global clang_version 15
%global __nprocs 8

%def_with clang

%ifnarch ppc64le
%def_with jemalloc
%else
%def_without jemalloc
%endif

# LTO causes random crashes, disable it
%global optflags_lto %nil

%if_with clang
ExclusiveArch: aarch64 x86_64
%else
ExclusiveArch: aarch64 x86_64 ppc64le
%endif

Name: clickhouse
Version: 22.8.13.20
Release: alt1
Summary: Open-source distributed column-oriented DBMS
License: Apache-2.0
Group: Databases
Url: https://clickhouse.yandex/

# https://github.com/ClickHouse/ClickHouse.git
Source: %name-%version.tar

Source1: %name-%version-contrib-abseil-cpp.tar
Source2: %name-%version-contrib-AMQP-CPP.tar
Source3: %name-%version-contrib-arrow.tar
Source4: %name-%version-contrib-arrow-cpp-submodules-parquet-testing.tar
Source5: %name-%version-contrib-arrow-testing.tar
Source6: %name-%version-contrib-avro.tar
Source7: %name-%version-contrib-aws.tar
Source8: %name-%version-contrib-aws-c-common.tar
Source9: %name-%version-contrib-aws-c-event-stream.tar
Source10: %name-%version-contrib-aws-checksums.tar
Source11: %name-%version-contrib-azure.tar
Source12: %name-%version-contrib-base64.tar
Source13: %name-%version-contrib-boost.tar
Source14: %name-%version-contrib-boringssl.tar
Source15: %name-%version-contrib-brotli.tar
Source16: %name-%version-contrib-brotli-research-esaxx.tar
Source17: %name-%version-contrib-brotli-research-libdivsufsort.tar
Source18: %name-%version-contrib-bzip2.tar
Source19: %name-%version-contrib-capnproto.tar
Source20: %name-%version-contrib-c-ares.tar
Source21: %name-%version-contrib-cassandra.tar
Source22: %name-%version-contrib-cctz.tar
Source23: %name-%version-contrib-cld2.tar
Source24: %name-%version-contrib-cppkafka.tar
Source25: %name-%version-contrib-cppkafka-third_party-Catch2.tar
Source26: %name-%version-contrib-croaring.tar
Source27: %name-%version-contrib-curl.tar
Source28: %name-%version-contrib-cyrus-sasl.tar
Source29: %name-%version-contrib-datasketches-cpp.tar
Source30: %name-%version-contrib-double-conversion.tar
Source31: %name-%version-contrib-dragonbox.tar
Source32: %name-%version-contrib-fast_float.tar
Source33: %name-%version-contrib-fastops.tar
Source34: %name-%version-contrib-flatbuffers.tar
Source35: %name-%version-contrib-fmtlib.tar
Source36: %name-%version-contrib-googletest.tar
Source37: %name-%version-contrib-grpc.tar
Source38: %name-%version-contrib-h3.tar
Source39: %name-%version-contrib-hashidsxx.tar
Source40: %name-%version-contrib-hive-metastore.tar
Source41: %name-%version-contrib-icu.tar
Source42: %name-%version-contrib-icudata.tar
Source43: %name-%version-contrib-jemalloc.tar
Source44: %name-%version-contrib-krb5.tar
Source45: %name-%version-contrib-lemmagen-c.tar
Source46: %name-%version-contrib-libcpuid.tar
Source47: %name-%version-contrib-libcxx.tar
Source48: %name-%version-contrib-libcxxabi.tar
Source49: %name-%version-contrib-libgsasl.tar
Source50: %name-%version-contrib-libhdfs3.tar
Source51: %name-%version-contrib-libpq.tar
Source52: %name-%version-contrib-libpqxx.tar
Source53: %name-%version-contrib-libprotobuf-mutator.tar
Source54: %name-%version-contrib-librdkafka.tar
Source55: %name-%version-contrib-libstemmer_c.tar
Source56: %name-%version-contrib-libunwind.tar
Source57: %name-%version-contrib-libuv.tar
Source58: %name-%version-contrib-libxml2.tar
Source59: %name-%version-contrib-llvm.tar
Source60: %name-%version-contrib-lz4.tar
Source61: %name-%version-contrib-magic_enum.tar
Source62: %name-%version-contrib-mariadb-connector-c.tar
Source63: %name-%version-contrib-miniselect.tar
Source64: %name-%version-contrib-minizip-ng.tar
Source65: %name-%version-contrib-msgpack-c.tar
Source66: %name-%version-contrib-msgpack-c-external-boost-predef.tar
Source67: %name-%version-contrib-msgpack-c-external-boost-preprocessor.tar
Source68: %name-%version-contrib-nanodbc.tar
Source69: %name-%version-contrib-nats-io.tar
Source70: %name-%version-contrib-nats-io-coveralls-cmake.tar
Source71: %name-%version-contrib-nlp-data.tar
Source72: %name-%version-contrib-NuRaft.tar
Source73: %name-%version-contrib-openldap.tar
Source74: %name-%version-contrib-orc.tar
Source75: %name-%version-contrib-poco.tar
Source76: %name-%version-contrib-protobuf.tar
Source77: %name-%version-contrib-qpl.tar
Source78: %name-%version-contrib-qpl-tools-third-party-google-test.tar
Source79: %name-%version-contrib-rapidjson.tar
Source80: %name-%version-contrib-rapidjson-thirdparty-gtest.tar
Source81: %name-%version-contrib-re2.tar
Source82: %name-%version-contrib-replxx.tar
Source83: %name-%version-contrib-rocksdb.tar
Source84: %name-%version-contrib-s2geometry.tar
Source85: %name-%version-contrib-sentry-native.tar
Source86: %name-%version-contrib-simdjson.tar
Source87: %name-%version-contrib-snappy.tar
Source88: %name-%version-contrib-snappy-third_party-benchmark.tar
Source89: %name-%version-contrib-snappy-third_party-googletest.tar
Source90: %name-%version-contrib-sparsehash-c11.tar
Source91: %name-%version-contrib-sqlite-amalgamation.tar
Source92: %name-%version-contrib-sysroot.tar
Source93: %name-%version-contrib-thrift.tar
Source94: %name-%version-contrib-unixodbc.tar
Source95: %name-%version-contrib-vectorscan.tar
Source96: %name-%version-contrib-wordnet-blast.tar
Source97: %name-%version-contrib-wyhash.tar
Source98: %name-%version-contrib-xz.tar
Source99: %name-%version-contrib-yaml-cpp.tar
Source100: %name-%version-contrib-zlib-ng.tar
Source101: %name-%version-contrib-zstd.tar
Source102: %name-%version-contrib-libdivide.tar


Source1000: clickhouse.watch

Patch0: %name-%version-%release.patch
Patch1: clickhouse-base64-ppc64le.patch
Patch2: clickhouse-avro-gcc10-compat.patch
Patch3: clickhouse-fastops-gcc-compat.patch
Patch4: clickhouse-llvm-build.patch
Patch5: clickhouse-22.3-use-system-toolchain.patch

BuildRequires(pre): rpm-build-python3
%if_with clang
BuildRequires: clang%llvm_version llvm%llvm_version lld%llvm_version
%else
BuildRequires: gcc-c++
%endif
BuildRequires: cmake libreadline-devel python3 gperf tzdata
BuildRequires: rpm-macros-cmake rpm-macros-ninja-build ninja-build /proc
BuildRequires: perl-JSON-XS libasan-devel-static
BuildRequires: libstdc++-devel-static

%add_python3_path %_datadir/clickhouse-test

Conflicts: clickhouse-lts

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
Conflicts: clickhouse-lts-common-static

%description common-static
This package provides common files for both clickhouse server and client.

%package server
Summary: Server binary for ClickHouse
Group: Databases
Requires: %name-common-static = %EVR
Conflicts: clickhouse-lts-server

%description server
This package contains server binaries for ClickHouse DBMS.

%package client
Summary: Client binary for ClickHouse
Group: Databases
Requires: %name-common-static = %EVR
Conflicts: clickhouse-lts-client

%description client
This package contains clickhouse-client, clickhouse-local and clickhouse-benchmark

%package test
Summary: ClickHouse tests
Group: Databases
Requires: %name-client = %EVR
Conflicts: clickhouse-lts-test

%description test
ClickHouse tests

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39 -a40 -a41 -a42 -a43 -a44 -a45 -a46 -a47 -a48 -a49 -a50 -a51 -a52 -a53 -a54 -a55 -a56 -a57 -a58 -a59 -a60 -a61 -a62 -a63 -a64 -a65 -a66 -a67 -a68 -a69 -a70 -a71 -a72 -a73 -a74 -a75 -a76 -a77 -a78 -a79 -a80 -a81 -a82 -a83 -a84 -a85 -a86 -a87 -a88 -a89 -a90 -a91 -a92 -a93 -a94 -a95 -a96 -a97 -a98 -a99 -a100 -a101 -a 102

%patch0 -p1

pushd contrib/base64
%patch1 -p1
popd

pushd contrib/avro
%patch2 -p1
popd

pushd contrib/fastops
%patch3 -p1
popd

pushd contrib/llvm
%patch4 -p1
popd

%patch5 -p1

%build
if [ %__nprocs -gt 6 ] ; then
	export NPROCS=6
else
	export NPROCS=%__nprocs
fi

# remove binary toolchain from clickhouse contrib
rm -rf contrib/sysroot/linux*

# strip debuginfo: with bundled llvm debuginfo takes too much space
%define optflags_debug -g0

# -DENABLE_HIVE:BOOL=OFF is needed to circumvent build failure due to not finding orc headers
export ALTWRAP_LLVM_VERSION="%llvm_version"
%cmake \
%if_with clang
	-DCMAKE_C_COMPILER=clang-%clang_version \
	-DENABLE_CCACHE=0 \
	-DCMAKE_CXX_COMPILER=clang++-%clang_version \
	-DUSE_LIBCXX:BOOL=ON \
	-DPARALLEL_COMPILE_JOBS=$NPROCS \
	-DPARALLEL_LINK_JOBS=1 \
%else
	-DUSE_LIBCXX:BOOL=OFF \
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
%endif
%if_with jemalloc
	-DENABLE_JEMALLOC:BOOL=ON \
%else
	-DENABLE_JEMALLOC:BOOL=OFF \
%endif
	-DENABLE_PARQUET:BOOL=OFF \
	-DENABLE_CLICKHOUSE_TEST:BOOL=ON \
	-DENABLE_S3:BOOL=OFF \
	-DENABLE_UTILS:BOOL=OFF \
	-DENABLE_HIVE:BOOL=OFF \
	-DUSE_UNWIND:BOOL=ON \
	%nil

%ninja_build -C %_cmake__builddir clickhouse-bundle

%install
%ninja_install -C %_cmake__builddir
install -Dm0644 packages/clickhouse-server.service %buildroot%_unitdir/clickhouse-server.service
mkdir -p %buildroot%_localstatedir/clickhouse
mkdir -p %buildroot%_logdir/clickhouse-server

# remove unpackaged files
rm -rfv %buildroot%_prefix/cmake
rm -fv %buildroot%_prefix/lib/*.a
rm -rf %buildroot%_sysconfdir/clickhouse-keeper

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
%_bindir/clickhouse-static-files-disk-uploader
%_datadir/bash-completion/completions/clickhouse
%_datadir/bash-completion/completions/clickhouse-bootstrap

%files server
%dir %_sysconfdir/clickhouse-server
%config(noreplace) %_sysconfdir/clickhouse-server/config.xml
%config(noreplace) %_sysconfdir/clickhouse-server/users.xml
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
%_bindir/clickhouse-disks
%_bindir/clickhouse-benchmark
%_bindir/clickhouse-obfuscator
%_bindir/clickhouse-format
%_bindir/clickhouse-extract-from-config
%_bindir/clickhouse-git-import
%_bindir/clickhouse-su
%_datadir/bash-completion/completions/clickhouse-benchmark
%_datadir/bash-completion/completions/clickhouse-client
%_datadir/bash-completion/completions/clickhouse-local

%files test
%_bindir/clickhouse-test
%_datadir/clickhouse-test

%changelog
* Wed Feb 01 2023 Anton Farygin <rider@altlinux.ru> 22.8.13.20-alt1
- 22.8.12.45 -> 22.8.13.20

* Tue Jan 17 2023 Anton Farygin <rider@altlinux.ru> 22.8.12.45-alt1
- 22.8.11.15 -> 22.8.12.45
- built with clang-15

* Thu Dec 15 2022 Anton Farygin <rider@altlinux.ru> 22.8.11.15-alt1
- 22.8.10.29 -> 22.8.11.15

* Sun Dec 04 2022 Anton Farygin <rider@altlinux.ru> 22.8.10.29-alt1
- 22.8.9.24 -> 22.8.10.29

* Tue Nov 22 2022 Anton Farygin <rider@altlinux.ru> 22.8.9.24-alt1
- 22.8.8.3 -> 22.8.9.24

* Tue Nov 01 2022 Anton Farygin <rider@altlinux.ru> 22.8.8.3-alt1
- 22.8.6.71 -> 22.8.8.3

* Sat Oct 22 2022 Anton Farygin <rider@altlinux.ru> 22.8.6.71-alt1
- 22.3.9.19 -> 22.8.6.71

* Wed Aug 03 2022 Anton Farygin <rider@altlinux.ru> 22.3.9.19-alt1
- 22.3.8.39 -> 22.3.9.19

* Mon Jul 11 2022 Anton Farygin <rider@altlinux.ru> 22.3.8.39-alt1
- 22.3.7.28 -> 22.3.8.39

* Tue Jun 28 2022 Anton Farygin <rider@altlinux.ru> 22.3.7.28-alt2
- fix version in clickhouse-client output

* Tue Jun 21 2022 Anton Farygin <rider@altlinux.ru> 22.3.7.28-alt1
- 22.3.6.5 -> 22.3.7.28

* Tue May 10 2022 Anton Farygin <rider@altlinux.ru> 22.3.6.5-alt1
- 22.3.3.44 -> 22.3.6.5

* Thu Apr 14 2022 Anton Farygin <rider@altlinux.ru> 22.3.3.44-alt2
- use system toolchain for building clickhouse
- removed clickhouse-keeper default config 

* Thu Apr 07 2022 Anton Farygin <rider@altlinux.ru> 22.3.3.44-alt1
- 22.3.2.2 -> 22.3.3.44

* Tue Mar 22 2022 Anton Farygin <rider@altlinux.ru> 22.3.2.2-alt2
- simplify backporting for stable ALT branches via define llvm_version

* Fri Mar 18 2022 Anton Farygin <rider@altlinux.ru> 22.3.2.2-alt1
- 22.2.3.5 -> 22.3.2.2

* Mon Feb 28 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 22.2.3.5-alt1
- Updated to stable upstream version 22.2.3.5.

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

