Name: nagios-plugins-check-mem
Version: 0.1
Release: alt3

Summary: Nagios(R) plug-in for check memory status on remote host
Summary(ru_RU.UTF-8): Плагин nagios для проверки состояния ОЗУ на удалённом хосте

License: GPL
Group: Monitoring
#Url: 

#Packager: Dmitriy Shestakov <mid@etersoft.ru>

Source: %name-%version.tar

BuildArchitectures: noarch

# nagios uses /usr/lib for plugins in any arch
%define plugindir %_prefix/lib/nagios/plugins

%description
Nagios plugin for check memory status on remote host through snmp written on bash.

%description -l UTF-8
Плагин nagios для проверки состояния ОЗУ на удалённом хосте по протоколу snmp.

%prep
%setup

%install
mkdir -p %buildroot%plugindir/
install -m755 check_mem %buildroot%plugindir/

%files
%plugindir/check_mem

%changelog
* Fri Aug 30 2013 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt3
- build for ALT Linux Sisyphus

* Thu Oct 13 2011 Dmitriy Shestakov <mid@etersoft.ru> 0.1-alt2
- fix order of input variables

* Thu Oct 13 2011 Dmitriy Shestakov <mid@etersoft.ru> 0.1-alt1
- init commit

