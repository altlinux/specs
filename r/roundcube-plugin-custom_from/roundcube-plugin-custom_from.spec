%define oname custom_from
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 1.1
Release: alt1

Summary: Custom From RoundCube plugin

License: GPL2
Group: Networking/Mail
Url: http://trac.roundcube.net/wiki/Plugin_Repository

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://remi.caput.fr/data/document/custom_from.tar

BuildArch: noarch

Requires: roundcube >= 0.6

%description
This plugin adds a blue button to the compose screen, next to the identities
selection dropdown. By clicking it, a textbox will replace the dropdown,
allowing you to enter whatever you want as sender value (it must be a valid
"From:" header field value, though).

When replying to an e-mail sent to you through an address not in your
identities list, plugin will automatically fire and set "From:" header to the
address the original e-mail was sent to.

%prep
%setup -n %oname

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/
rm -rf %buildroot%pluginsdir/%oname/lib
rm -rf %buildroot%pluginsdir/%oname/CHANGELOG

%files
%doc README
%pluginsdir/%oname/

%changelog
* Thu Feb 23 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Sisyphus

