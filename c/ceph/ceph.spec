%define git_version 4c3647a322c0ff5a1dd2344e039859dcbd28c830
%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%def_with ocf
%def_with tcmalloc
%def_without libzfs
%def_without selinux
%def_with libradosstriper
%ifarch x86_64 aarch64 ppc64le
%def_with lttng
%else
%def_without lttng
%endif
%def_without cephfs_java
%def_disable check
%def_without ceph_test_package
%def_with python3
%def_with system_boost
%def_with system_rocksdb
%def_without system_fmt
%def_without mgr_dashboard
%def_with blustore
%def_with liburing
%def_with pmem
%def_with rbd_rwl_cache
%def_with rbd_ssd_cache
%def_without seastar
%def_without jaeger
%def_without zbd
%def_with cephfs_shell
%def_without amqp_endpoint
%def_without kafka_endpoint
%def_with grafana
%def_with lua_packages

%if_with python3
%add_python3_path %_datadir/ceph/mgr
%allow_python3_import_path %_datadir/ceph/mgr
%endif

%def_without spdk
%def_without dpdk
%def_without system_dpdk

%ifndef build_parallel_jobs
%define build_parallel_jobs 16
%endif

Name: ceph
Version: 16.2.11
Release: alt1
Summary: User space components of the Ceph file system
Group: System/Base

License: LGPL-2.1 and LGPL-3.0 and CC-BY-SA-3.0 and GPL-2.0 and BSL-1.0 and BSD-3-Clause and MIT
Url: http://ceph.com/

ExcludeArch: %ix86 %arm %mips32 ppc

Source0: %name-%version.tar
%if_without system_boost
Source10: https://downloads.sourceforge.net/project/boost/boost/1.72.0/boost_1_72_0.tar.bz2
%endif
# git submodules
Source11: ceph-erasure-code-corpus.tar
Source12: ceph-object-corpus.tar
Source14: blkin.tar
Source15: civetweb.tar
Source16: isa-l_crypto.tar
Source17: dpdk.tar
Source18: gf-complete.tar
Source19: jerasure.tar
Source20: googletest.tar
Source21: isa-l.tar
Source23: rapidjson.tar
Source24: rocksdb.tar
Source25: spdk.tar
Source26: xxHash.tar
Source27: zstd.tar
Source28: c-ares.tar
Source29: dmclock.tar
Source30: seastar.tar
Source31: fmt.tar
Source32: spawn.tar
Source33: rook-client-python.tar
Source34: s3select.tar
Source35: opentracing-cpp.tar
Source36: jaeger-client-cpp.tar
Source37: thrift.tar
Source38: libkmip.tar

Patch: %name-%version.patch
Patch100: erasure_code-aarch64-textrel.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-systemd >= 5
# in cmake-3.10.2-alt add support find boost-1.66
BuildRequires: cmake >= 3.10.2-alt1 ninja-build
BuildRequires(pre): rpm-macros-cmake
%if_with system_boost
BuildRequires: boost-asio-devel boost-devel-headers >= 1.72.0 boost-program_options-devel boost-intrusive-devel
BuildRequires: boost-filesystem-devel boost-coroutine-devel boost-context-devel boost-lockfree-devel boost-msm-devel
%endif
BuildRequires: gcc-c++
BuildRequires: libaio-devel libblkid-devel libcryptsetup-devel
%{?_with_liburing:BuildRequires: liburing-devel}
BuildRequires: libcurl-devel libexpat-devel libcap-ng-devel
BuildRequires: libstdc++-devel-static
BuildRequires: libfuse-devel libkeyutils-devel
BuildRequires: libldap-devel libleveldb-devel libnss-devel
#BuildRequires: libkrb5-devel
BuildRequires: libssl-devel libudev-devel libxfs-devel libbtrfs-devel libnl-devel
%{?_with_libzfs:BuildRequires: libzfs-devel}
BuildRequires: nasm
%{?_with_amqp_endpoint:BuildRequires: librabbitmq-c-devel}
%{?_with_kafka_endpoint:BuildRequires: librdkafka-devel}
BuildRequires: zlib-devel bzlib-devel liblz4-devel libzstd-devel libsnappy-devel
BuildRequires: libsqlite3-devel
BuildRequires: libxml2-devel
BuildRequires: libuuid-devel
BuildRequires: libncurses-devel
BuildRequires: libicu-devel
BuildRequires: liboath-devel
%{?_with_system_fmt:BuildRequires: libfmt-devel >= 5.2.1}
BuildRequires: jq gperf
%{?_with_tcmalloc:BuildRequires: libgperftools-devel >= 2.7.90}
%{?_with_lttng:BuildRequires: liblttng-ust-devel libbabeltrace-devel}
%{?_with_cephfs_java:BuildRequires: java-devel}
%{?_with_selinux:BuildRequires: checkpolicy selinux-policy-devel}
%{?_enable_check:BuildRequires: socat ctest}
BuildRequires: libsystemd-devel
%{?_with_system_rocksdb:BuildRequires: librocksdb-devel}
BuildRequires: liblua5-devel >= 5.3 liblua5-devel-static >= 5.3
%{?_with_lua_packages:BuildRequires: lua5.3-luarocks}
%{?_with_system_dpdk:BuildRequires: dpdk-devel dpdk-tools}
%{?_with_dpdk:BuildRequires: libcryptopp-devel}
%{?_with_spdk:BuildRequires: CUnit-devel libiscsi-devel libnuma-devel}
%{?_with_zbd:BuildRequires: libzbd-devel}
%{?_with_pmem:BuildRequires: libpmem-devel libpmemobj-devel}
%{?_with_grafana:BuildRequires: jsonnet}
%ifnarch %arm
BuildRequires: rdma-core-devel
%endif

%if_with seastar
BuildRequires: libc-ares-devel
BuildRequires: libcryptopp-devel
BuildRequires: libgnutls-devel
BuildRequires: libhwloc-devel
BuildRequires: libpciaccess-devel
BuildRequires: liblksctp-tools-devel
BuildRequires: libnumactl-devel
BuildRequires: protobuf-compiler
BuildRequires: libprotobuf-devel
BuildRequires: ragel
BuildRequires: systemtap-sdt-devel
BuildRequires: libyaml-cpp-devel
%endif

%if_with jaeger
BuildRequires: bison
BuildRequires: flex
BuildRequires: nlohmann-json-devel
BuildRequires: libevent-devel
BuildRequires: libyaml-cpp-devel
%endif

%if_with python3
BuildRequires: python3-module-Cython python3-module-OpenSSL python3-devel python3-module-setuptools
%{?_with_system_boost:BuildRequires: boost-python3-devel}
BuildRequires: python3-module-prettytable python3-module-routes python3-module-bcrypt
BuildRequires: python3-module-html5lib python3-module-pyasn1
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink
BuildRequires: libxmlsec1-devel
%{?_enable_check:BuildRequires: python3-module-cherrypy python3-module-jwt python3-module-werkzeug python3-module-pecan python3-module-tox}
%endif


Requires: ceph-osd = %EVR
Requires: ceph-mds = %EVR
Requires: ceph-mgr = %EVR
Requires: ceph-mon = %EVR

%description
Ceph is a distributed network file system designed to provide excellent
performance, reliability, and scalability.

%package base
Summary: Ceph Base Package
Group: System/Base
Requires: ceph-common = %EVR
Requires: ntp-server
Requires: /usr/sbin/smartctl
Requires: /usr/sbin/nvme

%description base
Base is the package that includes all the files shared amongst ceph servers

%package common
Summary: Ceph Common
Group: System/Base
Requires: librbd1 = %EVR
Requires: librados2 = %EVR
Requires: libcephfs2 = %EVR
Requires: librgw2 = %EVR
Requires: python3-module-ceph-argparse = %EVR
%description common
Common utilities to mount and interact with a ceph storage cluster.
Comprised of files that are common to Ceph clients and servers.

%package -n cephadm
Summary: Utility to bootstrap Ceph clusters
Group: System/Base
BuildArch: noarch
Requires: podman >= 2.0.2
Requires: lvm2
%description -n cephadm
Utility to bootstrap a Ceph cluster and manage Ceph daemons deployed
with systemd and podman.

%package -n python3-module-ceph-common
Summary:	Python 3 utility libraries for Ceph
Group: Development/Python3
BuildArch: noarch
%description -n python3-module-ceph-common
This package contains data structures, classes and functions used by Ceph.
It also contains utilities used for the cephadm orchestrator.

%package -n python3-module-ceph_volume
Summary: Python3 utility libraries for Ceph CLI
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-ceph-common = %EVR

%description -n python3-module-ceph_volume
%summary

%package -n python3-module-ceph-argparse
Summary: Python 3 utility libraries for Ceph CLI
Group: Development/Python3
BuildArch: noarch
%description -n python3-module-ceph-argparse
This package contains types and routines for Python 3 used by the Ceph CLI as
well as the RESTful interface. These have to do with querying the daemons for
command-description information, validating user command input against those
descriptions, and submitting the command to the appropriate daemon.

%package mds
Summary: Ceph Metadata Server Daemon
Group: System/Base
Requires: ceph-base = %EVR
%description mds
ceph-mds is the metadata server daemon for the Ceph distributed file system.
One or more instances of ceph-mds collectively manage the file system
namespace, coordinating access to the shared OSD cluster.

%package mon
Summary: Ceph Monitor Daemon
Group: System/Base
Requires: ceph-base = %EVR

%description mon
ceph-mon is the cluster monitor daemon for the Ceph distributed file
system. One or more instances of ceph-mon form a Paxos part-time
parliament cluster that provides extremely reliable and durable storage
of cluster membership, configuration, and state.

%package mgr
Summary: Ceph Manager Daemon
Group: System/Base
Requires: ceph-base = %EVR
Requires: ceph-mgr-modules-core = %EVR
AutoProv: no

%if_with python3
%py3_provides ceph_module
%py3_provides mgr_module
%py3_provides mgr_util
%py3_provides orchestrator
%endif

%description mgr
ceph-mgr enables python modules that provide services (such as the REST
module derived from Calamari) and expose CLI hooks.  ceph-mgr gathers
the cluster maps, the daemon metadata, and performance counters, and
exposes all these to the python modules.

%package mgr-modules-core
Summary: Ceph Manager modules which are always enabled
Group: System/Base
Conflicts: ceph-mgr < 15.2.5-alt1
%description mgr-modules-core
ceph-mgr-modules-core provides a set of modules which are always
enabled by ceph-mgr.

%package mgr-dashboard
Summary: Dashboard module for Ceph Manager Daemon
Group: Monitoring
Requires: ceph-mgr = %EVR
Requires: ceph-mgr-restful = %EVR
Requires: ceph-grafana-dashboards = %EVR
AutoProv: no
%description mgr-dashboard
%summary.

%package mgr-insights
Summary: Insights module for Ceph Manager Daemon
Group: Monitoring
Requires: ceph-mgr = %EVR
AutoProv: no
%description mgr-insights
%summary.

%package mgr-influx
Summary: InfluxDB module for Ceph Manager Daemon
Group: Monitoring
Requires: ceph-mgr = %EVR
%if_with python3
Requires: python3-module-influxdb
%endif
AutoProv: no
%description mgr-influx
%summary.

%package mgr-prometheus
Summary: Prometheus module for Ceph Manager Daemon
Group: Monitoring
Requires: ceph-mgr = %EVR
AutoProv: no
%description mgr-prometheus
%summary.

%package mgr-restful
Summary: Restful module for Ceph Manager Daemon
Group: Monitoring
Requires: ceph-mgr = %EVR
AutoProv: no
%description mgr-restful
%summary.

%package mgr-telegraf
Summary: Telegraf module for Ceph Manager Daemon
Group: Monitoring
Requires: ceph-mgr = %EVR
AutoProv: no
%description mgr-telegraf
%summary.

%package mgr-diskprediction-local
Summary: Ceph Manager module for predicting disk failures
Group: Monitoring
Requires: ceph-mgr = %EVR
AutoProv: no
%description mgr-diskprediction-local
ceph-mgr-diskprediction-local is a ceph-mgr module that tries to predict
disk failures using local algorithms and machine-learning databases.

%package mgr-rook
Summary: Ceph Manager module for Rook-based orchestration
Group: System/Configuration/Other
Requires: ceph-mgr = %EVR
AutoProv: no
%description mgr-rook
ceph-mgr-rook is a ceph-mgr module for orchestration functions using
a Rook backend.

%package mgr-k8sevents
Summary: Ceph Manager module to orchestrate ceph-events to kubernetes' events API
Group: System/Configuration/Other
Requires: ceph-mgr = %EVR
AutoProv: no
%description mgr-k8sevents
ceph-mgr-k8sevents is a ceph-mgr module that sends every ceph-events
to kubernetes' events API

%package mgr-cephadm
Summary: Ceph Manager module for cephadm-based orchestration
Group: System/Configuration/Other
Requires: ceph-mgr = %EVR
Requires: cephadm = %EVR
Requires: openssh-clients
Requires: python3-module-jinja2
AutoProv: no
%description mgr-cephadm
ceph-mgr-cephadm is a ceph-mgr module for orchestration functions using
the integrated cephadm deployment tool management operations.

%package mgr-zabbix
Summary: Zabbix module for Ceph Manager Daemon
Group: Monitoring
Requires: ceph-mgr = %EVR
AutoProv: no
%description mgr-zabbix
%summary.

%package fuse
Summary: Ceph fuse-based client
Group: System/Kernel and hardware
Requires: fuse
Requires: python3
%description fuse
FUSE based client for Ceph distributed network file system

%package -n cephfs-mirror
Summary: Ceph daemon for mirroring CephFS snapshots
Group: System/Base
Requires: ceph-base = %EVR
Requires: librados2 = %EVR
Requires: libcephfs2 = %EVR
%description -n cephfs-mirror
Daemon for mirroring CephFS snapshots between Ceph clusters.

%package -n rbd-fuse
Summary: Ceph fuse-based client
Group: System/Base
Requires: librados2 = %EVR
Requires: librbd1 = %EVR
%description -n rbd-fuse
FUSE based client to map Ceph rbd images to files

%package -n rbd-mirror
Summary: Ceph daemon for mirroring RBD images
Group: System/Base
Requires: ceph-base = %EVR
Requires: librados2 = %EVR
%description -n rbd-mirror
Daemon for mirroring RBD images between Ceph clusters, streaming
changes asynchronously.

%package -n rbd-nbd
Summary: Ceph RBD client base on NBD
Group: System/Base
Requires: librados2 = %EVR
Requires: librbd1 = %EVR
%description -n rbd-nbd
NBD based client to map Ceph rbd images to local device

%package radosgw
Summary: Rados REST gateway
Group: System/Libraries
Requires: ceph-base = %EVR
Requires: librados2 = %EVR
Requires: librgw2 = %EVR
%description radosgw
RADOS is a distributed object store used by the Ceph distributed
storage system.  This package provides a REST gateway to the
object store that aims to implement a superset of Amazon's S3
service as well as the OpenStack Object Storage ("Swift") API.

%package immutable-object-cache
Summary: Ceph daemon for immutable object cache
Group: System/Base
Requires: ceph-base = %EVR
Requires: librados2 = %EVR
%description -n ceph-immutable-object-cache
Daemon for immutable object cache.

%package -n cephfs-top
Summary: top(1) like utility for Ceph Filesystem
Group: Monitoring
%description -n cephfs-top
This package provides a top(1) like utility to display Ceph Filesystem metrics
in realtime.

%package resource-agents
Summary: OCF-compliant resource agents for Ceph daemons
Group: System/Configuration/Other
License: LGPLv2
Requires: %name = %EVR
%description resource-agents
Resource agents for monitoring and managing Ceph daemons
under Open Cluster Framework (OCF) compliant resource
managers such as Pacemaker.

%package osd
Summary: Ceph Object Storage Daemon
Group: System/Base
Requires: ceph-base = %EVR
Requires: sudo
Requires: lvm2
Requires: /usr/sbin/smartctl
Requires: /usr/sbin/nvme
Requires: python3-module-ceph_volume = %EVR
%description osd
ceph-osd is the object storage daemon for the Ceph distributed file
system.  It is responsible for storing objects on a local file system
and providing access to them over the network.

%package -n librados2
Summary: RADOS distributed object store client library
Group: System/Libraries
License: LGPLv2
%description -n librados2
RADOS is a reliable, autonomic distributed object storage cluster
developed as part of the Ceph distributed storage system. This is a
shared library allowing applications to access the distributed object
store using a simple file-like interface.

%package -n librados-devel
Summary: RADOS headers
Group: Development/C
Requires: librados2 = %EVR
Provides: librados2-devel = %EVR
Obsoletes: librados2-devel < %EVR
%description -n librados-devel
This package contains libraries and headers needed to develop programs
that use RADOS object store.

%package -n python3-module-rados
Summary: Python3 libraries for the RADOS object store
Group: Development/Python3
Requires: librados2 = %EVR
Conflicts: python3-module-ceph < %EVR
%description -n python3-module-rados
This package contains Python3 libraries for interacting with Ceph RADOS
object store.

%package -n librgw2
Summary: RADOS gateway client library
Group: System/Libraries
Requires: librados2 = %EVR
%description -n librgw2
This package provides a library implementation of the RADOS gateway
(distributed object store with S3 and Swift personalities).

%package -n librgw-devel
Summary: RADOS gateway client library
Group: Development/C
License: LGPLv2
Requires: librados-devel = %EVR
Provides: librgw2-devel = %EVR
Obsoletes: librgw2-devel < %EVR
%description -n librgw-devel
This package contains libraries and headers needed to develop programs
that use RADOS gateway client library.

%package -n python3-module-rgw
Summary: Python3 libraries for the RADOS gateway
Group: Development/Python3
Requires: librgw2 = %EVR
Requires: python3-module-rados = %EVR
Conflicts: python3-module-ceph < %EVR
%description -n python3-module-rgw
This package contains Python3 libraries for interacting with Ceph RADOS
gateway.

%package -n libcephsqlite
Summary: SQLite3 VFS for Ceph
Group: System/Libraries
Requires: librados2 = %EVR
%description -n libcephsqlite
A SQLite3 VFS for storing and manipulating databases stored on Ceph's RADOS
distributed object store.

%package -n libcephsqlite-devel
Summary: SQLite3 VFS for Ceph headers
Group: Development/C
Requires: libsqlite3-devel
Requires: libcephsqlite = %EVR
Requires: librados-devel = %EVR
%description -n libcephsqlite-devel
A SQLite3 VFS for storing and manipulating databases stored on Ceph's RADOS
distributed object store.

%package -n libradosstriper1
Summary: RADOS striping interface
Group: System/Libraries
License: LGPLv2
Requires: librados2 = %EVR
%description -n libradosstriper1
Striping interface built on top of the rados library, allowing
to stripe bigger objects onto several standard rados objects using
an interface very similar to the rados one.

%package -n libradosstriper-devel
Summary: RADOS striping interface headers
Group: Development/C
Requires: libradosstriper1 = %EVR
Requires: librados-devel = %EVR
Conflicts: ceph-devel < %EVR
%description -n libradosstriper-devel
This package contains libraries and headers needed to develop programs
that use RADOS striping interface.

%package -n librbd1
Summary: RADOS block device client library
Group: System/Libraries
License: LGPLv2
Requires: librados2 = %EVR
%description -n librbd1
RBD is a block device striped across multiple distributed objects in
RADOS, a reliable, autonomic distributed object storage cluster
developed as part of the Ceph distributed storage system. This is a
shared library allowing applications to manage these block devices.

%package -n librbd-devel
Summary: RADOS block device headers
Group: Development/C
Requires: librbd1 = %EVR
Requires: librados-devel = %EVR
Conflicts: ceph-devel < %EVR
Provides: librbd1-devel = %EVR
Obsoletes: librbd1-devel < %EVR
%description -n librbd-devel
This package contains libraries and headers needed to develop programs
that use RADOS block device.

%package -n python3-module-rbd
Summary: Python3 libraries for the RADOS block device
Group: Development/Python3
Requires: librbd1 = %EVR
Requires: python3-module-rados = %EVR
Conflicts: python3-module-ceph < %EVR
%description -n python3-module-rbd
This package contains Python3 libraries for interacting with Ceph RADOS
block device.

%package -n libcephfs2
Summary: Ceph distributed file system client library
Group: System/Libraries
License: LGPLv2
%description -n libcephfs2
Ceph is a distributed network file system designed to provide excellent
performance, reliability, and scalability. This is a shared library
allowing applications to access a Ceph distributed file system via a
POSIX-like interface.

%package -n libcephfs-devel
Summary: Ceph distributed file system headers
Group: Development/C
Requires: libcephfs2 = %EVR
Requires: librados-devel = %EVR
Conflicts: ceph-devel < %EVR
Provides: libcephfs2-devel = %EVR
Obsoletes: libcephfs2-devel < %EVR
%description -n libcephfs-devel
This package contains libraries and headers needed to develop programs
that use Ceph distributed file system.

%package -n python3-module-cephfs
Summary: Python3 libraries for Ceph distributed file system
Group: Development/Python3
Requires: libcephfs2 = %EVR
Conflicts: python3-module-ceph < %EVR
%description -n python3-module-cephfs
This package contains Python3 libraries for interacting with Ceph distributed
file system.

%package -n libjaeger
Summary: Ceph distributed file system tracing library
Group: System/Libraries
%description -n libjaeger
This package contains libraries needed to provide distributed
tracing for Ceph.

%package test
Summary: Ceph benchmarks and test tools
Group: System/Libraries
Requires: ceph-common = %EVR
Requires: xmlstarlet
%description test
This package contains Ceph benchmarks and test tools.

%package -n libcephfs_jni1
Summary: Java Native Interface library for CephFS Java bindings
Group: Development/Java
Requires: java
Requires: libcephfs2 = %EVR
%description -n libcephfs_jni1
This package contains the Java Native Interface library for CephFS Java
bindings.

%package -n libcephfs_jni-devel
Summary: Development files for CephFS Java Native Interface library
Group: Development/Java
Requires: java
Requires: libcephfs_jni1 = %EVR
Conflicts: ceph-devel < %EVR
Provides: libcephfs_jni1-devel = %EVR
Obsoletes: libcephfs_jni1-devel < %EVR
%description -n libcephfs_jni-devel
This package contains the development files for CephFS Java Native Interface
library.

%package -n cephfs-java
Summary: Java libraries for the Ceph File System
Group: Development/Java
Requires: java
Requires: libcephfs_jni1 = %EVR
Requires: junit
BuildRequires: junit
%description -n cephfs-java
This package contains the Java libraries for the Ceph File System.

%package -n cephfs-shell
Summary: Interactive shell for Ceph file system
Group: Shells
Requires: python3-module-cmd2
Requires: python3-module-colorama
Requires: python3-module-cephfs
%description -n cephfs-shell
This package contains an interactive tool that allows accessing a Ceph
file system without mounting it by providing a nice pseudo-shell which
works like an FTP client.

%package devel
Summary: Ceph headers
Group: Development/C
License: LGPLv2
Requires: librados-devel = %EVR
%{?_with_libradosstriper:Requires: libradosstriper-devel = %EVR}
Requires: librbd-devel = %EVR
Requires: libcephfs-devel = %EVR
%{?_with_cephfs_java:Requires: libcephfs_jni-devel = %EVR}

%description devel
This package contains libraries and headers needed to develop programs
that use Ceph.

%package -n python3-module-ceph
Summary: Python3 libraries for the Ceph distributed filesystem
Group: Development/Python
Requires: python3-module-rados = %EVR
Requires: python3-module-rbd = %EVR
Requires: python3-module-cephfs = %EVR
Requires: python3-module-rgw = %EVR
Requires: python3-module-ceph-argparse = %EVR
Requires: python3-module-ceph-common = %EVR

%description -n python3-module-ceph
This package contains Python3 libraries for interacting with Ceph RADOS
object storage.

%package -n grafana-dashboards-ceph
Summary: The set of Grafana dashboards for monitoring purposes
Group: Monitoring
Provides: ceph-grafana-dashboards = %EVR

%description -n grafana-dashboards-ceph
This package provides a set of Grafana dashboards for monitoring of
Ceph clusters. The dashboards require a Prometheus server setup
collecting data from Ceph Manager "prometheus" module and Prometheus
project "node_exporter" module. The dashboards are designed to be
integrated with the Ceph Manager Dashboard web UI.

%package prometheus-alerts
Summary: Prometheus alerts for a Ceph deployment
BuildArch: noarch
Group: Monitoring

%description prometheus-alerts
This package provides Ceph default alerts for Prometheus.

%prep
%setup

# really? for build need "build" dir? not "BUILD"
mkdir -p build

%if_without system_boost
mkdir -p build/boost/src
install -m644 %SOURCE10 build/boost/src/
%endif

tar -xf %SOURCE11 -C ceph-erasure-code-corpus
tar -xf %SOURCE12 -C ceph-object-corpus
tar -xf %SOURCE14 -C src/blkin
tar -xf %SOURCE15 -C src/civetweb
tar -xf %SOURCE16 -C src/crypto/isa-l/isa-l_crypto
tar -xf %SOURCE18 -C src/erasure-code/jerasure/gf-complete
tar -xf %SOURCE19 -C src/erasure-code/jerasure/jerasure
tar -xf %SOURCE20 -C src/googletest
tar -xf %SOURCE21 -C src/isa-l
pushd src/isa-l
%patch100 -p1
popd
tar -xf %SOURCE23 -C src/rapidjson
%if_without system_rocksdb
tar -xf %SOURCE24 -C src/rocksdb
%endif
tar -xf %SOURCE25 -C src/spdk
%if_without system_dpdk
tar -xf %SOURCE17 -C src/spdk/dpdk
%endif
tar -xf %SOURCE26 -C src/xxHash
#tar -xf %%SOURCE27 -C src/zstd
tar -xf %SOURCE28 -C src/c-ares
tar -xf %SOURCE29 -C src/dmclock
tar -xf %SOURCE30 -C src/seastar
%if_without system_fmt
tar -xf %SOURCE31 -C src/fmt
%endif
tar -xf %SOURCE32 -C src/spawn
tar -xf %SOURCE33 -C src/pybind/mgr/rook/rook-client-python
tar -xf %SOURCE34 -C src/s3select
tar -xf %SOURCE35 -C src/jaegertracing/opentracing-cpp
tar -xf %SOURCE36 -C src/jaegertracing/jaeger-client-cpp
tar -xf %SOURCE37 -C src/jaegertracing/thrift
tar -xf %SOURCE38 -C src/libkmip

%patch -p1

cat << __EOF__ > src/.git_version
%git_version
%version
__EOF__


%build
export NPROCS=%build_parallel_jobs

%if_with cephfs_java
# Find jni.h
for i in /usr/{lib64,lib}/jvm/java/include{,/linux}; do
    [ -d $i ] && java_inc="$java_inc -I$i"
done
export CPPFLAGS="$java_inc"
%endif

%cmake \
    -GNinja \
    -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
    -DBUILD_CONFIG=rpmbuild \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir \
    -DCMAKE_INSTALL_LOCALSTATEDIR=%_localstatedir \
    -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
    -DCMAKE_INSTALL_MANDIR=%_mandir \
    -DCMAKE_INSTALL_DOCDIR=%_docdir/ceph \
    -DCMAKE_INSTALL_INCLUDEDIR=%_includedir \
    -DCMAKE_INSTALL_SYSTEMD_SERVICEDIR=%_unitdir \
    -DCMAKE_C_FLAGS:STRING='%optflags' \
    -DCMAKE_CXX_FLAGS:STRING='%optflags' \
    -DWITH_REENTRANT_STRSIGNAL=ON \
    -DWITH_THREAD_SAFE_RES_QUERY=ON \
%if_with system_boost
    -DWITH_SYSTEM_BOOST=ON \
%else
    -DBOOST_J=$NPROCS \
%endif
%if_with system_rocksdb
    -DWITH_SYSTEM_ROCKSDB=ON \
%endif
    -DWITH_SYSTEMD=ON \
    -DWITH_LZ4=ON \
%if_with python3
    -DWITH_PYTHON3=3 \
%endif
%if_without mgr_dashboard
    -DWITH_MGR_DASHBOARD_FRONTEND=OFF \
%endif
%if_without ceph_test_package
    -DWITH_TESTS=OFF \
%endif
%if_with cephfs_java
    -DWITH_CEPHFS_JAVA=ON \
%endif
%if_with selinux
    -DWITH_SELINUX=ON \
%endif
%if_with lttng
    -DWITH_LTTNG=ON \
    -DWITH_BABELTRACE=ON \
%else
    -DWITH_LTTNG=OFF \
    -DWITH_BABELTRACE=OFF \
%endif
%if_with ocf
    -DWITH_OCF=ON \
%endif
%if_with libzfs
    -DWITH_ZFS=ON \
%endif
%if_with cephfs_shell
    -DWITH_CEPHFS_SHELL=ON \
%endif
%if_with libradosstriper
    -DWITH_LIBRADOSSTRIPER=ON \
%else
    -DWITH_LIBRADOSSTRIPER=OFF \
%endif
%if_with amqp_endpoint
    -DWITH_RADOSGW_AMQP_ENDPOINT=ON \
%else
    -DWITH_RADOSGW_AMQP_ENDPOINT=OFF \
%endif
%if_with kafka_endpoint
    -DWITH_RADOSGW_KAFKA_ENDPOINT=ON \
%else
    -DWITH_RADOSGW_KAFKA_ENDPOINT=OFF \
%endif
%if_without lua_packages
    -DWITH_RADOSGW_LUA_PACKAGES=OFF \
%endif
%if_with blustore
    -DWITH_BLUESTORE=ON \
%else
    -DWITH_BLUESTORE=OFF \
%endif
%if_with zbd
    -DWITH_ZBD=ON \
%endif
%if_with liburing
    -DWITH_LIBURING=ON -DWITH_SYSTEM_LIBURING=ON \
%else
    -DWITH_LIBURING=OFF \
%endif
%if_with pmem
    -DWITH_BLUESTORE_PMEM=ON -DWITH_SYSTEM_PMDK=ON \
%if_with rbd_rwl_cache
    -DWITH_RBD_RWL=ON \
%endif
%endif
%if_with rbd_ssd_cache
    -DWITH_RBD_SSD_CACHE=ON \
%endif
%if_with jaeger
    -DWITH_JAEGER=ON \
%else
    -DWITH_JAEGER=OFF \
%endif
%if_with dpdk
    -DWITH_DPDK=ON \
%else
    -DWITH_DPDK=OFF \
%endif
%if_with spdk
    -DWITH_SPDK=ON \
%else
    -DWITH_SPDK=OFF \
%endif
%ifarch %arm
    -DWITH_RDMA=OFF \
%endif
%if_with grafana
    -DWITH_GRAFANA=ON \
%endif
    -DWITH_MANPAGE=ON

export VERBOSE=1
export V=1
export GCC_COLORS=
%cmake_build

%install
%cmake_install

# ??? 16.2.9 not install cephfs-shell
%if_with cephfs_shell
if [ ! -x %buildroot%_bindir/cephfs-shell ]; then
    install -m 0755 src/tools/cephfs/cephfs-shell %buildroot%_bindir/cephfs-shell
fi
%endif

mkdir -p %buildroot{%_unitdir,%_sbindir}
find %buildroot -type f -name "*.la" -exec rm -f {} ';'
find %buildroot -type f -name "*.a" -exec rm -f {} ';'
install -m 0644 -D src/etc-rbdmap %buildroot%_sysconfdir/ceph/rbdmap
install -m 0644 -D etc/sysconfig/ceph %buildroot%_sysconfdir/sysconfig/ceph
install -m 0644 -D etc/sysctl/90-ceph-osd.conf %buildroot%_sysctldir/90-ceph-osd.conf
install -m 0644 -D systemd/ceph.tmpfiles.d %buildroot%_tmpfilesdir/ceph-common.conf
install -m 0644 -D systemd/50-ceph.preset %buildroot%_presetdir/50-ceph.preset
install -m 0644 -D src/logrotate.conf %buildroot%_logrotatedir/ceph
install -m 0755 -D src/tools/rbd_nbd/rbd-nbd_quiesce %buildroot%_libexecdir/rbd-nbd/rbd-nbd_quiesce

rm -f %buildroot/etc/init.d/ceph

%if_with seastar
# package crimson-osd with the name of ceph-osd
install -m 0755 %buildroot%_bindir/crimson-osd %buildroot%_bindir/ceph-osd
%endif

mkdir -p %buildroot/sbin
mv %buildroot%_sbindir/mount.ceph %buildroot/sbin/mount.ceph

# udev rules
install -m 0644 -D udev/50-rbd.rules %buildroot%_udevrulesdir/50-rbd.rules

# cephadm
install -m 0755 src/cephadm/cephadm %buildroot%_sbindir/cephadm
mkdir -p %buildroot%_localstatedir/cephadm/.ssh
touch %buildroot%_localstatedir/cephadm/.ssh/authorized_keys

# sudoers.d
install -m 0400 -D sudoers.d/ceph-smartctl %buildroot%_sysconfdir/sudoers.d/ceph-smartctl

# prometheus alerts
install -m 644 -D monitoring/ceph-mixin/prometheus_alerts.yml %buildroot%_sysconfdir/prometheus/ceph/ceph_default_alerts.yml

#set up placeholder directories
mkdir -p %buildroot%_sysconfdir/ceph
mkdir -p %buildroot%_runtimedir/ceph
mkdir -p %buildroot%_logdir/ceph
mkdir -p %buildroot%_logdir/radosgw
mkdir -p %buildroot%_localstatedir/ceph/tmp
mkdir -p %buildroot%_localstatedir/ceph/mon
mkdir -p %buildroot%_localstatedir/ceph/osd
mkdir -p %buildroot%_localstatedir/ceph/mds
mkdir -p %buildroot%_localstatedir/ceph/mgr
mkdir -p %buildroot%_localstatedir/ceph/crash
mkdir -p %buildroot%_localstatedir/ceph/crash/posted
mkdir -p %buildroot%_localstatedir/ceph/radosgw
mkdir -p %buildroot%_localstatedir/ceph/bootstrap-osd
mkdir -p %buildroot%_localstatedir/ceph/bootstrap-mds
mkdir -p %buildroot%_localstatedir/ceph/bootstrap-mgr
mkdir -p %buildroot%_localstatedir/ceph/bootstrap-rgw
mkdir -p %buildroot%_localstatedir/ceph/bootstrap-rbd
mkdir -p %buildroot%_localstatedir/ceph/bootstrap-rbd-mirror


# cleanup
rm -rf %buildroot%_docdir/ceph

rm -rf %buildroot%_datadir/ceph/mgr/hello

rm -rf %buildroot%_datadir/ceph/mgr/test_orchestrator
rm -rf %buildroot%_datadir/ceph/mgr/dashboard/tests
rm -f %buildroot%_datadir/ceph/mgr/dashboard/tox.ini
rm -f %buildroot%_datadir/ceph/mgr/dashboard/*.sh
rm -f %buildroot%_datadir/ceph/mgr/insights/{run-tox.sh,tox.ini}
rm -rf %buildroot%_datadir/ceph/mgr/insights/tests
rm -rf %buildroot%_datadir/ceph/mgr/pg_autoscaler/tests
rm -rf %buildroot%_datadir/ceph/mgr/orchestrator/tests
rm -rf %buildroot%_datadir/ceph/mgr/progress/test_progress.py
rm -rf %buildroot%_datadir/ceph/mgr/progress/__pycache__/test_progress.cpython-*
rm -rf %buildroot%python3_sitelibdir_noarch/cephfs_shell-*.egg-info
rm -rf %buildroot%_datadir/ceph/mgr/dashboard/ci

%check
# run in-tree unittests
cd build
ctest %{?_smp_mflags}

%pre common
CEPH_GROUP_ID=167
CEPH_USER_ID=167
groupadd -r -f -g $CEPH_GROUP_ID ceph 2>/dev/null ||:
useradd -r -g ceph -u $CEPH_USER_ID -s /sbin/nologin -c "Ceph daemons" -d %_localstatedir/ceph ceph 2>/dev/null ||:

%post common
%tmpfiles_create %_tmpfilesdir/ceph-common.conf
%post_systemd_postponed rbdmap

%preun common
%systemd_preun rbdmap

%post base
# Allow execute smartctl for ceph user with sudo
control sudo public 2>/dev/null ||:
%systemd_post ceph.target ceph-crash.service
if [ $1 -eq 1 ] ; then
systemctl start ceph.target ceph-crash.service >/dev/null 2>&1 || :
fi

%preun base
%systemd_preun ceph.target ceph-crash.service

%post mds
%systemd_post ceph-mds.target
if [ $1 -eq 1 ] ; then
  systemctl start ceph-mds.target >/dev/null 2>&1 || :
fi

if [ $1 -eq 2 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%_sysconfdir/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    systemctl try-restart ceph-mds@\*.service > /dev/null 2>&1 || :
  fi
fi

%preun mds
%systemd_preun ceph-mds.target

%post mon
%systemd_post ceph-mon.target
if [ $1 -eq 1 ] ; then
  systemctl start ceph-mon.target >/dev/null 2>&1 || :
fi

if [ $1 -ge 2 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%_sysconfdir/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    systemctl try-restart ceph-mon@\*.service > /dev/null 2>&1 || :
  fi
fi

%preun mon
%systemd_preun ceph-mon.target

%post osd
%sysctl_apply 90-ceph-osd.conf
%systemd_post ceph-osd.target
if [ $1 -eq 1 ] ; then
  systemctl start ceph-osd.target >/dev/null 2>&1 || :
fi

if [ $1 -ge 2 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%_sysconfdir/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    systemctl try-restart ceph-osd@\*.service ceph-volume@\*.service > /dev/null 2>&1 || :
  fi
fi

%preun osd
%systemd_preun ceph-osd.target

%post mgr
%systemd_post ceph-mgr.target
if [ $1 -eq 1 ] ; then
  systemctl start ceph-mgr.target >/dev/null 2>&1 || :
fi

if [ $1 -ge 2 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%_sysconfdir/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    systemctl try-restart ceph-mgr@\*.service > /dev/null 2>&1 || :
  fi
fi

%preun mgr
%systemd_preun ceph-mgr.target

%post mgr-dashboard
if [ $1 -eq 1 ] ; then
    systemctl try-restart ceph-mgr.target >/dev/null 2>&1 || :
fi

%postun mgr-dashboard
if [ $1 -eq 1 ] ; then
    systemctl try-restart ceph-mgr.target >/dev/null 2>&1 || :
fi

%post mgr-diskprediction-local
if [ $1 -eq 1 ] ; then
    systemctl try-restart ceph-mgr.target >/dev/null 2>&1 || :
fi

%postun mgr-diskprediction-local
if [ $1 -eq 1 ] ; then
    systemctl try-restart ceph-mgr.target >/dev/null 2>&1 || :
fi

%post mgr-rook
if [ $1 -eq 1 ] ; then
    systemctl try-restart ceph-mgr.target >/dev/null 2>&1 || :
fi

%postun mgr-rook
if [ $1 -eq 1 ] ; then
    systemctl try-restart ceph-mgr.target >/dev/null 2>&1 || :
fi

%post mgr-k8sevents
if [ $1 -eq 1 ] ; then
    systemctl try-restart ceph-mgr.target >/dev/null 2>&1 || :
fi

%postun mgr-k8sevents
if [ $1 -eq 1 ] ; then
    systemctl try-restart ceph-mgr.target >/dev/null 2>&1 || :
fi

%post mgr-cephadm
if [ $1 -eq 1 ] ; then
    systemctl try-restart ceph-mgr.target >/dev/null 2>&1 || :
fi

%postun mgr-cephadm
if [ $1 -eq 1 ] ; then
    systemctl try-restart ceph-mgr.target >/dev/null 2>&1 || :
fi

%post -n cephfs-mirror
%systemd_post cephfs-mirror.target
if [ $1 -eq 1 ] ; then
  systemctl start cephfs-mirror.target >/dev/null 2>&1 || :
fi

if [ $1 -ge 2 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%_sysconfdir/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    systemctl try-restart cephfs-mirror@\*.service > /dev/null 2>&1 || :
  fi
fi

%preun -n cephfs-mirror
%systemd_preun cephfs-mirror.target

%post -n rbd-mirror
%systemd_post ceph-rbd-mirror.target
if [ $1 -eq 1 ] ; then
  systemctl start ceph-rbd-mirror.target >/dev/null 2>&1 || :
fi

if [ $1 -ge 2 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%_sysconfdir/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    systemctl try-restart ceph-rbd-mirror@\*.service > /dev/null 2>&1 || :
  fi
fi

%preun -n rbd-mirror
%systemd_preun ceph-rbd-mirror.target

%post radosgw
%systemd_post ceph-radosgw.target
if [ $1 -eq 1 ] ; then
  systemctl start ceph-radosgw.target >/dev/null 2>&1 || :
fi

if [ $1 -ge 2 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%_sysconfdir/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    systemctl try-restart ceph-radosgw@\*.service > /dev/null 2>&1 || :
  fi
fi

%preun radosgw
%systemd_preun ceph-radosgw.target

%post immutable-object-cache
%systemd_post ceph-immutable-object-cache.target
if [ $1 -eq 1 ] ; then
  systemctl start ceph-immutable-object-cache.target >/dev/null 2>&1 || :
fi

if [ $1 -ge 2 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%_sysconfdir/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    systemctl try-restart ceph-immutable-object-cache@\*.service > /dev/null 2>&1 || :
  fi
fi

%preun immutable-object-cache
%systemd_preun ceph-immutable-object-cache.target

%pre -n cephadm
groupadd -r -f cephadm 2>/dev/null ||:
useradd -r -g cephadm -s /bin/bash "cephadm user for mgr/cephadm" -d %_localstatedir/cephadm cephadm 2>/dev/null ||:


%files

%files base
%_bindir/ceph-crash
%_bindir/crushtool
%_bindir/monmaptool
%_bindir/osdmaptool
%_bindir/ceph-kvstore-tool
%_bindir/ceph-run
%_presetdir/50-ceph.preset
%_sbindir/ceph-create-keys
%dir %_libexecdir/ceph
%_libexecdir/ceph/ceph_common.sh
%dir %_libdir/rados-classes
%_libdir/rados-classes/*
%dir %_libdir/ceph
%dir %_libdir/ceph/erasure-code
%_libdir/ceph/erasure-code/libec_*.so*
%dir %_libdir/ceph/compressor
%_libdir/ceph/compressor/libceph_*.so*
%_unitdir/ceph-crash.service
%dir %_libdir/ceph/crypto
%_libdir/ceph/crypto/libceph_*.so*
%if_with lttng
%_libdir/libos_tp.so*
%_libdir/libosd_tp.so*
%endif
%config(noreplace) %_logrotatedir/ceph
%config(noreplace) %_sysconfdir/sysconfig/ceph
%_unitdir/ceph.target
%_mandir/man8/ceph-deploy.8*
%_mandir/man8/ceph-create-keys.8*
%_mandir/man8/ceph-run.8*
%_mandir/man8/crushtool.8*
%_mandir/man8/osdmaptool.8*
%_mandir/man8/monmaptool.8*
%_mandir/man8/ceph-kvstore-tool.8*
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/crash
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/crash/posted
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/tmp
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/bootstrap-osd
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/bootstrap-mds
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/bootstrap-rgw
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/bootstrap-mgr
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/bootstrap-rbd
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/bootstrap-rbd-mirror
%config(noreplace) %_sysconfdir/sudoers.d/ceph-smartctl

%files common
%doc AUTHORS COPYING README.md doc src/doc src/sample.ceph.conf
%_bindir/ceph
%_bindir/ceph-authtool
%_bindir/ceph-conf
%_bindir/ceph-dencoder
%_bindir/ceph-rbdnamer
%_bindir/ceph-syn
%_bindir/cephfs-data-scan
%_bindir/cephfs-journal-tool
%_bindir/cephfs-table-tool
%_bindir/rados
%_bindir/radosgw-admin
%_bindir/rbd
%_bindir/rbd-replay
%_bindir/rbd-replay-many
%_bindir/rbdmap
/sbin/mount.ceph
%if_with lttng
%_bindir/rbd-replay-prep
%endif
%_bindir/ceph-post-file
%dir %_libdir/ceph/denc
%_libdir/ceph/denc/denc-mod-*.so
%_tmpfilesdir/ceph-common.conf
%_mandir/man8/ceph-authtool.8*
%_mandir/man8/ceph-conf.8*
%_mandir/man8/ceph-dencoder.8*
%_mandir/man8/ceph-rbdnamer.8*
%_mandir/man8/ceph-syn.8*
%_mandir/man8/ceph-post-file.8*
%_mandir/man8/ceph.8*
%_mandir/man8/mount.ceph.8*
%_mandir/man8/rados.8*
%_mandir/man8/radosgw-admin.8*
%_mandir/man8/rbd.8*
%_mandir/man8/rbdmap.8*
%_mandir/man8/rbd-replay.8*
%_mandir/man8/rbd-replay-many.8*
%_mandir/man8/rbd-replay-prep.8*
%dir %_datadir/ceph
%_datadir/ceph/known_hosts_drop.ceph.com
%_datadir/ceph/id_rsa_drop.ceph.com
%_datadir/ceph/id_rsa_drop.ceph.com.pub
%dir %_sysconfdir/ceph
%config %_sysconfdir/bash_completion.d/ceph
%config %_sysconfdir/bash_completion.d/rados
%config %_sysconfdir/bash_completion.d/radosgw-admin
%config %_sysconfdir/bash_completion.d/rbd
%config(noreplace) %_sysconfdir/ceph/rbdmap
%_unitdir/rbdmap.service
%_udevrulesdir/50-rbd.rules

%attr(3770,root,ceph) %dir %_logdir/ceph
%attr(0750,ceph,ceph) %dir %_localstatedir/ceph

%files -n cephadm
%_sbindir/cephadm
%_man8dir/cephadm.8*
%attr(0700,cephadm,cephadm) %dir %_localstatedir/cephadm
%attr(0700,cephadm,cephadm) %dir %_localstatedir/cephadm/.ssh
%config(noreplace) %attr(0600,cephadm,cephadm) %_localstatedir/cephadm/.ssh/authorized_keys

%files mds
%_bindir/ceph-mds
%_mandir/man8/ceph-mds.8*
%_unitdir/ceph-mds@.service
%_unitdir/ceph-mds.target
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/mds

%files mon
%_bindir/ceph-mon
%_bindir/ceph-monstore-tool
%_mandir/man8/ceph-mon.8*
%_unitdir/ceph-mon@.service
%_unitdir/ceph-mon.target
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/mon

%files mgr
%_bindir/ceph-mgr
%_datadir/ceph/mgr/__pycache__
%_datadir/ceph/mgr/mgr_module.*
%_datadir/ceph/mgr/mgr_util.*
%_unitdir/ceph-mgr@.service
%_unitdir/ceph-mgr.target
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/mgr

%files mgr-modules-core
%dir %_datadir/ceph/mgr
%_datadir/ceph/mgr/alerts
%_datadir/ceph/mgr/balancer
%_datadir/ceph/mgr/crash
%_datadir/ceph/mgr/devicehealth
%_datadir/ceph/mgr/iostat
%_datadir/ceph/mgr/localpool
%_datadir/ceph/mgr/mds_autoscaler
%_datadir/ceph/mgr/mirroring
%_datadir/ceph/mgr/nfs
%_datadir/ceph/mgr/orchestrator
%_datadir/ceph/mgr/osd_perf_query
%_datadir/ceph/mgr/osd_support
%_datadir/ceph/mgr/pg_autoscaler
%_datadir/ceph/mgr/progress
%_datadir/ceph/mgr/rbd_support
%_datadir/ceph/mgr/selftest
%_datadir/ceph/mgr/snap_schedule
%_datadir/ceph/mgr/stats
%_datadir/ceph/mgr/status
%_datadir/ceph/mgr/telemetry
%_datadir/ceph/mgr/volumes

%files mgr-dashboard
%_datadir/ceph/mgr/dashboard

%files mgr-diskprediction-local
%_datadir/ceph/mgr/diskprediction_local

%files mgr-influx
%_datadir/ceph/mgr/influx

%files mgr-insights
%_datadir/ceph/mgr/insights

%files mgr-prometheus
%_datadir/ceph/mgr/prometheus

%files mgr-restful
%_datadir/ceph/mgr/restful

%files mgr-rook
%_datadir/ceph/mgr/rook

%files mgr-k8sevents
%_datadir/ceph/mgr/k8sevents

%files mgr-cephadm
%_datadir/ceph/mgr/cephadm

%files mgr-telegraf
%_datadir/ceph/mgr/telegraf

%files mgr-zabbix
%_datadir/ceph/mgr/zabbix

%files fuse
%_bindir/ceph-fuse
%_sbindir/mount.fuse.ceph
%_mandir/man8/ceph-fuse.8*
%_mandir/man8/mount.fuse.ceph.8*
%_unitdir/ceph-fuse@.service
%_unitdir/ceph-fuse.target

%files -n cephfs-mirror
%_bindir/cephfs-mirror
%_mandir/man8/cephfs-mirror.8*
%_unitdir/cephfs-mirror@.service
%_unitdir/cephfs-mirror.target

%files -n rbd-fuse
%_bindir/rbd-fuse
%_mandir/man8/rbd-fuse.8*

%files -n rbd-mirror
%_bindir/rbd-mirror
%_mandir/man8/rbd-mirror.8*
%_unitdir/ceph-rbd-mirror@.service
%_unitdir/ceph-rbd-mirror.target

%files -n rbd-nbd
%_bindir/rbd-nbd
%_mandir/man8/rbd-nbd.8*
%dir %_libexecdir/rbd-nbd
%_libexecdir/rbd-nbd/rbd-nbd_quiesce

%files radosgw
%_bindir/ceph-diff-sorted
%_bindir/radosgw
%_bindir/radosgw-es
%_bindir/radosgw-token
%_bindir/radosgw-object-expirer
%_bindir/rgw-gap-list
%_bindir/rgw-gap-list-comparator
%_bindir/rgw-orphan-list
%_mandir/man8/ceph-diff-sorted.8*
%_mandir/man8/radosgw.8*
%_mandir/man8/rgw-orphan-list.8*
%_logdir/radosgw
%dir %_localstatedir/ceph/radosgw
%_unitdir/ceph-radosgw@.service
%_unitdir/ceph-radosgw.target

%files immutable-object-cache
%_bindir/ceph-immutable-object-cache
%_man8dir/ceph-immutable-object-cache.8*
%_unitdir/ceph-immutable-object-cache@.service
%_unitdir/ceph-immutable-object-cache.target

%files osd
%_bindir/ceph-clsinfo
%_bindir/ceph-bluestore-tool
%_bindir/ceph-erasure-code-tool
%_bindir/ceph-objectstore-tool
%_bindir/ceph-osdomap-tool
%_bindir/ceph-osd
%_sbindir/ceph-volume
%_sbindir/ceph-volume-systemd
%_libexecdir/ceph/ceph-osd-prestart.sh
%_mandir/man8/ceph-clsinfo.8*
%_mandir/man8/ceph-osd.8*
%_mandir/man8/ceph-bluestore-tool.8*
%_mandir/man8/ceph-volume.8*
%_mandir/man8/ceph-volume-systemd.8*
%_unitdir/ceph-osd@.service
%_unitdir/ceph-osd.target
%_unitdir/ceph-volume@.service
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/osd
%_sysctldir/90-ceph-osd.conf

%if_with ocf
%files resource-agents
%_prefix/lib/ocf/resource.d/%name
%endif

%files -n librados2
%dir %_sysconfdir/ceph
%_libdir/librados.so.*
%dir %_libdir/ceph
%_libdir/ceph/libceph-common.so.*
%if_with lttng
%_libdir/librados_tp.so.*
%endif

%files -n librados-devel
%dir %_includedir/rados
%_includedir/rados/librados.h
%_includedir/rados/librados.hpp
%_includedir/rados/librados_fwd.hpp
%_includedir/rados/buffer.h
%_includedir/rados/buffer_fwd.h
%_includedir/rados/inline_memory.h
%_includedir/rados/objclass.h
%_includedir/rados/page.h
%_includedir/rados/crc32c.h
%_includedir/rados/rados_types.h
%_includedir/rados/rados_types.hpp
%_libdir/librados.so
%if_with lttng
%_libdir/librados_tp.so
%endif
%_bindir/librados-config
%_mandir/man8/librados-config.8*

%files -n libcephsqlite
%_libdir/libcephsqlite.so

%files -n libcephsqlite-devel
%_includedir/libcephsqlite.h

%if_with libradosstriper
%files -n libradosstriper1
%_libdir/libradosstriper.so.*

%files -n libradosstriper-devel
%dir %_includedir/radosstriper
%_includedir/radosstriper/*
%_libdir/libradosstriper.so
%endif

%files -n librbd1
%_libdir/librbd.so.*
%_libdir/ceph/librbd
%if_with lttng
%_libdir/librbd_tp.so.*
%endif

%files -n librbd-devel
%dir %_includedir/rbd
%_includedir/rbd/*
%_libdir/librbd.so
%if_with lttng
%_libdir/librbd_tp.so
%endif

%files -n librgw2
%_libdir/libradosgw.so.*
%_libdir/librgw.so.*
%if_with lttng
%_libdir/librgw_op_tp.so.*
%_libdir/librgw_rados_tp.so.*
%endif

%files -n librgw-devel
%_includedir/rados/librgw.h
%_includedir/rados/rgw_file.h
%_libdir/libradosgw.so
%_libdir/librgw.so
%if_with lttng
%_libdir/librgw_op_tp.so
%_libdir/librgw_rados_tp.so
%endif

%files -n libcephfs2
%dir %_sysconfdir/ceph
%_libdir/libcephfs.so.*

%files -n libcephfs-devel
%dir %_includedir/cephfs
%_includedir/cephfs/*
%_libdir/libcephfs.so

%files -n cephfs-top
# temporary exclude
%exclude %python3_sitelibdir_noarch/cephfs_top-*.egg-info
%_bindir/cephfs-top
%_mandir/man8/cephfs-top.8*

%if_with jaeger
%files -n libjaeger
%_libdir/libopentracing.so.*
%_libdir/libthrift.so.*
%_libdir/libjaegertracing.so.*
%endif

%if_with ceph_test_package
%files test
%_bindir/ceph_bench_log
%_bindir/ceph-client-debug
%_bindir/ceph_kvstorebench
%_bindir/ceph_multi_stress_watch
%_bindir/ceph_erasure_code_benchmark
%_bindir/ceph_omapbench
%_bindir/ceph_objectstore_bench
%_bindir/ceph_perf_objectstore
%_bindir/ceph_perf_local
%_bindir/ceph_perf_msgr_client
%_bindir/ceph_perf_msgr_server
%_bindir/ceph_psim
%_bindir/ceph_radosacl
%_bindir/ceph_rgw_jsonparser
%_bindir/ceph_rgw_multiparser
%_bindir/ceph_scratchtool
%_bindir/ceph_scratchtoolpp
%_bindir/ceph_smalliobench
%_bindir/ceph_smalliobenchdumb
%_bindir/ceph_smalliobenchfs
%_bindir/ceph_smalliobenchrbd
%_bindir/ceph_test_*
%_bindir/ceph_tpbench
%_bindir/ceph_xattr_bench
%_bindir/ceph-coverage
%_bindir/ceph-debugpack
%_bindir/ceph-dedup-tool
%if_with seastar
%_bindir/crimson-store-nbd
%endif
#_bindir/dmclock-tests
#_bindir/dmclock-data-struct-tests
%_mandir/man8/ceph-debugpack.8*
%_libdir/ceph/ceph-monstore-update-crush.sh
%endif


%if_with cephfs_java
%files -n libcephfs_jni1
%_libdir/libcephfs_jni.so.*

%files -n libcephfs_jni-devel
%_libdir/libcephfs_jni.so

%files -n cephfs-java
%_javadir/libcephfs.jar
%_javadir/libcephfs-test.jar
%endif

%if_with grafana
%files -n grafana-dashboards-ceph
%dir %_sysconfdir/grafana/dashboards/ceph-dashboard
%config(noreplace) %_sysconfdir/grafana/dashboards/ceph-dashboard/*
%endif

%files prometheus-alerts
%dir %_sysconfdir/prometheus/ceph
%config(noreplace) %_sysconfdir/prometheus/ceph/ceph_default_alerts.yml

%files devel

%if_with python3

%files -n python3-module-ceph

%files -n python3-module-ceph-common
%python3_sitelibdir_noarch/ceph
%python3_sitelibdir_noarch/ceph-*.egg-info

%files -n python3-module-ceph_volume
%python3_sitelibdir_noarch/ceph_volume
%python3_sitelibdir_noarch/ceph_volume-*.egg-info

%files -n python3-module-ceph-argparse
%python3_sitelibdir_noarch/ceph_argparse.py
%python3_sitelibdir_noarch/__pycache__/ceph_argparse.cpython*.py*
%python3_sitelibdir_noarch/ceph_daemon.py
%python3_sitelibdir_noarch/__pycache__/ceph_daemon.cpython*.py*

%files -n python3-module-rados
%python3_sitelibdir/rados.cpython*.so
%python3_sitelibdir/rados-*.egg-info

%files -n python3-module-rbd
%python3_sitelibdir/rbd.cpython*.so
%python3_sitelibdir/rbd-*.egg-info

%files -n python3-module-rgw
%python3_sitelibdir/rgw.cpython*.so
%python3_sitelibdir/rgw-*.egg-info

%files -n python3-module-cephfs
%python3_sitelibdir/cephfs.cpython*.so
%python3_sitelibdir/cephfs-*.egg-info
%python3_sitelibdir_noarch/ceph_volume_client.py*
%python3_sitelibdir_noarch/__pycache__/ceph_volume_client.cpython*.py*

%if_with cephfs_shell
%files -n cephfs-shell
%_bindir/cephfs-shell
%endif

%endif

%changelog
* Fri Mar 03 2023 Alexey Shabalin <shaba@altlinux.org> 16.2.11-alt1
- 16.2.11.
- enable lto.

* Tue Jul 26 2022 Alexey Shabalin <shaba@altlinux.org> 16.2.10-alt2
- 16.2.10 (Fixes: CVE-2022-0670).
- build with bundled fmtlib.

* Sun Jul 03 2022 Alexey Shabalin <shaba@altlinux.org> 16.2.9-alt2
- set version without prefix "v".

* Wed Jun 29 2022 Alexey Shabalin <shaba@altlinux.org> 16.2.9-alt1
- 16.2.9
- use CEPH_AUTO_RESTART_ON_UPGRADE from /etc/sysconfig/ceph for update in %%post scripts

* Tue Dec 21 2021 Alexey Shabalin <shaba@altlinux.org> 16.2.7-alt1
- 16.2.7

* Thu Oct 07 2021 Alexey Shabalin <shaba@altlinux.org> 16.2.6-alt1
- 16.2.6
- Update post and preun scripts for use macros from rpm-macros-systemd.

* Fri May 28 2021 Alexey Shabalin <shaba@altlinux.org> 15.2.13-alt1
- 15.2.13

* Sat May 15 2021 Alexey Shabalin <shaba@altlinux.org> 15.2.12-alt1
- 15.2.12 (Fixes: CVE-2021-3531, CVE-2021-3524, CVE-2021-3509)

* Tue Apr 20 2021 Alexey Shabalin <shaba@altlinux.org> 15.2.11-alt1
- 15.2.11 (Fixes: CVE-2021-20288).

* Fri Mar 19 2021 Alexey Shabalin <shaba@altlinux.org> 15.2.10-alt1
- 15.2.10
- Build with tcmalloc

* Thu Mar 11 2021 Stanislav Levin <slev@altlinux.org> 15.2.9-alt2
- Dropped dependency on python3(tests).

* Thu Feb 25 2021 Alexey Shabalin <shaba@altlinux.org> 15.2.9-alt1
- 15.2.9

* Thu Dec 24 2020 Alexey Shabalin <shaba@altlinux.org> 15.2.8-alt1
- 15.2.8
- Fixes for the following security vulnerabilities:
  + CVE-2020-27781 OpenStack Manila use of ceph_volume_client.py library
    allowed tenant access to any Ceph credential's secret.

* Fri Dec 04 2020 Alexey Shabalin <shaba@altlinux.org> 15.2.7-alt1
- 15.2.7

* Thu Nov 19 2020 Alexey Shabalin <shaba@altlinux.org> 15.2.6-alt1
- 15.2.6
- Fixes for the following security vulnerabilities:
  + CVE-2020-25660 Fix a regression in Messenger V2 replay attacks

* Thu Sep 17 2020 Alexey Shabalin <shaba@altlinux.org> 15.2.5-alt1
- 15.2.5
- drop python2 support
- build with -DWITH_REENTRANT_STRSIGNAL=ON
- build with -DWITH_THREAD_SAFE_RES_QUERY=ON
- add ceoh-cephadm and ceph-mgr-cephadm packages
- add ceph-immutable-object-cache package
- add ceph-prometheus-alerts with alert config for prometheus
- drop ceph-ssh, ceph-mgr-ansible, ceph-mgr-deepsea packages
- move basic mgr modules from ceph-mgr to ceph-mgr-modules-core
- add python3-module-ceph-common package

* Thu Aug 13 2020 Alexey Shabalin <shaba@altlinux.org> 14.2.11-alt1
- 14.2.11

* Sun Jun 28 2020 Alexey Shabalin <shaba@altlinux.org> 14.2.10-alt1
- 14.2.10
- Fixes for the following security vulnerabilities:
  + CVE-2020-10753 HTTP header injection via CORS ExposeHeader tag

* Wed Apr 15 2020 Alexey Shabalin <shaba@altlinux.org> 14.2.9-alt1
- 14.2.9
- Fixes for the following security vulnerabilities:
  + CVE-2020-1759 Fixed nonce reuse in msgr V2 secure mode
  + CVE-2020-1760 Fixed XSS due to RGW GetObject header-splitting

* Tue Mar 10 2020 Alexey Shabalin <shaba@altlinux.org> 14.2.8-alt1
- 14.2.8

* Wed Feb 19 2020 Alexey Shabalin <shaba@altlinux.org> 14.2.7-alt1
- 14.2.7 (Fixes: CVE-2020-1699, CVE-2020-1700)

* Wed Jan 22 2020 Alexey Shabalin <shaba@altlinux.org> 14.2.6-alt2
- do not enable mgr restful module after installation

* Wed Jan 15 2020 Alexey Shabalin <shaba@altlinux.org> 14.2.6-alt1
- 14.2.6

* Thu Dec 12 2019 Alexey Shabalin <shaba@altlinux.org> 14.2.5-alt1
- 14.2.5
- This release fixes a critical BlueStore bug introduced in 14.2.3
  (and also present in 14.2.4) that can lead to data corruption
  when a separate WAL device is used.

* Mon Oct 07 2019 Alexey Shabalin <shaba@altlinux.org> 14.2.4-alt1
- 14.2.4 (Fixes: CVE-2019-10222)

* Thu Jul 18 2019 Alexey Shabalin <shaba@altlinux.org> 14.2.2-alt1
- 14.2.2

* Wed Jul 10 2019 Alexey Shabalin <shaba@altlinux.org> 14.2.1-alt3
- drop SysV support

* Thu Jul 04 2019 Alexey Shabalin <shaba@altlinux.org> 14.2.1-alt2
- compat with zstd >= v1.4.0

* Wed May 08 2019 Alexey Shabalin <shaba@altlinux.org> 14.2.1-alt1
- 14.2.1

* Tue Mar 26 2019 Alexey Shabalin <shaba@altlinux.org> 14.2.0-alt2
- build with system zstd (fixed ALT#36406)
- build with system rocksdb

* Wed Mar 20 2019 Alexey Shabalin <shaba@altlinux.org> 14.2.0-alt1
- 14.2.0

* Sun Mar 17 2019 Alexey Shabalin <shaba@altlinux.org> 14.1.1-alt1
- 14.1.1

* Tue Feb 19 2019 Alexey Shabalin <shaba@altlinux.org> 13.2.4-alt1
- 13.2.4
- disable build for 32-bit arch
- build with python3 and without python2
- disable build mgr dashboard
- split ceph-mgr package
- build with spdk and dpdk support
- Fixes for the following security vulnerabilities:
  + CVE-2018-16846: rgw: enforce bounds on max-keys/max-uploads/max-parts
  + CVE-2018-14662: mon: limit caps allowed to access the config store

* Wed Jan 09 2019 Anton Farygin <rider@altlinux.ru> 12.2.10-alt1
- 12.2.10 (closes: #35798)

* Fri Oct 26 2018 Alexey Shabalin <shaba@altlinux.org> 12.2.9-alt1
- 12.2.9

* Sat Sep 08 2018 Alexey Shabalin <shaba@altlinux.org> 12.2.8-alt1
- 12.2.8
- fixed uninstall ceph-common (%%preun_service rbdmap)
- Fixes for the following security vulnerabilities:
  + CVE-2018-1128 auth: cephx authorizer subject to replay attack
  + CVE-2018-1129 auth: cephx signature check is weak
  + CVE-2018-10861 mon: auth checks not correct for pool ops

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 12.2.5-alt2
- NMU: rebuilt with boost-1.67.0

* Sat Apr 28 2018 Alexey Shabalin <shaba@altlinux.ru> 12.2.5-alt1
- 12.2.5
- build with rdma support

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 12.2.4-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Mar 05 2018 Alexey Shabalin <shaba@altlinux.ru> 12.2.4-alt1
- 12.2.4

* Tue Feb 27 2018 Alexey Shabalin <shaba@altlinux.ru> 12.2.3-alt1
- 12.2.3
- backport patches from luminous branch

* Thu Dec 07 2017 Alexey Shabalin <shaba@altlinux.ru> 12.2.2-alt1
- 12.2.2

* Tue Oct 03 2017 Alexey Shabalin <shaba@altlinux.ru> 12.2.1-alt2
- backport influx plugin for mgr from upstream master
- update requires for fix run mgr
- move mount.ceph to /sbin

* Wed Sep 27 2017 Alexey Shabalin <shaba@altlinux.ru> 12.2.1-alt1
- 12.2.1

* Mon Sep 11 2017 Alexey Shabalin <shaba@altlinux.ru> 12.2.0-alt1
- 12.2.0

* Tue Jul 11 2017 Alexey Shabalin <shaba@altlinux.ru> 10.2.8-alt1
- 10.2.8

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 10.2.7-alt1
- 10.2.7
- split packages osd,mds,mon

* Fri Apr 28 2017 Alexei Takaseev <taf@altlinux.org> 0.94.10-alt1
- 0.94.10

* Wed Apr 26 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.94.9-alt3
- Fixed build with gcc >= 6.

* Mon Sep 26 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.94.9-alt2
- fixed ceph --version
- packed udev rules

* Wed Aug 31 2016 Alexei Takaseev <taf@altlinux.org> 0.94.9-alt1
- 0.94.9

* Sat Aug 27 2016 Alexei Takaseev <taf@altlinux.org> 0.94.8-alt1
- 0.94.8

* Mon Jul 25 2016 Lenar Shakirov <snejok@altlinux.ru> 0.94.7-alt4
- Requires: gdisk added, sgdisk needed by ceph-disk (ALT bug #32132)

* Mon Jun 20 2016 Lenar Shakirov <snejok@altlinux.ru> 0.94.7-alt3
- Provides: ceph-mds added, needed by ceph-deploy

* Mon Jun 20 2016 Lenar Shakirov <snejok@altlinux.ru> 0.94.7-alt2
- Dirs under _localstatedir/ceph packed, needed by ceph-deploy

* Fri Jun 17 2016 Lenar Shakirov <snejok@altlinux.ru> 0.94.7-alt1
- 0.94.7

* Tue Apr 05 2016 Alexei Takaseev <taf@altlinux.org> 0.94.6-alt1
- 0.94.6

* Mon Jan 11 2016 Alexei Takaseev <taf@altlinux.org> 0.94.5-alt2
- Fix loss man

* Tue Oct 27 2015 Alexei Takaseev <taf@altlinux.org> 0.94.5-alt1
- 0.94.5

* Tue Oct 20 2015 Alexei Takaseev <taf@altlinux.org> 0.94.4-alt1
- 0.94.4

* Wed Oct 07 2015 Alexei Takaseev <taf@altlinux.org> 0.94.3-alt3
- add tmpfiles.d file (ALT:#31315)

* Wed Sep 23 2015 Alexei Takaseev <taf@altlinux.org> 0.94.3-alt2
- Fix path to ceph-osd-prestart.sh, add lost ceph.target
  (ALT:#31295)

* Thu Aug 27 2015 Alexei Takaseev <taf@altlinux.org> 0.94.3-alt1
- 0.94.3

* Thu Jun 11 2015 Alexei Takaseev <taf@altlinux.org> 0.94.2-alt1
- 0.94.2

* Thu May 28 2015 Alexei Takaseev <taf@altlinux.org> 0.94.1.2-alt1
- 0.94.1.2

* Tue Apr 14 2015 Alexei Takaseev <taf@altlinux.org> 0.94.1-alt1
- 0.94.1

* Mon Apr 13 2015 Alexei Takaseev <taf@altlinux.org> 0.94-alt1
- 0.94

* Sat Feb 28 2015 Alexei Takaseev <taf@altlinux.org> 0.93-alt1
- 0.93

* Wed Feb 04 2015 Alexei Takaseev <taf@altlinux.org> 0.92-alt1
- 0.92

* Thu Jan 15 2015 Alexei Takaseev <taf@altlinux.org> 0.91-alt1
- 0.91

* Thu Dec 25 2014 Alexei Takaseev <taf@altlinux.org> 0.90-alt1
- 0.90

* Sat Dec 06 2014 Alexei Takaseev <taf@altlinux.org> 0.89-alt1
- 0.89

* Wed Nov 12 2014 Alexei Takaseev <taf@altlinux.org> 0.88-alt1
- 0.88

* Thu Oct 30 2014 Alexei Takaseev <taf@altlinux.org> 0.87-alt1
- 0.87

* Wed Oct 08 2014 Alexei Takaseev <taf@altlinux.org> 0.86-alt1
- 0.86

* Tue Sep 09 2014 Alexei Takaseev <taf@altlinux.org> 0.85-alt1
- 0.85

* Tue Aug 19 2014 Alexei Takaseev <taf@altlinux.org> 0.84-alt1
- 0.84
- add BuildReq: boost-intrusive-devel

* Wed Jul 30 2014 Alexei Takaseev <taf@altlinux.org> 0.83-alt1
- 0.83

* Sat Jun 28 2014 Alexei Takaseev <taf@altlinux.org> 0.82-alt1
- 0.82

* Fri May 09 2014 Alexei Takaseev <taf@altlinux.org> 0.80-alt1
- 0.80

* Thu Apr 10 2014 Alexei Takaseev <taf@altlinux.org> 0.79-alt1
- 0.79

* Tue Mar 04 2014 Alexei Takaseev <taf@altlinux.org> 0.77-alt1
- 0.77

* Wed Jan 15 2014 Alexei Takaseev <taf@altlinux.org> 0.75-alt1
- 0.75

* Sun Jan 05 2014 Alexei Takaseev <taf@altlinux.org> 0.74-alt1
- 0.74

* Fri Dec 20 2013 Alexei Takaseev <taf@altlinux.org> 0.73-alt1
- 0.73

* Fri Nov 08 2013 Alexei Takaseev <taf@altlinux.org> 0.72-alt1
- 0.72

* Mon Oct 21 2013 Alexei Takaseev <taf@altlinux.org> 0.71-alt1
- 0.71

* Wed Jul 10 2013 Alexei Takaseev <taf@altlinux.org> 0.66-alt1
- 0.66

* Wed Jun 26 2013 Alexei Takaseev <taf@altlinux.org> 0.65-alt1
- 0.65

* Thu Jun 13 2013 Alexei Takaseev <taf@altlinux.org> 0.64-alt1
- 0.64

* Wed May 29 2013 Alexei Takaseev <taf@altlinux.org> 0.63-alt1
- 0.63

* Tue May 14 2013 Alexei Takaseev <taf@altlinux.org> 0.61.2-alt1
- 0.61.2

* Mon May 13 2013 Alexei Takaseev <taf@altlinux.org> 0.61.1-alt1
- 0.61.1

* Tue May 07 2013 Alexei Takaseev <taf@altlinux.org> 0.61-alt1
- 0.61

* Tue Apr 16 2013 Alexei Takaseev <taf@altlinux.org> 0.60-alt1
- 0.60
- remove leveldb source, user system libs

* Tue Mar 26 2013 Alexei Takaseev <taf@altlinux.org> 0.56.4-alt1
- 0.56.4

* Wed Feb 27 2013 Fr. Br. George <george@altlinux.ru> 0.56.3-alt1.1
- Rebuild with renamed gperftools
- Fix include files location

* Sun Feb 17 2013 Alexei Takaseev <taf@altlinux.org> 0.56.3-alt1
- 0.56.3

* Mon Feb 11 2013 Alexei Takaseev <taf@altlinux.org> 0.56.2-alt2
- Rebuild with boost 1.53.0

* Thu Jan 31 2013 Alexei Takaseev <taf@altlinux.org> 0.56.2-alt1
- 0.56.2

* Thu Jan 24 2013 Alexei Takaseev <taf@altlinux.org> 0.56.1-alt2
- added strict requires
- fix "condrestart" warning

* Wed Jan 09 2013 Alexei Takaseev <taf@altlinux.org> 0.56.1-alt1
- 0.56.1

* Wed Jan 02 2013 Alexei Takaseev <taf@altlinux.org> 0.56-alt1
- 0.56

* Fri Dec 14 2012 Alexei Takaseev <taf@altlinux.org> 0.55.1-alt1
- 0.55.1

* Wed Dec 05 2012 Alexei Takaseev <taf@altlinux.org> 0.55-alt1
- 0.55

* Wed Nov 28 2012 Alexei Takaseev <taf@altlinux.org> 0.54-alt2
- Rebuild with boost 1.52.0

* Fri Nov 16 2012 Alexei Takaseev <taf@altlinux.org> 0.54-alt1
- 0.54

* Wed Oct 17 2012 Alexei Takaseev <taf@altlinux.org> 0.53-alt1
- 0.53

* Fri Sep 28 2012 Alexei Takaseev <taf@altlinux.org> 0.52-alt1
- 0.52

* Tue Sep 11 2012 Alexei Takaseev <taf@altlinux.org> 0.51-alt2
- Fix build with boost 1.51.0

* Tue Aug 28 2012 Alexei Takaseev <taf@altlinux.org> 0.51-alt1
- 0.51

* Thu Aug 23 2012 Alexei Takaseev <taf@altlinux.org> 0.50-alt2
- edit requires

* Wed Aug 22 2012 Alexei Takaseev <taf@altlinux.org> 0.50-alt1
- 0.50

* Tue Jul 24 2012 Alexei Takaseev <taf@altlinux.org> 0.49-alt1
- 0.49

* Thu Jul 19 2012 Alexei Takaseev <taf@altlinux.org> 0.48-alt1
- 0.48

* Sat Jun 23 2012 Alexei Takaseev <taf@altlinux.org> 0.47.3-alt1
- 0.47.3

* Mon Jun 11 2012 Alexei Takaseev <taf@altlinux.org> 0.47.2-alt1
- Initial build for Sisyphus

