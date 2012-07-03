# -*- mode: rpm-spec; coding: utf-8 -*-
Name: modules_lookup
Version: 1.1
Release: alt1

Summary: A small helper to load required modules upon missing device inode lookup
Summary(ru_RU.UTF-8): Вспомогательная утилита для загрузки модулей при обращении к отсутствующему файлу устройства
License: GPL
Group: System/Configuration/Hardware
BuildArch: noarch
Source0: modules_lookup
Source1: modules_lookup.conf

%description
modules_lookup is a small bash script with configurable behaviour
which actually work somewhat similar to devfsd: it loads required
modules and performs other actions when a program tries to access
a missing device inode within /dev. 

Unlike devfsd which works on top of devfs (proclaimed obsoleted),
this script is intended for a patched version of tmpfs, which
supports user-level helper for missing device inodes lookups
(using http://www.uwsg.indiana.edu/hypermail/linux/kernel/0411.0/1568.html)

Be sure you've checked %_sysconfdir/modules_lookup.conf before actual
usage of this script. Author gives no warranty of any kind ;-)

%description -l ru_RU.UTF-8
modules_lookup - это небольшой bash-скрипт с настраиваемым поведением,
который работает сходным с devfsd образом: он загружает требуемые
модули и выполняет другие действия, когда некая программа пытается
обратиться к несуществующему файлу устройства в /dev.

В отличие от devfsd, который работает поверх devfs (объявленной
устаревшей), modules_lookup предназначен для модифицированной версии
tmpfs, поддерживающей вспомогательную "пользовательскую" программу
для отсутствующих файлов устройств (используя 
http://www.uwsg.indiana.edu/hypermail/linux/kernel/0411.0/1568.html)

Перед использованием обязательно убедитесь, что конфигурационный файл
%_sysconfdir/modules_lookup.conf содержит именно те настройки, которые
вы ожидаете получить. Автор не несет за это никакой ответственности :-)

%prep

%install
%__mkdir_p %buildroot{%_sysconfdir,/sbin}
install -m 0755 %SOURCE0 %buildroot/sbin/
install -m 0644 %SOURCE1 %buildroot%_sysconfdir/

%files
%config(noreplace) %_sysconfdir/*.conf
/sbin/*

%changelog
* Tue Mar 29 2005 Alexey Morozov <morozov@altlinux.org> 1.1-alt1
- Added several new modules lookup rules

* Thu Jan 13 2005 Alexey Morozov <morozov@altlinux.org> 1.0-alt1
- Initial build. Actually it's just written ;-)
