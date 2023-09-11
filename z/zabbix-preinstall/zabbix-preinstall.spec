Name: zabbix-preinstall
Version: 2.2.2
Release: alt2.4

Summary: One-time initialization for Zabbix server
License: GPL
Group: Monitoring

Url: http://altlinux.org/zabbix
Source: %name-%version.tar
BuildArch: noarch

Requires: zabbix-server-mysql zabbix-phpfrontend-apache2-mod_php8.1

%description
This package contains scripts to initialize Zabbix server:
- zabbix-init.sh: create and populate zabbix db;
- zabbix-allowcfg.sh: run before last setup step to allow configuration;
- zabbix-lockdown.sh: run upon saving configuration file.

%prep
%setup

%build

%install
mkdir -p %buildroot%_sbindir
cp -a zabbix-*.sh %buildroot%_sbindir

%files
%_sbindir/*

# TODO:
# - support other DB/frontend types?

%changelog
* Mon Sep 11 2023 Alexei Takaseev <taf@altlinux.org> 2.2.2-alt2.4
- Change Req: zabbix-phpfrontend-apache2-mod_php8.0 to zabbix-phpfrontend-apache2-mod_php8.1

* Wed May 24 2023 Alexei Takaseev <taf@altlinux.org> 2.2.2-alt2.3
- Change Req: zabbix-phpfrontend-apache2-mod_php7 to zabbix-phpfrontend-apache2-mod_php8.0

* Tue Sep 22 2020 Pavel Vasenkov <pav@altlinux.org> 2.2.2-alt2.2
- Set database path (closes: #37465)

* Tue Mar 05 2019 Alexei Takaseev <taf@altlinux.org> 2.2.2-alt2.1
- Change Req: zabbix-phpfrontend-apache2-mod_php5 to zabbix-phpfrontend-apache2-mod_php7

* Fri Apr 11 2014 Michael Shigorin <mike@altlinux.org> 2.2.2-alt2
- added specific zabbix db/frontend combo deps (closes: #29983)

* Wed Apr 09 2014 Michael Shigorin <mike@altlinux.org> 2.2.2-alt1
- initial release

