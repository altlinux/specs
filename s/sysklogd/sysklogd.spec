Name: sysklogd
Version: 1.4.1
Release: alt30

%define syslog_name syslogd
%define ROOT %_localstatedir/klogd

Summary: Base package for system logging and kernel message trapping daemons
License: GPLv2+
Group: System/Kernel and hardware
Url: http://www.infodrom.org/projects/sysklogd/
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source0: http://www.infodrom.org/projects/sysklogd/download/%name-%version.tar.bz2
Source1: syslog.conf
Source2: syslogd.log
Source3: syslogd.init
Source4: syslogd.sysconfig
Source5: klogd.init
Source6: klogd.sysconfig
Source7: reload-syslog

Patch0: sysklogd-1.4.1-cvs-20060928.patch

# RH
Patch1: sysklogd-1.4.2-rh-alt-warnings.patch
Patch2: sysklogd-1.4.2-rh-ksymless.patch
Patch3: sysklogd-1.4.1-rh-__syslog_chk.patch

# ALT/Owl
Patch11: sysklogd-1.4.2-alt-format.patch
Patch12: sysklogd-1.4.2-alt-redirect-std.patch
Patch13: sysklogd-1.4.2-alt-syslogd-nonblock.patch
Patch14: sysklogd-1.4.2-owl-syslogd-create-mode.patch
Patch15: sysklogd-1.4.2-owl-syslogd-doexit.patch

Patch21: sysklogd-1.4.2-caen-owl-klogd-drop-root.patch
Patch22: sysklogd-1.4.2-owl-klogd-kmsg.patch
Patch23: sysklogd-1.4.2-caen-owl-syslogd-bind.patch
Patch24: sysklogd-1.4.2-caen-owl-syslogd-drop-root.patch
Patch25: sysklogd-1.4.2-alt-syslogd-chroot.patch
Patch26: sysklogd-1.4.2-alt-syslogd-funix_dir.patch
Patch27: sysklogd-1.4.2-alt-SO_BSDCOMPAT.patch
Patch28: sysklogd-1.4.2-alt-syslog-symbols.patch

# ALT-specific
Patch31: sysklogd-1.4.2-alt-makefile.patch

PreReq: %syslog_name = %version-%release, klogd = %version-%release
Conflicts: logrotate < 0:3.3-ipl9mdk, vixie-cron < 0:3.0.1-ipl45mdk

BuildPreReq: coreutils

%description
This virtual package contains dependencies on syslogd and klogd.

%package -n %syslog_name
Summary: System logging daemon (%syslog_name)
Group: System/Kernel and hardware
Provides: %syslog_name-daemon
PreReq: syslog-common = %version-%release
PreReq: shadow-utils, service, coreutils, grep, chrooted-resolv, /var/resolv

%description -n %syslog_name
This package contains %syslog_name wich provide support for system logging.
syslogd runs as daemon (background process) and logs system messages to
different places according to a configuration file.

%package -n klogd
Summary: Kernel message trapping daemon (klogd)
Group: System/Kernel and hardware
PreReq: %syslog_name-daemon, shadow-utils, service
Conflicts: %syslog_name < %version-%release

%description -n klogd
This package contains klogd wich provide support for kernel logging.
klogd runs as daemon (background process) and logs kernel messages
via system logger.

%package -n syslog-common
Summary: Common stuff for system logs
Group: System/Kernel and hardware
Provides: /etc/syslog.d

%description -n syslog-common
This package contains log directories structure and logrotate scripts both for
classic syslog and syslog-ng.

%prep
%setup -q

%patch -p0

%patch1 -p1
%patch2 -p1
%patch3 -p1

%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1

%patch31 -p1

find -type f -name \*.orig -delete
sed -i '/linux\/linkage\.h/d' ksym_mod.c

%build
%make_build

%install
mkdir -p %buildroot{%_mandir/man{5,8},/sbin}

%makeinstall prefix=%buildroot

install -pD -m640 %SOURCE1 %buildroot%_sysconfdir/syslog.conf
install -pD -m640 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/syslog
install -pD -m755 %SOURCE3 %buildroot%_initdir/syslogd
install -pD -m640 %SOURCE4 %buildroot%_sysconfdir/sysconfig/%syslog_name

install -pD -m755 %SOURCE5 %buildroot%_initdir/klogd
install -pD -m640 %SOURCE6 %buildroot%_sysconfdir/sysconfig/klogd

chmod 755 %buildroot/sbin/*
mkdir -p %buildroot%_logdir/{kernel,user,mail,daemons,auth,lpr,news,uucp,cron,ftp,syslog}
touch %buildroot%_logdir/{kernel,user,mail,daemons,lpr,news,uucp,cron,ftp}/{info,warnings,errors} \
	%buildroot%_logdir/auth/{all,messages,secure} %buildroot%_logdir/mail/all \
	%buildroot%_logdir/syslog/{messages,alert,spooler,boot,sudo}
ln -s syslog/alert %buildroot%_logdir/alert
ln -s syslog/boot %buildroot%_logdir/boot.log
ln -s mail/all %buildroot%_logdir/maillog
ln -s syslog/messages %buildroot%_logdir/messages
ln -s auth/secure %buildroot%_logdir/secure
ln -s syslog/spooler %buildroot%_logdir/spooler

>%name.files
find %buildroot%_logdir -mindepth 1 -type d|
	fgrep -v uucp |
	sed -e 's|^%buildroot|%%dir %%attr(750,root,adm) |' >>%name.files
find %buildroot%_logdir -mindepth 1 -type l|
	sed -e 's|^%buildroot|%%attr(-,root,root)|' >>%name.files
find %buildroot%_logdir -mindepth 1 -type f|
	sed -e 's|^%buildroot|%%ghost %%attr(640,root,adm) %%verify(not md5 mtime size) |' >>%name.files

install -pD -m700 %SOURCE7 %buildroot/sbin/reload-syslog

mkdir -m700 %buildroot%_sysconfdir/syslog.d
ln -s %ROOT/dev/log %buildroot%_sysconfdir/syslog.d/klogd

# chroot stuff
mkdir -p %buildroot/%ROOT/dev
mksock %buildroot%ROOT/dev/log

%pre -n syslog-common
# Because RPM doesn't know the difference between files and directories,
# we need to verify if there is no file with the same name as the directory
# to be created for the new logdir architecture.
# If the name is the same and it is a file, rename it to name.old

for f in kernel user mail daemons auth lpr news uucp cron ftp syslog; do
	if [ -f "%_logdir/$f" -a ! -L "%_logdir/$f" ]; then
		%__mv -f "%_logdir/$f" "%_logdir/$f.old" &&
			%__mkdir "%_logdir/$f" &&
			%__mv "%_logdir/$f.old" "%_logdir/$f/"
	fi
done ||:

# Same comment about compatibility links.
for f in alert boot.log maillog messages secure spooler; do
	if [ -f "%_logdir/$f" -a ! -L "%_logdir/$f" ]; then
		%__mv -f "%_logdir/$f" "%_logdir/$f.old"
	fi
done ||:

%triggerpostun -- %name <= 1.4.1-alt3
if [ $1 -gt 1 ]; then
	if pidof /sbin/klogd >/dev/null; then
		/sbin/service klogd restart ||:
	fi
	if pidof /sbin/syslogd >/dev/null; then
		/sbin/service syslogd restart ||:
	fi
fi

%post -n syslog-common
cd %_logdir
# Create each log directory with logfiles.
for f in \
	{kernel,user,mail,daemons,lpr,news,uucp,cron,ftp}/{info,warnings,errors} \
	auth/{all,messages,secure} mail/all \
	syslog/{messages,alert,spooler,boot,sudo}
do
	if [ ! -f "$f" ]; then
		:>>"$f"
		%__chgrp adm "$f"
		%__chmod 640 "$f"
	fi
done ||:

%pre -n %syslog_name
/usr/sbin/groupadd -r -f syslogd
/usr/sbin/useradd -r -g syslogd -d /dev/null -s /dev/null -n syslogd >/dev/null 2>&1 ||:

%post -n %syslog_name
%post_service syslogd

%preun -n %syslog_name
%preun_service syslogd

%pre -n klogd
/usr/sbin/groupadd -r -f klogd
/usr/sbin/useradd -r -g klogd -d /dev/null -s /dev/null -n klogd >/dev/null 2>&1 ||:

%post -n klogd
%post_service klogd

%preun -n klogd
%preun_service klogd

%files

%files -n klogd
%config %_initdir/klogd
%config(noreplace) %_sysconfdir/sysconfig/klogd
%_sysconfdir/syslog.d/klogd
/sbin/klogd
%_mandir/man?/klogd*
%attr(710,root,klogd) %dir %ROOT
%attr(710,root,klogd) %dir %ROOT/dev
%attr(666,root,root) %ghost %ROOT/dev/log

%files -n %syslog_name
%config(noreplace) %attr(640,root,adm) %_sysconfdir/syslog.conf
%config(noreplace) %_sysconfdir/sysconfig/%syslog_name
%config %_initdir/syslogd
/sbin/syslog*
%doc ANNOUNCE README* NEWS

%_mandir/man?/sys*

%files -n syslog-common -f %name.files
%attr(700,root,root) %dir %_sysconfdir/syslog.d
%config(noreplace) %_sysconfdir/logrotate.d/*
%attr(750,uucp,adm) %dir %_logdir/uucp
/sbin/reload-syslog

%changelog
* Thu Feb 12 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt30
- klogd: Defined more syslog symbols to overcome unsuitable
  glibc syslog implementation.

* Sun Feb 08 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt29
- reload-syslog: Added rsyslogd support (closes #18556).

* Thu Oct 04 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt28
- Do not include linux/linkage.h: no longer necessary for build.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt27
- klogd.sysconfig: Removed "-2" option, added "-x" option.

* Fri Dec 01 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt26
- klogd: Do not use syslog(3) family functions from glibc, see
  http://sourceware.org/bugzilla/show_bug.cgi?id=3604 for details.

* Wed Oct 18 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt25
- klogd: Use syslog(3) family functions from glibc.
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.

* Mon Oct 02 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt24
- Updated to cvs snapshot 20060928.
- SO_BSDCOMPAT is obsolete, do not use it.

* Tue Sep 27 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt23
- syslog-common: Packaged all log files created in %%post script.
- klogd: Removed reopenlog patch introduced in 1.4.1-alt5.

* Wed Aug 24 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt22
- Changed klogd to terminate when read from previously opened
  /proc/kmsg returns EPERM.
- Added missing linefeed in usage messages.

* Wed Aug 17 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt21
- Updated to cvs snapshot 20050525.
- Rediffed patches.

* Mon Aug 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt20
- Updated to 1.4.1 snapshot 20040627.
- Merged upstream patches:
  rh-utmp,
  rh-ksyslog-nul,
  alt-ksym-leak-fix,
  owl-longjmp,
  owl-syslogd-crunch_list.

* Mon Apr 26 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt19
- Cleaned up the crunch_list() function in syslogd fixing the buffer
  overflow discovered by Steve Grubb and a number of other issues (Owl).

* Fri Apr 23 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt18
- syslogd: don't block on tty descriptors (#3968).

* Sat Feb 07 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt17
- Updated to 1.4.1 snapshot 20031022,
  alt-owl-syslogd-killing patch merged upstream.
- klogd: fixed fd leak in FindSymbolFile().
- Redirect std descriptors to /dev/null.

* Fri Aug 01 2003 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt16
- Updated URL.
- Updated documentation from CVS.
- %syslog_name: changed chroot jail from /var/empty
  to /var/resolv (#0002807).
- Updated build dependencies.

* Tue Jul 29 2003 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt15
- Build with explicitly enabled LFS suppport (#0002790).

* Tue May 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt14
- syslog-common: added /etc/syslog.d to explicit provides list.

* Sat Apr 26 2003 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt13
- Eliminated sysklogd-update script.
- Rewritten start/stop scripts to new rc scheme.

* Tue Oct 29 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.1-alt12
- rebuild with gcc3

* Tue Aug 13 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt11
- Fixed %_sysconfdir/syslog.d directory support.

* Fri May 31 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt10
- Shutup logrotate script (#0000891).
- Added "condreload" option to startup scripts.
- Added %ROOT/dev/log socket to klogd subpackage.
- Additional convention enforcement on patch file names.

* Mon Apr 15 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt9
- syslogd: added support for '-A' option and
  directory with symlinks on sockets to listen.
- syslog-common: added %_sysconfdir/syslog.d directory.
- klogd: added %_sysconfdir/syslog.d/klogd symlink
  to %ROOT/dev/log.

* Thu Feb 07 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.1-alt8
- Resurrected one of our patches lost in previous release.
- syslogd is now running chrooted to /var/empty.
- syslogd init script: call restart instead of reload
  in case of syskogd is chrooted.

* Tue Feb 05 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.1-alt7
- Merge with latest Owl patches:
  + Based the new klogd drop root patch on one from CAEN Linux.
  + Added syslogd patches derived from CAEN Linux to allow specifying a
    bind address for the UDP socket and to let syslogd run as non-root.
  + syslogd is now running as its dedicated pseudo-user, too.
+ klogd is now running chrooted to /var/lib/klogd.

* Tue Sep 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.1-alt6
- New package syslog-common. Now logrotate be happy.

* Tue Jul 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.1-alt5
- Corrected permissions on %_sysconfdir/syslog.conf
- Corrected startup scripts to use full pathnames.
- Patched klogd to reopen log socket on each ECONNRESET.

* Mon Jul 23 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.1-alt4
- Splited to separate %syslog_name and klogd packages.
- We will need it for syslog-ng.
- Added %_sysconfdir/sysconfig/* config scripts.

* Thu May 24 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.1-alt3
- Rebuild to use new macros post_service and preun_service

* Thu May 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.1-alt2
- Resurrected symlinks lost in prev release.

* Thu May 10 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.1-alt1
- Up to 1.4.1.
- Added patch from Owl.
- Fixed parent process killing bug.
- Chowned %_logdir/uucp to uucp user.

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-ipl5mdk
- Fixed permissions.

* Wed Jan 24 2001 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl4mdk
- Don't do busy loop when encounter two zero bytes
  (Troels Walsted Hansen <troels@thule.no>).

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl3mdk
- Added PreReq on initscripts.

* Wed Dec 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl2mdk
- Added compatibility links for /var/log/{alert,boot.log,maillog,messages,secure,spooler}.

* Wed Sep 20 2000 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl1mdk
- 1.4

* Thu Sep 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.3.33-ipl2mdk
- Conflicts: vixie-cron < 3.0.1-ipl45mdk.

* Wed Sep 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.3.33-ipl1mdk
- Completly rewritten syslog configuration.

* Fri Aug 25 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.3.33-1mdk
- update to 1.3-33
- Correct logrotate config script to prevent rotating previous files

* Thu Aug 10 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.3.31-15mdk
- add noreplace to make rpmlint happy

* Fri Jul 28 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.3.31-14mdk
- BM + macroszification
- bzipped config files

* Tue May 17 2000 Yoann Vandoorselaere <yoann@mandrakeosft.com> 1.3.31-13mdk
- correct path to killall in syslog.log

* Thu May 04 2000 Yoann Vandoorselaere <yoann@mandrakeosft.com> 1.3.31-12mdk
- create the mail & news log directory.
- update syslog.log

* Tue May 02 2000 Yoann Vandoorselaere <yoann@mandrakeosft.com> 1.3.31-11mdk
- kern.* is now logged to kern.log
- much more logfile now (cron, syslog, kernel, mail.log, mail.warn,
  mail.err, mail.info, auth.log, user.log, lpr.log, daemon.log ).
- do not sync() not important logfile everytime an entry is added.
- syslog.conf.rhs -> syslog.conf.mdk
- mail & news log are in their own directory.
- again a little config change.

* Thu Mar 23 2000 Daouda Lo <daouda@mandrakesoft.com> 1.3.31-8mdk
- fix group for the next release 7.1
* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with rh changes.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- fix handling of RPM_OPT_FLAGS

* Wed Feb 24 1999 Bill Nottingham <notting@redhat.com>
- update to sysklogd-1.3-31
- stop klogd *before* syslogd

* Tue Feb  9 1999 Jeff Johnson <jbj@redhat.com>
- escape naked percent chars in kernel messages (#1088).

* Thu Dec 17 1998 Jeff Johnson <jbj@redhat.com>
- rework last-gasp address-in-module oops trace for both 2.0.x/2.1.x modules.

* Mon Dec  7 1998 Jakub Jelinek <jj@ultra.linux.cz>
- make klogd translate SPARC register dumps and oopses.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- add %clean

* Tue Aug  4 1998 Chris Adams <cadams@ro.com>
- only log to entries that are USER_PROCESS (fix #822)

* Mon Jul 27 1998 Jeff Johnson <jbj@redhat.com>
- remove RPM_BUILD_ROOT from %post

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- patch to support Buildroot
- package is now buildrooted

* Wed Apr 29 1998 Michael K. Johnson <johnsonm@redhat.com>
- Added exit patch so that a normal daemon exit is not flagged as an error.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added (missingok) to init symlinks

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- added status|restart support to syslog.init
- added chkconfig support
- various spec file cleanups

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
