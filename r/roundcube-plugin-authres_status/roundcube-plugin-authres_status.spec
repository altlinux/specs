%define oname authres_status
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname
Version: 0.7.2
Release: alt1

Summary: Roundcube plugin to show the verification status of Authentication-Results

License: GPL-3.0-or-later
Group: Networking/Mail
Url: https://github.com/pimlie/authres_status

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/pimlie/authres_status/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

Requires: roundcube >= 1.7

%description
Roundcube plugin which checks the Authentication-Results headers of emails
(DKIM, SPF, DMARC, ARC) and displays the verification status when reading
a message and optionally as a column in the message list.

%prep
%setup
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/
rm -rv %buildroot%pluginsdir/%oname/{tests,phpcs.xml,phpunit.xml}
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
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt1
- initial build for Sisyphus
