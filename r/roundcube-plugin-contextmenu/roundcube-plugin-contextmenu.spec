%define oname contextmenu
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname
Version: 3.3.1
Release: alt1

Summary: Context Menu roundcube plugin

License: GPL-3.0-or-later
Group: Networking/Mail
Url: https://github.com/johndoh/roundcube-contextmenu

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/johndoh/roundcube-contextmenu/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

Requires: roundcube >= 1.7

%description
Adds context menus to the message list, folder list and address book. Menu
includes the abilities mark messages as read/unread, delete, reply
and forward.

%prep
%setup
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/

%files
%pluginsdir/%oname/

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt1
- new version 3.3.1 (import release tarballs from GitHub)
- fix License tag (upstream is GPL-3.0-or-later), require roundcube 1.7

* Thu Jan 12 2012 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- new version 1.8 (with rpmrb script)

* Tue Oct 19 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
