%define queuegraph_user _queuegraph
%define queuegraph_group _queuegraph
%define queuegraph_data %_localstatedir/%name

%define apache_group apache
%define apache2_group apache2
%define lighttpd_group lighttpd

Name: queuegraph
Version: 1.1
Release: alt3.20070212

Summary: a RRDtool frontend for Postfix queue-statistics
License: GPL
Group: Monitoring

Url: http://sbserv.stahl.bau.tu-bs.de/~hildeb/postfix/queuegraph
Source0: %name.tar
Source1: %name.htaccess
Source2: %name.cron
Source3: %name.apache.conf
Source6: %name.README.ALT
Source7: %name.control
Source8: 100-queuegraph.conf
Source9: A.queuegraph.conf
Patch0: %name-%version-%release.patch

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
BuildArch: noarch

BuildPreReq: rrd-perl

%description
Queuegraph is a very simple mail statistics RRDtool frontend for Postfix that
produces daily, weekly, monthly and yearly graphs of Postfix's active,
deferred, incoming and bounce queues.

%package common
Summary: a RRDtool frontend for Postfix queue-statistics
Group: Monitoring
Requires: rrd-utils

%description common
Queuegraph is a very simple mail statistics RRDtool frontend for Postfix that
produces daily, weekly, monthly and yearly graphs of Postfix's active,
deferred, incoming and bounce queues.

%package apache
Summary: apache-related config and control(8) call
Group: Monitoring
Requires: %name-common = %version-%release, apache

%description apache
Queuegraph is a very simple mail statistics RRDtool frontend for Postfix that
produces daily, weekly, monthly and yearly graphs of Postfix's active,
deferred, incoming and bounce queues.

%package apache2
Summary: apache2-related config and control(8) call
Group: Monitoring
Requires: %name-common = %version-%release, apache2

%description apache2
Queuegraph is a very simple mail statistics RRDtool frontend for Postfix that
produces daily, weekly, monthly and yearly graphs of Postfix's active,
deferred, incoming and bounce queues.

%package lighttpd
Summary: lighttpd-related control(8) call
Group: Monitoring
Requires: %name-common = %version-%release, lighttpd

%description lighttpd
Queuegraph is a very simple mail statistics RRDtool frontend for Postfix that
produces daily, weekly, monthly and yearly graphs of Postfix's active,
deferred, incoming and bounce queues

%package nginx
Summary: nginx-related control(8) call
Group: Monitoring
Requires: %name-common = %version-%release, nginx

%description nginx
Queuegraph is a very simple mail statistics RRDtool frontend for Postfix that
produces daily, weekly, monthly and yearly graphs of Postfix's active,
deferred, incoming and bounce queues

%prep
%setup -q -n %name
%patch0 -p1

%build

%install
install -d %buildroot%queuegraph_data{,/tmp}

# binaries
install -pD -m0755 queuegraph.cgi %buildroot%_var/www/cgi-bin/%name/%name.cgi
install -pD -m0755 queuegraph-rrd.sh %buildroot%_sbindir/%name-rrd

# .htaccess
install -pD -m0644 %SOURCE1 %buildroot%_var/www/cgi-bin/%name/.htaccess

# cron script
install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/cron.d/%name

# README.ALT
install %SOURCE6 README.ALT

# apache1 config
install -pD -m0644 %SOURCE3 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf

# apache2 configs
install -pD -m0644 %SOURCE9 %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf
install -pD -m0644 %SOURCE8 %buildroot%_sysconfdir/httpd2/conf/mods-start.d/100-%name.conf

# control(8) file
install -pDm0755 %SOURCE7 %buildroot%_controldir/%name

%pre common
%_sbindir/groupadd -r -f %queuegraph_group 2>/dev/null ||:
%_sbindir/useradd -g %queuegraph_group -c 'queuegraph Postfix queue-statistics' \
	-d %queuegraph_data -s /dev/null -r %queuegraph_user 2>/dev/null ||:
# dump facility state before upgrading package
if [ $1 -eq 2 ]; then
        %_sbindir/control-dump %name >/dev/null 2>&1 ||:
fi

%post common
# restore facility state after upgrading package
if [ $1 -eq 2 ]; then
        %_sbindir/control-restore %name >/dev/null 2>&1 ||:
fi

%post apache
%_sbindir/apxs -e -a -n expires %_libdir/apache/mod_expires.so >/dev/null 2>&1 ||:
# set facility at first package install
if [ $1 -eq 1 ]; then
        %_sbindir/control %name apache
fi
%_initdir/httpd condrestart 1>&2
find %queuegraph_data/tmp -mindepth 1 -type d -print0 \
	|xargs -0 rm -rf -- >/dev/null 2>&1 ||:

%post apache2
a2chkconfig
%_initdir/httpd2 reload >/dev/null 2>&1 ||:
# set facility at first package install
if [ $1 -eq 1 ]; then
        %_sbindir/control %name apache2
fi
find %queuegraph_data/tmp -mindepth 1 -type d -print0 \
        |xargs -0 rm -rf -- >/dev/null 2>&1 ||:

%post lighttpd
# set facility at first package install
if [ $1 -eq 1 ]; then
        %_sbindir/control %name lighttpd
fi
find %queuegraph_data/tmp -mindepth 1 -type d -print0 \
	|xargs -0 rm -rf -- >/dev/null 2>&1 ||:

%post nginx
# set facility at first package install
if [ $1 -eq 1 ]; then
        %_sbindir/control %name nginx
fi

%postun apache
%_initdir/httpd reload >/dev/null 2>&1 ||:

%postun apache2
if [ $1 -eq 0 ]; then
        a2chkconfig
        %_initdir/httpd2 reload >/dev/null 2>&1 ||:
fi

%triggerun -n %name-apache -- %name-apache < 1.1-alt3.20070212
%_sbindir/control %name apache

%triggerun -n %name-lighttpd -- %name-lighttpd < 1.1-alt3.20070212
%_sbindir/control %name lighttpd

%files common
%_sbindir/*
%_controldir/%name
%config(noreplace) %_sysconfdir/cron.d/%name
%_var/www/cgi-bin/%name/%name.cgi
%dir %_var/www/cgi-bin/%name
%config(noreplace) %_var/www/cgi-bin/%name/.htaccess
%dir %attr(1771,root,%queuegraph_group) %queuegraph_data
%dir %attr(1775,root,root) %queuegraph_data/tmp
%doc README.ALT

%files apache
%config(noreplace) %_sysconfdir/httpd/conf/addon-modules.d/%name.conf

%files apache2
%_sysconfdir/httpd2/conf/addon.d/A.%name.conf
%_sysconfdir/httpd2/conf/mods-start.d/100-%name.conf

%files lighttpd

%files nginx

%changelog
* Wed Apr 18 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1-alt3.20070212
- Updated to 2007.02.12 version
- Drop unactual %name-counter and %name-createrrd, their functionality located
  now in the queuegraph-rrd file
- Add apache2 support
- Implemented control(8) support for switching permissions of tmp-dir between
  webserwers
- Supress output of `httpd reload` (Closes: #11547)
- Also supress same other output
- Fixed %%name-apache subpackage dependencies (Closes: #11548)
- Updated README.ALT
- Switch to use .gear-tags

* Fri Feb 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1-alt2.20051113
- Added dependency on rrd-utils (Closes: #10415)
- Added lighttpd subpackage
- Enhanced README.ALT

* Wed Mar 15 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1-alt1.20051113
- Initial build for Sisyphus
