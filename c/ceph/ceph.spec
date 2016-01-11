%define _libexecdir /usr/libexec

Name: ceph
Version: 0.94.5
Release: alt2
Summary: User space components of the Ceph file system
Group: System/Base

Packager: Alexei Takaseev <taf@altlinux.ru>

License: LGPLv2
Url: http://ceph.com/

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: boost-devel-headers gcc-c++ libaio-devel libcurl-devel
BuildRequires: libedit-devel libexpat-devel libfcgi-devel libfuse-devel
BuildRequires: libgperftools-devel libgtkmm2-devel libkeyutils-devel
BuildRequires: libnss-devel libuuid-devel boost-program_options-devel
BuildRequires: libleveldb-devel libsnappy-devel libs3-devel libblkid-devel
BuildRequires: libxfs-devel yasm libudev-devel boost-intrusive-devel

BuildRequires(pre): rpm-build-python

Requires: librados2 = %version-%release
Requires: librbd1 = %version-%release
Requires: lsb-release
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
Requires: libcephfs1 = %version-%release
Requires: librados2 = %version-%release
Requires: librbd1 = %version-%release
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

%package resource-agents
Summary: OCF-compliant resource agents for Ceph daemons
Group: System/Configuration/Other
License: LGPLv2
BuildArch: noarch
Requires: %name = %version-%release
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
%description -n python-module-ceph
This package contains Python libraries for interacting with Cephs RADOS
object storage.

%prep
%setup
%patch0 -p1

rm -rf ceph-object-corpus
ln -s ceph-object-corpus_sub ceph-object-corpus

rm -rf src/civetweb
ln -s civetweb_sub src/civetweb

rm -rf src/erasure-code/jerasure/gf-complete
ln -s gf-complete_sub src/erasure-code/jerasure/gf-complete

rm -rf src/erasure-code/jerasure/jerasure
ln -s jerasure_sub src/erasure-code/jerasure/jerasure

rm -rf src/rocksdb
ln -s rocksdb_sub src/rocksdb

%build
./autogen.sh
export LIBS="$LIBS -lboost_system"
%add_optflags -DHAVE_GPERFTOOLS_PROFILER_H -DHAVE_GPERFTOOLS_HEAP_PROFILER_H -DHAVE_GPERFTOOLS_MALLOC_EXTENSION_H
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

install -dm0755 %buildroot%_unitdir
install -pDm0644 systemd/ceph-mds@.service %buildroot%_unitdir/ceph-mds@.service
install -pDm0644 systemd/ceph-mon@.service %buildroot%_unitdir/ceph-mon@.service
install -pDm0644 systemd/ceph-osd@.service %buildroot%_unitdir/ceph-osd@.service
install -pDm0644 systemd/ceph.target       %buildroot%_unitdir/ceph.target

install -Dpm 644 %name.tmpfiles %buildroot%_tmpfilesdir/%name.conf

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
%_bindir/ceph-brag
%_bindir/ceph-crush-location
%_bindir/ceph-syn
%_bindir/ceph-run
%_bindir/ceph-mon
%_bindir/ceph-mds
%_bindir/ceph-osd
%_bindir/ceph-post-file
%_bindir/ceph-rest-api
%_bindir/ceph-rbdnamer
%_bindir/ceph-dencoder
%_bindir/cephfs-journal-tool
%_bindir/cephfs-table-tool
%_bindir/librados-config
%_bindir/rados
%_bindir/rbd
%_bindir/rbd-replay
%_bindir/rbd-replay-many
%_bindir/ceph-debugpack
%_bindir/ceph-coverage
%_bindir/ceph-objectstore-tool
%_sbindir/ceph-create-keys
%_sbindir/ceph-disk
%_sbindir/ceph-disk-activate
%_sbindir/ceph-disk-prepare
%_sbindir/ceph-disk-udev
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
%config(noreplace) %_tmpfilesdir/*
%_sysconfdir/ceph/
%_mandir/man8/ceph-mon.8*
%_mandir/man8/ceph-mds.8*
%_mandir/man8/ceph-osd.8*
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
%_mandir/man8/rbd-replay-prep.8*
%_mandir/man8/rbd-replay.8*
%_mandir/man8/rbd-replay-many.8*
%_mandir/man8/ceph-rbdnamer.8*
%_mandir/man8/ceph-authtool.8*
%_mandir/man8/ceph-debugpack.8*
%_mandir/man8/ceph-clsinfo.8*
%_mandir/man8/ceph-create-keys.8*
%_mandir/man8/librados-config.8*
%_mandir/man8/ceph-post-file.8*
%_mandir/man8/ceph-rest-api.8*
%_mandir/man8/ceph-disk.8*
%_mandir/man8/ceph-deploy.8*
%_localstatedir/ceph/
/var/log/ceph/
%_runtimedir/ceph/
%_unitdir/ceph-*
%_unitdir/ceph.target
%_libexecdir/ceph/ceph-osd-prestart.sh

%files fuse
%_bindir/ceph-fuse
%_bindir/rbd-fuse
%_sbindir/mount.fuse.ceph
%_mandir/man8/ceph-fuse.8*
%_mandir/man8/rbd-fuse.8*

%files devel
%_includedir/cephfs/
%_includedir/rados/
%_includedir/radosstriper/
%_includedir/rbd/
%_libdir/libcephfs.so
%_libdir/librbd.so
%_libdir/librados.so
%_libdir/libradosstriper.so

%files radosgw
%_initdir/ceph-radosgw
%_bindir/radosgw
%_bindir/radosgw-admin
%_mandir/man8/radosgw.8*
%_mandir/man8/radosgw-admin.8*
/usr/sbin/rcceph-radosgw
/var/log/radosgw

%files resource-agents
%defattr(0755,root,root,-)
/usr/lib/ocf/resource.d/%name/

%files -n librados2
%_libdir/librados.so.*
%_libdir/libradosstriper.so.*

%files -n librbd1
%_libdir/librbd.so.*

%files -n libcephfs1
%_libdir/libcephfs.so.*

%files -n python-module-ceph
%python_sitelibdir_noarch/*

%changelog
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

