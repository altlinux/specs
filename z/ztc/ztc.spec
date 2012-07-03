%define zabbix_group zabbix

Name: ztc
Version: 10.11.1
Release: alt1.1

Summary: a collection of templates for zabbix monitoring system
License: GPLv3
Group: Monitoring

Url: http://trac.greenmice.info/ztc
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-devel

%setup_python_module %name

%description
ZTC is a collection of templates for zabbix monitoring system.

Intended audience: sysadmins & performance engineers
Purpose: aviability and performance monitoring and alerting for Linux
and *nix boxes

%package templates
Summary: collection of templates for zabbix monitoring system
Group: Monitoring
Provides: zabbix-template-collection = %version-%release
Obsoletes: zabbix-template-collection =< %version-%release

%description templates
%summary

%package -n python-module-%name
Summary: ZTC python module
Group: Monitoring

%description -n python-module-%name
%summary

%package -n python-module-%name-mysql
Summary: ZTC python module (mysql part)
Group: Monitoring

%description -n python-module-%name-mysql
%summary

%package -n python-module-%name-pgsql
Summary: ZTC python module (postgresql part)
Group: Monitoring

%description -n python-module-%name-pgsql
%summary

%package common
Summary: ZTC common part
Group: Monitoring

%description common
%summary

%package apache2
Summary: ZTC UserParameters for monitoring apache2
Group: Monitoring
Requires: %name-common
Requires: zabbix-agent >= 1:1.6.7-alt0.svn.8427.M40.1
Provides: zabbix-userparameters-apache2 = %version-%release
Obsoletes: zabbix-userparameters-apache2 =< %version-%release

%description apache2
%summary

%package nginx
Summary: ZTC UserParameters for monitoring nginx
Group: Monitoring
Requires: %name-common
Requires: zabbix-agent >= 1:1.6.7-alt0.svn.8427.M40.1
Provides: zabbix-userparameters-nginx = %version-%release
Obsoletes: zabbix-userparameters-nginx =< %version-%release

%description nginx
%summary

%package postgresql
Summary: ZTC UserParameters for monitoring postgresql
Group: Monitoring
Requires: %name-common
Requires: zabbix-agent >= 1:1.6.7-alt0.svn.8427.M40.1
# we need pg_buffercache and pg_freespacemap
#Requires: postgresql-contrib #TODO: provide postgresql-contrib in all major versions
Requires: python-module-ztc-pgsql
Provides: zabbix-userparameters-postgresql = %version-%release
Obsoletes: zabbix-userparameters-postgresql =< %version-%release

%description postgresql
%summary

%package slony
Summary: ZTC UserParameters for monitoring slony
Group: Monitoring
Requires: %name-common
Requires: zabbix-agent >= 1:1.6.7-alt0.svn.8427.M40.1
Provides: zabbix-userparameters-slony = %version-%release
Obsoletes: zabbix-userparameters-slony =< %version-%release

%description slony
%summary

%package linux
Summary: ZTC UserParameters for monitoring linux machine
Group: Monitoring
Requires: %name-common
Requires: zabbix-agent >= 1:1.6.7-alt0.svn.8427.M40.1
Provides: zabbix-userparameters-linux = %version-%release
Obsoletes: zabbix-userparameters-linux =< %version-%release

%description linux
%summary

%package mysql
Summary: ZTC UserParameters for monitoring MySQL
Group: Monitoring
Requires: %name-common
Requires: zabbix-agent >= 1:1.6.7-alt0.svn.8427.M40.1
Requires: python-module-ztc-mysql

%description mysql
%summary

%package hw
Summary: ZTC UserParameters for monitoring hardware devices
Group: Monitoring
Requires: %name-common
Requires: zabbix-agent >= 1:1.6.7-alt0.svn.8427.M40.1

%description hw
%summary

%package ovz
Summary: ZTC UserParameters for monitoring openvz CTs
Group: Monitoring
Requires: %name-common
Requires: zabbix-agent >= 1:1.6.7-alt0.svn.8427.M40.1
Requires: zabbix-agent-sudo

%description ovz
%summary

%prep
%setup

%build
%python_build

%install
%python_install

%files templates
%_datadir/ztc/
%doc README* REQUIREMENTS

%files -n python-module-%name
%dir %python_sitelibdir/%name
%python_sitelibdir/%name/*.py*
%python_sitelibdir/%name/vm
%python_sitelibdir/%name/system
%python_sitelibdir/%name/nginx
%python_sitelibdir/%name/apache
%python_sitelibdir/%name/hw
%python_sitelibdir/*.egg-info

%files -n python-module-%name-mysql
%python_sitelibdir/%name/mysql

%files -n python-module-%name-pgsql
%python_sitelibdir/%name/pgsql

%files common
%dir %attr(0750,root,%zabbix_group) %_sysconfdir/ztc

%files apache2
%_bindir/apache*
%config(noreplace) %_sysconfdir/zabbix/zabbix_agentd.conf.d/apache.conf
%config(noreplace)  %attr(0640,root,%zabbix_group) %_sysconfdir/ztc/apache.conf

%files nginx
%_bindir/nginx*
%config(noreplace) %_sysconfdir/zabbix/zabbix_agentd.conf.d/nginx.conf
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/ztc/nginx.conf

%files postgresql
%_bindir/pgsql*
%config(noreplace) %_sysconfdir/zabbix/zabbix_agentd.conf.d/pgsql.conf
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/ztc/pgsql.conf

%files mysql
%_bindir/mysql*
%config(noreplace) %_sysconfdir/zabbix/zabbix_agentd.conf.d/mysql.conf
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/ztc/mysql.conf

%files slony
%config(noreplace) %_sysconfdir/zabbix/zabbix_agentd.conf.d/slony.conf
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/ztc/slony.conf

%files linux
%_bindir/system*
%_bindir/vfs*
%_bindir/vm*
%_bindir/ntp*
%config(noreplace) %_sysconfdir/zabbix/zabbix_agentd.conf.d/linux.conf

%files hw
%_bindir/hw*
%config(noreplace) %_sysconfdir/zabbix/zabbix_agentd.conf.d/hw.conf
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/ztc/hw_raid_3ware.conf

%files ovz
%_bindir/get_beancounters
%config(noreplace) %_sysconfdir/zabbix/zabbix_agentd.conf.d/ovz.conf

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 10.11.1-alt1.1
- Rebuild with Python-2.7

* Thu Dec 09 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 10.11.1-alt1
- Update to 10.11.1.
- Add old UserParameter names for nginx (Closes: #24715).
- Update README.ALT.
- Add manual dependencies on python-module-ztc-{pgsql,mysql}.

* Tue Nov 30 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 10.11-alt2
- Add template and userparametrs for openvz monitoring.

* Wed Nov 17 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 10.11-alt1
- 10.11.
- Rename package from zabbix-template-collection to ztc.

* Wed Dec 02 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 9.9-alt1.svn.58
- Initial build for Sisyphus.

