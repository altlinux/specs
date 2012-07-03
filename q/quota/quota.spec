Name: quota
Version: 4.00
Release: alt1
Epoch: 2

Summary: System administration tools for monitoring users' disk usage
License: BSD-style
Group: System/Configuration/Other
Url: http://sourceforge.net/projects/linuxquota/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# http://downloads.sourceforge.net/linuxquota/quota-%version.tar.gz
Source: quota-%version.tar

Requires: vitmp
Provides: rquotad = %version

# Automatically added by buildreq on Thu Aug 21 2003
BuildRequires: libe2fs-devel libwrap-devel

%description
This package contains system administration tools for monitoring
and limiting users' and or groups' disk usage, per filesystem.

%prep
%setup -q

%build
%autoreconf
%configure \
	--enable-rootsbin \
	--disable-bsd_behaviour \
	--disable-strip-binaries \
	#
%make_build

%install
%make_install install ROOTDIR=%buildroot
ln -s quotaon.8 %buildroot%_man8dir/quotaoff.8
chmod 755 %buildroot/sbin/*

%find_lang %name

%files -f %name.lang
%config(noreplace) %_sysconfdir/*
/sbin/*
%_bindir/*
%_sbindir/*
#%_includedir/rpcsvc/* # conflicts with glibc
%_mandir/man?/*

%changelog
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
