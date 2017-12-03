%set_verify_elf_method relaxed

%def_enable bat
%def_enable readline
%def_disable debug


Name: bacula7
Version: 7.4.7
Release: alt3%ubt

License: AGPLv3
Summary: Network based backup program
Group: Archiving/Backup
Url: http://www.bacula.org/
Source: %name-%version.tar
Source1: bacula-dir.init
Source2: bacula-fd.init
Source3: bacula-sd.init
Source4: bacula-fd.sysconfig
Source5: bacula-fd.limit
Source8: %name-configs-default-%version.tar
Source9: %name-icons-%version.tar
Source10: bacula.sysconfig
Source11: tmpfiles.conf
Source12: bacula-fd.service
Source13: bacula-sd.service
Source14: bacula-dir.service
Patch0: %name-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: dvd+rw-tools gcc-c++ groff-base libMySQL-devel libssl-devel libncurses-devel libsqlite3-devel libssl libacl-devel libcap-devel python-devel zlib-devel iputils bc postgresql-devel

%filter_from_requires /libbaccats-%version\.so/d

%if_enabled readline
BuildRequires: libreadline-devel
%endif
%if_enabled bat
# bat buildrequires
BuildRequires: imake libICE-devel libX11-devel libqwt-devel xorg-cf-files
%endif

Requires: %name-common = %version-%release
Requires: %name-client = %version-%release
Requires: %name-storage = %version-%release
Requires: %name-console = %version-%release
Requires: %name-dir = %version-%release

%package client
Summary: Network based backup program (client only)
Group: Archiving/Backup
Provides: %name-fd = %version-%release
Conflicts: bacula-client
Requires: %name-common = %version-%release

%package storage
Summary: Network based backup program (storage only)
Group: Archiving/Backup
Conflicts: bacula-storage
Requires: %name-common = %version-%release

%package console
Summary: Network based backup program (console only)
Group: Archiving/Backup
Conflicts: bacula-console
Requires: %name-common = %version-%release

%if_enabled bat
%package bat
Summary: Network based backup program (QT4 Bacula Administration Tool)
Group: Archiving/Backup
BuildRequires(pre): libqt4-devel
Requires: libqt4-core >= %{get_version libqt4-core}
Conflicts: bacula-bat
%endif

%package director-common
Summary: Network based backup program (director common)
Group: Archiving/Backup
Requires: %name-common = %version-%release
Conflicts: bacula-director-common

%package director-mysql
Summary: Network based backup program (MySQL director only)
Group: Archiving/Backup
Requires(pre): %name-director-common = %version-%release
Provides: %name-director = %version-%release
Obsoletes: %name-director < %version-%release
Provides: %name-dir = %version-%release
Conflicts: bacula-director-mysql

%package director-sqlite3
Summary: Network based backup program (SQLITE3 director only)
Group: Archiving/Backup
Requires(pre): sqlite3
Requires(pre): %name-director-common = %version-%release
Provides: %name-dir = %version-%release
Conflicts: bacula-director-sqlite3

%package director-postgresql
Summary: Network based backup program (PostgreSQL director only)
Group: Archiving/Backup
Requires(pre): %name-director-common = %version-%release
Provides: %name-dir = %version-%release
Conflicts: bacula-director-postgresql

%package common
Summary: Network based backup program (common files)
Group: Archiving/Backup
Requires(pre): passwdqc-utils
Conflicts: bacula-common

%package debug
Summary: Network based backup program (debug files)
Group: Archiving/Backup
Requires: %name-common = %version-%release
BuildArch: noarch
Conflicts: bacula-debug

%package nagios
Summary: The check_bacula plugin for nagios
Group: Archiving/Backup
Conflicts: bacula-nagios

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
%patch0 -p1

mv ../%name-icons-%version icons

%build
export MTX=%_sbindir/mtx
autoheader -B autoconf autoconf/configure.in >autoconf/config.h.in
autoconf -B autoconf autoconf/configure.in >configure

%configure \
	--with-openssl \
	--with-python \
	--mandir=%_mandir \
	--with-working-dir=%_localstatedir/bacula \
	--with-scriptdir=%_datadir/bacula/scripts \
	--with-pid-dir=%_var/run/bacula \
	--sysconfdir=%_sysconfdir/bacula \
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
%if_enabled bat
	--enable-bat=yes \
%endif
	--with-mysql \
	--with-logdir=%_logdir \
	#
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

# make the nagios plugin
pushd examples/nagios/check_bacula
%make LIBS="-lpthread -ldl -lssl -lcrypto"
popd

%install

%make_install DESTDIR="%buildroot" install

mkdir -p %buildroot%_initdir %buildroot%_unitdir
install -pm 755 %SOURCE1 %buildroot%_initdir/bacula-dir
install -pm 644 %SOURCE14 %buildroot%_unitdir/bacula-dir.service
install -pm 755 %SOURCE2 %buildroot%_initdir/bacula-fd
install -pm 644 %SOURCE12 %buildroot%_unitdir/bacula-fd.service
install -pm 755 %SOURCE3 %buildroot%_initdir/bacula-sd
install -pm 644 %SOURCE13 %buildroot%_unitdir/bacula-sd.service

mkdir -p %buildroot%_tmpfilesdir/
install -pm 0644 %SOURCE11 %buildroot%_tmpfilesdir/bacula.conf

install -pD -m644 %_sourcedir/bacula.sysconfig \
	%buildroot%_sysconfdir/sysconfig/bacula
install -pD -m644 %_sourcedir/bacula-fd.sysconfig \
	%buildroot%_sysconfdir/sysconfig/bacula-fd

install -pD -m644 scripts/logrotate %buildroot%_sysconfdir/logrotate.d/bacula

install -pD -m644 %_sourcedir/bacula-fd.limit \
	%buildroot%_sysconfdir/sysconfig/limits.d/bacula-fd

mkdir -p %buildroot/var/run/bacula

mkdir -p %buildroot%_datadir/{applications,sample-configs}
mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_niconsdir
mkdir -p %buildroot%_datadir/bacula/sample-configs
mkdir -p %buildroot%_sysconfdir/{security/console.apps,pam.d}
install -d -m755 %buildroot%_bindir
mv %buildroot%_sbindir/bconsole %buildroot%_bindir/
chmod 755 %buildroot%_bindir/bconsole
mv %buildroot%_sysconfdir/bacula/bconsole.conf %buildroot%_datadir/bacula/sample-configs/

%if_enabled bat
mv %buildroot%_sbindir/bat %buildroot%_bindir/bat
install -pD -m644 icons/bat16x16.png %buildroot%_miconsdir/bat.png
install -pD -m644 icons/bat32x32.png %buildroot%_niconsdir/bat.png
install -pD -m644 icons/bat48x48.png %buildroot%_liconsdir/bat.png
install -pD -m644 scripts/bat.desktop %buildroot%_desktopdir/bat.desktop
mv %buildroot%_sysconfdir/bacula/bat.conf %buildroot%_datadir/bacula/sample-configs/
install -d %buildroot%_defaultdocdir/bacula/html
cp -a src/qt-console/help/*.html %buildroot%_defaultdocdir/bacula/html/
%endif

cp -ar ../%name-configs-default-%version/* %buildroot%_sysconfdir/bacula/

install -pD -m755 %buildroot%_datadir/bacula/scripts/mtx-changer %buildroot%_sbindir
install -pD -m644 %buildroot%_datadir/bacula/scripts/mtx-changer.conf %buildroot%_sysconfdir/bacula/
sed -i "s|%_datadir/bacula/scripts|%_sysconfdir/bacula|g" %buildroot%_sbindir/mtx-changer
install -pD -m755 %buildroot%_datadir/bacula/scripts/disk-changer %buildroot%_sbindir
install -pD -m755 %buildroot%_datadir/bacula/scripts/dvd-handler %buildroot%_sbindir
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

%pre common
%_sbindir/groupadd -r -f bacula
%_sbindir/useradd -r -n -g bacula -d /var/empty -s /bin/false -c "Bacula pseudo user" bacula >/dev/null 2>&1 ||:
%_sbindir/usermod -d /var/empty -s /bin/false bacula >/dev/null 2>&1

%post common
for i in %_sysconfdir/bacula/bacula-*-password.conf; do
 [ ! -s "$i" ] || continue
 printf 'Password = "%%s"\n' "$(pwqgen|sed -e 's/[\"$\`\\]/\\&/g')" > "$i";
done

%post client
%post_service bacula-fd

%pre storage
%_sbindir/groupadd -r -f tape
gpasswd -a bacula tape >/dev/null 2>&1

%post storage
%post_service bacula-sd

%post director-sqlite3
%post_service bacula-dir
if [ ! -s %_localstatedir/bacula/bacula.db ]; then
    %_datadir/bacula/scripts/make_sqlite3_tables
    chown bacula.bacula %_localstatedir/bacula/bacula.db
fi

%post director-mysql
%post_service bacula-dir

%post director-postgresql
%post_service bacula-dir

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
%attr (1770,root,bacula) %_localstatedir/bacula
%attr (0775,root,bacula) %dir %_var/run/bacula
%attr (0750,root,bacula) %dir %_sysconfdir/bacula
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/bacula-*-password.conf
%dir %_datadir/bacula
%dir %_datadir/bacula/scripts
%dir %_docdir/bacula
%_tmpfilesdir/*
%_man8dir/bacula.8.*
%_sbindir/bsmtp
%_man1dir/bsmtp.1.*
%_docdir/bacula/ReleaseNotes
%_docdir/bacula/LICENSE
%_libdir/libbac-%version.so
%_libdir/libbaccfg-%version.so
%_libdir/libbacfind-%version.so
%_libdir/libbac.so
%_libdir/libbaccfg.so
%_libdir/libbacfind.so

%files console
%attr (0644,root,root) %_datadir/bacula/sample-configs/bconsole.conf
%config(noreplace) %attr (0600,root,root) %_sysconfdir/bacula/bconsole.conf
%_bindir/bconsole
%_man8dir/bconsole.8.*

%if_enabled bat
%files bat
%attr (0644,root,root) %_datadir/bacula/sample-configs/bat.conf
%doc %_defaultdocdir/bacula/html
%attr (0755,root,root) %_bindir/bat
%_man1dir/bat.1.*
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
%_unitdir/bacula-fd.service
%_libdir/bpipe-fd.so
%_man8dir/bacula-fd.8.*

%files storage
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/bacula-sd.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/mtx-changer.conf
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/device.d
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/device.d/*.conf
%config %_initdir/bacula-sd
%_unitdir/bacula-sd.service
%_sbindir/bacula-sd
%_sbindir/bextract
%_sbindir/bls
%_sbindir/btape
%_sbindir/mtx-changer
%_sbindir/disk-changer
%_sbindir/dvd-handler
%_man8dir/bacula-sd.8.*
%_man8dir/bextract.8.*
%_man8dir/bls.8.*
%_man8dir/btape.8.*

%files debug
%_sbindir/btraceback
%_datadir/bacula/scripts/btraceback.dbx
%_datadir/bacula/scripts/btraceback.gdb
%_man8dir/btraceback.8.*

%files director-common
%doc COPYING ChangeLog ReleaseNotes VERIFYING updatedb
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/client.d
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/fileset.d
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/job.d
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/messages.d
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/pool.d
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/schedule.d
%dir %attr (0750,root,bacula) %_sysconfdir/bacula/storage.d
%dir %attr (1770,root,bacula) %_logdir/bacula/
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/bacula-dir.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/client.d/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/fileset.d/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/job.d/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/messages.d/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/pool.d/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/schedule.d/*.conf
%config(noreplace) %attr (0640,root,bacula) %_sysconfdir/bacula/storage.d/*.conf
%config(noreplace) %_sysconfdir/sysconfig/bacula
%_sbindir/bregex
%_sbindir/bwild
%_man8dir/bacula-dir.*
%_man8dir/dbcheck.*
%_man8dir/bscan.*
%_man8dir/bcopy.*
%_man8dir/bregex.*
%_man8dir/bwild.*
%_datadir/bacula/scripts/delete_catalog_backup
%_datadir/bacula/scripts/make_catalog_backup
%_datadir/bacula/scripts/make_catalog_backup.pl
%_sysconfdir/logrotate.d/bacula
%_unitdir/bacula-dir.service
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
%_datadir/bacula/scripts/create_mysql_database
%_datadir/bacula/scripts/drop_mysql_database
%_datadir/bacula/scripts/drop_mysql_tables
%_datadir/bacula/scripts/grant_mysql_privileges
%_datadir/bacula/scripts/make_mysql_tables
%_datadir/bacula/scripts/update_mysql_tables

%files director-postgresql
%_initdir/bacula-dir
%_altdir/bacula-dir.pgsql
%_libdir/libbaccats-postgresql*.so
%_datadir/bacula/scripts/create_postgresql_database
%_datadir/bacula/scripts/drop_postgresql_database
%_datadir/bacula/scripts/drop_postgresql_tables
%_datadir/bacula/scripts/grant_postgresql_privileges
%_datadir/bacula/scripts/make_postgresql_tables
%_datadir/bacula/scripts/update_postgresql_tables

%files director-sqlite3
%_initdir/bacula-dir
%_altdir/bacula-dir.sqlite3
%_libdir/libbaccats-sqlite3*.so
%_datadir/bacula/scripts/create_sqlite3_database
%_datadir/bacula/scripts/drop_sqlite3_database
%_datadir/bacula/scripts/drop_sqlite3_tables
%_datadir/bacula/scripts/grant_sqlite3_privileges
%_datadir/bacula/scripts/make_sqlite3_tables
%_datadir/bacula/scripts/update_sqlite3_tables

%files nagios
%_sysconfdir/nagios/commands/check_bacula.cfg
%_libdir/nagios/plugins/check_bacula

%files

%changelog
* Sun Dec 03 2017 Boris Gulay <boresexpress@altlinux.org> 7.4.7-alt3%ubt
- Fix bacula-dir cannot create PID-file (closes: 33645)
* Thu May 18 2017 Boris Gulay <boresexpress@altlinux.org> 7.4.7-alt2%ubt
- Use readline instead of conio.
- Update initscripts to use common style and check config before load.
* Wed Apr 19 2017 Boris Gulay <boresexpress@altlinux.org> 7.4.7-alt1%ubt
- Initial build of branch 7.X (spec based on v5).
- Change folder names for config files.
- Change way config files are included.
