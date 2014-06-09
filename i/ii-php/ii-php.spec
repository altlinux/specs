Name: ii-php
Version: 0.3
Release: alt1

Summary: Simply implementation of ii server, written on PHP
Summary(ru_RU.UTF-8): Простая реализация серверной части ii, написанная на PHP

Group: Networking/WWW
License: CC0
Url: https://github.com/vit1-irk/ii-php

Source: %name-%version.tar

Requires: php-engine webserver-common
BuildPreReq: rpm-build-webserver-common

BuildArch: noarch
Packager: Pavel Isopenko <pauli@altlinux.org>
%description
II is a russian-speaking FIDO-like distributed messaging network. For details look at http://ii.51t.ru

%description -l ru_RU.UTF-8
ii - это русская фидообразная сеть для обмена сообщениями, подробно узнать о ней вы можете на сайте http://ii.51t.ru.
В пакете находится простенькая php реализация серверной части ii. Для начала работы рядом со скриптами надо создать каталоги echo и msg. В файле ii-functions.php есть функция msg_to_ii, вызывая которую на своём сайте, вы можете писать сообщения в ii.

%prep
%setup

%install
mkdir -p %buildroot%webserver_webappsdir
cp -r ../%name-%version %buildroot%webserver_webappsdir/%name
mkdir -p %buildroot%webserver_webappsdir/%name/echo
mkdir -p %buildroot%webserver_webappsdir/%name/msg

%post

%files
%doc README.md
%dir %webserver_webappsdir/%name/
%webserver_webappsdir/%name/*.php
#%config(noreplace) %webserver_webappsdir/%name/.htaccess

%changelog
* Mon Jun 09 2014 Pavel Isopenko <pauli@altlinux.org> 0.3-alt1
- Initial build for Sisyphus

