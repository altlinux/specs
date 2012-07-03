Name: backupninja
Version: 0.9.9
Release: alt1

Summary: backup system
License: GPL v2
Group: Archiving/Backup

Url: http://dev.riseup.net/backupninja/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://labs.riseup.net/code/attachments/download/229/backupninja-0.9.9.tar.bz2
Source: %name-%version.tar

Requires: %_sysconfdir/cron.d %_sysconfdir/logrotate.d dialog

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir /var

%description
Backupninja lets you drop simple config files in %_sysconfdir/backup.d to coordinate
system backups. Backupninja is a master of many arts, including incremental
remote filesystem backup, mysql backup, and ldap backup. By creating simple
drop-in handler scripts, backupninja can learn new skills. Backupninja is a
silent flower blossom death strike to lost data.

In addition to backing up regular files, Backupninja has handlers to ease
backing up: ldap, maildir, mysql, svn, trac, and the output from shell scripts.

Backupninja currently supports common backup utilities, easing their
configuration, currently supported are: rdiff-backup, duplicity, CD/DVD.

%prep
%setup
%__subst "s|pkglib|pkglibexec|g" lib/Makefile.am

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
mkdir -p %buildroot%_sysconfdir/backup.d/

%files
%doc README TODO AUTHORS
%config(noreplace) %_sysconfdir/%name.conf
%_sysconfdir/cron.d/%name
%_sysconfdir/logrotate.d/%name
%attr(0700,root,root) %dir %_sysconfdir/backup.d/
%_datadir/%name/
%_libexecdir/%name/
%_man1dir/%name.1*
%_man1dir/ninjahelper.1*
%_man5dir/backup.d.5*
%_man5dir/%name.conf.5*
%_sbindir/%name
%_sbindir/ninjahelper

%changelog
* Wed Apr 18 2012 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt1
- new version 0.9.9 (with rpmrb script)
- replace pkglib with pkglibexec

* Tue Sep 28 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.8-alt1
- new version (0.9.8) import in git

* Mon Mar 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2
- drop out default --rsyncable for gzip (see alt bug #8184)

* Thu Feb 18 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version 0.9.7 (with rpmrb script)

* Sun Jan 25 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- new version 0.9.6 (with rpmrb script)

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt2
- replace automake with __autoreconf

* Thu Dec 06 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- new version 0.9.5
- set conf file as config, fix backup.d permissions
- fix missed quotes in rdiff script

* Thu Mar 29 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- new version 0.9.4, change Packager
- add source url, fix _localstatedir

* Mon Oct 02 2006 Alex V. Myltsev <avm@altlinux.ru> 0.9.3-alt1
- New version: bug fixes, more configuration options.

* Wed May 17 2006 Alex V. Myltsev <avm@altlinux.ru> 0.9.2-alt1
- Initial build for Sisyphus.

