# For minor update, merge with new tag, update version in the spec and do gear-update-tag -a
# For major update, checkout new branch upstream-vX.Y, commit .gear dir to it, do git mergs -s ours from gear/sisyphus and build

%define oname glusterfs
%define major 3.12
%define _with_fusermount yes
%define _without_ocf yes
%def_without ganesha

# if you wish to compile an rpm without rdma support, compile like this...
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --without rdma
%{?_without_rdma:%global _without_rdma --disable-ibverbs}

# if you wish to compile an rpm without epoll...
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --without epoll
%{?_without_epoll:%global _without_epoll --disable-epoll}

# if you wish to compile an rpm with fusermount...
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --with fusermount
%{?_with_fusermount:%global _with_fusermount --enable-fusermount}

# if you wish to compile an rpm without geo-replication support, compile like this...
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --without georeplication
%{?_without_georeplication:%global _without_georeplication --disable-geo-replication}

# if you wish to compile an rpm without the OCF resource agents...
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --without ocf
%{?_without_ocf:%global _without_ocf --without-ocf}

Name: glusterfs3
Version: %major.5
Release: alt1

Summary: Cluster File System

License: GPLv2/LGPLv3
Group: System/Base
Url: http://www.gluster.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source0-git: https://github.com/gluster/glusterfs.git
Source0: %name-%version.tar
Source1: glusterd.sysconfig
Source2: %name.watch
Source3: umount.glusterfs

Source4: glusterfs.logrotate

Source7: glusterd.init
Source8: glustereventsd.init


Patch0: %name-%version-%release.patch

%add_verify_elf_skiplist %_libdir/libgfdb.so.0.0.1
%add_verify_elf_skiplist %_libdir/libgfrpc.so.0.0.1
%add_verify_elf_skiplist %_libdir/glusterfs/xlator/mount/fuse.so

%define _init_install() install -D -p -m 0755 %1 %buildroot%_initdir/%2 ;

%define glusterlibdir %_libdir/glusterfs/%version

# manually removed: -static i586-glibc-devel i586-libssl-devel python-module-google python-module-mwlib python-module-oslo.config python-module-oslo.serialization python3 ruby ruby-stdlibs
# Automatically added by buildreq on Sat Jun 13 2015
# optimized out: gnu-config i586-glibc-core i586-glibc-pthread i586-libcrypto10 libcom_err-devel libdevmapper-devel libdevmapper-event libibverbs-devel libkrb5-devel libncurses-devel libssl-devel libtinfo-devel pkg-config python-base python-devel python-module-distribute python-module-oslo.i18n python-module-oslo.utils python-modules python-modules-ctypes python3-base userspace-rcu
BuildRequires: flex glib2-devel glibc-devel-static libacl-devel libaio-devel libattr-devel libdb4-devel liblvm2-devel libreadline-devel libsqlite3-devel libuuid-devel libxml2-devel python-module-cmd2 zlib-devel

BuildPreReq: libssl-devel

BuildPreReq: libuserspace-rcu-devel >= 0.9.1

Conflicts: %oname

Obsoletes: %oname-common < 3.1.0
Provides: %name-common = %version-%release
Provides: %name-core = %version-%release

%description
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package includes the glusterfs binary, the glusterfsd daemon and the
gluster command line, libglusterfs and glusterfs translator modules common to
both GlusterFS server and client framework.

%if 0%{!?_without_rdma:1}
%package rdma
Summary: GlusterFS rdma support for ib-verbs
Group: System/Base
BuildRequires: libibverbs-devel
BuildRequires: librdmacm-devel >= 1.0.19.1-alt1

Requires: %name = %version-%release

%description rdma
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides support to ib-verbs library.
%endif

%if_with ganesha
%package ganesha
Summary: NFS-Ganesha configuration
Group: System/Base
Requires: %name-server = %version-%release
Requires: nfs-ganesha
#Requires:         pcs
AutoReq: yes,noshell

%description ganesha
GlusterFS is a distributed file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the configuration and related files for using
NFS-Ganesha as the NFS server using GlusterFS.
%endif

%if 0%{!?_without_georeplication:1}
%package geo-replication
Summary: GlusterFS Geo-replication
Group: System/Base
Requires: %name = %version-%release
Requires: python-modules-ctypes, rsync >= 3.0.0

%description geo-replication
GlusterFS is a clustered file-system capable of scaling to several
peta-bytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file system in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in userspace and easily manageable.

This package provides support to geo-replication.
%endif

%package client
Summary: GlusterFS client
Group: System/Base
BuildRequires: libfuse-devel

Requires: %name = %version-%release

Obsoletes: %name-client < 3.1.0
Provides: %name-client = %version-%release

%description client
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides support to FUSE based clients.

%package -n lib%name-api
Summary: GlusterFS api library
Group: System/Libraries
#Requires: %name = %version-%release
#Requires:         %name-client-xlators = %version-%release

%description -n lib%name-api
GlusterFS is a distributed file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the glusterfs libgfapi library.

%package -n lib%name-api-devel
Summary: Development libraries for GlusterFS api library
Group: Development/Other
Requires: lib%name-api = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-api-devel
GlusterFS is a distributed file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the api include files.

%package server
Summary: Clustered file-system server
Group: System/Servers
Requires: %name = %version-%release
Requires: %name-client = %version-%release

%description server
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the glusterfs server daemon.

%package events
Summary: GlusterFS Events
Group: System/Servers
Requires: %name = %version-%release
Requires: python-module-%name = %version-%release

%description events
GlusterFS Events

%package vim
Summary: Vim syntax file
Group: Editors
Requires: vim-common
BuildArch: noarch

%description vim
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

Vim syntax file for GlusterFS.

%package -n lib%name-devel
Summary: Development Libraries
Group: Development/Other
Requires: lib%name = %version-%release
Requires: lib%name-api-devel = %version-%release
Conflicts: %oname-devel
Obsoletes: %name-devel < %version-%release
Provides: %name-devel = %version-%release

%description -n lib%name-devel
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the development libraries.

%package -n python-module-%name
Summary: Python module for %name
Group: Development/Python
BuildArch: noarch
%setup_python_module %name

%description -n python-module-%name
This package provides Python API for %name

%package -n lib%name
Summary: GlusterFS common libraries
Group: System/Base
Obsoletes: %oname-libs <= 2.0.0
Obsoletes: %name-libs
Provides: %name-libs = %version-%release

%description -n lib%name
GlusterFS is a distributed file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the base GlusterFS libraries.

%prep
%setup
%patch0 -p1
# due _libexecdir is /usr/lib
%__subst "s|/libexec/glusterfs|/lib/glusterfs|" ./configure.ac
# see build-aux/pkg-version
echo "v%version-%release" >VERSION

%build
# need from build from git repo (but incorporated in tarballs)
./autogen.sh
%configure  %{?_without_rdma} %{?_without_epoll} %{?_with_fusermount} %{?_without_georeplication} \
%{?_without_ocf} \
            --with-systemddir=%_unitdir \
            --localstatedir=/var/ \
            --libexecdir=%_libexecdir \
            --enable-qemu-block \
            --enable-bd-xlator

# Remove rpath
%__subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%__subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%makeinstall_std
# Install include directory
mkdir -p %buildroot%_includedir/glusterfs
install -p -m 0644 libglusterfs/src/*.h \
%buildroot%_includedir/glusterfs/
install -p -m 0644 contrib/uuid/*.h \
%buildroot%_includedir/glusterfs/
# Following needed by hekafs multi-tenant translator
mkdir -p %buildroot%_includedir/glusterfs/rpc
install -p -m 0644 rpc/rpc-lib/src/*.h \
%buildroot%_includedir/glusterfs/rpc/
install -p -m 0644 rpc/xdr/src/*.h \
%buildroot%_includedir/glusterfs/rpc/
mkdir -p %buildroot%_includedir/glusterfs/server
install -p -m 0644 xlators/protocol/server/src/*.h \
%buildroot%_includedir/glusterfs/server/
# We'll use our init.d
rm -f %buildroot/etc/init.d/glusterd

# Create logging directory
mkdir -p %buildroot%_logdir/glusterfs/

# Remove unwanted files from all the shared libraries
find %buildroot%_libdir -name '*.a' -delete
find %buildroot%_libdir -name '*.la' -delete

# Remove installed docs, we include them ourselves as %%doc
rm -rf %buildroot%_docdir/glusterfs/
# move binary from datadir to bindir
mv %buildroot%_datadir/glusterfs/scripts/gsync-sync-gfid %buildroot%_bindir/

# Rename the samples, so we can include them as %%config
#for file in %buildroot%_sysconfdir/glusterfs/*.sample; do
#  mv ${file} `dirname ${file}`/`basename ${file} .sample`
#done

# Remove wrong placed confs
for file in glusterfs-georep-logrotate glusterfs-logrotate; do
  rm -v %buildroot%_sysconfdir/glusterfs/${file}
done

# Create working directory
mkdir -p %buildroot%_sharedstatedir/glusterd/

# Update configuration file to /var/lib working directory
%__subst 's|option working-directory %_sysconfdir/glusterd|option working-directory %_sharedstatedir/glusterd|g' \
    %buildroot%_sysconfdir/glusterfs/glusterd.vol

install -D -m644 extras/systemd/glusterd.service %buildroot/%_unitdir/glusterd.service
install -D -m644 extras/systemd/glustereventsd.service %buildroot/%_unitdir/glustereventsd.service

# Install init script and sysconfig file
%_init_install %SOURCE7 glusterd
%_init_install %SOURCE8 glustereventsd
install -D -p -m 0644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/glusterd
# Install wrapper umount script
install -D -p -m 0755 %SOURCE3 %buildroot/sbin/umount.glusterfs

%if 0%{!?_without_georeplication:1}
install -D -p -m 0644 extras/glusterfs-georep-logrotate %buildroot%_sysconfdir/logrotate.d/glusterfs-georep
%endif
install -D -p -m 0644 %SOURCE4 %buildroot%_sysconfdir/logrotate.d/glusterfs

install -D -p -m 644 extras/glusterfs.vim \
%buildroot%_datadir/vim/vimfiles/syntax/glusterfs.vim

%if 0%{?_without_ocf:1}
rm -rf %buildroot%_libexecdir/ocf/
%endif

rm -rf %buildroot%_sbindir/conf.py

# TODO: selinux
# rm HACK due S10selinux-label-brick.sh: line 46: syntax error near unexpected token `('
rm -fv %buildroot%_sharedstatedir/glusterd/hooks/1/create/post/S10selinux-label-brick.sh
# drop req on policycoreutils (semanage)
rm -fv %buildroot%_sharedstatedir/glusterd/hooks/1/delete/pre/S10selinux-del-fcontext.sh

# TODO: move common part to -common?
%files
%doc ChangeLog INSTALL README.md THANKS COPYING-GPLV2 COPYING-LGPLV3
%_bindir/glusterfind

# cli
%_sbindir/gluster
%_sbindir/gluster-setgfid2path
%_man8dir/gluster.*
%_man8dir/gluster-setgfid2path.*

%glusterlibdir/rpc-transport/
%glusterlibdir/auth/
%glusterlibdir/xlator/
%exclude %glusterlibdir/xlator/mount/api.so
%_libexecdir/glusterfs/glusterfind/
%_sbindir/gfind_missing_files
%_libexecdir/glusterfs/gfind_missing_files/
%_sbindir/gcron.py
%_sbindir/snap_scheduler.py
%exclude %glusterlibdir/xlator/mount/fuse*
%_logdir/glusterfs/
%exclude %_man8dir/mount.glusterfs.8*
%if 0%{!?_without_rdma:1}
%exclude %glusterlibdir/rpc-transport/rdma*
%endif

%if 0%{!?_without_rdma:1}
%files rdma
%glusterlibdir/rpc-transport/rdma*
%endif

%if 0%{!?_without_georeplication:1}
%files geo-replication
%dir %_libexecdir/glusterfs/
%_libexecdir/glusterfs/gsyncd
%dir %_libexecdir/glusterfs/python/
%_libexecdir/glusterfs/gverify.sh
%_libexecdir/glusterfs/peer_add_secret_pub
%_libexecdir/glusterfs/peer_gsec_create
%_libexecdir/glusterfs/python/syncdaemon/
%_libexecdir/glusterfs/set_geo_rep_pem_keys.sh
%_datadir/glusterfs/scripts/get-gfid.sh
%_datadir/glusterfs/scripts/slave-upgrade.sh
%_datadir/glusterfs/scripts/gsync-upgrade.sh
%_datadir/glusterfs/scripts/generate-gfid-file.sh
%_datadir/glusterfs/scripts/schedule_georep.py
%_bindir/gsync-sync-gfid
%_libexecdir/glusterfs/peer_georep-sshkey.py
%_libexecdir/glusterfs/peer_mountbroker
%_libexecdir/glusterfs/peer_mountbroker.py
%_sbindir/gluster-georep-sshkey
%_sbindir/gluster-mountbroker
%config(noreplace) %_sysconfdir/logrotate.d/glusterfs-georep
%endif

%files -n lib%name-api
# libgfapi files
%_libdir/libgfapi.so.*
%glusterlibdir/xlator/mount/api.so

%files -n lib%name-api-devel
%_pkgconfigdir/glusterfs-api.pc
%_libdir/libgfapi.so
%_includedir/glusterfs/api/

%files client
# CHECKME: glusterfs is a symlink to glusterfsd, -server depends on -client.
%_sbindir/glusterfs
%_sbindir/glusterfsd
%_man8dir/glusterfs.8*
%_man8dir/glusterfsd.8*
%config(noreplace) %_sysconfdir/logrotate.d/glusterfs
%glusterlibdir/xlator/mount/fuse*
%_man8dir/mount.glusterfs.8*
/sbin/mount.glusterfs
/sbin/umount.glusterfs
%if 0%{?_with_fusermount:1}
%_bindir/fusermount-glusterfs
%endif

%files server
%_sbindir/glusterd
%_man8dir/glusterd.8*
%_initdir/glusterd
%_unitdir/glusterd.service
%config(noreplace) %_sysconfdir/sysconfig/glusterd
%dir %_sysconfdir/glusterfs/
%config(noreplace) %_sysconfdir/glusterfs/*
%exclude %_sysconfdir/glusterfs/eventsconfig.json

%_sharedstatedir/glusterd/
%exclude %_sharedstatedir/glusterd/events/

%_sbindir/glfsheal
%_sbindir/gf_attach
%_libdir/libgfdb.so.*

%dir %_datadir/glusterfs/scripts/

%_datadir/glusterfs/scripts/post-upgrade-script-for-quota.sh
%_datadir/glusterfs/scripts/pre-upgrade-script-for-quota.sh
%_datadir/glusterfs/scripts/stop-all-gluster-processes.sh

%if 0%{!?_without_ocf:1}
%dir %_libexecdir/ocf/resource.d/
%_libexecdir/ocf/resource.d/glusterfs/
%endif

%if_with ganesha
%files ganesha
%dir /etc/ganesha/
%config(noreplace) /etc/ganesha/ganesha-ha.conf.sample
%_libexecdir/ganesha/create-export-ganesha.sh
#%_libexecdir/ganesha/copy-export-ganesha.sh
%_libexecdir/ganesha/dbus-send.sh
%_libexecdir/ganesha/ganesha-ha.sh
%_libexecdir/ganesha/generate-epoch.py
%if 0%{!?_without_ocf:1}
%_libexecdir/ocf/resource.d/heartbeat/
%endif
%endif

# Events
%files events
%config(noreplace) %_sysconfdir/glusterfs/eventsconfig.json
%dir %attr(0755,-,-) %_sharedstatedir/glusterd/events/
%_libexecdir/glusterfs/events/
%_libexecdir/glusterfs/peer_eventsapi.py*
%_sbindir/glustereventsd
%_sbindir/gluster-eventsapi
%_datadir/glusterfs/scripts/eventsdash.py*
%_unitdir/glustereventsd.service
%_initdir/glustereventsd

%files vim
%doc COPYING-GPLV2 COPYING-LGPLV3
%_datadir/vim/vimfiles/syntax/glusterfs.vim

%files -n lib%name-devel
%_includedir/glusterfs/
%exclude %_includedir/glusterfs/api/
%exclude %_includedir/glusterfs/y.tab.h
%_libdir/libgfchangelog.so
%_libdir/libgfrpc.so
%_libdir/libgfxdr.so
%_libdir/libgfdb.so
%_libdir/libglusterfs.so
%_pkgconfigdir/libgfchangelog.pc
# pkgconfiglib.req: WARNING: /tmp/.private/lav/glusterfs3-buildroot/usr/lib64/pkgconfig/libgfdb.pc: cannot find -lgfchangedb library path (skip)
%_pkgconfigdir/libgfdb.pc

%files -n lib%name

# until we got -common subpackage
%dir %_libdir/glusterfs/
%dir %glusterlibdir/
%dir %_datadir/glusterfs/
%dir %_libexecdir/glusterfs/

%_libdir/libgfchangelog.so.*
%_libdir/libgfrpc.so.*
%_libdir/libgfxdr.so.*
%_libdir/libglusterfs.so.*

%files -n python-module-%name
%python_sitelibdir_noarch/*

%post server
%post_service glusterd

%preun server
%preun_service glusterd

%changelog
* Sat Jan 20 2018 Vitaly Lipatov <lav@altlinux.ru> 3.12.5-alt1
- new version 3.12.5 (with rpmrb script)

* Sun Dec 17 2017 Vitaly Lipatov <lav@altlinux.ru> 3.12.4-alt1
- new version 3.12.4 (with rpmrb script)

* Sun Dec 17 2017 Vitaly Lipatov <lav@altlinux.ru> 3.12.3-alt2
- move peer_mountbroker to its place in georeplication subpackage
- remove logrotate files from /etc/glusterd

* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 3.12.3-alt1
- new version 3.12.3 (with rpmrb script)
- drop ganesha subpackage

* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 3.12.0-alt1
- build LTE branch 3.12

* Sun Nov 12 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.7-alt3.1
- autorebuild with libuserspace-rcu.git=0.10.0-alt1

* Sat Nov 11 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.7-alt3
- rearrange logrotate files

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.7-alt2
- small fixes, pack dirs

* Sun Nov 05 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.7-alt1
- new version 3.10.7 (with rpmrb script)

* Tue Aug 29 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.5-alt1
- new version 3.10.5 (with rpmrb script)

* Mon Jul 24 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.4-alt2
- change the max of rda-cache-limit to INFINITY (RHbug# 1473968)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.4-alt1
- new version 3.10.4 (with rpmrb script)

* Sun Jun 11 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.3-alt1
- new version 3.10.3 (with rpmrb script)

* Wed May 17 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.2-alt1
- new version 3.10.2

* Wed Apr 05 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.1-alt1
- new version 3.10.1 (with rpmrb script)

* Tue Mar 21 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.0-alt2
- add build fix from https://bugzilla.redhat.com/show_bug.cgi?id=1429696

* Mon Mar 06 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.0-alt1
- build LTE branch 3.10

* Thu Jan 26 2017 Vitaly Lipatov <lav@altlinux.ru> 3.9.1-alt2
- fix hangs on 32 bit systems (eterbug #11620, RHbug# 1416684)

* Mon Jan 23 2017 Vitaly Lipatov <lav@altlinux.ru> 3.9.1-alt1
- new version 3.9.1 (with rpmrb script)

* Wed Nov 23 2016 Vitaly Lipatov <lav@altlinux.ru> 3.9.0-alt1
- build 3.9.0 version

* Sun Oct 02 2016 Vitaly Lipatov <lav@altlinux.ru> 3.8.4-alt1
- new bugfix release (3.8.4) with rpmgs script

* Fri Sep 02 2016 Vitaly Lipatov <lav@altlinux.ru> 3.8.3-alt1
- new version (3.8.3) with rpmgs script

* Thu Aug 11 2016 Vitaly Lipatov <lav@altlinux.ru> 3.8.2-alt1
- new version 3.8.2 - 2nd update to the 3.8 Long-Term-Maintenance version

* Mon Jul 25 2016 Vitaly Lipatov <lav@altlinux.ru> 3.8.1-alt2
- fix build with nfs-ganesha

* Sun Jul 10 2016 Vitaly Lipatov <lav@altlinux.ru> 3.8.1-alt1
- new version 3.8.1

* Mon Jun 20 2016 Vitaly Lipatov <lav@altlinux.ru> 3.8.0-alt0
- build around 3.8.0 version from 3.8 branch

* Sat May 21 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.11-alt3
- set correct build version

* Tue Apr 19 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.11-alt2
- fix packing
- pack correct version of systemd service

* Tue Apr 19 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.11-alt1
- new version 3.7.11

* Tue Mar 22 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.9-alt1
- new version 3.7.9

* Thu Feb 25 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.8-alt2
- rebuild with libuserspace-icu 0.9.1

* Tue Feb 23 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.8-alt1
- new version 3.7.8

* Mon Nov 23 2015 Vitaly Lipatov <lav@altlinux.ru> 3.7.6-alt1
- new version 3.7.6

* Sat Oct 17 2015 Vitaly Lipatov <lav@altlinux.ru> 3.7.5-alt2
- fix ganesha requires

* Sat Oct 17 2015 Vitaly Lipatov <lav@altlinux.ru> 3.7.5-alt1
- new version 3.7.5

* Mon Aug 10 2015 Vitaly Lipatov <lav@altlinux.ru> 3.7.3-alt1
- new version 3.7.3

* Tue Jun 23 2015 Vitaly Lipatov <lav@altlinux.ru> 3.7.2-alt1
- new version 3.7.2
- drop fake glusterfs3-devel package

* Mon Jun 15 2015 Vitaly Lipatov <lav@altlinux.ru> 3.7.1-alt6
- add fake glusterfs3-devel package (try to fix pkgconfig(glusterfs-api) provide problem)

* Mon Jun 15 2015 Vitaly Lipatov <lav@altlinux.ru> 3.7.1-alt5
- buildreq librdmacm-devel only if built with rdma
- move ALT build specific files to .gear
- fix interpackages requires

* Sun Jun 14 2015 Vitaly Lipatov <lav@altlinux.ru> 3.7.1-alt4
- backport patch glusterd: Buffer overflow causing crash for glusterd

* Sun Jun 14 2015 Vitaly Lipatov <lav@altlinux.ru> 3.7.1-alt3
- separate libs to libglusterfs3 (-devel) packages
- separate nfs part to -ganesha subpackage
- separate api to libglusterfs3-api (-devel) packages

* Fri Jun 12 2015 Vitaly Lipatov <lav@altlinux.ru> 3.7.1-alt2
- fix build, pack all new files
- update buildreqs

* Thu Jun 04 2015 Danil Mikhailov <danil@altlinux.org> 3.7.1-alt1
- new version 3.7.1

* Tue Jun 02 2015 Danil Mikhailov <danil@altlinux.org> 3.7.0-alt3
- Added glfsheal command

* Thu May 14 2015 Danil Mikhailov <danil@altlinux.org> 3.7.0-alt1
- new version 3.7.0

* Tue May 12 2015 Danil Mikhailov <danil@altlinux.org> 3.6.3-alt1
- new version 3.6.3 (closes: #30957)

* Wed Feb 04 2015 Anton Farygin <rider@altlinux.ru> 3.6.2-alt1
- new version (closes: #30699)

* Mon Jan 12 2015 Anton Farygin <rider@altlinux.ru> 3.6.1-alt1
- new version

* Thu Nov 13 2014 Anton Farygin <rider@altlinux.ru> 3.5.3-alt1
- new version

* Fri Aug 29 2014 Anton Farygin <rider@altlinux.ru> 3.5.2-alt2
- new version

* Mon Jul 07 2014 Anton Farygin <rider@altlinux.ru> 3.5.1-alt2
- initscript: start glusterd before netfs

* Tue Jul 01 2014 Anton Farygin <rider@altlinux.ru> 3.5.1-alt1
- new version

* Mon Jun 30 2014 Anton Farygin <rider@altlinux.ru> 3.5.0-alt2
- add patch from Anton Agapov (closes: #30089) :
    - left only one glusterd service
    - include correct logdir in package (closes: #29191)

* Thu Jun 19 2014 Anton Farygin <rider@altlinux.ru> 3.5.0-alt1
- new version
- build with linux AIO

* Sat Apr 12 2014 Alexei Takaseev <taf@altlinux.org> 3.4.3-alt1
- 3.4.3

* Sat Feb 15 2014 Alexei Takaseev <taf@altlinux.org> 3.4.2-alt1
- 3.4.2


* Wed Jul 17 2013 Alexei Takaseev <taf@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Jan 23 2013 Alexei Takaseev <taf@altlinux.org> 3.3.1-alt1
- 3.3.1

* Mon Nov 19 2012 Alexei Takaseev <taf@altlinux.org> 3.3.0-alt1
- 3.3.0

* Tue Aug 28 2012 Repocop Q. A. Robot <repocop@altlinux.org> 3.2.5-alt5.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * vendor-tag for glusterfs3-geo-replication
  * vendor-tag for glusterfs3-rdma-debuginfo
  * vendor-tag for glusterfs3-client
  * vendor-tag for glusterfs3-server
  * vendor-tag for glusterfs3
  * vendor-tag for glusterfs3-debuginfo
  * vendor-tag for glusterfs3-devel
  * vendor-tag for glusterfs3-client-debuginfo
  * vendor-tag for glusterfs3-vim
  * vendor-tag for glusterfs3-rdma
  * postclean-03-private-rpm-macros for the spec file
  * postclean-05-filetriggers for the spec file

* Wed Mar 28 2012 Denis Baranov <baraka@altlinux.ru> 3.2.5-alt5
- fix requires for package

* Tue Mar 27 2012 Denis Baranov <baraka@altlinux.ru> 3.2.5-alt4
- rename package and correct log directory

* Sat Mar 17 2012 Denis Baranov <baraka@altlinux.ru> 3.2.5-alt3
- Fix error with initial enviroment

* Tue Mar 13 2012 Denis Baranov <baraka@altlinux.ru> 3.2.5-alt2
- Fix error in init script

* Mon Nov 21 2011 Denis Baranov <baraka@altlinux.ru> 3.2.5-alt1
- initial build for ALT Linux Sisyphus

* Thu Nov 17 2011 Kaleb S. KEITHLEY <kkeithle@redhat.com> - 3.2.5-1
- Update to 3.2.5

* Wed Nov 16 2011 Kaleb S. KEITHLEY <kkeithle@redhat.com> - 3.2.4-3
- revised init.d/systemd to minimize fedora < 17
- get closer to the official glusterfs spec, including...
- add geo-replication, which should have been there since 3.2

* Wed Nov 2 2011 Kaleb S. KEITHLEY <kkeithle@redhat.com> - 3.2.4-2
- Convert init.d to systemd for f17 and later

* Fri Sep 30 2011 Kaleb S. KEITHLEY <kkeithle@redhat.com> - 3.2.4-1
- Update to 3.2.4

* Mon Aug 22 2011 Kaleb S. KEITHLEY <kkeithle@redhat.com> - 3.2.3-1
- Update to 3.2.3

* Mon Aug 22 2011 Kaleb S. KEITHLEY <kkeithle@redhat.com> - 3.2.2-1
- Update to 3.2.2

* Fri Aug 19 2011 Kaleb S. KEITHLEY <kkeithle@redhat.com> - 3.2.2-0
- Update to 3.2.2

* Wed Jun 29 2011 Dan Horák <dan[at]danny.cz> - 3.2.1-3
- disable InfiniBand on s390(x) unconditionally

* Thu Jun 16 2011 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.2.1-2
- Fix Source0 URL

* Thu Jun 16 2011 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1

* Tue Jun 01 2011 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Tue May 10 2011 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.1.4-1
- Update to 3.1.4

* Sun Mar 19 2011 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3
- Merge in more upstream SPEC changes
- Remove patches from GlusterFS bugzilla #2309 and #2311
- Remove inode-gen.patch

* Sun Feb 06 2011 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.1.2-3
- Add back in legacy SPEC elements to support older branches

* Tue Feb 03 2011 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.1.2-2
- Add patches from CloudFS project

* Tue Jan 25 2011 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.1.2-1
- Update to 3.1.2

* Wed Jan 5 2011 Dan Horák <dan[at]danny.cz> - 3.1.1-3
- no InfiniBand on s390(x)

* Sat Jan 1 2011 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.1.1-2
- Update to support readline
- Update to not parallel build

* Mon Dec 27 2010 Silas Sewell <silas@sewell.ch> - 3.1.1-1
- Update to 3.1.1
- Change package names to mirror upstream

* Mon Dec 20 2010 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.0.7-1
- Update to 3.0.7

* Wed Jul 28 2010 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.0.5-1
- Update to 3.0.x

* Sat Apr 10 2010 Jonathan Steffan <jsteffan@fedoraproject.org> - 2.0.9-2
- Move python version requires into a proper BuildRequires otherwise
  the spec always turned off python bindings as python is not part
  of buildsys-build and the chroot will never have python unless we
  require it
- Temporarily set -D_FORTIFY_SOURCE=1 until upstream fixes code
  GlusterFS Bugzilla #197 (#555728)
- Move glusterfs-volgen to devel subpackage (#555724)
- Update description (#554947)

* Sat Jan 2 2010 Jonathan Steffan <jsteffan@fedoraproject.org> - 2.0.9-1
- Update to 2.0.9

* Sat Nov 8 2009 Jonathan Steffan <jsteffan@fedoraproject.org> - 2.0.8-1
- Update to 2.0.8
- Remove install of glusterfs-volgen, it's properly added to
  automake upstream now

* Sat Oct 31 2009 Jonathan Steffan <jsteffan@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7
- Install glusterfs-volgen, until it's properly added to automake
  by upstream
- Add macro to be able to ship more docs

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> 2.0.6-2
- Rebuilt with new fuse

* Sat Sep 12 2009 Matthias Saou <http://freshrpms.net/> 2.0.6-1
- Update to 2.0.6.
- No longer default to disable the client on RHEL5 (#522192).
- Update spec file URLs.

* Mon Jul 27 2009 Matthias Saou <http://freshrpms.net/> 2.0.4-1
- Update to 2.0.4.

* Thu Jun 11 2009 Matthias Saou <http://freshrpms.net/> 2.0.1-2
- Remove libglusterfs/src/y.tab.c to fix koji F11/devel builds.

* Sat May 16 2009 Matthias Saou <http://freshrpms.net/> 2.0.1-1
- Update to 2.0.1.

* Thu May  7 2009 Matthias Saou <http://freshrpms.net/> 2.0.0-1
- Update to 2.0.0 final.

* Wed Apr 29 2009 Matthias Saou <http://freshrpms.net/> 2.0.0-0.3.rc8
- Move glusterfsd to common, since the client has a symlink to it.

* Fri Apr 24 2009 Matthias Saou <http://freshrpms.net/> 2.0.0-0.2.rc8
- Update to 2.0.0rc8.

* Sun Apr 12 2009 Matthias Saou <http://freshrpms.net/> 2.0.0-0.2.rc7
- Update glusterfsd init script to the new style init.
- Update files to match the new default vol file names.
- Include logrotate for glusterfsd, use a pid file by default.
- Include logrotate for glusterfs, using killall for lack of anything better.

* Sat Apr 11 2009 Matthias Saou <http://freshrpms.net/> 2.0.0-0.1.rc7
- Update to 2.0.0rc7.
- Rename "libs" to "common" and move the binary, man page and log dir there.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Matthias Saou <http://freshrpms.net/> 2.0.0-0.1.rc1
- Update to 2.0.0rc1.
- Include new libglusterfsclient.h.

* Mon Feb 16 2009 Matthias Saou <http://freshrpms.net/> 1.3.12-1
- Update to 1.3.12.
- Remove no longer needed ocreat patch.

* Thu Jul 17 2008 Matthias Saou <http://freshrpms.net/> 1.3.10-1
- Update to 1.3.10.
- Remove mount patch, it's been included upstream now.

* Fri May 16 2008 Matthias Saou <http://freshrpms.net/> 1.3.9-1
- Update to 1.3.9.

* Fri May  9 2008 Matthias Saou <http://freshrpms.net/> 1.3.8-1
- Update to 1.3.8 final.

* Tue Apr 23 2008 Matthias Saou <http://freshrpms.net/> 1.3.8-0.10
- Include short patch to include fixes from latest TLA 751.

* Mon Apr 22 2008 Matthias Saou <http://freshrpms.net/> 1.3.8-0.9
- Update to 1.3.8pre6.
- Include glusterfs binary in both the client and server packages, now that
  glusterfsd is a symlink to it instead of a separate binary.

* Sun Feb  3 2008 Matthias Saou <http://freshrpms.net/> 1.3.8-0.8
- Add python version check and disable bindings for version < 2.4.

* Sun Feb  3 2008 Matthias Saou <http://freshrpms.net/> 1.3.8-0.7
- Add --without client rpmbuild option, make it the default for RHEL (no fuse).
  (I hope "rhel" is the proper default macro name, couldn't find it...)

* Wed Jan 30 2008 Matthias Saou <http://freshrpms.net/> 1.3.8-0.6
- Add --without ibverbs rpmbuild option to the package.

* Mon Jan 14 2008 Matthias Saou <http://freshrpms.net/> 1.3.8-0.5
- Update to current TLA again, patch-636 which fixes the known segfaults.

* Thu Jan 10 2008 Matthias Saou <http://freshrpms.net/> 1.3.8-0.4
- Downgrade to glusterfs--mainline--2.5--patch-628 which is more stable.

* Tue Jan  8 2008 Matthias Saou <http://freshrpms.net/> 1.3.8-0.3
- Update to current TLA snapshot.
- Include umount.glusterfs wrapper script (really needed? dunno).
- Include patch to mount wrapper to avoid multiple identical mounts.

* Sun Dec 30 2007 Matthias Saou <http://freshrpms.net/> 1.3.8-0.1
- Update to current TLA snapshot, which includes "volume-name=" fstab option.

* Mon Dec  3 2007 Matthias Saou <http://freshrpms.net/> 1.3.7-6
- Re-add the /var/log/glusterfs directory in the client sub-package (required).
- Include custom patch to support vol= in fstab for -n glusterfs client option.

* Mon Nov 26 2007 Matthias Saou <http://freshrpms.net/> 1.3.7-4
- Re-enable libibverbs.
- Check and update License field to GPLv3+.
- Add glusterfs-common obsoletes, to provide upgrade path from old packages.
- Include patch to add mode to O_CREATE opens.

* Thu Nov 22 2007 Matthias Saou <http://freshrpms.net/> 1.3.7-3
- Remove Makefile* files from examples.
- Include RHEL/Fedora type init script, since the included ones don't do.

* Wed Nov 21 2007 Matthias Saou <http://freshrpms.net/> 1.3.7-1
- Major spec file cleanup.
- Add misssing %%clean section.
- Fix ldconfig calls (weren't set for the proper sub-package).

* Sat Aug 4 2007 Matt Paine <matt@mattsoftware.com> - 1.3.pre7
- Added support to build rpm without ibverbs support (use --without ibverbs
  switch)

* Sun Jul 15 2007 Matt Paine <matt@mattsoftware.com> - 1.3.pre6
- Initial spec file
