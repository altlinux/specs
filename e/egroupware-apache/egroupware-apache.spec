%define httpdconfdir %_sysconfdir/httpd2/conf/sites-available

Name: egroupware-apache
Version: 19.1
Release: alt2

Summary: EGroupware CE Apache configuration
Summary(ru_RU.UTF-8): Конфигурация Apache для EGroupware CE

Group: Networking/WWW
License: GPLv2
Url: https://github.com/EGroupware/egroupware

Source: %name-%version.tar
Requires: apache2 apache2-mod_php7 egroupware

BuildArch: noarch
Packager: Pavel Isopenko <pauli@altlinux.org>
Summary: Apache web-server configuration for EGroupware
Summary(ru_RU.UTF-8): Конфигурация веб-сервера Apache для EGroupware

%description
EGroupWare is a web-based groupware suite written in php. Package contains Apache2 web-server config for EGgroupware CE (Community Edition).
%description -l ru_RU.UTF-8
EGroupware - система организации групповой работы, написанная на PHP. Пакет содержит настройки веб-сервера Apache2
 и зависит от пакета egroupware. Таким образом, этого пакета достаточно для полной установки EGroupware CE (Community Edition) 

%prep
%setup

%install
mkdir -p %buildroot%httpdconfdir
cp egroupware.conf %buildroot%httpdconfdir
mkdir -p %buildroot%_sysconfdir/cron.d
cp egroupware %buildroot%_sysconfdir/cron.d

%files
%config %attr(644,root,root) %httpdconfdir/egroupware.conf
%_sysconfdir/cron.d/egroupware

%post
a2ensite egroupware
service httpd2 condreload

%preun
a2dissite egroupware

%postun
service httpd2 condreload

%changelog
* Fri May 08 2020 Pavel Isopenko <pauli@altlinux.org> 19.1-alt2
- add postun condreload

* Tue Mar 31 2020 Pavel Isopenko <pauli@altlinux.org> 19.1-alt1
- initial build for Sisyphus





