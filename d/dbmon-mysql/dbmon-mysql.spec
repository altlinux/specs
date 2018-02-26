%define oname dbmon
Summary: A simple script to monitor MySQL queries
Name: dbmon-mysql
Version: 0.1
Release: alt7
License: GPL
Group: Databases
Packager: Boris Savelev <boris@altlinux.org>
Url: http://faemalia.net/mysqlUtils/
Source: %oname.pl
Source1: %oname.init
Source2: %oname.sysconfig
Source3: %oname.readme
Source4: %oname.logrotate
Source5: %oname.monit

BuildArch: noarch

Requires: perl-DBI

# Automatically added by buildreq on Mon Dec 22 2008
BuildRequires: perl-DBI

%description
A simple script to monitor MySQL queries and log them into a file for future processing.
Optionally will kill long-running queries.

%install
mkdir -p %buildroot{%_datadir/%name,%_initdir,%_var/run/%name,%_sysconfdir/sysconfig,%_var/log/%oname}
install -m755 %SOURCE0 %buildroot%_datadir/%name
install -m755 %SOURCE1 %buildroot%_initdir/%name
install -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m644 -D -p %SOURCE4 %buildroot%_sysconfdir/logrotate.d/%name
install -m644 %SOURCE3 %_builddir/README.ALT
install -m644 %SOURCE5 %_builddir/monit-%name

%pre
%_sbindir/groupadd -r -f _dbmon &>/dev/null ||:
%_sbindir/useradd -r -g _dbmon -d /dev/null -s /dev/null \
		-c "DBMon user" -M -n _dbmon &>/dev/null ||:

%files
%doc README.ALT monit-%name
%_initdir/%name
%config %_sysconfdir/sysconfig/%name
%_sysconfdir/logrotate.d/%name
%_datadir/%name
%attr(2770,root,_dbmon) %dir %_var/run/%name
%attr(2770,root,_dbmon) %dir %_var/log/%oname

%changelog
* Mon Mar 22 2010 Boris Savelev <boris@altlinux.org> 0.1-alt7
- add '--interval' option
- change default interval from 25 (40 run per sec) to 1000 (1 run per sec)

* Thu Apr 09 2009 Boris Savelev <boris@altlinux.org> 0.1-alt6
- add perl-DBI to requires

* Thu Jan 22 2009 Boris Savelev <boris@altlinux.org> 0.1-alt5
- realy add monit rule

* Mon Jan 19 2009 Boris Savelev <boris@altlinux.org> 0.1-alt4
- fix monit rule destination

* Tue Dec 30 2008 Boris Savelev <boris@altlinux.org> 0.1-alt3
- add readme
- add logrotate rule
- add monit rule

* Fri Dec 26 2008 Boris Savelev <boris@altlinux.org> 0.1-alt2
- fix error in config (killong now killlong)

* Mon Dec 22 2008 Boris Savelev <boris@altlinux.org> 0.1-alt1
- initial build for Sisyphus

