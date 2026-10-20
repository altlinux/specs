%define oname listcommands
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname
Version: 2.5.2
Release: alt1

Summary: Roundcube plugin to show mailing list commands

License: GPL-2.0-only
Group: Networking/Mail
Url: https://github.com/corbosman/listcommands

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/corbosman/listcommands/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Patch: listcommands-php8-undefined-key.patch

BuildArch: noarch

Requires: roundcube >= 1.7

%description
Roundcube plugin which shows the List-* headers of mailing list messages
(subscribe, unsubscribe, post, archive, help) as links in the message view.

%prep
%setup
find -type f -print0 | xargs -0 chmod a-x
%patch -p1

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/

%files
%pluginsdir/%oname/

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 2.5.2-alt1
- initial build for Sisyphus
