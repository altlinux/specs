%define oname removeattachments
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 0.1
Release: alt1

Summary: Roundcube plugin for remove one or more attachments from a message

License: GPLv2
Group: Networking/Mail
Url: https://github.com/mediaversal/Roundcube-Plugin-Remove-Attachments

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/mediaversal/Roundcube-Plugin-Remove-Attachments.git
Source: %name-%version.tar

BuildArch: noarch

Requires: roundcube >= 0.7

%description
This plugin adds an option to remove one or more attachments from a message.

%prep
%setup
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/
rm -rf %buildroot%pluginsdir/%oname/CHANGELOG

%files
%doc README
%pluginsdir/%oname/

%changelog
* Thu Jan 26 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

