Name: ulogd
Version: 1.24
Release: alt15

Summary: ulogd - The userspace logging daemon for netfilter
Url: http://www.netfilter.org/projects/ulogd/
License: %gpl2plus
Group: System/Servers

Source: http://www.netfilter.org/projects/ulogd/files/%name-%version.tar
Source1: %name.init
Source2: %name.logrotate
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Tue Mar 20 2007
BuildRequires: libpcap-devel zlib-devel libMySQL-devel postgresql-devel libsqlite3-devel

%description
Ulogd is an universal logging daemon for the ULOG target of netfilter, the
Linux 2.6 firewalling subsystem. Ulogd is able to log packets in various
formats to different targets (text files, databases, etc..). It has an
easy-to-use plugin interface to add new protocols and new output targets.

%package mysql
Summary: MySQL output plugin for ulogd
Group: System/Servers
Requires: %name = %version-%release
Requires: zlib

%description mysql
ulogd-mysql is a MySQL output plugin for ulogd. It enables logging of
firewall information into a MySQL database.

%package pgsql
Summary: PostgreSQL output plugin for ulogd
Group: System/Servers
Requires: %name = %version-%release

%description pgsql
ulogd-pgsql is a PostgreSQL output plugin for ulogd. It enables logging of
firewall information into a PostgreSQL database.

%package sqlite3
Summary: SQLite3 output plugin for ulogd
Group: System/Servers
Requires: %name = %version-%release

%description sqlite3
ulogd-sqlite3 is a SQLite output plugin for ulogd. It enables logging of
firewall information into a SQLite v.3 database.

%prep
%setup
%patch0 -p1

%build
#export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure \
	--with-mysql=/usr/lib/mysql \
	--with-pgsql=/usr/lib/pgsql \
	--with-sqlite3 \
	--with-sqlite3-log-ip-as-string
make DESTDIR=%buildroot
#rm -f ulogd
#export LDFALGS="-pie"
#make ulogd

%install
mkdir -p %buildroot/%_logdir/%name
mkdir -p %buildroot/%_sysconfdir
mkdir -p %buildroot/%_libdir/%name
mkdir -p %buildroot/%_sbindir
make install DESTDIR=%buildroot

mkdir -p %buildroot/%_sysconfdir/rc.d/init.d
install %SOURCE1 %buildroot/%_sysconfdir/rc.d/init.d/%name

mkdir -p %buildroot/%_sysconfdir/logrotate.d
install %SOURCE2 %buildroot/%_sysconfdir/logrotate.d/%name

mkdir -p %buildroot/%_datadir/%name
install doc/mysql.table %buildroot/%_datadir/%name/
install doc/mysql.table.ipaddr-as-string %buildroot/%_datadir/%name/
install doc/pgsql.table %buildroot/%_datadir/%name/
install doc/sqlite3.table %buildroot/%_datadir/ulogd/
mkdir -p %buildroot/%_localstatedir/ulogd/

mkdir -p %buildroot/%_man8dir
install %name.8 %buildroot/%_man8dir/%name.8

rm -rf %buildroot/%_includedir/libipulog

%pre
%_sbindir/groupadd -r -f %name >/dev/null 2>&1
%_sbindir/useradd -r -n -g %name -d /dev/null -s /dev/null %name >/dev/null 2>&1 ||:

%preun
%preun_service %name

%files
%attr(0755,root,root) %_sbindir/%name
%attr(0640,root,%name) %config(noreplace) %_sysconfdir/%name.conf
%_sysconfdir/rc.d/init.d/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %_libdir/%name
%attr(1770,root,ulogd) %_logdir/%name
%_libdir/%name/*
%exclude %_libdir/%name/ulogd_MYSQL.so
%exclude %_libdir/%name/ulogd_PGSQL.so
%doc COPYING AUTHORS README
%doc doc/%name.txt doc/%name.a4.ps doc/%name.html
%_man8dir/*
%attr(1770,root,ulogd) %_localstatedir/%name/
%dir %_datadir/%name/

%files mysql
%_libdir/%name/ulogd_MYSQL.so
%_datadir/%name/mysql.table
%_datadir/%name/mysql.table.ipaddr-as-string

%files pgsql
%_libdir/%name/ulogd_PGSQL.so
%_datadir/%name/pgsql.table

%files sqlite3
%_libdir/%name/ulogd_SQLITE3.so
%_datadir/%name/sqlite3.table

%changelog
* Tue Oct 05 2010 Mikhail Efremov <sem@altlinux.org> 1.24-alt15
- To own /usr/share/ulogd/.
- Slightly spec cleanup.

* Sun Sep 19 2010 Mikhail Efremov <sem@altlinux.org> 1.24-alt14
- rebuild with libmysqlclient.so.16

* Thu Aug 27 2009 Mikhail Efremov <sem@altlinux.org> 1.24-alt13
- removed auto creation iptables rules.

* Wed Aug 19 2009 Mikhail Efremov <sem@altlinux.org> 1.24-alt12
- fixed build.
- package is revived

* Thu Feb 12 2009 Lebedev Sergey <barabashka@altlinux.org> 1.24-alt11.M41.1
- added auto creation iptables ulogd rules

* Wed Mar 26 2008 Avramenko Andrew <liks@altlinux.ru> 1.24-alt11
- Fix #15093 (Status option doesn't work in init script)

* Tue Dec 11 2007 Avramenko Andrew <liks@altlinux.ru> 1.24-alt10
- Fix permissions on /var/lib/ulogd dir

* Tue Nov 20 2007 Avramenko Andrew <liks@altlinux.ru> 1.24-alt9
- Fix #13469 (sqlite3 broken)

* Mon Nov 19 2007 Grigory Batalov <bga@altlinux.ru> 1.24-alt8
- Build with SQLite3 output plugin.

* Thu Nov  8 2007 Avramenko Andrew <liks@altlinux.ru> 1.24-alt7
- man page already in upstream. Removed from source.

* Mon Nov  5 2007 Avramenko Andrew <liks@altlinux.ru> 1.24-alt6
- now you can run ulogd under specified user (default: ulogd)
- add ulogd.8 manpage 
- small changes in the logrotate script
- removed libipulog-devel-static

* Tue Jul 17 2007 Avramenko Andrew <liks@altlinux.ru> 1.24-alt5
- removed dependency on libpq3

* Thu Jul 12 2007 Avramenko Andrew <liks@altlinux.ru> 1.24-alt4
- fix #12284 (2GB limit for log files)

* Wed Apr 25 2007 Avramenko Andrew <liks@altlinux.ru> 1.24-alt3
- moved to git
- spec clean up

* Wed Mar 21 2007 Avramenko Andrew <liks@altlinux.ru> 1.24-alt2
- add logrotate file
- fix #3267
- fix #3973, #6425, #8685

* Mon Mar 12 2007 Avramenko Andrew <liks@altlinux.ru> 1.24-alt1
- new version
- spec refreshing

* Mon Dec 29 2003 Victor V Ismakaev <ivv@altlinux.ru> 1.02-alt0.1
- new version

* Wed Oct 01 2003 Victor V Ismakaev <ivv@altlinux.ru> 1.01-alt0.1
- ulogd-1.01
- First build for ALTLinux

* Wed Mar 05 2003 Harald Welte <laforge@gnumonks.org>
- ulogd-1.00-1gm
- updated to 1.00 release

* Mon Sep 24 2001 Harald Welte <laforge@conectiva.com>
- ulogd-0.97-1cl
- updatd to 0.97 release (to fix endless-one-packet-loop bug)

* Sun Jun 17 2001 Harald Welte <laforge@conectiva.com>
- ulogd-0.96-2cl
- updated to 0.96 final release
- use ulogd.init from within source tgz

* Sun May 20 2001 Harald Welte <laforge@conectiva.com>
- ulogd-0.96-1cl
- Initial conectiva package
- cleaned up SPEC file
- created mysql subpackage

* Sun Nov 19 2000 Harald Welte <laforge@gnumonks.org>
- Initial RPM package for ulogd-0.9.
