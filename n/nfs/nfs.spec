Name: nfs
Version: 2.8.1
Release: alt1
Epoch: 1

Summary: The Linux NFS clients, utilities and server
License: GPLv2
Group: Networking/Other
Url: http://nfs.sourceforge.net/

Source0: %name-%version-%release.tar

BuildRequires: libblkid-devel libevent-devel libuuid-devel libxml2-devel
BuildRequires: libdevmapper-devel libkrb5-devel libsqlite3-devel
BuildRequires: libcap-devel libtirpc-devel libkeyutils-devel libmount-devel
BuildRequires: libnl-devel libreadline-devel
BuildRequires: rpcgen rpcsvc-proto-devel
BuildRequires: rpm-build-python3

%package -n libnfsidmap
Summary: Name to user id mapping library
Group: System/Libraries

%package -n libnfsidmap-devel
Summary: Name to user id mapping library and headers
Group: Development/C
Requires: libnfsidmap = %EVR

%package clients
Summary: The Linux NFS client
Group: Networking/Other
Provides: /sbin/rpc.statd

PreReq: shadow-utils
PreReq: %name-utils = %epoch:%version-%release
Requires(post): %post_service
Requires(preun): %preun_service
Requires: keyutils >= 1.4-alt2
Conflicts: libnfsidmap < 0.23

%package server
Summary: The Linux NFS server
Group: Networking/Other

PreReq: %name-clients = %epoch:%version-%release
Requires(post): %post_service
Requires(preun): %preun_service

%package utils
Summary: The Linux NFS services utilities
Group: Networking/Other

PreReq: control
Requires: rpcbind >= 0.2.0-alt1
Conflicts: mount < 2.12r-alt2
Conflicts: nfs-clients = 1:1.0.10-alt2

%package stats
Summary: The Linux NFS stats utilities
Group: Networking/Other
Conflicts: nfs-utils < 1:1.2.4-alt0.4

%description
This package provides the Linux NFS utilities and server.
This package replaces the old knfsd package.

%description -n libnfsidmap
libnfsidmap is a library holding mulitiple methods of mapping names to id's
and visa versa, mainly for NFSv4.

%description -n libnfsidmap-devel
libnfsidmap is a library holding mulitiple methods of mapping names to id's
and visa versa, mainly for NFSv4.
This package holds development part of libnfsidmap library

%description clients
This package provides the Linux NFS clients.

%description server
This package provides the Linux NFS server.

%description utils
This package provides the Linux NFS utilities,
including mount.nfs helper.

%description stats
This package provides the Linux NFS stats utilities.

%prep
%setup

%build
[ -f ./autogen.sh ] && sh ./autogen.sh
%configure \
    --libexecdir=%_prefix/libexec \
    --enable-nfsv4server \
    --enable-mount \
    --enable-libmount-mount \
    --enable-gss \
    --enable-svcgss \
    --enable-tirpc \
    --enable-ipv6 \
    --with-statduser=rpcuser \
    --with-statdpath=%_localstatedir/nfs/statd \
    --with-systemd=%_unitdir \
    --with-pluginpath=%_libdir/libnfsidmap \
    --disable-nfsdcld \
    --disable-static \
    --disable-sbin-override \
    #
sed -i 's/#define[[:blank:]]\+START_STATD.\+$/#undef START_STATD/' support/include/config.h
%make_build

%install
%make_install DESTDIR=%buildroot install

cp -a altlinux/etc %buildroot
cp -p systemd/README README.systemd

install -pm0644 nfs.conf %buildroot%_sysconfdir/nfs.conf
install -pm0644 support/nfsidmap/idmapd.conf %buildroot%_sysconfdir/idmapd.conf

ln -s nfs-blkmap.service %buildroot%systemd_unitdir/blkmapd.service
ln -s nfs-idmapd.service %buildroot%systemd_unitdir/idmapd.service
ln -s nfs-server.service %buildroot%systemd_unitdir/nfs.service
ln -s rpc-gssd.service %buildroot%systemd_unitdir/gssd.service
ln -s rpc-statd.service %buildroot%systemd_unitdir/nfslock.service
ln -s rpc-svcgssd.service %buildroot%systemd_unitdir/svcgssd.service

mkdir -p %buildroot%_localstatedir/nfs/{rpc_pipefs,v4recovery}

#-------------------------------------------------------------------------------
%pre clients
%_sbindir/groupadd -r -f rpcuser &> /dev/null
%_sbindir/useradd -r -g rpcuser -d %_localstatedir/nfs -s /dev/null -c 'RPC Service User' -n rpcuser &> /dev/null ||:
%_sbindir/groupadd -r -f nfsuser &> /dev/null
%_sbindir/useradd -r -g nfsuser -d /dev/null -s /dev/null -c 'NFS Service User' -n nfsuser &> /dev/null ||:

%pre utils
[ $1 -eq 1 ] || /usr/sbin/control-dump nfsmount

%post clients
%post_service nfslock
%post_service blkmapd
%post_service gssd

%post utils
[ $1 -eq 1 ] || /usr/sbin/control-restore nfsmount

%preun clients
%preun_service nfslock
%preun_service blkmapd
%preun_service gssd

%post server
%post_service nfs
%post_service idmapd
%post_service svcgssd

%preun server
%preun_service nfs
%preun_service idmapd
%preun_service svcgssd

%triggerpostun -- nfs-server <= 1.2.5-alt1
. /etc/init.d/functions
SourceIfNotEmpty /etc/sysconfig/nfs
is_yes "$SECURE_NFS" || exit 0
touch /var/lock/subsys/rpc.svcgssd
/sbin/chkconfig svcgssd on
/sbin/service svcgssd condrestart

#-------------------------------------------------------------------------------
%files -n libnfsidmap
%config(noreplace) %_sysconfdir/idmapd.conf
%_libdir/libnfsidmap.so.*
%dir %_libdir/libnfsidmap
%_libdir/libnfsidmap/*.so
%_man5dir/idmapd.conf.*

%files -n libnfsidmap-devel
%_libdir/libnfsidmap.so
%_includedir/nfsidmap.h
%_includedir/nfsidmap_plugin.h
%_pkgconfigdir/libnfsidmap.pc
%_man3dir/nfs4_uid_to_name.3*

%files server
%_initdir/nfs
%_initdir/idmapd
%_initdir/svcgssd

%systemd_unitdir/nfs.service
%systemd_unitdir/idmapd.service
%systemd_unitdir/svcgssd.service
%systemd_unitdir/fsidd.service

%systemd_unitdir/nfs-server.service
%systemd_unitdir/nfs-mountd.service
%systemd_unitdir/nfs-idmapd.service
%systemd_unitdir/rpc-svcgssd.service
%systemd_unitdir/proc-fs-nfsd.mount
%systemd_unitdir/nfsv4-server.service
%systemd_unitdir/nfsv4-exportd.service

%_sbindir/nfsdctl
%_sbindir/nfsdcltrack
%_sbindir/exportfs
%_sbindir/fsidd
%_sbindir/nfsref
%_sbindir/nfsstat
%_sbindir/rpc.idmapd
%_sbindir/rpc.mountd
%_sbindir/rpc.nfsd
%_sbindir/rpc.svcgssd
%_sbindir/nfsv4.exportd

%_man5dir/exports.*
%_man7dir/nfsd.*
%_man8dir/exportfs.*
%_man8dir/idmapd.*
%_man8dir/rpc.idmapd.*
%_man8dir/nfsref.*
%_man8dir/nfsstat.*
%_man8dir/nfsdcltrack.*
%_man8dir/mountd.*
%_man8dir/rpc.mountd.*
%_man8dir/nfsdctl.*
%_man8dir/nfsd.*
%_man8dir/rpc.nfsd.*
%_man8dir/svcgssd.*
%_man8dir/rpc.svcgssd.*
%_man8dir/exportd.*
%_man8dir/nfsv4.exportd.*

%config(noreplace) %_localstatedir/nfs/etab
%config(noreplace) %_localstatedir/nfs/rmtab
%dir %_localstatedir/nfs/v4recovery

#-------------------------------------------------------------------------------
%files clients
%doc README README.systemd
%dir %_localstatedir/nfs
%dir %_localstatedir/nfs/rpc_pipefs
%dir %attr(700,rpcuser,rpcuser) %_localstatedir/nfs/statd
%dir %attr(700,rpcuser,rpcuser) %_localstatedir/nfs/statd/sm
%dir %attr(700,rpcuser,rpcuser) %_localstatedir/nfs/statd/sm.bak
%ghost %attr(700,rpcuser,rpcuser) %_localstatedir/nfs/statd/state

%config(noreplace) %_sysconfdir/nfs.conf

%_initdir/blkmapd
%_initdir/nfslock
%_initdir/gssd

%systemd_unitdir/blkmapd.service
%systemd_unitdir/gssd.service
%systemd_unitdir/nfslock.service

%systemd_unitdir/rpc_pipefs.target
%systemd_unitdir/nfs-client.target
%systemd_unitdir/nfs-utils.service
%systemd_unitdir/auth-rpcgss-module.service
%systemd_unitdir/var-lib-nfs-rpc_pipefs.mount
%systemd_unitdir/nfs-blkmap.service
%systemd_unitdir/rpc-statd.service
%systemd_unitdir/rpc-statd-notify.service
%systemd_unitdir/rpc-gssd.service
%systemd_unitdir-generators/rpc-pipefs-generator
%systemd_unitdir-generators/nfs-server-generator

%_sbindir/rpc.gssd
%_sbindir/rpc.statd
%_sbindir/sm-notify
%_sbindir/blkmapd
%_sbindir/nfsidmap
%_sbindir/nfsconf
%_sbindir/rpcctl

%_man5dir/nfs.conf.*
%_man7dir/nfs.systemd.*
%_man8dir/gssd.*
%_man8dir/rpc.gssd*
%_man8dir/blkmapd.*
%_man8dir/statd.*
%_man8dir/rpc.statd.*
%_man8dir/rpcctl.*
%_man8dir/sm-notify.*
%_man8dir/rpc.sm-notify.*
%_man8dir/nfsidmap.*
%_man8dir/nfsconf.*

#-------------------------------------------------------------------------------
%files utils
%config %_sysconfdir/control.d/facilities/nfsmount
%_udevrulesdir/*.rules
%attr(700,root,root) %_sbindir/mount.nfs
%_sbindir/mount.nfs4
%_sbindir/umount.*
%_bindir/showmount
%_sbindir/rpcdebug
%_prefix/libexec/nfsrahead
%_man5dir/nfs.5*
%_man5dir/nfsmount.conf.*
%_man5dir/nfsrahead.*
%_man8dir/rpcdebug.*
%_man8dir/showmount.*
%_man8dir/mount.nfs.*
%_man8dir/umount.nfs.*

%files stats
%_sbindir/mountstats
%_sbindir/nfsdclnts
%_sbindir/nfsiostat
%_man8dir/mountstats.*
%_man8dir/nfsdclnts.*
%_man8dir/nfsiostat.*

%changelog
* Mon Oct 21 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1:2.8.1-alt1
- 2.8.1 released

* Fri Aug 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1:2.7.1-alt1
- 2.7.1 released

* Mon Jun 24 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1:2.6.4-alt2
- rebuilt for merged-usr

* Mon Nov 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.6.4-alt1
- 2.6.4 released

* Thu Apr 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.6.3-alt1
- 2.6.3 released

* Tue Feb 21 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.6.2-alt2
- Moved %_sbindir/rpcctl from %name-utils to %name-clients subpackage
  (ALT#45347).

* Tue Aug 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.6.2-alt1
- 2.6.2 released

* Fri Jun 03 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.6.1-alt2
- fix build with gcc-12

* Fri Jan 28 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.6.1-alt1
- 2.6.1 released

* Tue Jun 15 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.5.4-alt1
- 2.5.4 released

* Tue May 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.5.3-alt2
- rebuilt with explicit python3 req finder

* Wed Feb 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.5.3-alt1
- 2.5.3 released

* Mon Jan 25 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.5.2-alt2
- rebuilt with standalone rpcsvc-proto

* Fri Oct 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.5.2-alt1
- 2.5.2 released

* Thu Jun 25 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.5.1-alt1
- 2.5.1 released

* Mon Feb 10 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.4.3-alt1
- 2.4.3 released

* Tue Dec 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.4.2-alt1
- 2.4.2 released

* Mon Aug 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.4.1-alt1
- 2.4.1 released

* Thu Feb 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.3.3-alt1
- 2.3.3 released

* Thu Aug 30 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.3.2-alt3
- rebuilt without libwrap

* Thu Jul 19 2018 Stanislav Levin <slev@altlinux.org> 1:2.3.2-alt2
- add lost header file

* Thu Jul 19 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.3.2-alt1
- 2.3.2 released

* Tue Mar 27 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.3.1-alt1
- 2.3.1 released

* Thu Nov 02 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.2.1-alt1
- 2.2.1 released

* Tue Jan 17 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.1.1-alt1
- 2.1.1 released

* Wed Aug 31 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.3.4-alt1
- 1.3.4 released

* Wed Apr 27 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.3.3-alt2
- rebuilt with libtirpc-1.0.1

* Thu Oct 01 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.3.3-alt1
- 1.3.3 released

* Thu Feb 05 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.3.2-alt2
- use 4.0 as default nfs version for a while

* Wed Feb 04 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.3.2-alt1
- 1.3.2 released

* Mon Dec 29 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.3.2-alt0.4
- 1.3.2 rc4

* Thu Mar 20 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.9-alt1
- 1.2.9 released

* Tue Apr 23 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.8-alt1
- 1.2.8 released

* Wed Oct 31 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.6-alt2
- selinux security_label exports option support added (closes: 27906)
- more systemd related changes (shaba@)

* Fri Jun 22 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.6-alt1
- 1.2.6 released

* Wed Nov 23 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.5-alt2
- systemd related changes (shaba@):
  + rpc.svcgssd repackaged as separate service
  + systemd service files packaged

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.2.5-alt1.1
- Rebuild with Python-2.7

* Mon Sep 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.5-alt1
- 1.2.5 released

* Thu Jun 30 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt3
- rebuilt with fresh libgssglue

* Thu Jun 30 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt2
- 1.2.4 rereleased

* Wed Jun 29 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt1
- 1.2.4 released

* Wed Jun 29 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt0.11
- 1.2.4-rc9 released
- CVE-2011-2500 fixed

* Wed Jun 08 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt0.10
- updated from git.7235a216

* Thu May 05 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt0.9
- do not use libmount for a while

* Fri Apr 22 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt0.8
- 1.2.4-rc8 released

* Mon Mar 07 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt0.6
- 1.2.4-rc6 released

* Mon Feb 28 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt0.5
- 1.2.4-rc5 released

* Tue Nov 09 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt0.4
- nfs stats utilities separated to subpackage

* Mon Nov 08 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt0.3
- initscript changed

* Sat Nov 06 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.4-alt0.2
- 1.2.4 rc2 released

* Fri Mar 26 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.2.2-alt1
- 1.2.2 released

* Tue Apr 28 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.1.6-alt1
- 1.1.6 released

* Tue Mar 31 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.1.5-alt1
- 1.1.5 released

* Wed Mar  4 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.1.4-alt2
- ensure all required for krb5 sec flavour modules are loaded 
- added idmapd restart after nfs

* Fri Oct 17 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.1.4-alt1
- 1.1.4 released

* Mon Jul 28 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.1.3-alt1
- 1.1.3 released

* Sun Mar 30 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.1.2-alt1
- 1.1.2 released

* Thu Feb  7 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.1.1-alt3
- occasional exportfs crashes on x86_64 fixed, i hope \#14360

* Tue Oct 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.1.1-alt2
- use /sbin/sm-notify from statd

* Sat Oct 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.1.1-alt1
- 1.1.1 released

* Sat Mar 24 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.10-alt5
- do not create socket for kernel during mount, if not needed

* Sat Feb 24 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.10-alt4
- do not mount rpc_pipefs from none, \#10896
- added conflict of utils subpackage vs clients = 1.0.10-alt2, \#10854

* Wed Dec 20 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.10-alt3
- nhfsstone removed due unclear legal status
- mount.nfs moved from clients to utils subpackage

* Sat Dec  2 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.10-alt2
- enabled mount.nfs build
- made no_subtree_check the default
- patches applied:
  + nfs-utils-1.0.10-alt-rh-mountd.patch
  + nfs-utils-1.0.10-rh-idmapd-scandir-leak.patch
  + nfs-utils-1.0.10-rh-idmap-dirscancb-listloop.patch
  + nfs-utils-1.0.10-rh-udp-no-connect.patch
  + nfs-utils-1.0.10-rh-export-nosubtree.patch
  + nfs-utils-1.0.10-rh-nfsmount-authnone.patch
  + nfs-utils-1.0.10-rh-mount-options-v3.patch
  + nfs-utils-1.0.10-rh-lazy-umount.patch
  + nfs-utils-1.0.10-rh-mount-sloppy.patch
  + nfs-utils-1.0.10-rh-mount-man-nfs.patch
  + nfs-utils-1.0.10-rh-return-mount-error.patch
  + nfs-utils-1.0.10-rh-mount-remount.patch
  + nfs-utils-1.0.10-rh-mount-nfsvers.patch

* Mon Oct  9 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.10-alt1
- 1.0.10 released
- patches applied:
  + nfs-utils-1.0.9-statd-all.patch
  + nfs-utils-1.0.9-idmapd-pidfile.patch
  + nfs-utils-1.0.9-idmapd-conffile.patch
  + nfs-utils-1.0.9-gssd-pidfile.patch
  + nfs-utils-1.0.9-alt-krb5.patch
  + nfs-utils-1.0.9-alt-rh-zerostats.patch
  + nfs-utils-1.0.9-rh-gssd-mixed-case.patch

* Tue Jul 18 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.9-alt1
- 1.0.9 released

* Mon Jan 16 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.7-alt5
- fixed build on x86_64

* Sat Oct 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.7-alt4
- rebuilt with GSSAPI enabled

* Sat Apr  2 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.7-alt3
- dropped quota requirement, see #6327

* Mon Mar  7 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.7-alt2
- #6177 fixed

* Tue Feb 22 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.7-alt1
- 1.0.7
- partial support for NFSv4 added (no gssapi yet)

* Sat Nov 27 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.6-alt3
- statd fixes
- exports(5) manpage updated

* Thu Feb 12 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.6-alt2
- redundant kernel requirement dropped

* Sat Oct 11 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.6-alt1
- 1.0.6
- black magic for kernels < 2.4.20pre4 dropped

* Wed Jul  9 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1:1.0.3-alt3
- fixed xlog off-by-one bug

* Sat Jul  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1:1.0.3-alt2
- statd patches from CVS head
- initscripts
- don't obsolete nfs-utils

* Fri Mar 28 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1:1.0.3-alt1
- 1.0.3
- support for kernels < 2.2.19 dropped

* Sat Oct 19 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1:1.0.1-alt2
- rebuilt in new env

* Wed Jul 24 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.0.1-alt1
- 1.0.1

* Sat Mar  2 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.3.3-alt2
- rpc.statd fixed

* Wed Feb 27 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.3.3-alt1
- readopted for ALT
- UID/GID mapping disabled by default

* Thu Feb 21 2002 Grigory Milev <week@altlinux.ru> 0.3.3-2aw
- fixed run levels in nfs.init script
- cleaunup post and preun install scripts

* Wed Jan 16 2002 Grigory Milev <week@altlinux.ru> 0.3.3-1aw
- spec cleanup for compatible with bte

* Tue Dec 04 2001 Alexander Bokovoy <a.bokovoy@sam-solutions.net> 0.3.3-1aw
- 0.3.3
- AW integration
- Updated:
  + drop-privs patch
  + syslog patch removed [already in upstream]
- Added:
  + UID/GID mapping [enabled by default]

* Mon May 28 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.3.1-alt2
- Added rquotad to nfs-server prereq list.

* Fri May 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.3.1-alt1
- 0.3.1
- Merged RH patches.

* Wed Apr 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.2.1-ipl5mdk
- Moved %_sbindir/showmount to %_bindir/showmount.

* Tue Jan 23 2001 Dmitry V. Levin <ldv@fandra.org> 0.2.1-ipl4mdk
- Merged RH fixes.

* Sun Jan 21 2001 Dmitry V. Levin <ldv@fandra.org> 0.2.1-ipl3mdk
- RE adaptions.
- Renamed packages to %name-server and %name-clients.
- Rewritten init scripts.
- Added more documentation.
- Merged RH patches.

