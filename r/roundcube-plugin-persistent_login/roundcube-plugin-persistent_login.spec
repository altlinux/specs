%define oname persistent_login
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 0.1
Release: alt1

Summary: Roundcube Persistent Login Plugin (Remember Me)

License: GPLv2
Group: Networking/Mail
Url: http://www.insanefactory.com/roundcube-persistent-login-plugin/


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/mfreiholz/Roundcube-Persistent-Login-Plugin.git
Source: %name-%version.tar

BuildArch: noarch

Requires: roundcube >= 0.7

%description
This server-side plugin is useful for all Roundcube users who don't like
to log into their mail account each time they open their browser. The
plugin stores a persistent login cookie which automatically logs the
user in the next time he or she visits the Roundcube web mailer

%prep
%setup

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/

%files
%pluginsdir/%oname/

%changelog
* Thu Feb 23 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

