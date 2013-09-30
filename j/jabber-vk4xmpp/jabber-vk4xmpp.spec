Name: jabber-vk4xmpp
Version: 0.20130929
Release: alt1

Summary: VKontakte jabber transport

License: MIT
Group: System/Servers
Url: http://jawiki.ru/Vk4xmpp

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Git: https://github.com/mrDoctorWho/vk4xmpp.git
Source: %name-%version.tar
Source1: %name.init

BuildArch: noarch

# FIXME: how to fix find-requires?
Requires: python-modules-sqlite3 python-module-xmpp

%description
VKontakte jabber transport

%prep
%setup
# remove Windows related code
rm -vf library/dns/win32dns.py

%install
chmod 0755 gateway.py
mkdir -p %buildroot%_datadir/%name/
cp -a * %buildroot%_datadir/%name/

# create conf in normal place
mkdir -p %buildroot%_sysconfdir/%name/
cp Config_example.txt %buildroot%_sysconfdir/%name/vk4xmpp.conf
ln -s %_sysconfdir/%name/vk4xmpp.conf %buildroot%_datadir/%name/Config.txt

install -D %SOURCE1 %buildroot%_initddir/%name

%files
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/vk4xmpp.conf
%_initddir/%name
%_datadir/%name/

%changelog
* Mon Sep 30 2013 Vitaly Lipatov <lav@altlinux.ru> 0.20130929-alt1
- initial build for ALT Linux Sisyphus

