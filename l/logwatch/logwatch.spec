# -*- mode: rpm-spec; coding: utf-8 -*-
%define _perl_lib_path %_datadir/%name/lib

Name: logwatch
Version: 7.4.0
Release: alt1

Summary: Analyzes and Reports on system logs
License: MIT
Group: Monitoring
Url: http://www.logwatch.org
BuildArch: noarch
Source: %name-%version.tar
Source1: %name.sysconfig
Source2: %name.cron
Source3: ignore.conf
Source4: override.conf

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildPreReq: perl-base
PreReq: mailx

%description
Logwatch is a customizable, pluggable log-monitoring system.  It will go
through your logs for a given period of time and make a report in the areas
that you wish with the detail that you wish.  Easy to use - works right out
of the package on many systems.

%prep
%setup

%build
%install
install -m 0755 -d %buildroot%_var/cache/%name
install -m 0755 -d %buildroot%_sysconfdir/%name/scripts
install -m 0755 -d %buildroot%_sysconfdir/%name/conf
install -m 0755 -d %buildroot%_sysconfdir/%name/conf/logfiles
install -m 0755 -d %buildroot%_sysconfdir/%name/conf/services
install -m 0755 -d %buildroot%_datadir/%name/default.conf/logfiles
install -m 0755 -d %buildroot%_datadir/%name/default.conf/services
install -m 0755 -d %buildroot%_datadir/%name/default.conf/html
install -m 0755 -d %buildroot%_datadir/%name/dist.conf/logfiles
install -m 0755 -d %buildroot%_datadir/%name/dist.conf/services
install -m 0755 -d %buildroot%_datadir/%name/scripts/services
install -m 0755 -d %buildroot%_datadir/%name/scripts/shared
install -m 0755 -d %buildroot%_datadir/%name/lib

install -m 0755 scripts/%name.pl %buildroot%_datadir/%name/scripts/%name.pl
for i in scripts/logfiles/* ; do
   if [ $(ls $i | wc -l) -ne 0 ] ; then
      install -m 0755 -d %buildroot%_datadir/%name/$i
      install -m 0755 $i/* %buildroot%_datadir/%name/$i
   fi
done
install -m 0755 scripts/services/* %buildroot%_datadir/%name/scripts/services
install -m 0755 scripts/shared/* %buildroot%_datadir/%name/scripts/shared
install -m 0755 lib/* %buildroot%_datadir/%name/lib

install -m 0644 conf/*.conf %buildroot%_datadir/%name/default.conf
install -m 0644 conf/logfiles/* %buildroot%_datadir/%name/default.conf/logfiles
install -m 0644 conf/services/* %buildroot%_datadir/%name/default.conf/services
install -m 0644 conf/html/* %buildroot%_datadir/%name/default.conf/html

install -m 0755 -d %buildroot%_man8dir %buildroot%_man5dir
install -m 0644 ignore.conf.5 %buildroot%_man5dir
install -m 0644 %name.conf.5 %buildroot%_man5dir
install -m 0644 override.conf.5 %buildroot%_man5dir
install -m 0644 %name.8 %buildroot%_man8dir

install -m 0755 -d %buildroot%_sysconfdir/cron.daily %buildroot%_sysconfdir/sysconfig
install -m 644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name
install -m 0755 %SOURCE2 %buildroot%_sysconfdir/cron.daily/0%name

install -m 0755 -d %buildroot%_sbindir
ln -s %_datadir/%name/scripts/%name.pl %buildroot%_sbindir/%name

echo "# Local configuration options go here (defaults are in %_datadir/%name/default.conf/%name.conf)" > %buildroot%_sysconfdir/%name/conf/%name.conf
install -m 644 %SOURCE3 %buildroot%_sysconfdir/%name/conf/ignore.conf
install -m 644 %SOURCE4 %buildroot%_sysconfdir/%name/conf/override.conf

%files
%_sysconfdir/cron.daily/0%name

%dir %_var/cache/%name
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/scripts
%dir %_sysconfdir/%name/conf
%dir %_sysconfdir/%name/conf/logfiles
%dir %_sysconfdir/%name/conf/services
%dir %_datadir/%name
%dir %_datadir/%name/default.conf
%dir %_datadir/%name/default.conf/services
%dir %_datadir/%name/default.conf/logfiles
%dir %_datadir/%name/default.conf/html
%dir %_datadir/%name/dist.conf
%dir %_datadir/%name/dist.conf/services
%dir %_datadir/%name/dist.conf/logfiles
%dir %_datadir/%name/scripts
%dir %_datadir/%name/scripts/logfiles
%dir %_datadir/%name/scripts/services
%dir %_datadir/%name/scripts/shared
%dir %_datadir/%name/scripts/logfiles/*
%dir %_datadir/%name/lib
%_datadir/%name/scripts/%name.pl
%_sbindir/%name
%_datadir/%name/scripts/shared/*
%_datadir/%name/scripts/services/*
%_datadir/%name/scripts/logfiles/*/*
%_datadir/%name/lib/Logwatch.pm
%_datadir/%name/default.conf/*.conf
%_datadir/%name/default.conf/services/*.conf
%_datadir/%name/default.conf/logfiles/*.conf
%_datadir/%name/default.conf/html/*.html
%doc %_man5dir/*.5*
%doc %_man8dir/%name.8*
%config(noreplace) %_sysconfdir/%name/conf/*.conf
%config(noreplace) %_sysconfdir/sysconfig/%name

%doc README HOWTO* LICENSE

%changelog
* Tue Apr 26 2011 Terechkov Evgenii <evg@altlinux.org> 7.4.0-alt1
- 7.4.0

* Tue Jan  1 2008 Terechkov Evgenii <evg@altlinux.ru> 7.3.6-alt1.1
- Rebuild with new rpm-build-perl
- pam_tcb added to ignore.conf (commented out by default - half-fix for #11915)
- PreReq to mailx added (fixes #8832)

* Sat Sep 29 2007 Terechkov Evgenii <evg@altlinux.ru> 7.3.6-alt1
- 7.3.6
- Some additions to override.conf (apache1,2)
- Packager tag added to spec
- Russian translations removed from spec (Specspo)

* Sat Feb  3 2007 Terechkov Evgenii <evg@altlinux.ru> 7.3.1-alt3
- vsftpd added to override.conf
- typos in override.conf fixed

* Sun Jan 28 2007 Terechkov Evgenii <evg@altlinux.ru> 7.3.1-alt2
- Samba added to override.conf
- Spec converted to utf-8

* Sat Sep 16 2006 Terechkov Evgenii <evg@altlinux.ru> 7.3.1-alt1
- 7.3.1
- AutoReq: noperl  added

* Wed Feb  8 2006 Terechkov Evgenii <evg@altlinux.ru> 7.2.1-alt2
- 7.2.1
- Migration to /etc/logwatch config dir

* Fri Sep 16 2005 Ilya Evseev <evseev@altlinux.ru> 6.1.2-alt1
- initial build for ALTLinux

* Thu Feb 24 2005 Kirk Bauer <kirk@kaybee.org> 6.0.1-1
- Now includes ignore.conf in the RPM

* Mon Nov 03 2003 Kirk Bauer <kirk@kaybee.org> pre5.0-1
- Now can build without change as non-root user

* Thu Feb 27 2003 Erik Ogan <erik@ogan.net> 4.3.2
- Added libdir & lib/Logwatch.pm

* Sun Oct 13 2002 Kirk Bauer <kirk@kaybee.org> pre4.0-14
- Changed the 'logwatch' cron.daily job to '0logwatch' to run before logrotate

* Thu Oct 10 2002 Kirk Bauer <kirk@kaybee.org> pre4.0-1
- Cronjob is now just named logwatch and not 00-logwatch

* Wed May 01 2002 Kirk Bauer <kirk@kaybee.org> 3.0-6
- up2date packaged... finally!

* Wed May 01 2002 Kirk Bauer <kirk@kaybee.org> 3.0-5
- Hopefully now properly included the up2date filter!

* Mon Apr 29 2002 Kirk Bauer <kirk@kaybee.org> pre3.0-1
- Now properly includes logfile-specific scripts

* Tue Apr 09 2002 Kirk Bauer <kirk@kaybee.org> 2.8-2
- Made man page entry in files list backwards compatible

* Thu Mar 28 2002 Kirk Bauer <kirk@kaybee.org> 2.5-2
- Updated new changes from Red Hat's rawhide packaging

* Wed Nov 18 1998 Kirk Bauer <kirk@kaybee.org>
- Modified to comply with RHCN standards

* Sun Feb 23 1998 Kirk Bauer <kirk@kaybee.org>
- Minor changes and addition of man-page

* Sun Feb 22 1998 Kirk Bauer <kirk@kaybee.org>
- initial release

## EOF ##
