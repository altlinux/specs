%define oname markasjunk2
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 1.3
Release: alt1

Summary: Mark as Junk 2 roundcube plugin

License: GPL2
Group: Networking/Mail
Url: http://www.tehinterweb.co.uk/roundcube/#pimarkasjunk2

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.tehinterweb.co.uk/roundcube/plugins/%oname.tar

BuildArch: noarch

#Requires: pear-Net_Sieve >= 1.3.0
Requires: roundcube >= 0.4

Provides: roundcube-%oname
Obsoletes: roundcube-%oname

%description
Adds a new button to the mailbox toolbar to mark the selected messages as
Junk/Not Junk, optionally detaching original messages from spam reports if
the message is not junk and learning junk/not junk using various methods
(sa-learn, etc.).

%prep
%setup -n %oname

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/
rm -rf %buildroot%pluginsdir/%oname/CHANGELOG

%files
%doc README
%pluginsdir/%oname/

%changelog
* Mon Dec 12 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- initial build for ALT Linux Sisyphus

