%define oname ddnotes
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname
Version: 1.0.10
Release: alt1

Summary: DonDominio Notes, a Roundcube notes plugin storing notes in the database

License: Apache-2.0 and MIT and (Apache-2.0 or MPL-2.0) and OFL-1.1 and CC-BY-4.0
Group: Networking/Mail
Url: https://github.com/dondominio/ddnotes

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/dondominio/ddnotes/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
# DOMPurify 3.4.17 and marked 18.1.1 instead of the bundled DOMPurify 2.2.2 and marked 2.0.3 (upstream PR dondominio/ddnotes: pending)
Patch: ddnotes-update-dompurify-marked.patch

BuildArch: noarch

Requires: roundcube >= 1.7

%description
Roundcube plugin to manage notes within the mailbox. The notes (text,
markdown or html, uploaded PDF files and images) are saved directly in the
Roundcube database. The SQL schemas are in %pluginsdir/ddnotes/SQL/.

%prep
%setup
%patch -p1
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/
# only the css and webfonts of fontawesome are used
rm -rv %buildroot%pluginsdir/%oname/includes/fontawesome/{svgs,sprites,metadata,js,less,scss}
find %buildroot%pluginsdir/%oname -name '*.map' -print -delete
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
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.10-alt1
- initial build for Sisyphus
