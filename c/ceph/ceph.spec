Name: ceph
Version: 0.47.3
Release: alt1
Summary: User space components of the Ceph file system
Group: System/Base

Packager: Alexei Takaseev <taf@altlinux.ru>

License: LGPLv2
Url: http://ceph.com/

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

Requires: librbd1 = %version-%release
Requires: librados2 = %version-%release
Requires: libcephfs1 = %version-%release

BuildRequires: boost-devel-headers gcc-c++ libaio-devel libcurl-devel
BuildRequires: libedit-devel libexpat-devel libfcgi-devel libfuse-devel
BuildRequires: libgoogle-perftools-devel libgtkmm2-devel libkeyutils-devel
BuildRequires: libnss-devel libuuid-devel

BuildRequires(pre): rpm-build-python

%description
Ceph is a distributed network file system designed to provide excellent
performance, reliability, and scalability.

%package fuse
Summary: Ceph fuse-based client
Group: System/Kernel and hardware
Requires: %name = %version-%release
%description fuse
FUSE based client for Ceph distributed network file system

%package devel
Summary: Ceph headers
Group: Development/C
License: LGPLv2
Requires: %name = %version-%release
Requires: librados2 = %version
Requires: librbd1 = %version
Requires: libcephfs1 = %version
%description devel
This package contains libraries and headers needed to develop programs
that use Ceph.

%package radosgw
Summary: Rados REST gateway
Group: System/Libraries
Requires: librados2 = %version-%release
%description radosgw
radosgw is an S3 HTTP REST gateway for the RADOS object store. It is
implemented as a FastCGI module using libfcgi, and can be used in
conjunction with any FastCGI capable web server.

%package obsync
Summary: synchronize data between cloud object storage providers or a local directory
Group: Networking/Other
License: LGPLv2
BuildArch: noarch
%description obsync
obsync is a tool to synchronize objects between cloud object
storage providers, such as Amazon S3 (or compatible services), a
Ceph RADOS cluster, or a local directory.

%package gcephtool
Summary: Ceph graphical monitoring tool
Group: Monitoring
License: LGPLv2
%description gcephtool
gcephtool is a graphical monitor for the clusters running the Ceph distributed
file system.

%package resource-agents
Summary: OCF-compliant resource agents for Ceph daemons
Group: System/Configuration/Other
License: LGPLv2
BuildArch: noarch
Requires: %name = %version
%description resource-agents
Resource agents for monitoring and managing Ceph daemons
under Open Cluster Framework (OCF) compliant resource
managers such as Pacemaker.

%package -n librados2
Summary: RADOS distributed object store client library
Group: System/Libraries
License: LGPLv2
%description -n librados2
RADOS is a reliable, autonomic distributed object storage cluster
developed as part of the Ceph distributed storage system. This is a
shared library allowing applications to access the distributed object
store using a simple file-like interface.

%package -n librbd1
Summary: RADOS block device client library
Group: System/Libraries
License: LGPLv2
Requires: librados2 = %version-%release
%description -n librbd1
RBD is a block device striped across multiple distributed objects in
RADOS, a reliable, autonomic distributed object storage cluster
developed as part of the Ceph distributed storage system. This is a
shared library allowing applications to manage these block devices.

%package -n libcephfs1
Summary: Ceph distributed file system client library
Group: System/Libraries
License: LGPLv2
%description -n libcephfs1
Ceph is a distributed network file system designed to provide excellent
performance, reliability, and scalability. This is a shared library
allowing applications to access a Ceph distributed file system via a
POSIX-like interface.

%package -n python-module-ceph
Summary: Python libraries for the Ceph distributed filesystem
Group: Development/Python
License: LGPLv2
BuildArch: noarch
Requires: librados2 = %version-%release
Requires: librbd1 = %version-%release
Requires: libcephfs1 = %version-%release
%description -n python-module-ceph
This package contains Python libraries for interacting with Cephs RADOS
object storage.

%prep
%setup
%patch0 -p1

rm -rf ceph-object-corpus
ln -s ceph-object-corpus_sub ceph-object-corpus

rm -rf src/leveldb
ln -s leveldb_sub src/leveldb

rm -rf src/libs3
ln -s libs3_sub src/libs3

%build
./autogen.sh
%configure	--without-hadoop \
		--without-libatomic-ops \
		--with-radosgw \
		--with-gtk2 \
		--with-ocf \
		--with-tcmalloc
%make_build

%install
%makeinstall

find %buildroot -type f -name "*.la" -exec rm -f {} ';'
find %buildroot -type f -name "*.a" -exec rm -f {} ';'
install -D src/init-ceph %buildroot%_initdir/ceph
install -D ceph-radosgw.init %buildroot%_initdir/ceph-radosgw
ln -sf ../../etc/init.d/ceph %buildroot%_sbindir/rcceph
ln -sf ../../etc/init.d/ceph-radosgw %buildroot%_sbindir/rcceph-radosgw
install -m 0644 -D src/logrotate.conf %buildroot%_sysconfdir/logrotate.d/ceph
mkdir -p %buildroot%_localstatedir/ceph/tmp/
mkdir -p %buildroot/var/log/ceph
mkdir -p %buildroot/var/log/radosgw
mkdir -p %buildroot%_runtimedir/ceph/
mkdir -p %buildroot%_sysconfdir/ceph/

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS COPYING INSTALL README doc src/doc src/sample.ceph.conf src/sample.fetch_config
%_bindir/ceph
%_bindir/cephfs
%_bindir/ceph-conf
%_bindir/ceph-clsinfo
%_bindir/crushtool
%_bindir/monmaptool
%_bindir/osdmaptool
%_bindir/ceph-authtool
%_bindir/ceph-syn
%_bindir/ceph-run
%_bindir/ceph-mon
%_bindir/ceph-mds
%_bindir/ceph-osd
%_bindir/ceph-rbdnamer
%_bindir/ceph-dencoder
%_bindir/librados-config
%_bindir/rados
%_bindir/rbd
%_bindir/ceph-debugpack
%_bindir/boto_tool
%_bindir/ceph-coverage
%_bindir/ceph-kdump-copy
%_sbindir/mkcephfs
%_sbindir/mount.ceph
%_sbindir/rcceph
%_initdir/ceph
%_libdir/rados-classes/
%_libdir/ceph/
%_libdir/rados-classes/libcls_rbd.so*
%_libdir/rados-classes/libcls_rgw.so*
%config %_sysconfdir/bash_completion.d/ceph
%config %_sysconfdir/bash_completion.d/rados
%config %_sysconfdir/bash_completion.d/radosgw-admin
%config %_sysconfdir/bash_completion.d/rbd
%config(noreplace) %_sysconfdir/logrotate.d/ceph
%_sysconfdir/ceph/
%_mandir/man8/ceph-mon.8*
%_mandir/man8/ceph-mds.8*
%_mandir/man8/ceph-osd.8*
%_mandir/man8/mkcephfs.8*
%_mandir/man8/ceph-run.8*
%_mandir/man8/ceph-syn.8*
%_mandir/man8/ceph-dencoder.8*
%_mandir/man8/crushtool.8*
%_mandir/man8/osdmaptool.8*
%_mandir/man8/monmaptool.8*
%_mandir/man8/ceph-conf.8*
%_mandir/man8/ceph.8*
%_mandir/man8/cephfs.8*
%_mandir/man8/mount.ceph.8*
%_mandir/man8/rados.8*
%_mandir/man8/rbd.8*
%_mandir/man8/ceph-rbdnamer.8*
%_mandir/man8/ceph-authtool.8*
%_mandir/man8/ceph-debugpack.8*
%_mandir/man8/ceph-clsinfo.8.gz
%_mandir/man8/librados-config.8.gz
%_localstatedir/ceph/
/var/log/ceph/
%_runtimedir/ceph/

%files obsync
%_bindir/obsync
%_mandir/man1/obsync.1*

%files fuse
%_bindir/ceph-fuse
%_mandir/man8/ceph-fuse.8*

%files devel
%_includedir/cephfs/
%_includedir/crush/
%_includedir/rados/
%_includedir/rbd/
%_libdir/libcephfs.so
%_libdir/librbd.so
%_libdir/librados.so

%files radosgw
%_initdir/ceph-radosgw
%_bindir/radosgw
%_bindir/radosgw-admin
%_mandir/man8/radosgw.8*
%_mandir/man8/radosgw-admin.8*
/usr/sbin/rcceph-radosgw
/var/log/radosgw

%post radosgw
%post_service ceph-radosgw

%preun radosgw
%preun_service ceph-radosgw

%files gcephtool
%_bindir/gceph
%_datadir/ceph_tool/

%files resource-agents
%defattr(0755,root,root,-)
/usr/lib/ocf/resource.d/%name/

%files -n librados2
%_libdir/librados.so.*

%files -n librbd1
%_libdir/librbd.so.*

%files -n libcephfs1
%_libdir/libcephfs.so.*

%files -n python-module-ceph
%python_sitelibdir_noarch/*

%changelog
* Sat Jun 23 2012 Alexei Takaseev <taf@altlinux.org> 0.47.3-alt1
- 0.47.3

* Mon Jun 11 2012 Alexei Takaseev <taf@altlinux.org> 0.47.2-alt1
- Initial build for Sisyphus

