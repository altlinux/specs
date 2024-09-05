%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define _runtimedir /run
%define _libexecdir %_prefix/libexec

%define on_off_switch() %{expand:%%{?_with_%{1}:ON}%%{!?_with_%{1}:OFF}}

%def_with nfsidmap
%def_with nullfs
%def_with mem
%def_without gpfs
%def_without xfs
%def_without lustre
%ifnarch %ix86 %arm %mips32 ppc
%def_with ceph
%def_with rgw
%def_with rados_recov
%def_with rados_urls
%def_with gluster
%else
%def_without ceph
%def_without rgw
%def_without rados_recov
%def_without rados_urls
%def_without gluster
%endif
%def_without kvsfs
%def_without rdma
%def_without 9P
%def_without 9P_rdma
%def_without jemalloc
%def_without lttng
%def_without saunafs
%def_without lizardfs
%def_with utils
%def_with gui_utils
%def_with system_ntirpc
%def_with man_page
%def_with rpcbind
%def_with mspac_support
%def_without monitoring_support
%def_without legacy_python_install

Name: nfs-ganesha
Version: 6.0
Release: alt1
Summary: NFS-Ganesha is a NFS Server running in user space
Group: System/Servers
License: LGPL-3.0-or-later
Url: https://github.com/nfs-ganesha/nfs-ganesha/wiki
Vcs: https://github.com/nfs-ganesha/nfs-ganesha.git
Source: %name-%version.tar
Source1: libntirpc-0.tar
Source2: prometheus-cpp-lite-0.tar
Patch: %name-%version.patch

Requires: dbus
Requires: nfs-utils
%{?_with_rpcbind:Requires: rpcbind}

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd
BuildRequires: cmake gcc-c++ ninja-build
BuildRequires: bison
BuildRequires: flex
BuildRequires: libunwind-devel
BuildRequires: libkrb5-devel
BuildRequires: libdbus-devel
BuildRequires: libcap-devel
BuildRequires: libblkid-devel
BuildRequires: libuuid-devel
BuildRequires: libnsl2-devel
BuildRequires: libattr-devel libacl-devel
%{?_with_system_ntirpc:BuildRequires: libntirpc-devel >= 3.3}
BuildRequires: libuserspace-rcu-devel
BuildRequires: /usr/bin/sphinx-build-3
%{?_with_mspac_support:BuildRequires: libwbclient-devel}
%{?_with_monitoring_support:BuildRequires: libcurl-devel zlib-ng-devel civetweb-devel libprometheus-cpp-devel}
%{?_with_rados_recov:BuildRequires: librados-devel >= 0.61}
%{?_with_rados_urls:BuildRequires: librados-devel >= 0.61}
%{?_with_ceph:BuildRequires: libcephfs-devel >= 12.2.0}
%{?_with_rgw:BuildRequires: librgw-devel >= 12.2.0}
%{?_with_nfsidmap:BuildRequires: libnfsidmap-devel}
%{?_with_rdma:BuildRequires: rdma-core-devel}
%{?_with_9P_rdma:BuildRequires: libmooshika-devel}
%{?_with_jemalloc:BuildRequires: libjemalloc-devel}
%{?_with_gluster:BuildRequires: pkgconfig(glusterfs-api) >= 7.6.6}
%{?_with_xfs:BuildRequires: libxfs-devel}
%{?_with_lttng:BuildRequires: lttng-ust-devel >= 2.3}
%{?_with_kvsfs:BuildRequires: libkvsns-devel >= 1.2.0}
%{?_with_saunafs:BuildRequires: libsaunafs-devel}
%{?_with_lizardfs:BuildRequires: liblizardfs-client-devel}
%if_with utils
BuildRequires: python3-module-setuptools
%{?_without_legacy_python_install:BuildRequires: python3-module-wheel python3-module-build python3-module-installer}
%{?_with_gui_utils:BuildRequires: python3-module-PyQt5-devel}
%endif

%description
nfs-ganesha : NFS-GANESHA is a NFS Server running in user space.
It comes with various back-end modules (called FSALs) provided as
shared objects to support different file systems and name-spaces.

%package mount-9P
Summary: a 9p mount helper
Group: System/Servers

%description mount-9P
This package contains the mount.9P script that clients can use
to simplify mounting to NFS-GANESHA. This is a 9p mount helper.

%package vfs
Summary: The NFS-GANESHA's VFS FSAL
Group: System/Servers
Requires: %name = %EVR

%description vfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support VFS based filesystems

%package proxy-v4
Summary: The NFS-GANESHA PROXY_V4 FSAL
Group: System/Servers
Requires: %name = %EVR

%description proxy-v4
This package contains a FSAL shared object to
be used with NFS-Ganesha to support PROXY_V4 based filesystems

%package proxy-v3
Summary: The NFS-GANESHA PROXY_V3 FSAL
Group: System/Servers
Requires: %name = %EVR

%description proxy-v3
This package contains a FSAL shared object to
be used with NFS-Ganesha to support PROXY_V3 based filesystems

%package utils
Summary: The NFS-GANESHA's util
Group: Networking/Other
BuildArch: noarch

%description utils
This package contains utility scripts for managing the NFS-GANESHA server

%package utils-gui
Summary: The NFS-GANESHA's GUI util
Group: Networking/Other
BuildArch: noarch

%description utils-gui
This package contains GUI utility scripts for managing the NFS-GANESHA server

%package lttng
Summary: The NFS-GANESHA's library for use with LTTng
Group: System/Servers
Requires: liblttng-ust >= 2.3
Requires: %name = %EVR

%description lttng
This package contains the libganesha_trace.so library. When preloaded
to the ganesha.nfsd server, it makes it possible to trace using LTTng.

# NULL
%package nullfs
Summary: The NFS-GANESHA's NULLFS Stackable FSAL
Group: System/Servers
Requires: %name = %EVR

%description nullfs
This package contains a Stackable FSAL shared object to be used with NFS-Ganesha.
This is mostly a template for future (more sophisticated) stackable FSALs

# MEM
%package mem
Summary: The NFS-GANESHA Memory backed testing FSAL
Group: System/Servers
Requires: %name = %EVR

%description mem
This package contains a FSAL shared object to be used with NFS-Ganesha. This
is used for speed and latency testing.

# GPFS
%package gpfs
Summary: The NFS-GANESHA's GPFS FSAL
Group: System/Servers
Requires: %name = %EVR

%description gpfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support GPFS backend

# CEPH
%package ceph
Summary: The NFS-GANESHA's CEPH FSAL
Group: System/Servers
Requires: %name = %EVR

%description ceph
This package contains a FSAL shared object to
be used with NFS-Ganesha to support CEPH

%package rados-grace
Summary: The NFS-GANESHA command for managing the RADOS grace database
Group: System/Servers
Requires: %name = %EVR
 
%description rados-grace
This package contains the ganesha-rados-grace tool for interacting with the
database used by the rados_cluster recovery backend and the
libganesha_rados_grace shared library for using RADOS storage for
recovery state.

%package rados-urls
Summary: The NFS-GANESHA library for use with RADOS URLs
Group: System/Servers
Requires: %name = %EVR

%description rados-urls
This package contains the libganesha_rados_urls library used for
handling RADOS URL configurations.

%package rgw
Summary: The NFS-GANESHA Ceph RGW FSAL
Group: System/Servers
Requires: %name = %EVR

%description rgw
This package contains a FSAL shared object to
be used with NFS-Ganesha to support Ceph RGW

# XFS
%package xfs
Summary: The NFS-GANESHA's XFS FSAL
Group: System/Servers
Requires: %name = %EVR

%description xfs
This package contains a shared object to be used with FSAL_VFS
to support XFS correctly

# LUSTRE
%package lustre
Summary: The NFS-GANESHA's LUSTRE FSAL
Group: System/Servers
Requires: %name = %EVR

%description lustre
This package contains a FSAL shared object to
be used with NFS-Ganesha to support LUSTRE

# KVSFS
%package kvsfs
Summary: The NFS-GANESHA KVSFS FSAL
Group: System/Servers
Requires: %name = %EVR

%description kvsfs
This package contains a FSAL shared object to
be used with NFS-Ganesha to support KVSFS/libkvsns

# GLUSTER
%package gluster
Summary: The NFS-GANESHA's GLUSTER FSAL
Group: System/Servers
Requires: %name = %EVR

%description gluster
This package contains a FSAL shared object to
be used with NFS-Ganesha to support Gluster

# LizardFS
%package lizardfs
Summary: The NFS-GANESHA's LizardFS FSAL
Group: System/Servers
Requires: %name = %EVR
Conflicts: lizardfs-nfs-ganesha

%description lizardfs
This package contains a FSAL shared object to be used with NFS-Ganesha
to support LizardFS.

%prep
%setup
tar xf %SOURCE1 -C src
tar xf %SOURCE2 -C src/monitoring
%patch -p1

%build
%add_optflags %(getconf LFS_CFLAGS)
pushd src
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_CONFIG=rpmbuild \
    -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
    -DUSE_MAN_PAGE=ON \
    -DUSE_FSAL_NULL=%{on_off_switch nullfs} \
    -DUSE_FSAL_MEM=%{on_off_switch mem} \
    -DUSE_FSAL_XFS=%{on_off_switch xfs} \
    -DUSE_FSAL_LUSTRE=%{on_off_switch lustre} \
    -DUSE_FSAL_CEPH=%{on_off_switch ceph} \
    -DUSE_FSAL_RGW=%{on_off_switch rgw} \
    -DUSE_RADOS_RECOV=%{on_off_switch rados_recov} \
    -DRADOS_URLS=%{on_off_switch rados_urls} \
    -DUSE_FSAL_GPFS=%{on_off_switch gpfs} \
    -DUSE_FSAL_KVSFS=%{on_off_switch kvsfs} \
    -DUSE_FSAL_GLUSTER=%{on_off_switch gluster} \
    -DUSE_FSAL_SAUNAFS=%{on_off_switch saunafs} \
    -DUSE_FSAL_LIZARDFS=%{on_off_switch lizardfs} \
    -DUSE_SYSTEM_NTIRPC=%{on_off_switch system_ntirpc} \
    -DUSE_LTTNG=%{on_off_switch lttng} \
    -DUSE_ADMIN_TOOLS=%{on_off_switch utils} \
    -DUSE_GUI_ADMIN_TOOLS=%{on_off_switch gui_utils} \
    -DUSE_9P=%{on_off_switch 9P} \
    -DUSE_9P_RDMA=%{on_off_switch 9P_rdma} \
    -DUSE_FSAL_VFS=ON \
    -DENABLE_VFS_POSIX_ACL=ON \
    -DUSE_FSAL_PROXY_V4=ON \
    -DUSE_FSAL_PROXY_V3=ON \
    -DUSE_DBUS=ON \
    -DRPCBIND=%{on_off_switch rpcbind} \
    -D_MSPAC_SUPPORT=%{on_off_switch mspac_support} \
    -DUSE_MONITORING=%{on_off_switch monitoring_support} \
%if_with jemalloc
    -DALLOCATOR=jemalloc \
%else
    -DALLOCATOR=libc \
%endif
    -DDISTNAME_HAS_GIT_DATA=OFF \
    -DUSE_LEGACY_PYTHON_INSTALL=%{on_off_switch legacy_python_install} \
    -GNinja

%cmake_build
popd

%install
mkdir -p %buildroot%_sysconfdir/ganesha/
mkdir -p %buildroot%_sysconfdir/dbus-1/system.d
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_sysconfdir/logrotate.d
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_libdir/ganesha
mkdir -p %buildroot%_libexecdir/ganesha
mkdir -p %buildroot%_docdir/ganesha

pushd src
install -m 644 config_samples/logrotate_ganesha	%buildroot%_logrotatedir/ganesha
install -m 644 scripts/ganeshactl/org.ganesha.nfsd.conf	%buildroot%_sysconfdir/dbus-1/system.d
install -m 755 scripts/nfs-ganesha-config.sh	%buildroot%_libexecdir/ganesha
%if_with 9P
install -m 755 tools/mount.9P	%buildroot%_sbindir/mount.9P
%endif

install -m 644 config_samples/vfs.conf %buildroot%_sysconfdir/ganesha/
%if_with rgw
install -m 644 config_samples/rgw.conf %buildroot%_sysconfdir/ganesha/
%endif

mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_unitdir/nfs-ganesha-lock.service.d
install -m 644 scripts/systemd/nfs-ganesha.service.el7 %buildroot%_unitdir/nfs-ganesha.service
install -m 644 scripts/systemd/nfs-ganesha-lock.service.el8 %buildroot%_unitdir/nfs-ganesha-lock.service
install -m 644 scripts/systemd/rpc-statd.conf.el8 %buildroot%_unitdir/nfs-ganesha-lock.service.d/rpc-statd.conf
sed -i -e 's|/usr/sbin/rpc.statd|/sbin/rpc.statd|' %buildroot%_unitdir/nfs-ganesha-lock.service.d/rpc-statd.conf
install -m 644 scripts/systemd/nfs-ganesha-config.service %buildroot%_unitdir/nfs-ganesha-config.service
install -m 644 scripts/systemd/sysconfig/nfs-ganesha %buildroot%_sysconfdir/sysconfig/ganesha
mkdir -p %buildroot%_logdir/ganesha

# TODO: adapt sysvinit script for ALT
#mkdir -p %%buildroot%%_initdir
#install -m 755 scripts/init.d/nfs-ganesha.el6 %%buildroot%%_initdir/nfs-ganesha

%if_with lustre
install -m 644 config_samples/lustre.conf %buildroot%_sysconfdir/ganesha/
%endif

%if_with xfs
install -m 644 config_samples/xfs.conf %buildroot%_sysconfdir/ganesha/
%endif

%if_with ceph
install -m 644 config_samples/ceph.conf %buildroot%_sysconfdir/ganesha/
%endif

%if_with rgw
install -m 644 config_samples/rgw.conf %buildroot%_sysconfdir/ganesha/
install -m 644 config_samples/rgw_bucket.conf %buildroot%_sysconfdir/ganesha/
%endif

%if_with gluster
install -m 644 config_samples/logrotate_fsal_gluster %buildroot%_logrotatedir/ganesha-gfapi
%endif

%if_with gpfs
install -m 644 config_samples/gpfs.conf	%buildroot%_sysconfdir/ganesha/
install -m 644 config_samples/gpfs.ganesha.nfsd.conf %buildroot%_sysconfdir/ganesha/
install -m 644 config_samples/gpfs.ganesha.main.conf %buildroot%_sysconfdir/ganesha/
install -m 644 config_samples/gpfs.ganesha.log.conf %buildroot%_sysconfdir/ganesha/
install -m 644 config_samples/gpfs.ganesha.exports.conf	%buildroot%_sysconfdir/ganesha/
%endif

%cmake_install
popd

%pre
groupadd -r -f ganesha
useradd -M -r -d %_runtimedir/ganesha -s /sbin/nologin -c "NFS-Ganesha Daemon" -g ganesha ganesha >/dev/null 2>&1 || :

%post
%post_systemd nfs-ganesha.service nfs-ganesha-lock.service nfs-ganesha-config.service

%preun
%preun_systemd nfs-ganesha.service nfs-ganesha-lock.service nfs-ganesha-config.service

%files
%doc src/LICENSE.txt
%_bindir/ganesha.nfsd
%_libdir/libganesha_nfsd.so*
%dir %_libdir/ganesha
%config %_sysconfdir/dbus-1/system.d/org.ganesha.nfsd.conf
%config(noreplace) %_sysconfdir/sysconfig/ganesha
%config(noreplace) %_logrotatedir/ganesha
%dir %_sysconfdir/ganesha
%config(noreplace) %_sysconfdir/ganesha/ganesha.conf
%dir %_libexecdir/ganesha
%_libexecdir/ganesha/nfs-ganesha-config.sh
%dir %attr(0755,ganesha,ganesha) %_logdir/ganesha
%if_with utils
%_bindir/sm_notify.ganesha
%endif

#%%_initdir/nfs-ganesha
%_unitdir/nfs-ganesha.service
%_unitdir/nfs-ganesha-lock.service
%_unitdir/nfs-ganesha-config.service
%_unitdir/nfs-ganesha-lock.service.d
%_man8dir/ganesha-config.8*
%_man8dir/ganesha-core-config.8*
%_man8dir/ganesha-export-config.8*
%_man8dir/ganesha-cache-config.8*
%_man8dir/ganesha-log-config.8*

%if_without system_ntirpc
%files -n libntirpc
%_libdir/libntirpc.so.*

%files -n libntirpc-devel
%_libdir/libntirpc.so
%_includedir/ntirpc
%_pkgconfigdir/libntirpc.pc
%endif

%if_with rados_recov
%files rados-grace
%_bindir/ganesha-rados-grace
%_libdir/libganesha_rados_recov.so*
%_man8dir/ganesha-rados-grace.8*
%_man8dir/ganesha-rados-cluster-design.8*
%endif

%if_with rados_urls
%files rados-urls
%_libdir/libganesha_rados_urls.so*
%endif

%if_with 9P
%files mount-9P
%_sbindir/mount.9P
%endif

%files vfs
%_libdir/ganesha/libfsalvfs*
%config(noreplace) %_sysconfdir/ganesha/vfs.conf
%_man8dir/ganesha-vfs-config.8*

%files proxy-v4
%_libdir/ganesha/libfsalproxy_v4*
%_man8dir/ganesha-proxy-v4-config.8*

%files proxy-v3
%_libdir/ganesha/libfsalproxy_v3*
%_man8dir/ganesha-proxy-v3-config.8*

# Optional packages
%if_with lustre
%files lustre
%_libdir/ganesha/libfsallustre*
%config(noreplace) %_sysconfdir/ganesha/lustre.conf
%_man8dir/ganesha-lustre-config.8*
%endif

%if_with nullfs
%files nullfs
%_libdir/ganesha/libfsalnull*
%endif

%if_with mem
%files mem
%_libdir/ganesha/libfsalmem*
%endif

%if_with gpfs
%files gpfs
%_libdir/ganesha/libfsalgpfs*
%config(noreplace) %_sysconfdir/ganesha/gpfs.conf
%config(noreplace) %_sysconfdir/ganesha/gpfs.ganesha.nfsd.conf
%config(noreplace) %_sysconfdir/ganesha/gpfs.ganesha.main.conf
%config(noreplace) %_sysconfdir/ganesha/gpfs.ganesha.log.conf
%config(noreplace) %_sysconfdir/ganesha/gpfs.ganesha.exports.conf
%_man8dir/ganesha-gpfs-config.8*
%endif

%if_with xfs
%files xfs
%_libdir/ganesha/libfsalxfs*
%config(noreplace) %_sysconfdir/ganesha/xfs.conf
%_man8dir/ganesha-xfs-config.8*
%endif

%if_with ceph
%files ceph
%_libdir/ganesha/libfsalceph*
%config(noreplace) %_sysconfdir/ganesha/ceph.conf
%_man8dir/ganesha-ceph-config.8*
%endif

%if_with rgw
%files rgw
%_libdir/ganesha/libfsalrgw*
%config(noreplace) %_sysconfdir/ganesha/rgw.conf
%config(noreplace) %_sysconfdir/ganesha/rgw_bucket.conf
%_man8dir/ganesha-rgw-config.8*
%endif

%if_with gluster
%files gluster
%config(noreplace) %_logrotatedir/ganesha-gfapi
%_libdir/ganesha/libfsalgluster*
%_man8dir/ganesha-gluster-config.8*
%endif

%if_with kvsfs
%files kvsfs
%_libdir/ganesha/libfsalkvsfs*
%endif

%if_with lttng
%files lttng
%_libdir/ganesha/libganesha_trace*
%endif

%if_with lizardfs
%files lizardfs
%_libdir/ganesha/libfsallizardfs*
%endif

%if_with utils
%files utils
%_bindir/ganesha-top
%python3_sitelibdir_noarch/ganesha_top-*-info
%_bindir/fake_recall
%_bindir/get_clientids
%_bindir/grace_period
%_bindir/ganesha_stats
%_bindir/ganesha_mgr
%_bindir/ganesha_conf
%_man8dir/ganesha_conf.8*

%if_with gui_utils
%files utils-gui
%python3_sitelibdir_noarch/Ganesha
%python3_sitelibdir_noarch/ganeshactl-*-info
%_bindir/ganesha-admin
%_bindir/manage_clients
%_bindir/manage_exports
%_bindir/manage_logger
%_bindir/ganeshactl
%if_with 9P
%_bindir/client_stats_9pOps
%_bindir/export_stats_9pOps
%else
%exclude %_bindir/client_stats_9pOps
%exclude %_bindir/export_stats_9pOps
%endif
%endif

%endif

%changelog
* Wed Sep 04 2024 Vitaly Chikunov <vt@altlinux.org> 6.0-alt1
- Update to V6.0 (2024-08-23).

* Thu Jul 04 2024 Alexey Shabalin <shaba@altlinux.org> 5.9-alt1
- New version 5.9.

* Mon Feb 19 2024 Alexey Shabalin <shaba@altlinux.org> 5.7-alt1
- New version 5.7.

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt2
- rebuild with libntirpc 3.5

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt1
- new version 3.5 (with rpmrb script)

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt1
- new version 3.3 (with rpmrb script)

* Thu May 30 2019 Vitaly Lipatov <lav@altlinux.ru> 2.7.3-alt1
- new version 2.7.3 (with rpmrb script)

* Wed Mar 27 2019 Vitaly Lipatov <lav@altlinux.ru> 2.7.2-alt1
- new version 2.7.2 (with rpmrb script)

* Fri Jan 11 2019 Michael Shigorin <mike@altlinux.org> 2.7.1-alt2
- extended ceph knob (BR: librados2-devel might be a problem)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.7.1-alt1
- new version 2.7.1 (with rpmrb script)

* Sat Sep 29 2018 Vitaly Lipatov <lav@altlinux.ru> 2.7.0-alt1
- new version 2.7.0 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 2.6.2-alt1
- new version 2.6.2 (with rpmrb script)

* Tue Mar 27 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.4-alt2
- libnfsidmap soname bump

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.4-alt1
- new version 2.5.4 (with rpmrb script)

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.3-alt1
- new version 2.5.3 (with rpmrb script)

* Wed Oct 18 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt3
- add rpm-build-intro buildreq (fix /var/lib/run)

* Tue Aug 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt2
- build with new libntirpc 1.5.3

* Sun Jun 11 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0

* Mon Dec 05 2016 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Sun Oct 02 2016 Vitaly Lipatov <lav@altlinux.ru> 2.4.0.1-alt1
- new version 2.4.0.1 (with rpmrb script)

* Sun Jul 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt0.dev26
- new version (2.4.0-dev26) with rpmgs script

* Fri Jul 22 2016 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- new version 2.3.2 (with rpmrb script)

* Sat Jul 16 2016 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- initial build for ALT Linux Sisyphus

