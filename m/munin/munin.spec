%def_without sybase		# add Sybase support to munin-node

%define _pseudouser_user     _munin
%define _pseudouser_group    _munin
%define _pseudouser_home     %_localstatedir/%name

%define htmldir %webserver_htdocsdir/%name

%add_findreq_skiplist /usr/share/munin/plugins/*

Name: munin
Version: 1.4.5
Release: alt3

Summary: resource monitoring tool
License: GPL
Group: Monitoring

Url: http://munin.sourceforge.net/
BuildArch: noarch
Source: %name-%version.tar
Source1: %name-node.init
Source2: %name.cron
Source3: %name-apache.conf
Source4: %name.logrotate
Source5: %name-node.logrotate

BuildRequires(pre): rpm-macros-webserver-common
BuildRequires: perl-Net-Server perl-DBD-Sybase perl-DBD-mysql perl-DBD-SQLite rrd-perl perl-Text-Balanced perl-Date-Manip perl-Net-SNMP perl-libwww
BuildRequires: perl-Log-Log4perl perl-FCGI perldoc perl-Module-Build perl-HTML-Template

Requires: %name-common = %version-%release
Requires: perl-Date-Manip
Requires: perl-HTML-Template
Requires: perl-Net-Server
Requires: rrdtool >= 1.2.11

%description
Munin, formerly known as The Linpro RRD server, queries a number of
nodes, and processes the data using RRDtool and presents it on web
pages.

%package common
Summary: common files for munin
Group: Monitoring

%description common
Munin, formerly known as The Linpro RRD server, queries a number of
nodes, and processes the data using RRDtool and presents it on web
pages.

%package node
Summary: data agent for munin
Group: Monitoring
Requires: %name-common = %version-%release
Requires: perl-Net-Netmask
Requires: perl-Net-SNMP
Requires: perl-Net-Server
Requires: perl-libwww
Requires: procps >= 2.0.7
Requires: sysstat

%description node
The Munin node package returns statistical data on the request of a
Munin server.

%package man
Summary: man pages for munin
Group: Monitoring

%description man
Munin man pages

%prep
%setup
sed -i -e "s,@htmldir@,%htmldir,g" Makefile.config

%build
%make build

%install
install -d %buildroot%_sysconfdir/{munin{,plugin-conf.d},rc.d/init.d,cron.d,logrotate.d}

%makeinstall_std

install %SOURCE1 %buildroot%_sysconfdir/rc.d/init.d/munin-node
install %SOURCE2 %buildroot%_sysconfdir/cron.d/munin
install %SOURCE4 %buildroot%_sysconfdir/logrotate.d/munin
install %SOURCE5 %buildroot%_sysconfdir/logrotate.d/munin-node

install %SOURCE3 %buildroot%_sysconfdir/munin/apache.conf

install dists/tarball/plugins.conf %buildroot%_sysconfdir/munin
ln -sf %_sysconfdir/munin/plugins.conf %buildroot%_sysconfdir/munin/plugin-conf.d/munin-node

%pre common
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'Munin Node agent' \
	-d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%post node
%post_service munin-node

%preun node
%preun_service munin-node

%files
%_bindir/munin-check
%_bindir/munin-cron
%_bindir/munindoc
%dir %_sysconfdir/munin/munin-conf.d
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/cron.d/munin
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/munin/munin.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/logrotate.d/munin
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/munin/apache.conf
%_sysconfdir/munin/templates
%attr(775,root,%_pseudouser_group) %dir %htmldir
%attr(644,root,%_pseudouser_group) %htmldir/.htaccess
%_datadir/munin/*.ttf
%_datadir/munin/munin-graph
%_datadir/munin/munin-html
%_datadir/munin/munin-limits
%_datadir/munin/munin-update
%_datadir/munin/www/cgi/munin-*
%perl_vendorlib/Munin/Master

%files common
%doc README ChangeLog logo* Checklist
%dir %_sysconfdir/munin
%dir %_datadir/munin
%attr(770,root,%_pseudouser_group) %dir %_pseudouser_home
%perl_vendorlib/Munin/Common
%attr(770,root,%_pseudouser_group) %dir %_logdir/%name

%files man
%_man1dir/munin*
%_man3dir/Munin*
%_man5dir/munin*
%_man8dir/munin*

%files node
%dir %_sysconfdir/munin/plugins
%dir %_sysconfdir/munin/plugin-conf.d
%dir %attr(770,root,%_pseudouser_group) %_pseudouser_home/plugin-state
%attr(640,root,%_pseudouser_group) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/munin/munin-node.conf
%attr(640,root,%_pseudouser_group) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/munin/plugins.conf
%attr(640,root,%_pseudouser_group) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/munin/plugin-conf.d/munin-node
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/logrotate.d/munin-node
%attr(755,root,root) %_initdir/munin-node
%attr(755,root,root) %_sbindir/munin-run
%attr(755,root,root) %_sbindir/munin-node
%attr(755,root,root) %_sbindir/munin-node-configure
%perl_vendorlib/Munin/Plugin*
%perl_vendorlib/Munin/Node
%_datadir/munin/plugins

%if !%{with sybase}
%exclude %_datadir/munin/plugins/sybase_space
%endif

%changelog
* Mon Feb 14 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.5-alt3
- change pseudouser name to "_munin"
- fix permissions according to ALT security policy
- fix munin-node.logrotate: call killall without full path (which was
  wrong)
- don't package /var/log/archive/munin
- initscript: do restart() when called reload
- munin.cron: call munin-cron without absolute path
- munin-node: bind to localhost by default

* Sat Dec 18 2010 Denis Klimov <zver@altlinux.org> 1.4.5-alt2
- fix build. add missing files

* Sat Dec 11 2010 Denis Klimov <zver@altlinux.org> 1.4.5-alt1
- new version
- add man subpackage
- remove defattr
- add groupadd
- change logrotate config

* Thu Mar 27 2008 Nick S. Grechukh <gns@altlinux.org> 1.3.3-alt0.8
- goes to sisyphus

* Thu Mar 27 2008 Nick S. Grechukh <gns@altlinux.org> 1.3.3-alt0.7
- another initscript improvements. useradd in postun

* Thu Mar 27 2008 Nick S. Grechukh <gns@altlinux.org> 1.3.3-alt0.4
- initscript reworked. very ugly although...

* Wed Mar 26 2008 Nick S. Grechukh <gns@altlinux.org> 1.3.3-alt0.4
- should work now, with findreq_skiplist

* Tue Mar 25 2008 Nick S. Grechukh <gns@altlinux.org> 1.3.3-alt0.3
- fixed requires

* Tue Mar 25 2008 Nick S. Grechukh <gns@altlinux.org> 1.3.3-alt0.1
- second try...

