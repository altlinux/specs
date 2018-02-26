Name: crontabs
Version: 1.8
Release: alt1

Summary: Root crontab files used to schedule the execution of programs
License: public domain
Group: System/Configuration/Other
BuildArch: noarch
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: crontab

%define cron_dirs %_sysconfdir/cron.{hour,dai,week,month}ly
Provides: %(echo %cron_dirs)
PreReq: service >= 0.0.3-alt1
Requires: vixie-cron

%description
The %name package contains root crontab files.  Crontab is the
program used to install, uninstall or list the tables used to drive the
cron daemon.  The cron daemon checks the crontab files to see when
particular commands are scheduled to be executed.  If commands are
scheduled, it executes them.

Crontabs handles a basic system function, so it should be installed on
your system.

%install
%__mkdir_p $RPM_BUILD_ROOT{%_bindir,%cron_dirs}

%__install -p -m600 %SOURCE0 $RPM_BUILD_ROOT%_sysconfdir/

%files
%config(noreplace) %_sysconfdir/crontab
%attr(750,root,root) %dir %_sysconfdir/cron.*ly

%changelog
* Thu Apr 24 2003 Dmitry V. Levin <ldv@altlinux.org> 1.8-alt1
- run-parts: moved to service package.
- crontab: do not redefine cron(8) defaults.

* Fri Mar 07 2003 Dmitry V. Levin <ldv@altlinux.org> 1.7-ipl13mdk
- Requires: vixie-cron.

* Mon Nov 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.7-ipl12mdk
- rebuild

* Tue Apr 02 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.7-ipl11mdk
- Added missing provides.

* Thu Sep 21 2000 Dmitry V. Levin <ldv@fandra.org> 1.7-ipl10mdk
- RE adaptions.

* Tue Sep 19 2000 Francis Galiegue <fg@mandrakesoft.com> 1.7-10mdk
- /etc/crontab is %%config(noreplace)

* Fri Jul 28 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.7-9mdk
- macroszifications

* Mon Apr  3 2000 Adam Lebsack <adam@mandrakesoft.com> 1.7-8mdk
- Release build.

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Release build.

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- don't run .rpm{save,new,orig} files (bug #2190)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Mon Nov 30 1998 Bill Nottingham <notting@redhat.com>
- crontab: set HOME=/

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- run-parts: skip sub-directories (e.g. CVS) found instead of complaining

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Erik Troan <ewt@redhat.com>
- moved crontab jobs up a bit to make sure they aren't confused by
  switching to and fro daylight savings time

* Fri Oct 24 1997 Erik Troan <ewt@redhat.com>
- removed tmpwatch and at entries

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
