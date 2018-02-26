%define oname copymessage
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 1.0
Release: alt1

Summary: Copy Message (Context Menu extension) roundcube plugin

License: GPL2
Group: Networking/Mail
Url: http://roundcube.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.tehinterweb.co.uk/roundcube/plugins/%oname.tar
Patch: %name-ru.patch

BuildArch: noarch

Requires: roundcube >= 0.4

Requires: roundcube-plugin-contextmenu

%description
Adds a copy message option to the context menu,
allowing messages to be copied to another folder.

%prep
%setup -n %oname
%patch
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/

%files
%pluginsdir/%oname/

%changelog
* Tue Oct 19 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus

