Name: anacron
Version: 2.3
Release: alt3
Epoch: 1

Summary: A cron-like program that doesn't go by time
License: GPLv2+
Group: System/Servers
Url: http://anacron.sourceforge.net/

# http://download.sourceforge.net/anacron/anacron-%version.orig.tar.bz2
Source: anacron-%version.orig.tar
Source1: anacrontab
Source2: anacron.init
Source3: run-anacronjobs
Source4: anacronjobs.sysconfig

Patch1: anacron-2.3-re.patch
Patch2: anacron-2.3-alt-lock-file.patch

%define lockfile %_lockdir/subsys/anacron

%description
Anacron (like `anac(h)ronistic') is a periodic command scheduler.  It
executes commands at intervals specified in days.  Unlike cron, it
does not assume that the system is running continuously.  It can
therefore be used to control the execution of daily, weekly and
monthly jobs (or anything with a period of n days), on systems that
don't run 24 hours a day.  When installed and configured properly,
Anacron will make sure that the commands are run at the specified
intervals as closely as machine-uptime permits.

This package is pre-configured to execute the daily jobs of the OS.
You should install this program if your system isn't powered on
24 hours a day to make sure the maintenance jobs of other packages
are executed each day.

%prep
%setup
%patch1 -p1
%patch2 -p1
rm gregor.*

%build
%add_optflags -D_GNU_SOURCE -DLOCKFILE=\\\"%lockfile\\\"
%make_build

%install
install -pD -m755 anacron %buildroot%_sbindir/anacron
install -pD -m644 anacron.8 %buildroot%_mandir/man8/anacron.8
install -pD -m644 anacrontab.5 %buildroot%_mandir/man5/anacrontab.5
install -pD -m644 %_sourcedir/anacrontab %buildroot%_sysconfdir/anacrontab
install -pD -m755 %SOURCE2 %buildroot%_initdir/anacron
install -pD -m755 %SOURCE3 %buildroot%_bindir/run-anacronjobs
install -pD -m644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/anacronjobs
mkdir -p %buildroot/var/{run,spool}/anacron

for f in cron.{dai,week,month}ly; do
	mkdir -p "%buildroot%_sysconfdir/$f"
cat << EOF >"%buildroot%_sysconfdir/$f/000%name"
#!/bin/sh
#
# %name's cron script
#
# This script updates %name time stamps. It is called through run-parts
# either by %name itself or by cron.
#
# The script is called "000%name" to assure that it will be executed
# _before_ all other scripts.

exec %_sbindir/anacron -u $f
EOF
chmod 750 "%buildroot%_sysconfdir/$f/000%name"
done

sed -i s,RPM_LOCKFILE,%lockfile, %buildroot%_initdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/run-anacronjobs
%_sbindir/anacron
%config(noreplace) %_initdir/anacron
%config(noreplace) %attr(640,root,adm) %_sysconfdir/anacrontab
%config(noreplace) %attr(640,root,adm) %_sysconfdir/sysconfig/anacronjobs
%config(noreplace) %_sysconfdir/cron.*/*
%_mandir/man?/*
%attr(700,root,root) /var/*/anacron
%doc ChangeLog README TODO

%changelog
* Thu Jun 07 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.3-alt3
- Create /var/run/anacron before creating tmp files there (closes: #27371).

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.3-alt2
- Added anacron jobs filter (Alexey Gladkov).

* Wed Apr 23 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.3-alt1
- Updated release numbering.

* Fri Nov 14 2003 Stanislav Ievlev <inger@altlinux.org> 2.3-ipl9mdk
- anacron now delete lockfile itself at success exit

* Thu Dec 19 2002 Stanislav Ievlev <inger@altlinux.ru> 2.3-ipl8mdk
- #0001651

* Mon Sep 23 2002 Stanislav Ievlev <inger@altlinux.ru> 2.3-ipl7mdk
- rebuild with gcc3
- fixed URL.

* Thu May 24 2001 Stanislav Ievlev <inger@altlinux.ru> 2.3-ipl6mdk
- Rebuild for use new macros post_service and preun_service

* Thu Feb 22 2001 Dmitry V. Levin <ldv@fandra.org> 2.3-ipl5mdk
- Use __progname.
- Rewritten timestamp analysis logic (now use seconds precision).

* Sat Jan 13 2001 Dmitry V. Levin <ldv@fandra.org> 2.3-ipl4mdk
- Create tmpfiles in more secure way.

* Wed Sep 20 2000 Dmitry V. Levin <ldv@fandra.org> 2.3-ipl3mdk
- RE adaptions.

* Tue Sep 12 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 2.3-3mdk
- added use of subsys in initscript

* Thu Sep  7 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 2.3-2mdk
- changed source (taken from debian instead of sourceforge)
- added Prereq
- changed init script (took redhat one)
- changed preun and added postun to stop and restart service properly
- added config(noreplace) on default tasks and init script

* Thu Aug 24 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 2.3-1mdk
- new version
- chkconfig in post install and preuninstall
- slight improvements (noreplace, url)
- improved init.d script

* Fri Jul 21 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.1-6mdk
- BM
- macroqwekrvhuqwjrncasdfkl;kl;vbwerkl;vbzations

* Mon Jul 10 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.1-5mdk
- use spec-helper & new macros
- add a %%install section (...) : now spec-helper will work on
  anacron rpm.

* Fri Apr 14 2000 David BAUDENS <baudens@mandrakesoft.com> 2.1-4mdk
- Fix Description and Summary
- Use %%_tmppath for BuildRoot

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 2.1-3mdk
- fix group

* Wed Dec 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove cron.hourly check (unusefull).

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.1 from debian.
- Fix typo in initscripts.

* Thu Jul 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix wrong entries in anacrontab.
- Add a /etc/rc.d/rc.sysinit/ script

* Tue Apr 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix bug with /var/spool/anacron/

* Sat Apr 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- First version mainly inspired from the Debian package.
