Name: autofs
Version: 5.0.6
Release: alt1

Summary: A tool for automatically mounting and unmounting filesystems
License: GPL
Group: System/Kernel and hardware
Url: ftp://ftp.kernel.org/pub/linux/daemons/autofs/v4/

Source: %name-%version-%release.tar

Requires(post): %post_service
Requires(preun): %preun_service

BuildRequires: bison flex
BuildRequires: libkrb5-devel libldap-devel libsasl2-devel libssl-devel libxml2-devel

%package ldap
Summary: A tool for automatically mounting and unmounting filesystems
Group: System/Kernel and hardware
Requires: %name = %version-%release 

# {{{ descriptions

%description
Autofs controls the operation of the automount daemons.  The automount daemons
automatically mount filesystems when you use them and unmount them after a
period of inactivity.  Filesystems can include network filesystems, CD-ROMs,
floppies and others.

Install this package if you want a program for automatically mounting and
unmounting filesystems.

%description ldap
Autofs controls the operation of the automount daemons.  The automount daemons
automatically mount filesystems when you use them and unmount them after a
period of inactivity.  Filesystems can include network filesystems, CD-ROMs,
floppies and others.

This package adds LDAP support to the %name package

# }}}

%prep
%setup

%build
%autoreconf
export ac_cv_path_MODPROBE=/sbin/modprobe
%configure --disable-mount-locking --enable-ignore-busy --enable-forced-shutdown
%make_build DONTSTRIP=1

%install
%make_install install INSTALLROOT=%buildroot
rm -f %buildroot%_sysconfdir/auto.{misc,net}
(cd altlinux && find . -type f |cpio -pumd %buildroot)
chmod 0644 samples/auto.*

%define docdir %_defaultdocdir/%name-%version
mkdir -p %buildroot%docdir
rm -f samples/rc.autofs* samples/autofs.conf.default* samples/Makefile
cp -pr CHANGELOG CREDITS COPYRIGHT README* samples %buildroot%docdir

%post
%post_service %name

%preun
%preun_service %name

%triggerun -- autofs < 5.0.1
[ $2 -gt 0 ] || exit 0
if /sbin/start-stop-daemon --stop --quiet \
    --signal USR2 --retry 5 --exec /usr/sbin/automount; then
/sbin/service autofs start ||:
fi

%files
%dir %docdir
%dir %docdir/samples
%docdir/[A-Z]*
%docdir/samples/auto.master
%docdir/samples/auto.misc
%docdir/samples/auto.net
%docdir/samples/auto.smb

%config(noreplace) %_initdir/autofs
%config(noreplace) %_sysconfdir/auto.master
%config(noreplace) %_sysconfdir/auto.tab
%config(noreplace) %_sysconfdir/auto.avahi
%config(noreplace,missingok) %_sysconfdir/auto.smb
%config(noreplace) %_sysconfdir/sysconfig/%name

%dir %_libdir/%name
%_libdir/%name/*
%exclude %_libdir/%name/lookup_ldap.so
%exclude %_libdir/%name/lookup_ldaps.so

%_sbindir/*
%_mandir/man?/*

%files ldap
%docdir/samples/autofs.schema
%docdir/samples/auto.master.ldap
%docdir/samples/ldap-*

%_sysconfdir/autofs_ldap_auth.conf

%_libdir/%name/lookup_ldaps.so
%_libdir/%name/lookup_ldap.so

%changelog
* Thu Jun 30 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.6-alt1
- 5.0.6 released

* Mon Apr 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.5-alt3
- add explicit build-dep to sasl2

* Mon Aug 30 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.5-alt2
- do not expect /sbin/modprobe exists during build 

* Sat Sep 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.5-alt1
- 5.0.5 released

* Wed Feb 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.4-alt3
- avahi-based program map added

* Tue Dec 16 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.4-alt2
- expire specific submount only
- fix negative cache non-existent key

* Tue Nov  4 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.4-alt1
- 5.0.4 released

* Thu May 22 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.3-alt1
- 5.0.3 released

* Mon Jun 18 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.2-alt1
- 5.0.2 released

* Sat Feb 24 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.1-alt1
- 5.0.1 released

* Mon Jan  1 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.1-alt0.2
- 5.0.1rc2
- built w/o ldap

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 4.1.4-alt0.3.1
- Rebuilt with libldap-2.3.so.0.

* Sun May  8 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.4-alt0.3
- 4.1.4

* Mon Jul  5 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.3-alt0.3
- adjust_autofs: do not pretend to mountpoints assigned to subfs

* Thu Jun 10 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.3-alt0.2
- patches added:
  + autofs-4.1.3-mtab_lock.patch
  + autofs-4.1.3-strict.patch
  + autofs-4.1.3-icmp_ping.patch

* Tue May 25 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.3-alt0.1
- 4.1.3

* Wed Feb 12 2003 Stanislav Ievlev <inger@altlinux.ru> 4.0.0-alt0.6.pre10
- Added support for quiet mount option

* Mon Dec 30 2002 Dmitry V. Levin <ldv@altlinux.org> 4.0.0-alt0.5.pre10
- Added %_sbindir/adjust_autofs (from initscripts).

* Tue Dec 17 2002 Dmitry V. Levin <ldv@altlinux.org> 4.0.0-alt0.4.pre10
- Add skipstart support in startup script (required for fix #0000530).

* Fri Jan 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 4.0.0-alt0.3.pre10
- Enable by default, added TABFILE option, added tabfile check.

* Mon Jun 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.0.0-alt0.2.pre10
- Updated startup script.
- Dropped openldap for a while.

* Fri Jun 15 2001 Mikhail Zabaluev <mhz@altlinux.ru> 4.0.0-alt0.1
- ALT Linux adaptations
- Manually edited shell requires (the script sucked ypcat in)
- Fixed an ugliness in the init script patch

* Mon Jun 11 2001 Vincent Saugey <vince@mandrakesoft.com> 4.0.0-0.9mdk
- rebuild with ldap2 lib

* Tue Apr 10 2001 Renaud Chaillat <rchaillat@mandrakesoft.com> 4.0.0-0.8mdk
- new version (pre10)

* Thu Mar 29 2001 Frederic Lepied <flepied@mandrakesoft.com> 4.0.0-0.7mdk
- use the new rpm macros for servers.

* Mon Mar 26 2001 Frederic Lepied <flepied@mandrakesoft.com> 4.0.0-0.6mdk
- removed /misc and /net

* Mon Nov  6 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 4.0.0-0.5mdk
- new version
- updated patches and init script

* Tue Sep  5 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.0.0-0.4mdk
- use condrestart on upgrade.
- enabled again init patch to have a condrestart and to have a start at 18 level.

* Wed Aug 30 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.0.0-0.3mdk
- rebuild for the user of _initrddir macro.

* Fri Aug 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 4.0.0-0.2mdk
- rebuild to get rid of "if your Red Hat Linux machine is.."
  thanks to Anton Graham <darkimage@bigfoot.com>

* Thu Aug 17 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.0.0-0.1mdk
- 4.0.0pre7

* Thu Jul 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1.5-1mdk
- 3.1.5
- BM
- macroqeivhqowicvjzificationning

* Fri Apr 28 2000 Warly <warly@mandrakesoft.com> 3.1.4-4mdk
- change rc.init value to S72 K08

* Tue Mar 22 2000 Daouda Lo <daouda@mandrakesoft.com> 3.1.4-3mdk
- fix wrong date.
- 3.1.4 (new release).
- remove ugly patches.
- add smbmount support.

* Tue Nov 23 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- strip

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Enable $SMP build/check

* Wed Oct  6 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- checkconfig --del in %preun, not %postun (rh).
- add patch from HJLu to handle NIS auto.master better (rh).

* Fri Sep 24 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Forgot to fix the bloody permissions :/

* Fri Sep 24 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- remove rc patch it's breaking yp
- again with the redhat mergeings:
	* Wed Aug 25 16:00:00 1999 Cristian Gafton <gafton@redhat.com>
	- fix bug #4708
	* Sat Aug 21 16:00:00 1999 Bill Nottingham <notting@redhat.com>
	- fix perms on /usr/lib/autofs/*
	- add support for specifying maptype in auto.master

* Tue Aug 17 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- RedHat Merge:
	* Fri Aug 13 1999 Cristian Gafton <gafton@redhat.com>
	- add patch from rth to avoid an infinite loop

* Wed Jun 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Patch from H.J Lu <hjl@varesearch.com> :
	-* fix rc script for /var/lock/subsys.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- enahanced initscript to try to load maps over NIS
- changed the mount point back to misc (there is a reason we leave /mnt
  alone)
- patched back autofs.misc to the version shipped on 5.2 to avoid replacing
  yet one more config file for those who upgrade

* Wed Mar 24 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 3.1.3, fixing smbfs stuff and other things
- changed mountpoint from /misc to /mnt

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 10)

* Mon Feb  8 1999 Bill Nottingham <notting@redhat.com>
- build for kernel-2.2/glibc2.1

* Tue Oct  6 1998 Bill Nottingham <notting@redhat.com>
- fix bash2 breakage in init script

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- typo in man page.

* Mon Jul 20 1998 Jeff Johnson <jbj@redhat.com>
- added sparc to ExclusiveArch.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- updated to 3.1.1

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscripts

* Fri Dec 05 1997 Michael K. Johnson <johnsonm@redhat.com>
- Link with -lnsl for glibc compliance.

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- exclusivearch for i386 for now, since our kernel packages on
  other platforms don't include autofs yet.
- improvements to initscripts.

* Thu Oct 16 1997 Michael K. Johnson <johnsonm@redhat.com>
- Built package from 0.3.14 for 5.0

