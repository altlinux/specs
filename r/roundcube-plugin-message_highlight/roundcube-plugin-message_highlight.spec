%define oname message_highlight
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname
Version: 4.4
Release: alt1

Summary: Roundcube plugin to color messages in the list by rules

License: GPL-2.0-only
Group: Networking/Mail
Url: https://github.com/corbosman/message_highlight

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/corbosman/message_highlight/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

Requires: roundcube >= 1.7

%description
Roundcube plugin which assigns colors to messages in the message list
based on the Subject, Sender, Recipient or CC.

%prep
%setup
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/
# the plugin settings live in /etc/roundcube/plugins/%oname/
mkdir -p %buildroot%_sysconfdir/roundcube/plugins/%oname/
mv %buildroot%pluginsdir/%oname/config.inc.php-dist %buildroot%_sysconfdir/roundcube/plugins/%oname/config.inc.php
ln -s %_sysconfdir/roundcube/plugins/%oname/config.inc.php %buildroot%pluginsdir/%oname/config.inc.php

%files
%pluginsdir/%oname/
%dir %_sysconfdir/roundcube/plugins/
%dir %_sysconfdir/roundcube/plugins/%oname/
%config(noreplace) %_sysconfdir/roundcube/plugins/%oname/config.inc.php

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 4.4-alt1
- initial build for Sisyphus
