%define fuser _vk4xmpp

Name: jabber-vk4xmpp
Version: 0.20160725
Release: alt2

Summary: VKontakte jabber transport

License: MIT
Group: System/Servers
Url: http://jawiki.ru/Vk4xmpp

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Git: https://github.com/mrDoctorWho/vk4xmpp.git
Source: %name-%version.tar
Source1: %name.init
Source2: %name.conf

AutoReq: yes,noperl,nosymlinks

BuildArch: noarch

# FIXME: how to fix find-requires?
Requires: python-modules-sqlite3 python-module-xmpp python-module-simplejson

%description
VKontakte jabber transport

%prep
%setup

%install
chmod 0755 gateway.py
mkdir -p %buildroot/var/lib/%name/
mkdir -p %buildroot%_datadir/%name/
cp -a * %buildroot%_datadir/%name/
rm -rf %buildroot%_datadir/%name/{DEBIAN,init.d,systemd,README.md,Makefile}

# create conf in normal place
mkdir -p %buildroot%_sysconfdir/%name/
cp %SOURCE2 %buildroot%_sysconfdir/%name/vk4xmpp.conf
%__subst "s|users.db|/var/lib/%name/users.db|g" %buildroot%_sysconfdir/%name/vk4xmpp.conf
# we set it via --config arg too
ln -s %_sysconfdir/%name/vk4xmpp.conf %buildroot%_datadir/%name/Config.txt

mkdir -p %buildroot%_runtimedir/%name/
mkdir -p %buildroot%_logdir/%name/crash/

ln -s %_runtimedir/%name/%name.pid %buildroot%_datadir/%name/pidFile.txt
ln -s %_logdir/%name/%name.log %buildroot%_datadir/%name/vk4xmpp.log
ln -s %_logdir/%name/crash %buildroot%_datadir/%name/crash
ln -s /var/lib/%name/users.db %buildroot%_datadir/%name/users.db

install -D %SOURCE1 %buildroot%_initddir/%name
install -D systemd/vk4xmpp.service %buildroot%_unitdir/%name

%pre
/usr/sbin/useradd -r -d %_datadir/%name -s /dev/null -c '%summary' %fuser >/dev/null 2>&1 ||:

%files
%doc README.md
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/vk4xmpp.conf
%_initddir/%name
%_unitdir/%name
%_datadir/%name/
%dir %attr (0770,%fuser,root) /var/lib/%name/
%dir %attr (0770,%fuser,root) %_logdir/%name/
%dir %attr (0770,%fuser,root) %_logdir/%name/crash/
%dir %attr (0770,%fuser,root) %_runtimedir/%name/

%changelog
* Tue Aug 30 2016 Vitaly Lipatov <lav@altlinux.ru> 0.20160725-alt2
- add alt adopted conf file
- fix config for ALT Linux

* Mon Jul 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.20160725-alt1
- update to 20160725

* Fri Sep 05 2014 Vitaly Lipatov <lav@altlinux.ru> 0.20140903-alt1
- update to 20140903

* Mon Sep 30 2013 Vitaly Lipatov <lav@altlinux.ru> 0.20130929-alt1
- initial build for ALT Linux Sisyphus

