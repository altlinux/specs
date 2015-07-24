Name: nagios-plugins-check-mem
Version: 0.1
Release: alt4

Summary: Nagios(R) plug-in for check memory status on remote host
Summary(ru_RU.UTF-8): Плагин nagios для проверки состояния ОЗУ на удалённом хосте

License: GPL
Group: Monitoring
Url: http://wiki.etersoft.ru/Nagios-plugins

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: http://git.etersoft.ru:/people/lav/packages/nagios-plugins-check-mem.git
Source: %name-%version.tar

BuildArchitectures: noarch

# nagios uses /usr/lib for plugins in any arch
%define plugindir %_libexecdir/nagios/plugins

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
* Fri Jul 24 2015 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt4
- cleanup spec
- add fixes from Oct 17 2011

* Fri Aug 30 2013 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt3
- build for ALT Linux Sisyphus

* Mon Oct 17 2011 Dmitriy Shestakov <mid@etersoft.ru> 0.1-alt2.1
- rewrite in pure sh, fix some dependences

* Thu Oct 13 2011 Dmitriy Shestakov <mid@etersoft.ru> 0.1-alt2
- fix order of input variables

* Thu Oct 13 2011 Dmitriy Shestakov <mid@etersoft.ru> 0.1-alt1
- init commit

