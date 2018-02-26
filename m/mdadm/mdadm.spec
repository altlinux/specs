Name: mdadm
Version: 3.2.3
Release: alt1

Summary: A tool for managing Soft RAID under Linux
License: GPLv2+
Group: System/Configuration/Hardware
Url: http://neil.brown.name/blog/mdadm

# http://git.altlinux.org/gears/m/mdadm.git
Source: %name-%version-%release.tar

# due to /lib/udev/rules.d/64-md-raid.rules
Conflicts: udev < 151

%description
mdadm is a program that can be used to create, manage, and monitor
Linux MD (Software RAID) devices.

As such is provides similar functionality to the raidtools packages.
The particular differences to raidtools is that mdadm is a single
program, and it can perform (almost) all functions without a
configuration file (that a config file can be used to help with
some common tasks).

%prep
%setup -n %name-%version-%release

%build
%make_build mdadm mdmon CXFLAGS='%optflags' SYSCONFDIR='%_sysconfdir'
bzip2 -9fk ChangeLog

%install
%makeinstall_std MANDIR=%_mandir BINDIR=/sbin
install -pD -m755 alt/mdadm.init %buildroot%_initdir/mdadm
install -pD -m755 misc/syslog-events %buildroot/sbin/mdadm-syslog-events
install -pD -m600 alt/mdadm.conf %buildroot%_sysconfdir/mdadm.conf
install -pD -m644 alt/mdadm.service %buildroot%systemd_unitdir/mdadm.service

install -pD -m755 alt/checkarray %buildroot%_datadir/mdadm/checkarray
install -pD -m644 alt/mdadm.sysconfig %buildroot%_sysconfdir/sysconfig/mdadm
install -pD -m644 alt/mdadm.crond %buildroot%_sysconfdir/cron.d/mdadm


%post -f alt/raidtabtomdadm.sh
%post_service mdadm

%preun
%preun_service mdadm

%files
/sbin/md*
/lib/udev/rules.d/64-md-raid.rules
%config(noreplace,missingok) %_sysconfdir/mdadm.conf
%config(noreplace) %_sysconfdir/sysconfig/mdadm
%_sysconfdir/cron.d/mdadm
%_mandir/man?/md*
%_initdir/mdadm
%_datadir/mdadm/
%systemd_unitdir/mdadm.service
%doc TODO ChangeLog.bz2 mdadm.conf-example ANNOUNCE-%version alt/README*

%changelog
* Tue Jan 31 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Sat Aug 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.2-alt2
- fix AUTOCHECK check in autocheck script (ALT #25641)

* Thu Jul 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Mon May 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.4-alt3
- add crond job for periodical array check (ALT #25641)

* Fri May 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.4-alt2
- shaba@:
    add mdadm.service for systemd

* Mon Sep 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.4-alt1
- Updated to mdadm-3.1.4-2-ga2ce5a1 (closes: #23792).
- Packaged README.recipes from Debian (closes: #11518).
- Packaged mdmon.
- Dropped unused mdassemble.
- Cleaned up specfile and startup script.

* Sun Sep 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6.3-alt2
- pack 64-md-raid.rules (removed by udev upstream in ver. 151)

* Wed Aug 22 2007 Ilya Evseev <evseev@altlinux.ru> 2.6.3-alt1
- updated to new version 2.6.3

* Tue May 22 2007 Ilya Evseev <evseev@altlinux.ru> 2.6.2-alt1
- updated to new version 2.6.2, fix patch #3

* Mon Apr 16 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.1-alt3.1
- mdadm.init: Fixed typo introduced in 2.6.1-alt3 release.
- %%triggerun: Removed.
- %%triggerin: Do not spam on every package update.

* Sun Apr 15 2007 Ilya Evseev <evseev@altlinux.ru> 2.6.1-alt3
- bugfixes:
   + 11021: shutdown previous versions of mdadm at /usr/sbin on RPM upgrade
   + 11431: dont start service when no records in /proc/mdstat

* Sat Mar  3 2007 Ilya Evseev <evseev@altlinux.ru> 2.6.1-alt2
- fixed installation path for mdadm-syslog-events

* Sat Mar  3 2007 Ilya Evseev <evseev@altlinux.ru> 2.6.1-alt1
- updated to version 2.6.1, simplify patch #3
- bugfixes:
   + 10357 (mdassemble crashes because dietlibc < 0.30-alt2
            with gcc4.1 needs -fno-stack-protector)
   + 10727 (missing mdassemble.8 manpage)
   + 10782 (strange events in mdmonitor - possibly fixed in upstream?)
   + 10909 (change 740 permissions to 755)
   + 10910 (support condstop in service script)
   + 10915 (move binaries from /usr/sbin to /sbin)

* Wed Jan 24 2007 Ilya Evseev <evseev@altlinux.ru> 2.6-alt2
- fixed x86_64 problems

* Mon Jan 22 2007 Ilya Evseev <evseev@altlinux.ru> 2.6-alt1
- updated to new version 2.6

* Wed Nov 22 2006 Ilya Evseev <evseev@altlinux.ru> 2.5.6-alt1
- updated to new version 2.5.6

* Fri Oct 27 2006 Ilya Evseev <evseev@altlinux.ru> 2.5.5-alt1
- updated to new version 2.5.5
- patch for ignoring asprintf result (yes, I know that's dirty..)

* Sat Sep  2 2006 Ilya Evseev <evseev@altlinux.ru> 2.5.3-alt2
- fixed dietlibc-related problems (#9939) on x86_64
- added optional disabling of dietlibc usage

* Tue Aug  8 2006 Ilya Evseev <evseev@altlinux.ru> 2.5.3-alt1
- updated to new version 2.5.3

* Tue Jul 25 2006 Ilya Evseev <evseev@altlinux.ru> 2.5.2-alt1
- updated to new version 2.5.2

* Thu Jun 22 2006 Ilya Evseev <evseev@altlinux.ru> 2.5.1-alt1
- updated to new version 2.5.1
- patch #1 is no more needed because the same thing is now in the upstream
- fixup command line arguments for mdassemble build

* Mon May 29 2006 Ilya Evseev <evseev@altlinux.ru> 2.5-alt2
- added patch #1 for omitting openssl dependency
- little description changes

* Fri May 26 2006 Ilya Evseev <evseev@altlinux.ru> 2.5-alt1
- updated to new version 2.5

* Fri Apr 28 2006 Ilya Evseev <evseev@altlinux.ru> 2.4.1-alt1
- updated to new version 2.4.1

* Thu Feb  9 2006 Ilya Evseev <evseev@altlinux.ru> 2.3.1-alt1
- updated to new version 2.3.1

* Fri Feb  3 2006 Ilya Evseev <evseev@altlinux.ru> 2.3-alt1
- updated to new version 2.3
- small specfile improvements:
   + mdadm stuff was compiled twice
   + more strict permissions for installed stuff

* Fri Oct 14 2005 Ilya Evseev <evseev@altlinux.ru> 2.1-alt3
- more once attempt to break new Sysiphus restrictions
  (halt on undefined macros even they are commented)

* Mon Oct 10 2005 Ilya Evseev <evseev@altlinux.ru> 2.1-alt2
- added workaround for new Sisyphus restriction:
  all macros should be defined even they are referenced in comments.

* Fri Sep 16 2005 Ilya Evseev <evseev@altlinux.ru> 2.1-alt1
- update to new version

* Wed Jul 27 2005 Ilya Evseev <evseev@altlinux.ru> 1.12.0-alt2
- bugfix #7087 (use grep instead of egrep in service script)
- watch udev (un)install and display warnings about changed devices naming
- created our own minimalistic configuration file for mdmonitor;
  however, it should be completely functional in most cases

* Wed Jul 13 2005 Michael Shigorin <mike@altlinux.org> 1.12.0-alt1
- 1.12.0
- removed peet@'s patch (fixed in 1.11.0)

* Thu May 12 2005 Peter V. Saveliev <peet@altlinux.ru> 1.10.0-rad1
- fixed device add

* Sun Apr 10 2005 Ilya Evseev <evseev@altlinux.ru> 1.10.0-alt1
- updated to 1.10.0, fixed segfault on 'mdadm -c partitions'
- changed project URL and source URL
- mdassemble cannot be disabled; it's installed to /sbin
- documentation: placed patch that should be applied to /etc/rc.d/rc.sysinit
  (see details on https://bugzilla.altlinux.org/show_bug.cgi?id=6322 and 6397)

* Mon Mar  8 2005 Ilya Evseev <evseev@altlinux.ru> 1.9.0-alt1
- 1.9.0
- specfile:
   + added russian summary and description,
   + changed source URL,
   + added mdmpd reference.
- taken from Mdk:
   + service init script,
   + raidtools conversion script,
   + diet libc bindings (may be turned off).

* Mon Jan 26 2004 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt1
- Updated to 1.5.0.

* Thu Dec 18 2003 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.
- Specfile cleanup.

* Tue May 20 2003 Alexander Bokovoy <ab@altlinux.ru> 1.2.0-alt1
- Initial build for ALT Linux Sisyphus

* Fri May 10 2002  <neilb@cse.unsw.edu.au>
- update to 1.0.0
- Set CXFLAGS instead of CFLAGS

* Sat Apr  6 2002  <neilb@cse.unsw.edu.au>
- change install to use "make install"

* Fri Mar 15 2002  <gleblanc@localhost.localdomain>
- beautification
- made mdadm.conf non-replaceable config
- renamed Copyright to License in the header
- added missing license file
- used macros for file paths

* Fri Mar 15 2002 Luca Berra <bluca@comedia.it>
- Added Obsoletes: mdctl
- missingok for configfile

* Wed Mar 12 2002 NeilBrown <neilb@cse.unsw.edu.au>
- Add md.4 and mdadm.conf.5 man pages

* Fri Mar 08 2002		Chris Siebenmann <cks@cquest.utoronto.ca>
- builds properly as non-root.

* Fri Mar 08 2002 Derek Vadala <derek@cynicism.com>
- updated for 0.7, fixed /usr/share/doc and added manpage

* Tue Aug 07 2001 Danilo Godec <danci@agenda.si>
- initial RPM build
