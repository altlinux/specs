%define stage 42-g779b491

%def_enable bdb
%def_enable ibverbs
%def_enable libglusterfsclient
%def_disable static

Summary: GNU Cluster File System
Name: glusterfs
Version: 2.0.9
Release: alt0.42.g779b491.1
License: GPLv3 or later
Group: System/Base
Packager: L.A. Kostis <lakostis@altlinux.ru>

%{?_enable_bdb:BuildRequires: db4-devel}
%{?_enable_libglusterfsclient:BuildRequires: libfuse-devel}
%{?_enable_ibverbs:BuildRequires: libibverbs-devel}

BuildRequires: libtool
BuildRequires: bison flex

# due recent incompatibility between releases :(
Requires: lib%name = %version-%release
%{?_enable_libglusterfsclient:Requires: libglusterfsclient = %version-%release}

Url: http://www.glusterfs.org
Source0: ftp://ftp.zresearch.com/pub/gluster/glusterfs/2.0/%name-%{version}-%{stage}.tar.gz
Source1: %{name}d.init
Source2: %{name}d

%description
GlusterFS is a clustered file-system capable of scaling to several
peta-bytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file system in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in userspace and easily manageable.

%package -n lib%{name}
Summary: GlusterFS Libraries
Group: System/Libraries

%description -n lib%{name}
This package provides system libraries for GlusterFS.

%if_enabled libglusterfsclient
%package -n libglusterfsclient
Summary: FUSE based GlusterFS client
Group: System/Base
Requires: lib%name = %version-%release
Obsoletes: %name-client < 2.0.0
Provides: %name-client

%description -n libglusterfsclient
This package provides the FUSE based GlusterFS client.
%endif

%package devel
Summary: GlusterFS Development Libraries
Group: Development/C
Requires: %name = %version-%release

%description devel
GlusterFS is a clustered file-system capable of scaling to several
peta-bytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file system in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in userspace and easily manageable.

This package provides the development libraries.

%package devel-static
Summary: GlusterFS Development Libraries
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package provides the static version of GlusterFS development libraries.

%prep
%setup

%build
%autoreconf
%configure \
	--localstatedir=%{_var} \
	%{subst_enable static} \
	%{subst_enable bdb} \
	%{subst_enable libglusterfsclient} \
	%{subst_enable ibverbs}
%make_build

%install
%__make install DESTDIR=%buildroot
%__mkdir_p %buildroot{%_sysconfdir/sysconfig,%_initrddir}
rm -rf %buildroot%_initrddir/*
find %buildroot%_libdir/%name -name *.la -exec rm -rf {} \;
%__install -m755 %SOURCE1 %buildroot%_initrddir/%{name}d
%__install -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/
%__mkdir_p %buildroot{%_includedir/%name,%buildroot%_logdir/%name}
touch %buildroot%_logdir/%name/exports.log
%__cp %_builddir/%name-%version/libglusterfs/src/*.h %buildroot%_includedir/glusterfs/
%__mkdir_p %buildroot%_docdir/%name-%version
%__cp -a AUTHORS COPYING NEWS %buildroot%_docdir/%name-%version/
%__cp -a extras/*.sh %buildroot%_docdir/%name-%version/
%__mv %buildroot%_docdir/%name/examples %buildroot%_docdir/%name-%version/

%files
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/%{name}d.vol.sample
%config(noreplace) %_sysconfdir/sysconfig/%{name}d
%_initrddir/*
%_sbindir/%{name}d
%if_disabled libglusterfsclient
%config %_sysconfdir/%name/%name.vol.sample
%dir %_logdir/%name
%_sbindir/%{name}
%_man8dir/%{name}*
%endif
%_bindir/%{name}-volgen
%dir %_datadir/%{name}
%_datadir/%{name}
%ghost %_logdir/%name/exports.log
%dir %_docdir/%name-%version
%_docdir/%name-%version

%post
%post_service %{name}d

%preun
%preun_service %{name}d

%files -n libglusterfs
%dir %_libdir/%name
%_libdir/%name
%_libdir/lib*.so.*

%if_enabled libglusterfsclient
%files -n libglusterfsclient
%config %_sysconfdir/%name/%name.vol.sample
%_sbindir/%{name}
/sbin/mount.glusterfs
%dir %_logdir/%name
%_man8dir/*%{name}*
%endif

%files devel
%_libdir/*.so
%dir %_includedir/glusterfs
%_includedir/glusterfs/*
%exclude %_includedir/glusterfs/y.tab.h
%if_enabled libglusterfsclient
%_includedir/libglusterfsclient.h
%endif

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.9-alt0.42.g779b491.1
- Rebuild with Python-2.7

* Tue May 18 2010 L.A. Kostis <lakostis@altlinux.ru> 2.0.9-alt0.42.g779b491
- Updated to GIT v2.0.9-42-g779b491 snapshot.

* Mon Jan 25 2010 L.A. Kostis <lakostis@altlinux.ru> 2.0.9-alt0.9.ge553411
- Updated to GIT v2.0.9-9-ge553411 snapshot.

* Thu Jan 14 2010 L.A. Kostis <lakostis@altlinux.ru> 2.0.9-alt0.1.ge700afa
- Updated to GIT v2.0.9-1-ge700afa snapshot.
- Added patches:
  + libglusterfsclient/read: fix data corruption (BUG:531).

* Mon Nov 30 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.8-alt3
- Updated to GIT v2.0.8-11-g5a131d6 snapshot.
- Local fixes:
  - glusterfs/libglusterfs/src/protocol.h: apply fix from Kirill Shutemov
    fixing compilation with recent gcc (see upstream #197 for details).
  - glusterfs.spec: add post/preun actions (by vvk@) (closes #21513).

* Thu Nov 12 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.8-alt1
- Updated to 2.0.8.

* Wed Oct 07 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.7-alt0.git20091005
- GIT v2.0.7-6-g65c68a0 snapshot.

* Thu Oct 01 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.6-alt2.git20090930
- switch to v2.0.6-91-g7ba8901.
- add volume generator script from extras.

* Sat Aug 29 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.6-alt2.git20090817
- fix logfile handling, remove useless documentation files.

* Thu Aug 27 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.6-alt1.git20090817
- switch to GIT v2.0.6-13-g86f2f04.
- add hack to disable FORTIFY_SOURCE=2 optimisation due unpredictable
  logic in gcc (closes #20977).

* Sat Aug 15 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.6-alt1
- Updated to 2.0.6.

* Sun Aug 09 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.6-alt0.1.git20090807.rc4
- switch to GIT 8dfdde5 from release-2.0 branch.

* Fri Aug 07 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.6-alt0.1.git20090806.rc2
- GIT 57a6cb (fixed registration of saved_fds).

* Thu Aug 06 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.6-alt0.1.git20090804.rc2
- GIT 546390 snapshot (fixing some major segfaults in gluster core).
- harmonize git records ;)

* Sun Jul 19 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.4-alt1.git20090715
- GIT 48cbf6 snapshot.
- remove mod_glusterfs (will use booster instead).
- add mount.glusterfs man page.

* Mon May 25 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.1-alt1.git20090522
- GIT 8b5617 snapshot (fix crash in __socket_reset).

* Thu May 14 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.1-alt1
- 2.0.1 release.
- add include/glusterfs to -devel.

* Sun May 03 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt3.rel
- 2.0.0 release + some misc fixes from GIT (f827d15).

* Thu Apr 09 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt2.pre35
- GIT fb034b shapshot (many fixes in AFR and BDB storage).

* Tue Mar 31 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt1.rc7
- GIT 3276e6 snapshot (contains fix for memory leak in client protocol).

* Fri Mar 27 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt0.1.rc7
- 2.0.0rc7.
- GIT 6c28cb.

* Sun Mar 22 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt0.rc5.3
- GIT 270621 snapshot (fixing crash in write-behind translator).
- exclude *.la.

* Sat Mar 21 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt0.rc5.2
- fix init.d script.
- strict version requires for server/client.

* Thu Mar 19 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt0.rc5.1
- 2.0.0rc5.
- GIT c2035 snapshot.

* Tue Mar 17 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt0.rc4.1
- remove obsoleted macros.
- GIT 1601b snapshot.

* Thu Mar 12 2009 L.A. Kostis <lakostis@altlinux.ru> 2.0.0-alt0.rc4
- 2.0.0rc4 test build.

* Thu Dec 11 2008 L.A. Kostis <lakostis@altlinux.ru> 1.3.12-alt0.M41.2
- new build.

* Thu Dec 11 2008 L.A. Kostis <lakostis@altlinux.ru> 1.3.12-alt1.1
- fix (hope finally) separate client/server packaging.

* Fri Nov 28 2008 L.A. Kostis <lakostis@altlinux.ru> 1.3.12-alt0.M41.1
- Backport for branch 4.1.

* Fri Nov 28 2008 L.A. Kostis <lakostis@altlinux.ru> 1.3.12-alt1
- new version.
- add init.d script for server.

* Sun Sep 07 2008 L.A. Kostis <lakostis@altlinux.ru> 1.3.9-alt2
- split -client and -libs.

* Tue Sep 02 2008 L.A. Kostis <lakostis@altlinux.ru> 1.3.9-alt1
- initial build for ALTLinux.

* Sat Apr 19 2008 Amar Tumballi <amar@zresearch.com> - 1.3.8pre6
- Merged common, client and server packages into one package.

* Fri Apr 11 2008 Harshavardhana <harsha@zresearch.com> - 1.3.8pre5
- Changed many hardcoded variables to standard rpm variables. Removed
  *.la unnecessary for the release.  Python option removed as it
  is not present with the coming releases.

* Tue Feb 12 2008 Harshavardhana <harsha@zresearch.com> - 1.3.8
- Replaced configure_options with different names for each configure
  options as it is observed that configure_options never get appended
  with extra options provided.

* Wed Jan 16 2008 Matt Paine <matt@mattsoftware.com> - 1.3.8
- Change all /usr/libx directory references to %_libdir
- Added new switch to enable build without building client RPMS

* Sun Jan 6 2008 Anand V. Avati <avati@zresearch.com> - 1.3.8
- glusterfs-booster.so back in libdir

* Fri Nov 09 2007 Harshavardhana Ranganath <harsha@zresearch.com> -  1.3.8
- Bumped to new version fixed problem with build for new glusterfs-booster.so
  inside /usr/bin

* Sun Oct 18 2007 Harshavardhana Ranganath <harsha@zresearch.com> - 1.3.7
- Bumped to new version

* Sun Oct 18 2007 Harshavardhana Ranganath <harsha@zresearch.com> - 1.3.6
- Bumped to new version

* Sun Oct 14 2007 Harshavardhana Ranganath <harsha@zresearch.com> - 1.3.5
- Bumped to new version

* Tue Oct 09 2007 Harshavardhana Ranganath <harsha@zresearch.com> - 1.3.4
- Bumped to new version

* Tue Oct 02 2007 Harshavardhana Ranganath <harsha@zresearch.com> - 1.3.3
- Bumped to new version

* Tue Oct 02 2007 Harshavardhana Ranganath <harsha@zresearch.com> - 1.3.2
- Bumped to new version

* Thu Sep 20 2007 Harshavardhana Ranganath <harsha@zresearch.com> - 1.3.1
- built new rpms with ibverbs seperate

* Sat Aug 4 2007 Matt Paine <matt@mattsoftware.com> - 1.3.pre7
- Added support to build rpm without ibverbs support (use --without ibverbs switch)

* Sun Jul 15 2007 Matt Paine <matt@mattsoftware.com> - 1.3.pre6
- Initial spec file

