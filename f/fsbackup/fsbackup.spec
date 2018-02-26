Name: fsbackup
Version: 1.2pl2
Release: alt4.1

Summary: file system backup and synchronization utility
License: GPL
Group: Archiving/Backup

Url: http://www.opennet.ru/dev/fsbackup
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name.cron
Source2: sqlite_backup.conf
Source3: create_backup.conf
Source4: mysql_backup.conf
Source5: pgsql_backup.conf
Source6: sysbackup.conf
Source7: sysrestore.conf
Source8: fsrestore.conf
Source9: README.ALT.UTF8

Requires: openssh-clients gnupg mailx schedutils

# Automatically added by buildreq on Thu Dec 06 2007 (-bi)
BuildRequires: fdisk net-tools perl-DBM perl-libnet recode
BuildRequires: perl-podlators

%description
file system backup and synchronization utility

%prep
%setup

%build
# man
pod2man fsbackup.pl > %name.1

# recode to utf8
find . -type f -print0 | xargs -0 recode koi8-r..utf8 --

%install
# scripts
install -pD -m0755 create_backup.sh %buildroot/%_sbindir/create_backup.sh
install -pD -m0755 fsbackup.pl %buildroot/%_sbindir/fsbackup.pl
install -pD -m0755 scripts/fsrestore.sh %buildroot/%_sbindir/fsrestore.sh
install -pD -m0755 scripts/mysql_backup.sh %buildroot/%_sbindir/mysql_backup.sh
install -pD -m0755 scripts/pgsql_backup.sh %buildroot/%_sbindir/pgsql_backup.sh
install -pD -m0755 scripts/sqlite_backup.sh %buildroot/%_sbindir/sqlite_backup.sh
install -pD -m0755 scripts/sysbackup.sh %buildroot/%_sbindir/sysbackup.sh
install -pD -m0755 scripts/sysrestore.sh %buildroot/%_sbindir/sysrestore.sh

# config
install -pD -m0640 cfg_example %buildroot/%_sysconfdir/%name/fsbackup.conf
install -pD -m0640 %SOURCE2 %buildroot/%_sysconfdir/%name/sqlite_backup.conf
install -pD -m0640 %SOURCE3 %buildroot/%_sysconfdir/%name/create_backup.conf
install -pD -m0640 %SOURCE4 %buildroot/%_sysconfdir/%name/mysql_backup.conf
install -pD -m0640 %SOURCE5 %buildroot/%_sysconfdir/%name/pgsql_backup.conf
install -pD -m0640 %SOURCE6 %buildroot/%_sysconfdir/%name/sysbackup.conf
install -pD -m0640 %SOURCE7 %buildroot/%_sysconfdir/%name/sysrestore.conf
install -pD -m0640 %SOURCE8 %buildroot/%_sysconfdir/%name/fsrestore.conf

# dirs
install -d -m0700 %buildroot/%_localstatedir/%name/cache/
install -d -m0700 %buildroot/%_localstatedir/%name/archive/
install -d -m0700 %buildroot/%_localstatedir/%name/sys_backup/

# man
install -pD -m0644 %name.1 %buildroot/%_man1dir/%name.1

# README.ALT
install -pD -m0644 %SOURCE9 README.ALT.UTF8

# cron
install -pD -m0644 %SOURCE1 %buildroot/%_sysconfdir/cron.d/%name

%files
%_sbindir/*
%config(noreplace) %_sysconfdir/cron.d/%name
%config(noreplace) %_sysconfdir/%name/*.conf
%dir %attr(0700,root,root) %_sysconfdir/%name
%dir %attr(0700,root,root) %_localstatedir/%name
%dir %attr(0700,root,root) %_localstatedir/%name/cache
%dir %attr(0700,root,root) %_localstatedir/%name/archive
%dir %attr(0700,root,root) %_localstatedir/%name/sys_backup
%_man1dir/*
%doc CHANGES FAQ README* TODO contrib

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.2pl2-alt4.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 02 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2pl2-alt4
- Fixed regression intoduced in 1.2pl2-alt3

* Thu Jan 31 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2pl2-alt3
- Run backup script with idle ionice prio
- Recode scripts to utf8 too

* Mon Dec 10 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2pl2-alt2
- Add requires not found by buildreq (Closes: #13641)
- Fix ps(1) call (Closes: #13643)

* Thu Dec 06 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2pl2-alt1
- New version

* Thu Sep 06 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2pl1-alt2
- Recode all files to utf8

* Tue Sep 26 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2pl1-alt1
- Initial build for Sisyphus
