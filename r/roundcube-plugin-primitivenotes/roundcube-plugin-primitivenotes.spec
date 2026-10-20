%define oname primitivenotes
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname
Version: 2.3.4
Release: alt1

Summary: Simple notes plugin for Roundcube

License: AGPL-3.0-only
Group: Networking/Mail
Url: https://codeberg.org/Offerel/roundcube_primitivenotes

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://codeberg.org/Offerel/roundcube_primitivenotes/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

Requires: roundcube >= 1.7

%description
A deadly simple notes plugin for Roundcube. The notes are stored in the
IMAP account of the user.

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
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt1
- initial build for Sisyphus
