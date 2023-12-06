Name: ulogd
Version: 2.0.8
Release: alt1

%def_disable nfacct

%define _unpackaged_files_terminate_build 1

Summary: ulogd - The userspace logging daemon for netfilter
Url: http://www.netfilter.org/projects/ulogd/
License: GPLv2+
Group: System/Servers

Vcs: git://git.netfilter.org/ulogd2
Source: http://www.netfilter.org/projects/ulogd/files/%name-%version.tar
Source1: %name.init
Source2: %name.logrotate
Source3: %name.service
Patch0: %name-%version-%release.patch

BuildRequires: libpcap-devel zlib-devel libMySQL-devel postgresql-devel libsqlite3-devel libdbi-devel
BuildRequires: libnfnetlink-devel libmnl-devel libnetfilter_log-devel >= 1.0.2 libnetfilter_conntrack-devel
%{?_enable_nfacct:BuildRequires: libnetfilter_acct-devel}

# For JSON plugin
BuildRequires: libjansson-devel

# For documentation
BuildRequires: linuxdoc-tools OpenSP

%description
Ulogd is an universal logging daemon for the ULOG target of netfilter, the
Linux 2.6 firewalling subsystem. Ulogd is able to log packets in various
formats to different targets (text files, databases, etc..). It has an
easy-to-use plugin interface to add new protocols and new output targets.

%package mysql
Summary: MySQL output plugin for ulogd
Group: System/Servers
Requires: %name = %EVR

%description mysql
ulogd-mysql is a MySQL output plugin for ulogd. It enables logging of
firewall information into a MySQL database.

%package pgsql
Summary: PostgreSQL output plugin for ulogd
Group: System/Servers
Requires: %name = %EVR

%description pgsql
ulogd-pgsql is a PostgreSQL output plugin for ulogd. It enables logging of
firewall information into a PostgreSQL database.

%package sqlite3
Summary: SQLite3 output plugin for ulogd
Group: System/Servers
Requires: %name = %EVR

%description sqlite3
ulogd-sqlite3 is a SQLite output plugin for ulogd. It enables logging of
firewall information into a SQLite v.3 database.

%package dbi
Summary: Libdbi framework output plugin for %name
Group: System/Servers
Requires: %name = %EVR

%description dbi
%name-dbi is a libdbi output plugin for %name. It enables logging of
firewall information through a libdbi interface.

%prep
%setup
%patch0 -p1

%build
#export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%autoreconf
%configure \
	--disable-static \
	--enable-json \
	%{subst_enable nfacct}

make DESTDIR=%buildroot
make -C doc

%install
mkdir -p %buildroot/%_logdir/%name
mkdir -p %buildroot/%_sysconfdir
mkdir -p %buildroot/%_libdir/%name
mkdir -p %buildroot/%_sbindir
%makeinstall_std

mkdir -p %buildroot/%_sysconfdir/rc.d/init.d
install %SOURCE1 %buildroot/%_sysconfdir/rc.d/init.d/%name

install -pDm644 %SOURCE3 %buildroot/%_unitdir/%name.service

install -pDm644 %SOURCE2 %buildroot/%_sysconfdir/logrotate.d/%name

mkdir -p %buildroot/%_datadir/%name
install -pm644 doc/*.sql %buildroot/%_datadir/%name/
install -pm644 doc/sqlite3.table %buildroot/%_datadir/ulogd/
mkdir -p %buildroot/%_localstatedir/ulogd/

mkdir -p %buildroot/%_man8dir
install -pm644 %name.8 %buildroot/%_man8dir/%name.8

install -Dm0640 %name.conf %buildroot%_sysconfdir/%name.conf

%if_disabled nfacct
sed -i -r 's;^(plugin="%_libdir/ulogd/ulogd_inpflow_NFACCT\.so");#\1;' %buildroot%_sysconfdir/%name.conf
%endif

%pre
%_sbindir/groupadd -r -f %name >/dev/null 2>&1
%_sbindir/useradd -r -N -g %name -d /dev/null -s /dev/null %name >/dev/null 2>&1 ||:

%preun
%preun_service %name

%files
%attr(0755,root,root) %_sbindir/%name
%attr(0640,root,%name) %config(noreplace) %_sysconfdir/%name.conf
%_sysconfdir/rc.d/init.d/%name
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %_libdir/%name
%attr(1770,root,ulogd) %_logdir/%name
%_libdir/%name/*.so
%doc COPYING AUTHORS README
%doc doc/%name.txt doc/%name.html
%_man8dir/*
%attr(1770,root,ulogd) %_localstatedir/%name/
%dir %_datadir/%name/
%exclude  %_libdir/%name/*.la
%exclude %_libdir/%name/ulogd_output_MYSQL.so
%exclude %_libdir/%name/ulogd_output_PGSQL.so
%exclude %_libdir/%name/ulogd_output_SQLITE3.so
%exclude %_libdir/%name/ulogd_output_DBI.so

%files mysql
%_libdir/%name/ulogd_output_MYSQL.so
%_datadir/%name/mysql-*.sql

%files pgsql
%_libdir/%name/ulogd_output_PGSQL.so
%_datadir/%name/pgsql-*.sql

%files sqlite3
%_libdir/%name/ulogd_output_SQLITE3.so
%_datadir/%name/sqlite3.table

%files dbi
%_libdir/%name/ulogd_output_DBI.so

%changelog
* Wed Dec 06 2023 Mikhail Efremov <sem@altlinux.org> 2.0.8-alt1
- Don't use rpm-build-licenses.
- Use useradd -N instead of -n.
- Updated to 2.0.8.

* Wed Feb 06 2019 Mikhail Efremov <sem@altlinux.org> 2.0.7-alt1
- ulogd.logrotate: Replace *.pktlog with *.json.
- Fix log path for json1.
- Updated to 2.0.7.

* Fri Oct 27 2017 Mikhail Efremov <sem@altlinux.org> 2.0.5-alt4
- Use _unpackaged_files_terminate_build.
- ulogd: restructures signal handling by self-pipe trick.
- Fix default log path.

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.5-alt3
- Rebuilt with libdbi-0.9.0.

* Thu Dec 17 2015 Mikhail Efremov <sem@altlinux.org> 2.0.5-alt2
- Fix documentation files mode.
- Fix logrotate config mode.
- Fix logrotate config.

* Thu May 21 2015 Mikhail Efremov <sem@altlinux.org> 2.0.5-alt1
- Updated to 2.0.5.

* Mon Apr 21 2014 Mikhail Efremov <sem@altlinux.org> 2.0.4-alt1
- Enable JSON plugin.
- Updated to 2.0.4.

* Tue Nov 26 2013 Mikhail Efremov <sem@altlinux.org> 2.0.3-alt1
- Drop obsoleted patches.
- Updated to 2.0.3.

* Thu Aug 22 2013 Mikhail Efremov <sem@altlinux.org> 2.0.2-alt1
- Update ulogd.logrotate.
- Run ulogd from user "ulogd".
- init script: Use --pidfile option for ulogd.
- Patches from Debian:
    + Implement PID file writing
    + Improve pid file handling
    + Run nice() before giving up root with setuid().
    + Enable NFLOG => LOGEMU stack by default.
- Change logfiles and databases paths.
- Don't build documentation in PS format.
- Updated to 2.0.2.

* Tue Mar 12 2013 Mikhail Efremov <sem@altlinux.org> 1.24-alt16
- Fix plugins packaging.
- Added systemd service file (closes: #28096).

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
