%define oname messagesize
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 1.2
Release: alt1

Summary: Limit overall message size roundcube plugin

License: GPL2
Group: Networking/Mail
Url: http://www.tehinterweb.co.uk/roundcube/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/JohnDoh/Roundcube-Plugin-Message-Size.git
Source: %name-%version.tar

BuildArch: noarch

Requires: roundcube >= 0.7

%description
This plugin limits the overall size of a message by capping the cumulative size
of all the attachments.

%prep
%setup
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/
rm -rf %buildroot%pluginsdir/%oname/lib
rm -rf %buildroot%pluginsdir/%oname/CHANGELOG

%files
%doc README
%pluginsdir/%oname/

%changelog
* Thu Jan 12 2012 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Linux Sisyphus

