%set_verify_elf_method relaxed

%def_enable bat
%def_disable bwx
%def_enable tray
%def_disable readline
%def_disable debug

Name: bacula
Version: 5.2.10
Release: alt1

License: AGPLv3
Summary: Network based backup program
Group: Archiving/Backup
Url: http://www.bacula.org/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Source: bacula-%version.tar
Source1: bacula-dir.init
Source2: bacula-fd.init
Source3: bacula-sd.init
Source4: bacula-fd.sysconfig
Source5: bacula-fd.limit
Source8: bacula-configs-default-%version.tar
Source9: bacula-icons-%version.tar
Source10: bacula.sysconfig

BuildRequires: dvd+rw-tools gcc-c++ groff-base libMySQL-devel libssl-devel libncurses-devel libsqlite3-devel libssl libacl-devel libcap-devel python-devel zlib-devel iputils bc postgresql-devel

%filter_from_requires /libbaccats-%version\.so/d

%if_enabled bwx
# console-wx buildrequires
BuildRequires: imake libICE-devel libX11-devel wxGTK-devel xorg-cf-files
%endif

%if_enabled bat
# bat buildrequires
BuildRequires: imake libICE-devel libX11-devel libqwt-devel xorg-cf-files
%endif

%if_enabled tray
# tray buildrequires
BuildRequires: libgnomeui-devel
%endif

Provides: bacula-updatedb = %version-%release
Obsoletes: bacula-updatedb < %version-%release
Requires: bacula-common = %version-%release
Requires: bacula-client = %version-%release
Requires: bacula-storage = %version-%release
Requires: bacula-console = %version-%release
Requires: bacula-dir = %version-%release

%package client
Summary: Network based backup program (client only)
Group: Archiving/Backup
Provides: bacula-fd = %version-%release
Requires: bacula-common = %version-%release

%package storage
Summary: Network based backup program (storage only)
Group: Archiving/Backup
Requires: bacula-common = %version-%release

%package console
Summary: Network based backup program (console only)
Group: Archiving/Backup
Requires: bacula-common = %version-%release

%if_enabled bwx
%package console-wx
Summary: Network based backup program (wxWidgets console only)
Group: Archiving/Backup
%endif

%if_enabled tray
%package tray-monitor
Summary: Network based backup program (tray monitor only)
Group: Archiving/Backup
%endif

%if_enabled bat
%package bat
Summary: Network based backup program (QT4 Bacula Administration Tool)
Group: Archiving/Backup
BuildRequires(pre): libqt4-devel
Requires: libqt4-core >= %{get_version libqt4-core}
%endif

%package director-common
Summary: Network based backup program (director common)
Group: Archiving/Backup
Requires: bacula-common = %version-%release

%package director-mysql
Summary: Network based backup program (MySQL director only)
Group: Archiving/Backup
Requires(pre): bacula-director-common = %version-%release
Provides: bacula-director = %version-%release
Obsoletes: bacula-director < %version-%release
Provides: bacula-dir = %version-%release

%package director-sqlite3
Summary: Network based backup program (SQLITE3 director only)
Group: Archiving/Backup
Requires(pre): sqlite3
Requires(pre): bacula-director-common = %version-%release
Provides: bacula-dir = %version-%release

%package director-postgresql
Summary: Network based backup program (PostgreSQL director only)
Group: Archiving/Backup
Requires(pre): bacula-director-common = %version-%release
Provides: bacula-dir = %version-%release

%package common
Summary: Network based backup program (common files)
Group: Archiving/Backup
Requires(pre): passwdqc-utils

%package debug
Summary: Network based backup program (debug files)
Group: Archiving/Backup
Requires: bacula-common = %version-%release
BuildArch: noarch

%package nagios
Summary: The check_bacula plugin for nagios
Group: Archiving/Backup

%description
Bacula is a set of computer programs that permits the system
administrator to manage backup, recovery, and verification of computer
data across a network of computers of different kinds.
Bacula can also run entirely upon a single computer and can backup to
various types of media, including tape and disk. In technical terms, it
is a network Client/Server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage
management features that make it easy to find and recover lost or
damaged files. Due to its modular design, Bacula is scalable from small
single computer systems to systems consisting of hundreds of computers
located over a large network.

%description client
Bacula File services (or Client program) is the software program that is
installed on the machine to be backed up. It is specific to the
operating system on which it runs and is responsible for providing the
file attributes and data when requested by the Director. The File
services are also responsible for the file system dependent part of
restoring the file attributes and data during a recovery operation.
This program runs as a daemon on the machine to be backed up, and in
some of the documentation, the File daemon is referred to as the Client
(for example in Bacula configuration file)

%description storage
Bacula Storage services consist of the software programs that perform
the storage and recovery of the file attributes and data to the physical
backup media or volumes. In other words, the Storage daemon is
responsible for reading and writing your tapes (or other storage media,
e.g. files).
The Storage services runs as a daemon on the machine that has the backup
device (usually a tape drive).

%description director-common
Director common package for bacula.

%description director-mysql
Bacula Director is the program that supervises all the backup, restore,
verify and archive operations. The system administrator uses the Bacula
Director to schedule backups and to recover files.
Catalog services are comprised of the software programs responsible for
maintaining the file indexes and volume databases for all files backed up.
The Catalog services permit the System Administrator or user to quickly
locate and restore any desired file, since it maintains a record of all
Volumes used, all Jobs run, and all Files saved.
This package contains Director built for MySQL backend.

%description director-sqlite3
Bacula Director is the program that supervises all the backup, restore,
verify and archive operations. The system administrator uses the Bacula
Director to schedule backups and to recover files.
Catalog services are comprised of the software programs responsible for
maintaining the file indexes and volume databases for all files backed up.
The Catalog services permit the System Administrator or user to quickly
locate and restore any desired file, since it maintains a record of all
Volumes used, all Jobs run, and all Files saved.
This package contains Director built for SQLite3 backend.

%description director-postgresql
Bacula Director is the program that supervises all the backup, restore,
verify and archive operations. The system administrator uses the Bacula
Director to schedule backups and to recover files.
Catalog services are comprised of the software programs responsible for
maintaining the file indexes and volume databases for all files backed up.
The Catalog services permit the System Administrator or user to quickly
locate and restore any desired file, since it maintains a record of all
Volumes used, all Jobs run, and all Files saved.
This package contains Director built for PostgreSQL backend.

%description console
Bacula Console is the program that allows the administrator or user to
communicate with the Bacula Director.
This package contains text based management console.

%if_enabled bwx
%description console-wx
Bacula Console is the program that allows the administrator or user to
communicate with the Bacula Director.
This package contains WXWindows based management console.
%endif

%if_enabled tray
%description tray-monitor
Tray monitor package for bacula.
%endif

%if_enabled bat
%description bat
Bacula Administration Tool package.
%endif

%description common
Common files for bacula parts.

%description debug
Debug files for bacula.

%description nagios
The check_bacula plugin for nagios.

%prep
%setup -b 0
%setup -b 8
%setup -b 9

mv ../%name-icons-%version icons

sed -i 's|qmake|qmake-qt4|g' autoconf/configure.in
sed -i 's|-lreadline -lhistory -ltermcap|-lreadline -lhistory|g' autoconf/configure.in


%build
export MTX=%_sbindir/mtx
autoheader -B autoconf autoconf/configure.in >autoconf/config.h.in
autoconf -B autoconf autoconf/configure.in >configure

%configure \
	--with-openssl \
	--with-python \
	--mandir=%_mandir \
	--with-working-dir=%_localstatedir/bacula \
	--with-scriptdir=%_datadir/%name/scripts \
	--with-pid-dir=%_var/run/bacula \
	--sysconfdir=%_sysconfdir/%name \
	--enable-batch-insert \
%if_enabled readline
	--with-readline \
	--disable-conio \
%endif
	--with-dir-user=bacula \
	--with-dir-group=bacula \
	--with-sd-user=bacula \
	--with-sd-group=bacula \
	--with-postgresql \
	--with-sqlite3 \
	--enable-tray-monitor \
	--enable-bat=yes \
	--enable-bwx-console \
	--with-mysql \
	#
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

# make the nagios plugin
pushd examples/nagios/check_bacula
%make LIBS="-lpthread -ldl -lssl -lcrypto"
popd

%install

%make_install DESTDIR="%buildroot" install

mkdir -p %buildroot%_initdir
install -pm 755 %SOURCE1 %buildroot%_initdir/bacula-dir
install -pm 755 %SOURCE2 %buildroot%_initdir/bacula-fd
install -pm 755 %SOURCE3 %buildroot%_initdir/bacula-sd

install -pD -m644 %_sourcedir/bacula.sysconfig \
	%buildroot%_sysconfdir/sysconfig/bacula
install -pD -m644 %_sourcedir/bacula-fd.sysconfig \
	%buildroot%_sysconfdir/sysconfig/bacula-fd

install -pD -m644 scripts/logrotate %buildroot%_sysconfdir/logrotate.d/%name

install -pD -m644 %_sourcedir/bacula-fd.limit \
	%buildroot%_sysconfdir/sysconfig/limits.d/bacula-fd

mkdir -p %buildroot/var/run/%name

mkdir -p %buildroot%_datadir/{applications,sample-configs}
mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_niconsdir
mkdir -p %buildroot%_datadir/%name/sample-configs
mkdir -p %buildroot%_sysconfdir/{security/console.apps,pam.d}
install -d -m755 %buildroot%_bindir
mv %buildroot%_sbindir/bconsole %buildroot%_bindir/
chmod 755 %buildroot%_bindir/bconsole
mv %buildroot%_sysconfdir/%name/bconsole.conf %buildroot%_datadir/%name/sample-configs/

%if_enabled bwx
install -pD -m644 icons/wxwin16x16.xpm %buildroot%_miconsdir/bacula-wxwin.xpm
install -pD -m644 icons/wxwin32x32.xpm %buildroot%_niconsdir/bacula-wxwin.xpm
install -pD -m644 icons/wxwin48x48.xpm %buildroot%_liconsdir/bacula-wxwin.xpm
install -pD -m644 scripts/wxconsole.desktop.consolehelper %buildroot%_desktopdir/wxconsole.desktop
install -pD -m640 scripts/wxconsole.console_apps %buildroot%_sysconfdir/security/console.apps/bwx-console
mv %buildroot%_sbindir/bwx-console %buildroot%_bindir
chmod 755 %buildroot%_bindir/bwx-console
mv %buildroot%_sysconfdir/%name/bwx-console.conf %buildroot%_datadir/%name/sample-configs/
%endif

%if_enabled tray
install -pD -m644 scripts/bacula-tray-monitor.desktop %buildroot%_desktopdir/bacula-tray-monitor.desktop
install -pD -m644 icons/bacula-tray-monitor16x16.xpm %buildroot%_miconsdir/bacula-tray-monitor.xpm
install -pD -m644 icons/bacula-tray-monitor32x32.xpm %buildroot%_niconsdir/bacula-tray-monitor.xpm
install -pD -m644 icons/bacula-tray-monitor48x48.xpm %buildroot%_liconsdir/bacula-tray-monitor.xpm
mv %buildroot%_sbindir/bacula-tray-monitor %buildroot%_bindir
chmod 755 %buildroot%_bindir/bacula-tray-monitor
mv %buildroot%_sysconfdir/%name/tray-monitor.conf %buildroot%_datadir/%name/sample-configs/

%endif

%if_enabled bat
mv %buildroot%_sbindir/bat %buildroot%_bindir/bat
install -pD -m644 icons/bat16x16.png %buildroot%_miconsdir/bat.png
install -pD -m644 icons/bat32x32.png %buildroot%_niconsdir/bat.png
install -pD -m644 icons/bat48x48.png %buildroot%_liconsdir/bat.png
install -pD -m644 scripts/bat.desktop %buildroot%_desktopdir/bat.desktop
mv %buildroot%_sysconfdir/%name/bat.conf %buildroot%_datadir/%name/sample-configs/
install -d %buildroot%_defaultdocdir/%name/html
cp -a src/qt-console/help/*.html %buildroot%_defaultdocdir/%name/html/
%endif

cp -ar ../%name-configs-default-%version/* %buildroot%_sysconfdir/%name/

install -pD -m755 %buildroot%_datadir/%name/scripts/mtx-changer %buildroot%_sbindir
install -pD -m644 %buildroot%_datadir/%name/scripts/mtx-changer.conf %buildroot%_sysconfdir/bacula/
sed -i "s|%_datadir/%name/scripts|%_sysconfdir/bacula|g" %buildroot%_sbindir/mtx-changer
install -pD -m755 %buildroot%_datadir/%name/scripts/disk-changer %buildroot%_sbindir
install -pD -m755 %buildroot%_datadir/%name/scripts/dvd-handler %buildroot%_sbindir
chmod 755 %buildroot%_sbindir/*

# install the nagios plugin
install -d %buildroot%_sysconfdir/nagios/commands
install -d %buildroot%_libdir/nagios/plugins

install -m0755 examples/nagios/check_bacula/check_bacula %buildroot%_libdir/nagios/plugins/

cat > %buildroot%_sysconfdir/nagios/commands/check_bacula.cfg << EOF
# 'check_bacula' command definition
define command{
    command_name    check_bacula
    command_line    %_libdir/nagios/plugins/check_bacula -H \$HOSTADDRESS$ -D \$ARG1\$ -M \$ARG2\$ -K \$ARG3\$ -P \$ARG4\$
}
EOF

mkdir -p %buildroot/%_altdir
echo "%_libdir/libbaccats-%version.so %_libdir/libbaccats-postgresql-%version.so      5" > %buildroot/%_altdir/bacula-dir.pgsql
echo "%_libdir/libbaccats-%version.so %_libdir/libbaccats-sqlite3-%version.so        10" > %buildroot/%_altdir/bacula-dir.sqlite3
echo "%_libdir/libbaccats-%version.so %_libdir/libbaccats-mysql-%version.so          20" > %buildroot/%_altdir/bacula-dir.mysql

mkdir -p %buildroot/%_logdir/bacula/
sed -i "s|/var/lib/bacula/log|/var/log/bacula/log|g" %buildroot/%_sysconfdir/logrotate.d/%name

%pre common
%_sbindir/groupadd -r -f bacula
%_sbindir/useradd -r -n -g bacula -d /var/empty -s /bin/false -c "Bacula pseudo user" bacula >/dev/null 2>&1 ||:
%_sbindir/usermod -d /var/empty -s /bin/false bacula >/dev/null 2>&1

%post common
for i in %_sysconfdir/bacula/bacula-*-password.conf; do
 [ ! -s "$i" ] || continue
 printf 'Password = "%%s"\n' "$(pwqgen|sed -e 's/[\"$\`\\]/\\&/g')" > "$i";
done

%pre client
if [ -f /var/run/bacula/bacula-fd.9102.pid ]; then
  mv /var/run/bacula/bacula-fd.9102.pid /var/run/bacula/bacula-fd.pid
fi

%post client
%post_service bacula-fd

%pre storage
%_sbindir/groupadd -r -f tape
gpasswd -a bacula tape >/dev/null 2>&1
if [ -f /var/run/bacula/bacula-sd.9103.pid ]; then
  mv /var/run/bacula/bacula-sd.9103.pid /var/run/bacula/bacula-sd.pid
fi

%post storage
%post_service bacula-sd

%post director-sqlite3
%force_update_alternatives
%post_service bacula-dir
if [ ! -s %_localstatedir/bacula/bacula.db ]; then
    %_datadir/bacula/scripts/make_sqlite3_tables
    chown bacula.bacula %_localstatedir/bacula/bacula.db
fi

%post director-mysql
%force_update_alternatives
%post_service bacula-dir

%post director-postgresql
%force_update_alternatives
%post_service bacula-dir

%pre director-sqlite3
 if [ -f /var/run/bacula/bacula-dir.9101.pid ]; then
  mv /var/run/bacula/bacula-dir.9101.pid /var/run/bacula/bacula-dir.pid
 fi
%pre director-mysql
 if [ -f /var/run/bacula/bacula-dir.9101.pid ]; then
  mv /var/run/bacula/bacula-dir.9101.pid /var/run/bacula/bacula-dir.pid
 fi
%pre director-postgresql
 if [ -f /var/run/bacula/bacula-dir.9101.pid ]; then
  mv /var/run/bacula/bacula-dir.9101.pid /var/run/bacula/bacula-dir.pid
 fi

%triggerun director-common -- bacula-director-common < 3.0.1-alt4
if [ $1 -eq 2 ]; then
  mv /var/lib/bacula/log* /var/log/bacula/
  sed -i "s|/var/lib/bacula/log|/var/log/bacula/log|g" /etc/bacula/messages/*.conf
  sed -i "s|/var/lib/bacula//log|/var/log/bacula/log|g" /etc/bacula/messages/*.conf
fi

%triggerpostun director-common -- bacula-director-common < 5.2.0-alt1
echo "Updating bacula < 5.2.0, catalog upgrade required!
use appropriate %_datadir/bacula/scripts/update_*_tables script"

%preun director-sqlite3
%preun_service bacula-dir

%preun director-mysql
%preun_service bacula-dir

%preun director-postgresql
%preun_service bacula-dir

%preun client
%preun_service bacula-fd

%preun storage
%preun_service bacula-sd

%files common
%attr (0770,root,bacula) %_localstatedir/bacula
%attr (0775,root,bacula) %dir %_var/run/bacula
%attr (0750,root,bacula) %dir %_sysconfdir/bacula
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/bacula-*-password.conf
%dir %_datadir/bacula
%dir %_datadir/bacula/scripts
%dir %_docdir/bacula
%_man8dir/bacula.8.gz
%_sbindir/bsmtp
%_man1dir/bsmtp.1.gz
%_docdir/bacula/ReleaseNotes
%_docdir/bacula/LICENSE
%_libdir/libbac-%version.so
%_libdir/libbaccfg-%version.so
%_libdir/libbacfind-%version.so
%_libdir/libbacpy-%version.so
%_libdir/libbac.so
%_libdir/libbaccfg.so
%_libdir/libbacfind.so
%_libdir/libbacpy.so

%files console
%attr (0644,root,root) %_datadir/%name/sample-configs/bconsole.conf
%config(noreplace) %attr (0600,root,root) %_sysconfdir/bacula/bconsole.conf
%_bindir/bconsole
%_man8dir/bconsole.8.gz

%if_enabled bwx
%files console-wx
%attr (0644,root,root) %_datadir/%name/sample-configs/bwx-console.conf
%_bindir/bwx-console
%_man1dir/bacula-bwxconsole.1.gz
%_miconsdir/bacula-wxwin.xpm
%_liconsdir/bacula-wxwin.xpm
%_niconsdir/bacula-wxwin.xpm
%_desktopdir/wxconsole.desktop
%endif

%if_enabled tray
%files tray-monitor
%attr (0644,root,root) %_datadir/%name/sample-configs/tray-monitor.conf
%_bindir/bacula-tray-monitor
%_man1dir/bacula-tray-monitor.1.gz
%_miconsdir/bacula-tray-monitor.xpm
%_liconsdir/bacula-tray-monitor.xpm
%_niconsdir/bacula-tray-monitor.xpm
%_desktopdir/bacula-tray-monitor.desktop
%endif

%if_enabled bat
%files bat
%attr (0644,root,root) %_datadir/%name/sample-configs/bat.conf
%doc %_defaultdocdir/%name/html
%attr (0755,root,root) %_bindir/bat
%_man1dir/bat.1.gz
%_miconsdir/bat.png
%_liconsdir/bat.png
%_niconsdir/bat.png
%_desktopdir/bat.desktop
%endif

%files client
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/sysconfig/bacula-fd
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/sysconfig/limits.d/bacula-fd
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/bacula-fd.conf
%_sbindir/bacula-fd
%config %_initdir/bacula-fd
%_libdir/bpipe-fd.so
%_man8dir/bacula-fd.8.gz

%files storage
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/bacula-sd.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/mtx-changer.conf
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/device
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/device/*.conf
%config %_initdir/bacula-sd
%_sbindir/bacula-sd
%_sbindir/bextract
%_sbindir/bls
%_sbindir/btape
%_sbindir/mtx-changer
%_sbindir/disk-changer
%_sbindir/dvd-handler
%_man8dir/bacula-sd.8.gz
%_man8dir/bextract.8.gz
%_man8dir/bls.8.gz
%_man8dir/btape.8.gz

%files debug
%_sbindir/btraceback
%_datadir/%name/scripts/btraceback.dbx
%_datadir/%name/scripts/btraceback.gdb
%_man8dir/btraceback.8.gz

%files director-common
%doc COPYING ChangeLog ReleaseNotes VERIFYING kernstodo updatedb
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/client
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/fileset
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/job
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/messages
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/pool
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/schedule
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/storage
%dir %attr (0750,bacula,bacula) %_logdir/bacula/
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/bacula-dir.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/client/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/fileset/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/job/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/messages/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/pool/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/schedule/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/storage/*.conf
%config(noreplace) %_sysconfdir/sysconfig/bacula
%_sbindir/bregex
%_sbindir/bwild
%_man8dir/bacula-dir.*
%_man8dir/dbcheck.*
%_man8dir/bscan.*
%_man8dir/bcopy.*
%_man8dir/bregex.*
%_man8dir/bwild.*
%_datadir/%name/scripts/delete_catalog_backup
%_datadir/%name/scripts/make_catalog_backup
%_datadir/%name/scripts/make_catalog_backup.pl
%_sysconfdir/logrotate.d/%name
%_sbindir/bacula-dir
%_sbindir/bcopy
%_sbindir/bscan
%_sbindir/dbcheck
%_libdir/libbacsql-%version.so
%_libdir/libbacsql.so

%files director-mysql
%_initdir/bacula-dir
%_altdir/bacula-dir.mysql
%_libdir/libbaccats-mysql*.so
%_datadir/%name/scripts/create_mysql_database
%_datadir/%name/scripts/drop_mysql_database
%_datadir/%name/scripts/drop_mysql_tables
%_datadir/%name/scripts/grant_mysql_privileges
%_datadir/%name/scripts/make_mysql_tables
%_datadir/%name/scripts/update_mysql_tables

%files director-postgresql
%_initdir/bacula-dir
%_altdir/bacula-dir.pgsql
%_libdir/libbaccats-postgresql*.so
%_datadir/%name/scripts/create_postgresql_database
%_datadir/%name/scripts/drop_postgresql_database
%_datadir/%name/scripts/drop_postgresql_tables
%_datadir/%name/scripts/grant_postgresql_privileges
%_datadir/%name/scripts/make_postgresql_tables
%_datadir/%name/scripts/update_postgresql_tables

%files director-sqlite3
%_initdir/bacula-dir
%_altdir/bacula-dir.sqlite3
%_libdir/libbaccats-sqlite3*.so
%_datadir/%name/scripts/create_sqlite3_database
%_datadir/%name/scripts/drop_sqlite3_database
%_datadir/%name/scripts/drop_sqlite3_tables
%_datadir/%name/scripts/grant_sqlite3_privileges
%_datadir/%name/scripts/make_sqlite3_tables
%_datadir/%name/scripts/update_sqlite3_tables

%files nagios
%_sysconfdir/nagios/commands/check_bacula.cfg
%_libdir/nagios/plugins/check_bacula

%files
%changelog
* Wed Jul 04 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.10-alt1
- 5.2.10

* Fri Jun 15 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.9-alt1
- 5.2.9

* Mon Feb 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.6-alt1
- 5.2.6

* Sat Jan 28 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.5-alt1
- 5.2.5

* Mon Jan 23 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.4-alt1
- 5.2.4

* Tue Jan 17 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.3-alt2
- Fix bat permissions 0750 -> 0755 (ALT #26805)

* Tue Dec 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.3-alt1
- 5.2.3

* Mon Nov 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.2-alt1
- 5.2.2

* Mon Nov 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.1-alt1
- 5.2.1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.3-alt3.1
- Rebuild with Python-2.7

* Sun Oct 03 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.3-alt3
- rebuild with openssl-1.0.0a

* Sat Sep 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.3-alt2
- rebuild with libmysqlclient.so.16

* Thu Aug 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.3-alt1
- 5.0.3
- install bat help files (mike@, ALT #23858)
- tightened permissions on /etc/bacula/ (ALT #23851)

* Thu May 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.2-alt1
- 5.0.2
- fix wrong DB_HOST obtaining (ALT #23152)

* Thu Feb 25 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.1-alt2
- Release-5.0.1
- realy fix /etc/bacula permissions (ALT #22925)

* Thu Feb 11 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.1-alt1
- fix /etc/bacula permissions (ALT #22925)
- updated from upstream/Branch-5.0
- disabled wx console build

* Fri Jan 29 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.0-alt1
- 5.0.0 (ALT #22844)
- no more gconsole

* Fri Dec 18 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.3-alt2
- use pg_dump -h instead of pg_dump -c (ALT #22506)

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1.1
- Rebuilt with python 2.6

* Tue Oct 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.3-alt1
- 3.0.3 (ALT #21379)

* Wed Sep 30 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.2-alt6
- libdbi director added
- make_catalog_backup now parse director config for DB settings

* Wed Sep 23 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.2-alt5
- ldv: fix lowering caps

* Wed Sep 23 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.2-alt4
- ldv: bacula-fd: Implement keep readall capabilities support
- vitty: Implement console 'timeout' feature

* Fri Aug 28 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.2-alt3
- fix typo in make_catalog_backup

* Mon Aug 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.2-alt2
- merge patches from alb@

* Mon Jul 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.2-alt1
- 3.0.2
- Fix 'Always Full' problem (ALT #20815)

* Tue Jun 30 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt8
- Add strict version dependency for qt4 in bacula-bat package (ALT #20630)

* Mon Jun 22 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt7
- Patches from alb@:
- fix pidfiles names (remove port)
- add altlinux platform

* Fri Jun 19 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt6
- apply some upstream patches
- fix initscripts for fd and sd (SIGHUP not handled)

* Wed Jun 17 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt5
- create logfile with correct permissions
- add user 'bacula' to group 'tape' for storage (ALT #20464)
- change default director config to simplify parsing

* Fri Jun 05 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt4
- move log to %_logdir (ALT #20318)
- fix director startup (check catalog before daemonizing,ALT #20319)

* Thu Jun 04 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt3
- default configs fix

* Wed Jun 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt2
- move schedule from JobDefs to Job in default configs

* Thu Apr 30 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt1
- 3.0.1

* Fri Apr 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.0-alt1
- 3.0.0
- new director-postgresql subpackage

* Sat Apr 04 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.4-alt8
- Upstream patches for 2.4.4

* Wed Mar 25 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.4-alt7
- fix #19238
- fix forgotten dir ownership

* Tue Mar 24 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.4-alt6
- fix initscripts (expect-user)

* Tue Mar 24 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.4-alt5
- fix typo in client config

* Fri Mar 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.4-alt4
- Auto passwords generation (local setup)
- Split storage config (/etc/bacula/devices)

* Fri Mar 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.4-alt3
- Minor changes to default configs

* Thu Feb 26 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.4-alt2
- build with sqlite3 

* Wed Jan 07 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Mon Nov 10 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt6
- docs packaged
- icons in standard place

* Wed Nov 05 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt5
- added nagios plugin, web interface
- enabled gnome console, tray monitor
- dropped consolehelper usage for consoles,
- consoles configs are now in ~/.bacula/
- look for examples in /usr/share/bacula/sample-configs

* Wed Nov 05 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt4
- upstream patch to fix a case of orphaned jobs (and possible deadlock)

* Fri Oct 31 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt3
- Fix build with new tollchain

* Tue Oct 28 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt2
- Fix #17637
- Apply upstream patch to fix 1175

* Sat Oct 11 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt1
- 2.4.3 bugfix release

* Thu Aug 21 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.2-alt2
- fix #15577
- applied upstream patches

* Fri Aug 01 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Thu Jun 05 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue May 06 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.8-alt3
- update_menus for bat
- fixed path to mtx (#15578)
- changed storage scripts location to %_sbindir

* Fri Mar 28 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.8-alt2
- Applying patches to fix #1031,1047 and some other (upstream recommended)
- update_menus patch

* Thu Feb 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.8-alt1
- 2.2.8
- unmets with new rpmbuild fixed

* Wed Jan 09 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.7-alt1
- 2.2.7
- Patch to fix #1034

* Wed Dec 26 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.6-alt3
- Repaired build with new autotools

* Fri Nov 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.6-alt2
- Applying patches to fix #1008, 1015, 1016, 1007, 1021

* Mon Nov 12 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.6-alt1
- 2.2.6
- Split director config into multiple files

* Wed Oct 31 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.5-alt3
- Applying patches to fix #991, 993, 979, 982, 947, 1003

* Thu Oct 25 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.5-alt2
- Patches to fix #991, 993, 979
- move director start/stop after/before mysql

* Mon Oct 22 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.5-alt1
- 2.2.5 release with patches to fix #986,#989
- Version 2.2.5 is a major bug fix release to version 2.2.4
- It fixes the following bugs: #961, 962, 963, 969, 968, 960,
- 964, (possibly 935 and 903), 953, 953, 967, 966, 965, 954,
- 957, 908, 958, and 955.
- It also improves listing performance problems in bat pointed
- out by Chris Howells.

* Mon Oct 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.4-alt4
- Applying upstream patch which resolves bug #969 where the user can't
- change the replace option in the restore menu

* Tue Oct 02 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.4-alt3
- Applying upstream patches to fix bugs #954,#964,#908,#955,#953,#958

* Mon Sep 24 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.4-alt2
- Default location of bat configfile changed

* Thu Sep 20 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.4-alt1
- 2.2.4 release

* Mon Sep 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.2.3-alt1
- 2.2.3 release.
- fix build on x86_64 with libmysql (patch2), thx shaba@.

* Sun Sep 02 2007 Alexey Shabalin <shaba@altlinux.ru> 2.2.1-alt1
- 2.2.1
- add packages:
  + bacula-bat
  + bacula-console-wx
  + bacula-console-gnome (include bacula-tray-monitor). Disabled build - need fix linking.
- support build with readline (but default build with conio)
- bacula-bat, bacula-console-wx, bacula-console-gnome run over consolehelper
- bsmtp move to bacula-common
- bcopy,bextract,bls,bscan,btape move to bacula-storage
- not use macros %%exclude in %%files sections

* Thu Aug 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.2.0-alt2
- New packaging scheme:
  + bacula package is a purely virtual one that requires:
    * bacula-director
    * bacula-client
	* bacula-storage
	* bacula-console
	* bacula-debug
  + Each one of bacula-* subpackages require bacula-common.
  + bacula package now provides obsoleted updatedb subpackage.
  + Renamed bacula-sd subpackage to bacula-storage.

- Added proper initscripts instead of old hellish messed up ones.
- Moved to SMP-aware build.
- Marked config files as %%config (noreplace) ones.
- Fixed/created preun/post for subpackages.
- Fix attributes for config files, %%_localstatedir/bacula and
- %%_var/run/bacula, logrotate files.

- Cosmetics:
  + Split BuildRequires.
  + Aligned description.
  + configure: each parameter on separate line.
  + Fixed summaries.

* Mon Aug 13 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.0-alt1
- New upstream 2.2.0

* Thu Jul 19 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.3-alt2
- Set autoreq to 'no' for updatedb package

* Wed Jul 18 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.3-alt1
- New upstream version 2.0.3
- New package for client-only installations
- New package for database update
- Many bugfixes, see Changelog for details

* Mon Apr 16 2007 Michail Yakushin <silicium@altlinux.ru> 2.0.1-alt0
- intial build for alt
