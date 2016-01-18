Name: quota
Version: 4.03
Release: alt1
Epoch: 2

%def_disable rpcsetquota

# quota_nld.c, quotaio_xfs.h:       GPLv2
# bylabel.c copied from util-linux: GPLv2+
# svc_socket.c copied from glibc:   LGPLv2+
# doc/quotas.ms, quotaops.c, quot.c, quotaon.c, edquota.c, quot.h, quota.c,
# quotaio_v1.c:                     BSD
License: BSD and LGPLv2+ and GPLv2+
Summary: System administration tools for monitoring users' disk usage
Group: System/Configuration/Other
Url: http://sourceforge.net/projects/linuxquota/

# http://downloads.sourceforge.net/linuxquota/quota-%version.tar.gz
# git://linuxquota.git.sourceforge.net/gitroot/linuxquota/linuxquota
# git://git.altlinux.org/gears/q/quota.git
Source: %name-%version-%release.tar

Requires: vitmp
BuildRequires: libe2fs-devel

%description
This package contains system administration tools for monitoring
and limiting user and or group disk usage per file system.

%package rpc
Group: Networking/Other
Summary: RPC quota daemon
Requires: %name = %EVR
Provides: rquotad = %version

%description rpc
rpc.rquotad is an rpc(3) server which returns quotas for a user
of a local filesystem which is mounted by a remote machine over the NFS.

%package devel
Group: Development/C
Summary: Remote quota protocol header files and documentation
BuildArch: noarch
Requires: %name = %EVR

%description devel
This package contains remote quota protocol header files and documentation.

%prep
%setup -n %name-%version-%release

%build
%autoreconf
%configure \
	--enable-ext2direct \
	--enable-werror \
	--disable-bsd_behaviour \
	--disable-ldapmail \
	--disable-libwrap \
	--disable-netlink \
	--disable-silent-rules \
	--disable-xfs-roothack \
	%{subst_enable rpcsetquota} \
	#
%make_build

%install
%makeinstall_std
mkdir %buildroot/sbin
mv %buildroot%_sbindir/quota{on,off,check} %buildroot/sbin/
install -Dpm644 rpc-rquotad.service %buildroot%_unitdir/rpc-rquotad.service
install -Dpm644 rpc-rquotad.sysconfig %buildroot/etc/sysconfig/rpc-rquotad
%define docdir %_docdir/%name
gzip -9n %buildroot%docdir/*.eps
gzip -c9n Changelog > %buildroot%docdir/Changelog.gz

%find_lang %name

%post rpc
%post_service rpc.rquotad

%preun rpc
%preun_service rpc.rquotad

%files -f %name.lang
%config(noreplace) /etc/*quota*
/sbin/*
%_bindir/*
%_sbindir/*
%exclude %_sbindir/rpc.rquotad
%_man1dir/*
%_man5dir/*
%_man8dir/*
%exclude %_man8dir/rpc.rquotad.8*
%doc %docdir/

%files rpc
%config(noreplace) /etc/sysconfig/rpc-rquotad
%_unitdir/rpc-rquotad.service
%_sbindir/rpc.rquotad
%_man8dir/rpc.rquotad.8*

%files devel
%_includedir/rpcsvc/*
%_man3dir/*

%changelog
* Mon Jan 18 2016 Dmitry V. Levin <ldv@altlinux.org> 2:4.03-alt1
- v4.00 -> v4.03-3-g861154e.
- Moved rpc.rquotad to %name-rpc subpackage.
- Moved %_includedir/rpcsvc/* to %name-devel subpackage.

* Tue Feb 15 2011 Anton Protopopov <aspsk@altlinux.org> 2:4.00-alt1
- quotasync.c: use GNU implementation of basename(3)
- Add epoch:2 to prevent version conflicts with quota from branches

* Thu Feb 10 2011 Anton Protopopov <aspsk@altlinux.org> 4.00-alt1
- Apply/rebase ALT patches from old repo:
  * Fix XFS over loopback support
  * Don't strip binaries
  * Use more polite messages in e-mail warnings
  * Fix quota{on,off} paths in quota{on,off}.8
  * Use vitmp instead of vi in edquota(8)
  * Fix errors uncovered by compiler
  * Use configure macros instead of hardcoded defaults
  * rquota_svc.c (parse_options): Import FC enhancement to port range check
  * Fix build with --disable-bsd_behaviour
- Updated to 4.00-pre2+ (ALT #25056)

* Sun Apr 15 2007 Dmitry V. Levin <ldv@altlinux.org> 2:3.14-alt1
- Updated to 3.14+ cvs snapshot 20070326.

* Mon Jun 27 2005 Dmitry V. Levin <ldv@altlinux.org> 2:3.13-alt1
- Updated to 3.13 release.
- Removed merged upstream alt-format patch.
- Rediffed patches.
- Enabled build with glibc kernel headers.

* Sat Jun 18 2005 Dmitry V. Levin <ldv@altlinux.org> 2:3.12-alt5
- Fixed XFS over loopback support.

* Sun Apr 03 2005 Dmitry V. Levin <ldv@altlinux.org> 2:3.12-alt4
- Updated to cvs snapshot 20050331.

* Fri Mar 25 2005 Dmitry V. Levin <ldv@altlinux.org> 2:3.12-alt3
- Updated to cvs snapshot 20050318.
- Updated patches.

* Wed Mar 23 2005 Dmitry V. Levin <ldv@altlinux.org> 2:3.12-alt2
- Fixed several format string bugs.
- quota: fixed potential garbage in error output.

* Tue Aug 03 2004 Dmitry V. Levin <ldv@altlinux.org> 2:3.12-alt1
- Updated to 3.12.
- Added quotaoff(8) manpage symlink (#4214).

* Thu Mar 18 2004 Dmitry V. Levin <ldv@altlinux.org> 2:3.11-alt1
- Updated to 3.11.

* Thu Aug 21 2003 Dmitry V. Levin <ldv@altlinux.org> 2:3.09-alt1
- Updated to 3.09.
- Updated build dependencies.

* Thu Feb 13 2003 Dmitry V. Levin <ldv@altlinux.org> 2:3.08-alt1
- Updated to 3.08, reviewed patches.

* Fri Nov 15 2002 Konstantin Volckov <goldhead@altlinux.ru> 2:3.07-alt1
- 3.07
- Fixed file lists

* Wed Jun 26 2002 Konstantin Volckov <goldhead@altlinux.ru> 2:3.06-alt1
- 3.06 release

* Mon May 20 2002 Konstantin Volckov <goldhead@altlinux.ru> 2:3.05-alt1
- 3.05 release
- Fixed XFS detection BUG

* Fri May 17 2002 Dmitry V. Levin <ldv@altlinux.org> 2:3.05-alt0.2pre1
- Set default edquota(8) editor to vitmp(1).

* Mon Apr 01 2002 Konstantin Volckov <goldhead@altlinux.ru> 2:3.05-alt0.1pre1
- 3.05pre1
- Fixed some bugs
- Added modprobe support for new 2.4 kernels

* Thu Feb 28 2002 Stanislav Ievlev <inger@altlinux.ru> 2:3.03-alt1
- 3.03
- return old name

* Tue Nov 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.01-alt0.9
- 3.01pre9
- Some spec fixes

* Wed May 30 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.00-alt4
- Fixed reiserfs quota support

* Mon May 28 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.00-alt3
- Added manpage symlink for rpc.rquotad.
- Add rquotad for provides.

* Fri May 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.00-alt2
- Re-enabled rquotad stuff.

* Fri May 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.00-alt1
- ALT adaptions.

* Fri Mar 30 2001 Preston Brown <pbrown@redhat.com>
- use rpc.rquotad from here again (#33738)

* Thu Mar 15 2001 Preston Brown <pbrown@redhat.com>
- enable ALT_FORMAT for edquota

* Tue Mar 13 2001 Preston Brown <pbrown@redhat.com>
- I broke passing devices on the cmd line.  Fixed.

* Fri Mar 09 2001 Preston Brown <pbrown@redhat.com>
- quota 3.00 is required by recent kernel 2.4 changes
- no warnquota included this time, not yet ported
- quite a bit of work on quotacheck to make is backwards compatible
- we will likely go back to "quota 2.00" as these projects merge...
