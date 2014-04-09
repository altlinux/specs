Name: zabbix-preinstall
Version: 2.2.2
Release: alt1

Summary: One-time initialization for Zabbix server
License: GPL
Group: Monitoring

Url: http://altlinux.org/zabbix
Source: %name-%version.tar
BuildArch: noarch

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

%changelog
* Wed Apr 09 2014 Michael Shigorin <mike@altlinux.org> 2.2.2-alt1
- initial release

