%define oname glusterfs
%define major 3.2
# if you wish to compile an rpm without rdma support, compile like this...
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --without rdma
%{?_without_rdma:%global _without_rdma --disable-ibverbs}

# No RDMA Support on s390(x)
%ifarch s390 s390x
%global _without_rdma --disable-ibverbs
%endif

# if you wish to compile an rpm without epoll...
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --without epoll
%{?_without_epoll:%global _without_epoll --disable-epoll}

# if you wish to compile an rpm with fusermount...
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --with fusermount
%{?_with_fusermount:%global _with_fusermount --enable-fusermount}

# if you wish to compile an rpm without geo-replication support, compile like this...
# rpmbuild -ta @PACKAGE_NAME@-@PACKAGE_VERSION@.tar.gz --without georeplication
%{?_without_georeplication:%global _without_georeplication --disable-geo-replication}

Summary: Cluster File System
Name: glusterfs3
Version: %major.5
Release: alt5
License: GPLv3
Group: System/Base
Vendor: Red Hat
Url: http://www.gluster.org/docs/index.php/GlusterFS
Packager: Denis Baranov <baraka@altlinux.ru>

Source: http://download.gluster.com/pub/gluster/glusterfs/%major/%version/glusterfs-%version.tar
Source1: glusterd.sysconfig
Source2: glusterfsd.sysconfig
Source3: umount.glusterfs
Source4: glusterfs-fuse.logrotate
Source5: glusterd.logrotate
Source6: glusterfsd.logrotate

Source7: glusterd.init
Source8: glusterfsd.init
%define _init_install() install -D -p -m 0755 %1 %buildroot%_initdir/%2 ;
%define _init_file1     %_initdir/glusterd
%define _init_file2     %_initdir/glusterfsd

# Automatically added by buildreq on Sun Mar 11 2012
# optimized out: libncurses-devel libtinfo-devel pkg-config python-base python-devel python-module-distribute python-module-peak python-modules python-modules-ctypes
BuildRequires: flex glibc-devel-static libibverbs-devel libreadline-devel libxml2-devel python-module-mwlib python-module-paste

Conflicts: %oname

Obsoletes: %oname-libs <= 2.0.0
Obsoletes: %oname-common < 3.1.0
Provides: %name-libs = %version-%release
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

%if 0%{!?_without_georeplication:1}
%package geo-replication
Summary: GlusterFS Geo-replication
Group: System/Base
Requires: %name = %version-%release , python-modules-ctypes , rsync >= 3.0.0

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

%package vim
Summary: Vim syntax file
Group: Editors
Requires: vim-common

%description vim
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

Vim syntax file for GlusterFS.

%package devel
Summary: Development Libraries
Group: Development/Other
Requires: %name = %version-%release
Conflicts: %oname-devel

%description devel
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the development libraries.

%prep
%setup -n %oname-%version

%build
#autoreconf
%configure %{?_without_rdma} %{?_without_epoll} %{?_with_fusermount} %{?_without_georeplication} --localstatedir=/var/

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
mkdir -p %buildroot%_logdir/gluster
mkdir -p %buildroot%_logdir/gluster/glusterd
mkdir -p %buildroot%_logdir/gluster/glusterfs
mkdir -p %buildroot%_logdir/gluster/glusterfsd

# Remove unwanted files from all the shared libraries
find %buildroot%_libdir -name '*.a' -delete
find %buildroot%_libdir -name '*.la' -delete

# Remove installed docs, we include them ourselves as %%doc
rm -rf %buildroot%_docdir/glusterfs/

# Rename the samples, so we can include them as %%config
for file in %buildroot%_sysconfdir/glusterfs/*.sample; do
  mv ${file} `dirname ${file}`/`basename ${file} .sample`
done

# Create working directory
mkdir -p %buildroot%_sharedstatedir/glusterd



# Update configuration file to /var/lib working directory
%__subst 's|option working-directory %_sysconfdir/glusterd|option working-directory %_sharedstatedir/glusterd|g' \
%buildroot%_sysconfdir/glusterfs/glusterd.vol
# Clean up the examples we want to include as %%doc
cp -a doc/examples examples
rm -f examples/Makefile*

# Install init script and sysconfig file
%_init_install %SOURCE7 glusterd
%_init_install %SOURCE8 glusterfsd
install -D -p -m 0644 %SOURCE1 \
%buildroot%_sysconfdir/sysconfig/glusterd
install -D -p -m 0644 %SOURCE2 \
%buildroot%_sysconfdir/sysconfig/glusterfsd
# Install wrapper umount script
install -D -p -m 0755 %SOURCE3 \
%buildroot/sbin/umount.glusterfs
# Client logrotate entry
install -D -p -m 0644 %SOURCE4 \
%buildroot%_sysconfdir/logrotate.d/glusterfs-fuse
# Server logrotate entry
install -D -p -m 0644 %SOURCE5 \
%buildroot%_sysconfdir/logrotate.d/glusterd
# Legacy server logrotate entry
install -D -p -m 0644 %SOURCE6 \
%buildroot%_sysconfdir/logrotate.d/glusterfsd
# Install vim syntax plugin
install -D -p -m 644 extras/glusterfs.vim \
%buildroot%_datadir/vim/vimfiles/syntax/glusterfs.vim

%files
%doc ChangeLog COPYING INSTALL README THANKS
#%config(noreplace) %_sysconfdir/logrotate.d/glusterd
#%config(noreplace) %_sysconfdir/sysconfig/glusterd
#%_libdir/glusterfs
%_libdir/*.so.*
%_sbindir/glusterfs*
%_sbindir/gluster
%_sbindir/glusterd
%dir %_libdir/glusterfs/
%dir %_libdir/glusterfs/%version/
%_libdir/glusterfs/%version/rpc-transport/
%_libdir/glusterfs/%version/auth/
%_libdir/glusterfs/%version/xlator/
%exclude %_libdir/glusterfs/%version/xlator/mount/fuse*
%_logdir/gluster/*
%_man8dir/*gluster*.8*
%if 0%{!?_without_rdma:1}
%exclude %_libdir/glusterfs/%version/rpc-transport/rdma*
%endif

%if 0%{!?_without_rdma:1}
%files rdma
%_libdir/glusterfs/%version/rpc-transport/rdma*
%endif

%if 0%{!?_without_georeplication:1}
%post geo-replication
#restart glusterd.
#%_initdir/glusterd restart &> /dev/null
%endif

%if 0%{!?_without_georeplication:1}
%files geo-replication
%dir %_libexecdir/glusterfs/
%_libexecdir/glusterfs/gsyncd
%dir %_libexecdir/glusterfs/python/
%_libexecdir/glusterfs/python/syncdaemon/
%endif

%files client
%config(noreplace) %_sysconfdir/logrotate.d/glusterfs-fuse
%_libdir/glusterfs/%version/xlator/mount/fuse*
#%_man8dir/mount.glusterfs.8*
/sbin/mount.glusterfs
/sbin/umount.glusterfs
%if 0%{?_with_fusermount:1}
%_bindir/fusermount-glusterfs
%endif

%files server
%doc examples/ doc/glusterfs*.vol.sample
%config(noreplace) %_sysconfdir/logrotate.d/glusterd
%config(noreplace) %_sysconfdir/sysconfig/glusterd
%config(noreplace) %_sysconfdir/glusterfs
# Legacy configs
%config(noreplace) %_sysconfdir/logrotate.d/glusterfsd
%config(noreplace) %_sysconfdir/sysconfig/glusterfsd
%_sharedstatedir/glusterd
%_init_file1
%_init_file2

%files vim
%doc COPYING
%_datadir/vim/vimfiles/syntax/glusterfs.vim

%files devel
%_includedir/glusterfs
%exclude %_includedir/glusterfs/y.tab.h
%_libdir/*.so

%post server
%post_service glusterfsd
%post_service glusterd

%preun server
%preun_service glusterfsd
%preun_service glusterd

%changelog
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
