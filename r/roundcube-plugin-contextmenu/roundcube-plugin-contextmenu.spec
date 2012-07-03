%define oname contextmenu
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 1.8
Release: alt1

Summary: Context Menu roundcube plugin

License: GPL2
Group: Networking/Mail
Url: http://roundcube.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.tehinterweb.co.uk/roundcube/plugins/%oname.tar

BuildArch: noarch

Requires: roundcube >= 0.7.0

%description
Adds context menus to the message list, folder list and address book. Menu
includes the abilities mark messages as read/unread, delete, reply
and forward.

%prep
%setup -n %oname
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/
rm -f %buildroot%pluginsdir/%oname/CHANGELOG

%files
%pluginsdir/%oname/

%changelog
* Thu Jan 12 2012 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- new version 1.8 (with rpmrb script)

* Tue Oct 19 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
