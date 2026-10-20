%define oname removeattachments
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 0.3.1
Release: alt1

Summary: Roundcube plugin for remove one or more attachments from a message

License: GPL-3.0-or-later
Group: Networking/Mail
Url: https://github.com/dsoares/roundcube-removeattachments

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/dsoares/roundcube-removeattachments.git
Source: %name-%version.tar

BuildArch: noarch

Requires: roundcube >= 1.7

%description
This plugin adds an option to remove one or more attachments from a message.

%prep
%setup
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/

%files
%doc README.md
%pluginsdir/%oname/

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- new version 0.3.1 (merge upstream git, tag 0.3.1)

* Fri Feb 12 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.9-alt1
- build fork from Diana Soares for RoundCube 1.1
- add russian localization

* Thu Jan 26 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

