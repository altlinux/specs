%define dnsgraph_user _dnsgraph
%define dnsgraph_group _dnsgraph
%define dnsgraph_home %_localstatedir/%name

Name: dnsgraph
Version: 0.9.cvs20051126
Release: alt1

Summary: a RRDtool frontend for named (bind) Statistics
License: GPL
Group: Monitoring

Url: http://dnsgraph.sourceforge.net/
BuildArch: noarch
Source0: http://heanet.dl.sourceforge.net/sourceforge/dnsgraph/%name-%version.tar.gz
Source1: %name
Source2: %name.conf
Source3: %name.cron
Source4: %name.README.ALT
Source5: %name.apache.conf
Source6: %name.htaccess
Patch1: %name-0.9-alt-filepath.patch

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

BuildPreReq: rrd-perl, perl-File-Tail
Requires: bind

%description
dnsgraph is a very simple named statistics RRDtool frontend for BIND
that produces daily, weekly, monthly and yearly graphs of
success/failure, recursion/referral, nxrrset/nxdomain (DNS traffic).

%package apache
Summary: %name's config files for apache
Group: Monitoring
Requires: %name, apache

%description apache
%name's config files for apache

%prep
%setup -q
%patch1 -p1

%build

%install
%__mkdir_p %buildroot%_localstatedir/%name

%__install -pD -m0755 %SOURCE1 %buildroot%_bindir/%name
%__install -m0755 {dnsanalise.pl,dnsreport.pl} %buildroot%_bindir
%__install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/%name.conf
%__install -pD -m0644 %SOURCE3 %buildroot%_sysconfdir/cron.d/%name
%__install -p -m0644 %SOURCE4 README.ALT

%__install -pD -m0644 %SOURCE5 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf
%__install -pD -m0644 %SOURCE6 %buildroot%_var/www/html/addon-modules/%name/.htaccess

%__mkdir_p %buildroot%_var/www/html/addon-modules/%name/imgs

%pre
/usr/sbin/groupadd -r -f %dnsgraph_group ||:
/usr/sbin/useradd -g %dnsgraph_group -G named -c 'dnsgraph' \
	-d %dnsgraph_home -s /dev/null -r %dnsgraph_user >/dev/null 2>&1 ||:

%post apache
%_sbindir/apxs -e -a -n expires %_libdir/apache/mod_expires.so
%_sbindir/apachectl reload

%postun apache
%_sbindir/apachectl reload

%files
%_bindir/*
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/cron.d/*
%dir %attr(1771,root,%dnsgraph_group) %_localstatedir/%name
%doc README*

%files apache
%config(noreplace) %_sysconfdir/httpd/conf/addon-modules.d/*
%config(noreplace) %_var/www/html/addon-modules/%name/.htaccess
%dir %attr(1775,root,%dnsgraph_group) %_var/www/html/addon-modules/%name
%dir %attr(1775,root,%dnsgraph_group) %_var/www/html/addon-modules/%name/imgs

%changelog
* Sat Nov 26 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.9.cvs20051126-alt1
- Updated to cvs-version for get normal work with rrd > 1.2
- Do not touch cron script, conf-file and apache-related config at upgrade-time
- Changed default path to named.stats
- Updated cron-script
- Updated mod_expires directives
- Minor spec update
- Updated README.ALT

* Thu Oct 27 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.9-alt1
- Initial build for Sisyphus
- added dnsgraph-0.9-alt-filepath.patch - fix default locations of files
- conf-files for apache moved into several package %name-apache
- enabled auto-activation of mod_expires apache module for %name-apache
