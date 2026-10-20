%define oname persistent_login
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 5.3.0
Release: alt1

Summary: Roundcube Persistent Login Plugin (Remember Me)

License: GPL-3.0-or-later
Group: Networking/Mail
Url: https://github.com/mfreiholz/persistent_login

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/mfreiholz/persistent_login.git
Source: %name-%version.tar

BuildArch: noarch

Requires: roundcube >= 1.7

%description
This server-side plugin is useful for all Roundcube users who don't like
to log into their mail account each time they open their browser. The
plugin stores a persistent login cookie which automatically logs the
user in the next time he or she visits the Roundcube web mailer

%prep
%setup
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/
# the plugin settings live in /etc/roundcube/plugins/%oname/
mkdir -p %buildroot%_sysconfdir/roundcube/plugins/%oname/
mv %buildroot%pluginsdir/%oname/config.inc.php.dist %buildroot%_sysconfdir/roundcube/plugins/%oname/config.inc.php
ln -s %_sysconfdir/roundcube/plugins/%oname/config.inc.php %buildroot%pluginsdir/%oname/config.inc.php

%files
%pluginsdir/%oname/
%dir %_sysconfdir/roundcube/plugins/
%dir %_sysconfdir/roundcube/plugins/%oname/
%config(noreplace) %_sysconfdir/roundcube/plugins/%oname/config.inc.php

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 5.3.0-alt1
- new version 5.3.0 (merge upstream git, tag version-5.3.0)
- move the config to /etc/roundcube/plugins/persistent_login/

* Thu Feb 23 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

