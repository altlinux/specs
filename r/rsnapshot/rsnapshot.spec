Name:    rsnapshot
Version: 1.4.5
Release: alt1

Summary: local and remote filesystem snapshot utility

License: %gpl2plus
Group:   Archiving/Backup
URL:     http://rsnapshot.org/
BuildArch: noarch

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.logrotate
Source2: %name.cron

Patch0:  %name-%version-%release.patch
Patch1:  %name-1.4.5-alt-conf_file.patch

BuildRequires(pre): rpm-build-licenses

Requires: %_bindir/rsync, %_bindir/ssh, %_bindir/logger
Requires: perl(Lchown.pm)

# Automatically added by buildreq on Sun Nov 28 2010
BuildRequires: openssh-clients perl-Pod-Parser rsync

%description
rsnapshot is an rsync-based filesystem snapshot utility. It can take
incremental backups of local and remote filesystems for any number of
machines. rsnapshot makes extensive use of hard links, so disk space
required is just a little more than the space of one full backup,
plus incrementals.

Depending on your configuration, it is quite possible to set up in
just a few minutes. Files can be restored by the users who own them,
without the root user getting involved.

%prep
%setup
%patch0 -p1

%patch1

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
./autogen.sh
%configure \
	--with-perl="%__perl" \
	--with-rsync="%_bindir/rsync" \
	--with-ssh="%_bindir/ssh" \
	--with-logger="%_bindir/logger" \
	--with-cp=/bin/cp \
	--with-rm=/bin/rm \
	--with-du=/bin/du \
	--sysconfdir=%_sysconfdir/%name \
	%nil

%make_build

# Tune different pathes in scripts, etc. 
sed -e 's#/etc/%{name}#/etc/%name/%{name}#g' -i utils/rsnapshotdb/{INSTALL.txt,rsnapshotDB.pl}
sed -e 's#%_logdir/#%_logdir/%{name}/#g' -i  utils/random_file_verify.sh utils/rsnapshotdb/rsnapshotDB.pl
sed -e 's#/usr/local/pgsql/bin/pg_dumpall#%_bindir/pg_dumpall#g' -i utils/backup_pgsql.sh
sed -e 's#/usr/local/samba/bin/smbclient#%_bindir/smbclient#g' -i utils/backup_smb_share.sh
sed -e 's#/usr/local/bin/#%_bindir/#g' -i utils/rsnapshot_if_mounted.sh

sed -e 's@#!/usr/bin/env perl@#!%__perl@' -i utils/rsnapreport.pl

sed -e 's#B<%_sysconfdir/%name.conf#B<%_sysconfdir/%name/%name.conf#g' -i rsnapshot
sed -e 's#/%_logdir/%{name}#%_logdir/%name/%name.log#' -i rsnapshot rsnapshot.1

sed -e 's#/path/to/mount#/bin/mount#'        \
    -e 's#/path/to/umount#/bin/umount#'      \
    -e 's#/path/to/lvcreate#/sbin/lvcreate#' \
    -e 's#/path/to/lvremove#/sbin/lvremove#' \
    -i rsnapshot.conf.default

%install
install -d -- %buildroot%_bindir
install -m 755 -- rsnapshot %buildroot%_bindir/rsnapshot
install -m 755 -- rsnapshot-diff %buildroot%_bindir/rsnapshot-diff
install -m 755 -- utils/rsnapreport.pl %buildroot%_bindir/rsnapreport.pl

install -d -- %buildroot%_man1dir
install -m 644 -- rsnapshot*.1* %buildroot%_man1dir

install -d -- %buildroot%_sysconfdir/%name
install -m 644 -- rsnapshot.conf.default %buildroot%_sysconfdir/%name/rsnapshot.conf.default
install -m 600 -- rsnapshot.conf.default %buildroot%_sysconfdir/%name/rsnapshot.conf

# Removing executable bit from sample scripts
find utils/ -type f -print0 | xargs -0 chmod -R a-X

# Installing logrotate and cron files
install -d -- %buildroot%_sysconfdir/{logrotate.d,cron.d}
install -m 644 -- %SOURCE1 %buildroot%_sysconfdir/logrotate.d/%name
install -m 644 -- %SOURCE2 %buildroot%_sysconfdir/cron.d/%name

install -d -- %buildroot%_logdir/%name

%pre
%_sbindir/groupadd -r -f _%name &>/dev/null ||:

%post
#
# upgrade rsnapshot config file
#
RSNAPSHOT_CONFIG_VERSION=`%_bindir/rsnapshot check-config-version`
if test $? != 0; then
	echo "Can't check config file (%_sysconfdir/%name/rsnapshot.conf) version!"
else 
	if test "$RSNAPSHOT_CONFIG_VERSION" = "1.2"; then
		# already latest version
		exit 0
	fi

	if test "$RSNAPSHOT_CONFIG_VERSION" != "unknown"; then
		%_bindir/rsnapshot upgrade-config-file
		if test $? != 0; then
			echo "Error upgrading %_sysconfdir/%name/rsnapshot.conf!"
			echo "You need to uprade it manually!"
		fi
	else
		echo "Error upgrading %_sysconfdir/%name/rsnapshot.conf. Config format unknown!"
	fi
fi
exit 0

%files
%doc AUTHORS ChangeLog README.md INSTALL.md
%doc --no-dereference COPYING
%doc docs/Upgrading_from_1.1 docs/HOWTOs/rsnapshot-HOWTO.en.html
%doc utils

%dir %attr(0770,root,_%name) %_sysconfdir/%name
%config %_sysconfdir/%name/rsnapshot.conf.default
%config(noreplace) %verify(user group mode) %_sysconfdir/%name/rsnapshot.conf

%config %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/cron.d/%name

%dir %attr(1770,root,_%name) %_logdir/%name

%_bindir/rsnapshot
%_bindir/rsnapshot-diff
%_bindir/rsnapreport.pl
%_man1dir/rsnapshot*

%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.4.5-alt1
- New version
  * documentation updates and fixes

* Sun Jun 27 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.4.4-alt1
- New version

* Wed Jun 10 2020 Nikolay A. Fetisov <naf@altlinux.org> 1.4.3-alt1
- New version

* Sun Jun 12 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.2-alt1
- New version

* Sat Nov 7 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.1-alt1
- New version

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.3.1-alt3
- fix POD syntax

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.3.1-alt2
- fix build with Perl 5.12

* Sat Jul 18 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.3.1-alt1
- Initial build for ALT Linux Sisyphus
