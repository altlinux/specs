%define oname sauserprefs
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 0.20111204
Release: alt1

Summary: Roundcube Webmail SAUserPrefs

License: GPL2
Group: Networking/Mail
Url: http://wiki.apache.org/spamassassin/UsingSQL

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %oname-%version.tar

BuildArch: noarch

Requires: roundcube >= 0.7.1

%description
This plugin adds the ability for users to edit they SpamAssassin user prefs
from within Roundcube. It interacts with preferences storied in a database via
SQL.

%prep
%setup -n %oname-%version

%build
find -type f -print0 | xargs -0 chmod a-x

%install

mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/
rm -rf %buildroot%pluginsdir/%oname/CHANGELOG

%files
%doc README
%pluginsdir/%oname/

%changelog
* Fri Mar 23 2012 Vitaly Lipatov <lav@altlinux.ru> 0.20111204-alt1
- initial build for ALT Linux Sisyphus

