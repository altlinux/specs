%global __find_debuginfo_files %nil
%define _unpackaged_files_terminate_build 1
%global llvm_version 17.0
%global clang_version 17
%global __nprocs 8

%def_with clang

%ifnarch x86_64
%define relax ||:
%else
%define relax %nil
%endif

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
Version: 24.3.4.147
Release: alt1
Summary: Open-source distributed column-oriented DBMS
License: Apache-2.0
Group: Databases
Url: https://clickhouse.com
VCS: https://github.com/ClickHouse/ClickHouse.git
Source: %name-%version.tar.xz

Source100: %name-%version-contrib-abseil-cpp.tar
Source101: %name-%version-contrib-aklomp-base64.tar
Source102: %name-%version-contrib-AMQP-CPP.tar
Source103: %name-%version-contrib-annoy.tar
Source104: %name-%version-contrib-arrow.tar
Source105: %name-%version-contrib-avro.tar
Source106: %name-%version-contrib-aws.tar.xz
Source107: %name-%version-contrib-aws-c-auth.tar
Source108: %name-%version-contrib-aws-c-cal.tar
Source109: %name-%version-contrib-aws-c-common.tar
Source110: %name-%version-contrib-aws-c-compression.tar
Source111: %name-%version-contrib-aws-c-event-stream.tar
Source112: %name-%version-contrib-aws-checksums.tar
Source113: %name-%version-contrib-aws-c-http.tar
Source114: %name-%version-contrib-aws-c-io.tar
Source115: %name-%version-contrib-aws-c-mqtt.tar
Source116: %name-%version-contrib-aws-crt-cpp.tar
Source117: %name-%version-contrib-aws-c-s3.tar
Source118: %name-%version-contrib-aws-c-sdkutils.tar
Source119: %name-%version-contrib-aws-s2n-tls.tar
Source120: %name-%version-contrib-aws-s2n-tls-tests-cbmc-aws-verification-model-for-libcrypto.tar
Source121: %name-%version-contrib-azure.tar
Source122: %name-%version-contrib-boost.tar
Source123: %name-%version-contrib-boringssl.tar
Source124: %name-%version-contrib-brotli.tar
Source125: %name-%version-contrib-brotli-research-esaxx.tar
Source126: %name-%version-contrib-brotli-research-libdivsufsort.tar
Source127: %name-%version-contrib-bzip2.tar
Source128: %name-%version-contrib-capnproto.tar
Source129: %name-%version-contrib-c-ares.tar
Source130: %name-%version-contrib-cassandra.tar
Source131: %name-%version-contrib-cctz.tar
Source132: %name-%version-contrib-cld2.tar
Source133: %name-%version-contrib-corrosion.tar
Source134: %name-%version-contrib-cppkafka.tar
Source135: %name-%version-contrib-cppkafka-third_party-Catch2.tar
Source136: %name-%version-contrib-crc32-s390x.tar
Source137: %name-%version-contrib-crc32-vpmsum.tar
Source138: %name-%version-contrib-croaring.tar
Source139: %name-%version-contrib-curl.tar
Source140: %name-%version-contrib-cyrus-sasl.tar
Source141: %name-%version-contrib-datasketches-cpp.tar
Source142: %name-%version-contrib-double-conversion.tar
Source143: %name-%version-contrib-dragonbox.tar
Source144: %name-%version-contrib-fast_float.tar
Source145: %name-%version-contrib-fastops.tar
Source146: %name-%version-contrib-flatbuffers.tar
Source147: %name-%version-contrib-fmtlib.tar
Source148: %name-%version-contrib-FP16.tar
Source149: %name-%version-contrib-google-benchmark.tar
Source150: %name-%version-contrib-google-protobuf.tar
Source151: %name-%version-contrib-googletest.tar
Source152: %name-%version-contrib-grpc.tar
Source153: %name-%version-contrib-h3.tar
Source154: %name-%version-contrib-hive-metastore.tar
Source155: %name-%version-contrib-icu.tar
Source156: %name-%version-contrib-icudata.tar
Source157: %name-%version-contrib-idna.tar
Source158: %name-%version-contrib-idxd-config.tar
Source159: %name-%version-contrib-incbin.tar
Source160: %name-%version-contrib-isa-l.tar
Source161: %name-%version-contrib-jemalloc.tar
Source162: %name-%version-contrib-krb5.tar
Source163: %name-%version-contrib-lemmagen-c.tar
Source164: %name-%version-contrib-libarchive.tar
Source165: %name-%version-contrib-libbcrypt.tar
Source166: %name-%version-contrib-libcpuid.tar
Source167: %name-%version-contrib-libdivide.tar
Source168: %name-%version-contrib-libfiu.tar
Source169: %name-%version-contrib-libgsasl.tar
Source170: %name-%version-contrib-libhdfs3.tar
Source171: %name-%version-contrib-libpq.tar
Source172: %name-%version-contrib-libpqxx.tar
Source173: %name-%version-contrib-libprotobuf-mutator.tar
Source174: %name-%version-contrib-librdkafka.tar
Source175: %name-%version-contrib-libssh.tar
Source176: %name-%version-contrib-libstemmer_c.tar
Source177: %name-%version-contrib-libunwind.tar
Source178: %name-%version-contrib-liburing.tar
Source179: %name-%version-contrib-libuv.tar
Source180: %name-%version-contrib-libxml2.tar
Source181: %name-%version-contrib-llvm-project.tar.xz
Source182: %name-%version-contrib-lz4.tar
Source183: %name-%version-contrib-magic_enum.tar
Source184: %name-%version-contrib-mariadb-connector-c.tar
Source185: %name-%version-contrib-miniselect.tar
Source186: %name-%version-contrib-minizip-ng.tar
Source187: %name-%version-contrib-morton-nd.tar
Source188: %name-%version-contrib-msgpack-c.tar
Source189: %name-%version-contrib-msgpack-c-external-boost-predef.tar
Source190: %name-%version-contrib-msgpack-c-external-boost-preprocessor.tar
Source191: %name-%version-contrib-nanodbc.tar
Source192: %name-%version-contrib-nats-io.tar
Source193: %name-%version-contrib-nats-io-coveralls-cmake.tar
Source194: %name-%version-contrib-nlp-data.tar
Source195: %name-%version-contrib-NuRaft.tar
Source196: %name-%version-contrib-NuRaft-asio.tar
Source197: %name-%version-contrib-openldap.tar
Source198: %name-%version-contrib-openssl.tar
Source199: %name-%version-contrib-openssl-gost-engine.tar
Source200: %name-%version-contrib-openssl-gost-engine-libprov.tar
Source201: %name-%version-contrib-openssl-krb5.tar
Source202: %name-%version-contrib-openssl-pyca-cryptography.tar
Source203: %name-%version-contrib-openssl-wycheproof.tar
Source204: %name-%version-contrib-orc.tar
Source205: %name-%version-contrib-pocketfft.tar
Source206: %name-%version-contrib-qatlib.tar
Source207: %name-%version-contrib-QAT-ZSTD-Plugin.tar
Source208: %name-%version-contrib-qpl.tar
Source209: %name-%version-contrib-qpl-tools-third-party-benchmark.tar
Source210: %name-%version-contrib-qpl-tools-third-party-google-test.tar
Source211: %name-%version-contrib-rapidjson.tar
Source212: %name-%version-contrib-re2.tar
Source213: %name-%version-contrib-replxx.tar
Source214: %name-%version-contrib-robin-map.tar
Source215: %name-%version-contrib-rocksdb.tar
Source216: %name-%version-contrib-s2geometry.tar
Source217: %name-%version-contrib-sentry-native.tar
Source218: %name-%version-contrib-simdjson.tar
Source219: %name-%version-contrib-SimSIMD.tar
Source220: %name-%version-contrib-snappy.tar
Source221: %name-%version-contrib-snappy-third_party-benchmark.tar
Source222: %name-%version-contrib-snappy-third_party-googletest.tar
Source223: %name-%version-contrib-sparsehash-c11.tar
Source224: %name-%version-contrib-sqids-cpp.tar
Source225: %name-%version-contrib-sqlite-amalgamation.tar
Source226: %name-%version-contrib-sysroot.tar
Source227: %name-%version-contrib-thrift.tar
Source228: %name-%version-contrib-ulid-c.tar
Source229: %name-%version-contrib-unixodbc.tar
Source230: %name-%version-contrib-usearch.tar
Source231: %name-%version-contrib-usearch-fp16.tar
Source232: %name-%version-contrib-usearch-simsimd.tar
Source233: %name-%version-contrib-vectorscan.tar
Source234: %name-%version-contrib-wordnet-blast.tar
Source235: %name-%version-contrib-wyhash.tar
Source236: %name-%version-contrib-xxHash.tar
Source237: %name-%version-contrib-xz.tar
Source238: %name-%version-contrib-yaml-cpp.tar
Source239: %name-%version-contrib-zlib-ng.tar
Source240: %name-%version-contrib-zstd.tar

Source1000: clickhouse.watch

Patch0: %name-%version-%release.patch
Patch2: clickhouse-avro-gcc10-compat.patch
Patch3: clickhouse-fastops-gcc-compat.patch
Patch4: clickhouse-23.8-rust-copy-vendor-directory.patch
Patch5: clickhouse-24.3-use-system-toolchain.patch

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
BuildRequires: yasm nasm

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

%prep
%setup -a100 -a101 -a102 -a103 -a104 -a105 -a106 -a107 -a108 -a109 -a110 -a111 -a112 -a113 -a114 -a115 -a116 -a117 -a118 -a119 -a120 -a121 -a122 -a123 -a124 -a125 -a126 -a127 -a128 -a129 -a130 -a131 -a132 -a133 -a134 -a135 -a136 -a137 -a138 -a139 -a140 -a141 -a142 -a143 -a144 -a145 -a146 -a147 -a148 -a149 -a150 -a151 -a152 -a153 -a154 -a155 -a156 -a157 -a158 -a159 -a160 -a161 -a162 -a163 -a164 -a165 -a166 -a167 -a168 -a169 -a170 -a171 -a172 -a173 -a174 -a175 -a176 -a177 -a178 -a179 -a180 -a181 -a182 -a183 -a184 -a185 -a186 -a187 -a188 -a189 -a190 -a191 -a192 -a193 -a194 -a195 -a196 -a197 -a198 -a199 -a200 -a201 -a202 -a203 -a204 -a205 -a206 -a207 -a208 -a209 -a210 -a211 -a212 -a213 -a214 -a215 -a216 -a217 -a218 -a219 -a220 -a221 -a222 -a223 -a224 -a225 -a226 -a227 -a228 -a229 -a230 -a231 -a232 -a233 -a234 -a235 -a236 -a237 -a238 -a239 -a240

%patch0 -p1

pushd contrib/avro
%patch2 -p1
popd

pushd contrib/fastops
%patch3 -p1
popd

%patch4 -p1
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
	-DCOMPILER_CACHE=disabled \
	-DUSE_LIBCXX:BOOL=ON \
	-DPARALLEL_COMPILE_JOBS=$NPROCS \
	-DPARALLEL_LINK_JOBS=1 \
%else
	-DUSE_LIBCXX:BOOL=OFF \
	-DPARALLEL_COMPILE_JOBS=$NPROCS \
	-DPARALLEL_LINK_JOBS=$NPROCS \
%endif
	-DOMIT_HEAVY_DEBUG_SYMBOLS=ON \
	-DSPLIT_DEBUG_SYMBOLS=OFF \
	-DENABLE_RUST=OFF \
	-DBUILD_STANDALONE_KEEPER=1 \
	-DENABLE_CLICKHOUSE_KEEPER=1 \
	-DCMAKE_VERBOSE_MAKEFILE=1 \
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
%ifarch aarch64
	-DNO_ARMV81_OR_HIGHER=1 \
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

# remove empty debuginfo
rm -rf %buildroot%_libdir/debug


%check
./%_cmake__builddir/src/unit_tests_dbms --gtest_filter='-CoordinationTest.TestRotateIntervalChanges:ReadBufferAIOTest.TestReadAfterAIO:WeakHash32.*:Common.ReverseDNS:ParserPRQL/*' %relax

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
%_datadir/clickhouse
%_datadir/bash-completion/completions/clickhouse
%_datadir/bash-completion/completions/clickhouse-bootstrap

%files server
%dir %_sysconfdir/clickhouse-server
%config(noreplace) %_sysconfdir/clickhouse-server/config.xml
%config(noreplace) %_sysconfdir/clickhouse-server/users.xml
%config(noreplace) %_sysconfdir/clickhouse-keeper/keeper_config.xml
%_bindir/ch*
%_bindir/clickhouse-server
%_bindir/clickhouse-keeper
%_bindir/clickhouse-keeper-client
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

%changelog
* Mon Jul 01 2024 Anton Farygin <rider@altlinux.ru> 24.3.4.147-alt1
- 24.3.2.23 -> 24.3.4.147

* Sun Apr 28 2024 Anton Farygin <rider@altlinux.ru> 24.3.2.23-alt1
- 24.3.1.2672 -> 24.3.2.23

* Thu Mar 28 2024 Anton Farygin <rider@altlinux.ru> 24.3.1.2672-alt1
- 23.8.9.54 -> 24.3.1.2672

* Tue Jan 23 2024 Anton Farygin <rider@altlinux.ru> 23.8.9.54-alt1
- 23.8.7.24 > 23.8.9.54

* Tue Nov 21 2023 Anton Farygin <rider@altlinux.ru> 23.8.7.24-alt1
- 23.3.13.6 -> 23.8.7.24

* Wed Oct 04 2023 Anton Farygin <rider@altlinux.ru> 23.3.13.6-alt1
- 23.3.11.5 -> 23.3.13.6

* Fri Sep 01 2023 Anton Farygin <rider@altlinux.ru> 23.3.11.5-alt1
- 23.3.8.21 -> 23.3.11.5

* Tue Aug 08 2023 Anton Farygin <rider@altlinux.ru> 23.3.8.21-alt1
- 23.3.7.5 -> 23.3.8.21

* Fri Jul 07 2023 Anton Farygin <rider@altlinux.ru> 23.3.7.5-alt1
- 23.3.3.52 -> 23.3.7.5

* Thu Jun 15 2023 Anton Farygin <rider@altlinux.ru> 23.3.3.52-alt1
- 23.3.2.37 -> 23.3.3.52

* Wed May 03 2023 Anton Farygin <rider@altlinux.ru> 23.3.2.37-alt1
- 22.8.17.17 -> 23.3.2.37

* Wed Apr 26 2023 Anton Farygin <rider@altlinux.ru> 22.8.17.17-alt1
- 22.8.13.20 -> 22.8.17.17

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

