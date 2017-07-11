%define _libexecdir /usr/libexec
%define git_version 50e863e0f4bc8f4b9e31156de690d765af245185

%def_with ocf
%def_with tcmalloc
%def_with libzfs
%def_without lttng
%def_without cephfs_java

Name: ceph
Version: 10.2.8
Release: alt1
Summary: User space components of the Ceph file system
Group: System/Base

License: LGPLv2
Url: http://ceph.com/

Source0: %name-%version.tar
Source1: ceph-radosgw.init
Source2: rbdmap.init

# git submodules
Source11: ceph-erasure-code-corpus.tar
Source12: ceph-object-corpus.tar
Source13: civetweb.tar
Source14: gf-complete.tar
Source15: jerasure.tar
Source16: gmock.tar
Source17: rocksdb.tar
Source18: spdk.tar
Source19: xxHash.tar
Source20: gtest.tar

Patch0: %name-%version-%release.patch

BuildRequires: boost-asio-devel boost-devel-headers boost-program_options-devel boost-intrusive-devel
BuildRequires: gcc-c++ libaio-devel libblkid-devel libcurl-devel libexpat-devel
BuildRequires: libfcgi-devel libfuse-devel libkeyutils-devel
BuildRequires: libldap-devel libleveldb-devel libnss-devel libsnappy-devel
BuildRequires: libssl-devel libudev-devel libxfs-devel libbtrfs-devel
%{?_with_libzfs:BuildRequires: libzfs-devel}
BuildRequires: yasm zlib-devel bzlib-devel liblz4-devel
BuildRequires: libssl-devel libudev-devel
BuildRequires: python-module-Cython
BuildRequires: python-module-backports.ssl_match_hostname python-module-enum34
BuildRequires: python-module-html5lib python-module-pyasn1 python-module-virtualenv
BuildRequires: python-sphinx-objects.inv python-module-sphinx
%{?_with_tcmalloc:BuildRequires: libgperftools-devel}
%{?_with_lttng:BuildRequires: liblttng-ust-devel libbabeltrace-devel}
%{?_with_cephfs_java:BuildRequires: java-devel}
BuildRequires: libsystemd-devel

BuildRequires(pre): rpm-build-python

Requires: ceph-osd = %EVR
Requires: ceph-mds = %EVR
Requires: ceph-mon = %EVR

%description
Ceph is a distributed network file system designed to provide excellent
performance, reliability, and scalability.

%package base
Summary: Ceph Base Package
Group: System/Base
Requires: ceph-common = %EVR
Requires: librbd1 = %EVR
Requires: librados2 = %EVR
Requires: libcephfs1 = %EVR
Requires: librgw2 = %EVR
Requires: ntp-server
Requires: lsb-release
%description base
Base is the package that includes all the files shared amongst ceph servers

%package common
Summary: Ceph Common
Group: System/Base
Requires: librbd1 = %EVR
Requires: librados2 = %EVR
Requires: libcephfs1 = %EVR
Requires: librgw2 = %EVR

%description common
Common utilities to mount and interact with a ceph storage cluster.
Comprised of files that are common to Ceph clients and servers.

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

%package fuse
Summary: Ceph fuse-based client
Group: System/Kernel and hardware
%description fuse
FUSE based client for Ceph distributed network file system

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
Requires: ceph-common = %EVR
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
Requires: ceph-common = %EVR
Requires: librados2 = %EVR
Requires: librgw2 = %EVR
%description radosgw
radosgw is an S3 HTTP REST gateway for the RADOS object store. It is
implemented as a FastCGI module using libfcgi, and can be used in
conjunction with any FastCGI capable web server.

%package resource-agents
Summary: OCF-compliant resource agents for Ceph daemons
Group: System/Configuration/Other
License: LGPLv2
BuildArch: noarch
Requires: %name = %EVR
%description resource-agents
Resource agents for monitoring and managing Ceph daemons
under Open Cluster Framework (OCF) compliant resource
managers such as Pacemaker.

%package osd
Summary: Ceph Object Storage Daemon
Group: System/Base
Requires: ceph-base = %EVR
# for sgdisk, used by ceph-disk
Requires: gdisk
Requires: parted
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

%package -n librados2-devel
Summary: RADOS headers
Group: Development/C
Requires: librados2 = %EVR
%description -n librados2-devel
This package contains libraries and headers needed to develop programs
that use RADOS object store.

%package -n librgw2
Summary: RADOS gateway client library
Group: System/Libraries
Requires: librados2 = %EVR
%description -n librgw2
This package provides a library implementation of the RADOS gateway
(distributed object store with S3 and Swift personalities).

%package -n librgw2-devel
Summary: RADOS gateway client library
Group: Development/C
License: LGPLv2
Requires: librados2 = %EVR
%description -n librgw2-devel
This package contains libraries and headers needed to develop programs
that use RADOS gateway client library.

%package -n python-module-rados
Summary: Python libraries for the RADOS object store
Group: Development/Python
Requires: librados2 = %EVR
Conflicts: python-module-ceph < %EVR
%description -n python-module-rados
This package contains Python libraries for interacting with Cephs RADOS
object store.

%package -n libradosstriper1
Summary: RADOS striping interface
Group: System/Libraries
License: LGPLv2
Requires: librados2 = %EVR
%description -n libradosstriper1
Striping interface built on top of the rados library, allowing
to stripe bigger objects onto several standard rados objects using
an interface very similar to the rados one.

%package -n libradosstriper1-devel
Summary: RADOS striping interface headers
Group: Development/C
Requires: libradosstriper1 = %EVR
Requires: librados2-devel = %EVR
Conflicts: ceph-devel < %EVR
%description -n libradosstriper1-devel
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

%package -n librbd1-devel
Summary: RADOS block device headers
Group: Development/C
Requires: librbd1 = %EVR
Requires: librados2-devel = %EVR
Conflicts: ceph-devel < %EVR
%description -n librbd1-devel
This package contains libraries and headers needed to develop programs
that use RADOS block device.

%package -n python-module-rbd
Summary: Python libraries for the RADOS block device
Group: Development/Python
Requires: librbd1 = %EVR
Requires: python-module-rados = %EVR
Conflicts: python-module-ceph < %EVR

%description -n python-module-rbd
This package contains Python libraries for interacting with Cephs RADOS
block device.

%package -n libcephfs1
Summary: Ceph distributed file system client library
Group: System/Libraries
License: LGPLv2
%description -n libcephfs1
Ceph is a distributed network file system designed to provide excellent
performance, reliability, and scalability. This is a shared library
allowing applications to access a Ceph distributed file system via a
POSIX-like interface.

%package -n libcephfs1-devel
Summary: Ceph distributed file system headers
Group: Development/C
Requires: libcephfs1 = %EVR
Requires: librados2-devel = %EVR
Conflicts: ceph-devel < %EVR
%description -n libcephfs1-devel
This package contains libraries and headers needed to develop programs
that use Cephs distributed file system.

%package -n python-module-cephfs
Summary: Python libraries for Ceph distributed file system
Group: Development/Python
Requires: libcephfs1 = %EVR
Requires: python-module-rados = %EVR
Conflicts: python-module-ceph < %EVR
%description -n python-module-cephfs
This package contains Python libraries for interacting with Cephs distributed
file system.

%package test
Summary: Ceph benchmarks and test tools
Group: System/Libraries
Requires: ceph-common
Requires: xmlstarlet
%description test
This package contains Ceph benchmarks and test tools.


%package -n libcephfs_jni1
Summary: Java Native Interface library for CephFS Java bindings
Group: System/Libraries
Requires: java
Requires: libcephfs1 = %EVR
%description -n libcephfs_jni1
This package contains the Java Native Interface library for CephFS Java
bindings.

%package -n libcephfs_jni1-devel
Summary: Development files for CephFS Java Native Interface library
Group: System Environment/Libraries
Requires: java
Requires: libcephfs_jni1 = %EVR
Conflicts: ceph-devel < %EVR
%description -n libcephfs_jni1-devel
This package contains the development files for CephFS Java Native Interface
library.

%package -n cephfs-java
Summary: Java libraries for the Ceph File System
Group: System/Libraries
Requires: java
Requires: libcephfs_jni1 = %EVR
Requires:       junit
BuildRequires:  junit
%description -n cephfs-java
This package contains the Java libraries for the Ceph File System.


%package devel
Summary: Ceph headers
Group: Development/C
License: LGPLv2
Requires: librados2-devel = %EVR
Requires: libradosstriper1-devel = %EVR
Requires: librbd1-devel = %EVR
Requires: libcephfs1-devel = %EVR
%if_with cephfs_java
Requires: libcephfs_jni1-devel = %EVR
%endif

%description devel
This package contains libraries and headers needed to develop programs
that use Ceph.

%package -n python-module-ceph
Summary: Python libraries for the Ceph distributed filesystem
Group: Development/Python
Requires: python-module-rados = %EVR
Requires: python-module-rbd = %EVR
Requires: python-module-cephfs = %EVR
%description -n python-module-ceph
This package contains Python libraries for interacting with Cephs RADOS
object storage.

%prep
%setup

tar -xf %SOURCE11 -C ceph-erasure-code-corpus
tar -xf %SOURCE12 -C ceph-object-corpus
tar -xf %SOURCE13 -C src/civetweb
tar -xf %SOURCE14 -C src/erasure-code/jerasure/gf-complete
tar -xf %SOURCE15 -C src/erasure-code/jerasure/jerasure
tar -xf %SOURCE16 -C src/gmock
tar -xf %SOURCE17 -C src/rocksdb
tar -xf %SOURCE18 -C src/spdk
tar -xf %SOURCE19 -C src/xxHash
tar -xf %SOURCE20 -C src/gmock/gtest

%patch0 -p1

%build
./autogen.sh
#export LIBS="$LIBS -lboost_system"
export CPPFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
#%add_optflags -DHAVE_GPERFTOOLS_PROFILER_H -DHAVE_GPERFTOOLS_HEAP_PROFILER_H -DHAVE_GPERFTOOLS_MALLOC_EXTENSION_H
%configure	--without-hadoop \
		--without-libatomic-ops \
		--with-systemdsystemunitdir=%_unitdir \
		--with-radosgw \
		--with-debug \
		%{subst_with ocf} \
		%{subst_with tcmalloc} \
		%{subst_with libzfs} \
		--with-nss \
		--without-cryptopp \
		%{?_without_lttng: --without-lttng --without-babeltrace} \
		%{?_with_cephfs_java: --enable-cephfs-java} \
		--with-man-pages

cat << __EOF__ > src/.git_version
%git_version
v%version
__EOF__

%make_build

%install
%makeinstall_std

find %buildroot -type f -name "*.la" -exec rm -f {} ';'
find %buildroot -type f -name "*.a" -exec rm -f {} ';'
install -m 0644 -D src/etc-rbdmap %buildroot%_sysconfdir/ceph/rbdmap
install -m 0644 -D etc/sysconfig/ceph %buildroot%_sysconfdir/sysconfig/ceph

install -m 0644 -D systemd/ceph.tmpfiles.d %buildroot%_tmpfilesdir/ceph-common.conf
install -m 0644 -D systemd/50-ceph.preset %buildroot/lib/systemd/system-preset/50-ceph.preset
mkdir -p %buildroot%_sbindir
install -m 0644 -D src/logrotate.conf %buildroot%_sysconfdir/logrotate.d/ceph

install -D src/init-ceph %buildroot%_initdir/ceph
install -D %SOURCE1 %buildroot%_initdir/ceph-radosgw
install -D %SOURCE2 %buildroot%_initdir/rbdmap

# udev rules
install -m 0644 -D udev/50-rbd.rules %buildroot%_udevrulesdir/50-rbd.rules
install -m 0644 -D udev/60-ceph-by-parttypeuuid.rules %buildroot%_udevrulesdir/60-ceph-by-parttypeuuid.rules
install -m 0644 -D udev/95-ceph-osd.rules %buildroot%_udevrulesdir/95-ceph-osd.rules

#set up placeholder directories
mkdir -p %buildroot%_sysconfdir/ceph
mkdir -p %buildroot%_runtimedir/ceph
mkdir -p %buildroot%_logdir/ceph
mkdir -p %buildroot%_logdir/radosgw
mkdir -p %buildroot%_localstatedir/ceph/tmp
mkdir -p %buildroot%_localstatedir/ceph/mon
mkdir -p %buildroot%_localstatedir/ceph/osd
mkdir -p %buildroot%_localstatedir/ceph/mds
mkdir -p %buildroot%_localstatedir/ceph/radosgw
mkdir -p %buildroot%_localstatedir/ceph/bootstrap-osd
mkdir -p %buildroot%_localstatedir/ceph/bootstrap-mds
mkdir -p %buildroot%_localstatedir/ceph/bootstrap-rgw

%ifarch x86_64
mv -f %buildroot%python_sitelibdir_noarch/* %buildroot%python_sitelibdir/
%endif

# cleanup
rm -rf %buildroot%_docdir/ceph

%pre common
%_sbindir/groupadd -r -f ceph 2>/dev/null ||:
%_sbindir/useradd  -r -g ceph -s /sbin/nologin -c "Ceph daemons" -d %_localstatedir/ceph ceph 2>/dev/null ||:

%post common
systemd-tmpfiles --create %_tmpfilesdir/ceph-common.conf
%post_service rbdmap

%postun common
%preun_service rbdmap

%post base
#post_service ceph
SYSTEMCTL=systemctl
if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" daemon-reload ||:
        if [ "$1" -eq 1 ]; then
                "$SYSTEMCTL" -q preset ceph.target ||:
        else
                "$SYSTEMCTL" try-restart ceph.target ||:
        fi
else
        if [ "$1" -eq 1 ]; then
                chkconfig --add ceph ||:
        else
                chkconfig ceph resetpriorities ||:
                service ceph condrestart ||:
        fi
fi

%preun base
#preun_service ceph
if [ "$1" -eq 0 ]; then
        SYSTEMCTL=systemctl
        if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
                "$SYSTEMCTL" --no-reload -q disable ceph.target ||:
                "$SYSTEMCTL" stop ceph.target ||:
        else
                chkconfig --del ceph ||:
                service ceph condstop ||:
        fi

fi

%post mds
#post_service mds
SYSTEMCTL=systemctl
if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" daemon-reload ||:
        if [ "$1" -eq 1 ]; then
                "$SYSTEMCTL" -q preset ceph-mds@\*.service ceph-mds.target ||:
        else
                "$SYSTEMCTL" try-restart ceph-mds.target ||:
        fi
else
        %post_service ceph
fi

%preun mds
#preun_service mds
if [ "$1" -eq 0 ]; then
        SYSTEMCTL=systemctl
        if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
                "$SYSTEMCTL" --no-reload -q disable ceph-mds@\*.service ceph-mds.target ||:
                "$SYSTEMCTL" stop ceph-mds@\*.service ceph-mds.target ||:
        else
                %preun_service ceph
        fi

fi

%post mon
#post_service mon
SYSTEMCTL=systemctl
if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" daemon-reload ||:
        if [ "$1" -eq 1 ]; then
                "$SYSTEMCTL" -q preset ceph-mon@\*.service ceph-mon.target ||:
        else
                "$SYSTEMCTL" try-restart ceph-mon.target ||:
        fi
else
        %post_service ceph
fi

%preun mon
#preun_service mon
if [ "$1" -eq 0 ]; then
        SYSTEMCTL=systemctl
        if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
                "$SYSTEMCTL" --no-reload -q disable ceph-mon@\*.service ceph-mon.target ||:
                "$SYSTEMCTL" stop ceph-mon@\*.service ceph-mon.target ||:
        else
                %preun_service ceph
        fi

fi

%post osd
#post_service osd
SYSTEMCTL=systemctl
if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" daemon-reload ||:
        if [ "$1" -eq 1 ]; then
                "$SYSTEMCTL" -q preset ceph-osd@\*.service ceph-osd.target ||:
        else
                "$SYSTEMCTL" try-restart ceph-osd.target ||:
        fi
else
        %post_service ceph
fi

%preun osd
#preun_service osd
if [ "$1" -eq 0 ]; then
        SYSTEMCTL=systemctl
        if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
                "$SYSTEMCTL" --no-reload -q disable ceph-osd@\*.service ceph-osd.target ||:
                "$SYSTEMCTL" stop ceph-osd@\*.service ceph-osd.target ||:
        else
                %preun_service ceph
        fi

fi

%post -n rbd-mirror
#post_service rbd-mirror
SYSTEMCTL=systemctl
if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" daemon-reload ||:
        if [ "$1" -eq 1 ]; then
                "$SYSTEMCTL" -q preset ceph-rbd-mirror@\*.service ceph-rbd-mirror.target ||:
        else
                "$SYSTEMCTL" try-restart ceph-rbd-mirror.target ||:
        fi
#else
#        %post_service ceph-rbd-mirror
fi

%preun -n rbd-mirror
#preun_service mon
if [ "$1" -eq 0 ]; then
        SYSTEMCTL=systemctl
        if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
                "$SYSTEMCTL" --no-reload -q disable ceph-rbd-mirror@\*.service ceph-rbd-mirror.target ||:
                "$SYSTEMCTL" stop ceph-rbd-mirror@\*.service ceph-rbd-mirror.target ||:
#        else
#                %preun_service ceph-rbd-mirror
        fi

fi

%post radosgw
#post_service radosgw
SYSTEMCTL=systemctl
if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" daemon-reload ||:
        if [ "$1" -eq 1 ]; then
                "$SYSTEMCTL" -q preset ceph-radosgw@\*.service ceph-radosgw.target ||:
        else
                "$SYSTEMCTL" try-restart ceph-radosgw.target ||:
        fi
else
        %post_service ceph-radosgw
fi

%preun radosgw
#preun_service radosgw
if [ "$1" -eq 0 ]; then
        SYSTEMCTL=systemctl
        if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
                "$SYSTEMCTL" --no-reload -q disable ceph-radosgw@\*.service ceph-radosgw.target ||:
                "$SYSTEMCTL" stop ceph-radosgw@\*.service ceph-radosgw.target ||:
        else
                %preun_service ceph-radosgw
        fi

fi


%files

%files base
%doc AUTHORS COPYING INSTALL README doc src/doc src/sample.ceph.conf src/sample.fetch_config
%_bindir/crushtool
%_bindir/monmaptool
%_bindir/osdmaptool
%_bindir/ceph-run
%_bindir/ceph-detect-init
%_bindir/ceph-client-debug
%_bindir/cephfs
%_unitdir/ceph-create-keys@.service
/lib/systemd/system-preset/50-ceph.preset
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
%if_with lttng
%_libdir/libos_tp.so*
%_libdir/libosd_tp.so*
%endif
%config %_sysconfdir/bash_completion.d/ceph
%config(noreplace) %_sysconfdir/logrotate.d/ceph
%config(noreplace) %{_sysconfdir}/sysconfig/ceph
%_unitdir/ceph.target
%_initdir/ceph
%python_sitelibdir/ceph_detect_init*
%python_sitelibdir/ceph_disk*
%_mandir/man8/ceph-deploy.8*
%_mandir/man8/ceph-detect-init.8*
%_mandir/man8/ceph-create-keys.8*
%_mandir/man8/ceph-run.8*
%_mandir/man8/crushtool.8*
%_mandir/man8/osdmaptool.8*
%_mandir/man8/monmaptool.8*
%_mandir/man8/cephfs.8*
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/tmp
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/bootstrap-osd
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/bootstrap-mds
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/bootstrap-rgw

%files common
%_bindir/ceph
%_bindir/ceph-authtool
%_bindir/ceph-conf
%_bindir/ceph-dencoder
%_bindir/ceph-rbdnamer
%_bindir/ceph-syn
%_bindir/ceph-crush-location
%_bindir/cephfs-data-scan
%_bindir/cephfs-journal-tool
%_bindir/cephfs-table-tool
%_bindir/rados
%_bindir/rbd
%_bindir/rbd-replay
%_bindir/rbd-replay-many
%_bindir/rbdmap
%_sbindir/mount.ceph
%if_with lttng
%_bindir/rbd-replay-prep
%endif
%_bindir/ceph-post-file
%_bindir/ceph-brag
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
%config %_sysconfdir/bash_completion.d/rados
%config %_sysconfdir/bash_completion.d/rbd
%config(noreplace) %_sysconfdir/ceph/rbdmap
%_unitdir/rbdmap.service
%_initdir/rbdmap
%_udevrulesdir/50-rbd.rules
%python_sitelibdir/ceph_argparse.py*
%python_sitelibdir/ceph_daemon.py*

%attr(3770,root,ceph) %dir %_logdir/ceph
%attr(0750,ceph,ceph) %dir %_localstatedir/ceph

%files mds
%_bindir/ceph-mds
%_mandir/man8/ceph-mds.8*
%_unitdir/ceph-mds@.service
%_unitdir/ceph-mds.target
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/mds

%files mon
%_bindir/ceph-mon
%_bindir/ceph-rest-api
%_mandir/man8/ceph-mon.8*
%_mandir/man8/ceph-rest-api.8*
%python_sitelibdir/ceph_rest_api.py*
%_unitdir/ceph-mon@.service
%_unitdir/ceph-mon.target
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/mon

%files fuse
%_bindir/ceph-fuse
%_mandir/man8/ceph-fuse.8*
%_sbindir/mount.fuse.ceph

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

%files radosgw
%_bindir/radosgw
%_bindir/radosgw-admin
%_bindir/radosgw-token
%_bindir/radosgw-object-expirer
%_mandir/man8/radosgw.8*
%_mandir/man8/radosgw-admin.8*
%_logdir/radosgw
%config %_sysconfdir/bash_completion.d/radosgw-admin
%dir %_localstatedir/ceph/radosgw
%_unitdir/ceph-radosgw@.service
%_unitdir/ceph-radosgw.target
%_initdir/ceph-radosgw

%files osd
%_bindir/ceph-clsinfo
%_bindir/ceph-bluefs-tool
%_bindir/ceph-objectstore-tool
%_bindir/ceph-osd
%_sbindir/ceph-disk
%_sbindir/ceph-disk-udev
%_libexecdir/ceph/ceph-osd-prestart.sh
%_udevrulesdir/60-ceph-by-parttypeuuid.rules
%_udevrulesdir/95-ceph-osd.rules
%_mandir/man8/ceph-clsinfo.8*
%_mandir/man8/ceph-disk.8*
%_mandir/man8/ceph-osd.8*
%_unitdir/ceph-osd@.service
%_unitdir/ceph-osd.target
%_unitdir/ceph-disk@.service
%attr(750,ceph,ceph) %dir %_localstatedir/ceph/osd


%if_with ocf
%files resource-agents
%_prefix/lib/ocf/resource.d/%name
%endif

%files -n librados2
%_libdir/librados.so.*
%if_with lttng
%_libdir/librados_tp.so.*
%endif

%files -n librados2-devel
%dir %_includedir/rados
%_includedir/rados/librados.h
%_includedir/rados/librados.hpp
%_includedir/rados/buffer.h
%_includedir/rados/buffer_fwd.h
%_includedir/rados/page.h
%_includedir/rados/crc32c.h
%_includedir/rados/rados_types.h
%_includedir/rados/rados_types.hpp
%_includedir/rados/memory.h
%_libdir/librados.so
%if_with lttng
%_libdir/librados_tp.so
%endif
%_bindir/librados-config
%_mandir/man8/librados-config.8*

%files -n python-module-rados
%python_sitelibdir/rados.so
%python_sitelibdir/rados-*.egg-info

%files -n libradosstriper1
%_libdir/libradosstriper.so.*

%files -n libradosstriper1-devel
%dir %_includedir/radosstriper
%_includedir/radosstriper/*
%_libdir/libradosstriper.so

%files -n librbd1
%_libdir/librbd.so.*
%if_with lttng
%_libdir/librbd_tp.so.*
%endif

%files -n librbd1-devel
%dir %_includedir/rbd
%_includedir/rbd/*
%_libdir/librbd.so
%if_with lttng
%_libdir/librbd_tp.so
%endif

%files -n librgw2
%_libdir/librgw.so.*

%files -n librgw2-devel
%_includedir/rados/librgw.h
%_includedir/rados/rgw_file.h
%_libdir/librgw.so

%files -n python-module-rbd
%python_sitelibdir/rbd.so
%python_sitelibdir/rbd-*.egg-info

%files -n libcephfs1
%_libdir/libcephfs.so.*

%files -n libcephfs1-devel
%dir %_includedir/cephfs
%_includedir/cephfs/*
%_libdir/libcephfs.so

%files -n python-module-cephfs
%python_sitelibdir/cephfs.so
%python_sitelibdir/cephfs-*.egg-info
%python_sitelibdir/ceph_volume_client.py*

%files -n ceph-test
%_bindir/ceph_bench_log
%_bindir/ceph_kvstorebench
%_bindir/ceph_multi_stress_watch
%_bindir/ceph_erasure_code
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
%_bindir/librgw_file*
%_bindir/ceph_tpbench
%_bindir/ceph_xattr_bench
%_bindir/ceph-coverage
%_bindir/ceph-monstore-tool
%_bindir/ceph-osdomap-tool
%_bindir/ceph-kvstore-tool
%_bindir/ceph-debugpack
%_mandir/man8/ceph-debugpack.8*
%_libdir/ceph/ceph-monstore-update-crush.sh

%if_with cephfs_java
%files -n libcephfs_jni1
%_libdir/libcephfs_jni.so.*

%files -n libcephfs_jni1-devel
%_libdir/libcephfs_jni.so

%files -n cephfs-java
%_javadir/libcephfs.jar
%_javadir/libcephfs-test.jar
%endif


%files devel

%files -n python-module-ceph

%changelog
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

