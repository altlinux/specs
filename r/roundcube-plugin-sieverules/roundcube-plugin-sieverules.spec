%define oname sieverules
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 1.16
Release: alt1

Summary: SieveRules (Managesieve) roundcube plugin

License: GPL2
Group: Networking/Mail
Url: http://roundcube.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.tehinterweb.co.uk/roundcube/plugins/sieverules.tar

BuildArch: noarch

Requires: pear-Net_Sieve >= 1.3.0
Requires: roundcube >= 0.6

Provides: roundcube-%oname
Obsoletes: roundcube-%oname

%description
SieveRules (Managesieve) roundcube plugin.
Adds a 'Filters' tab to the 'Personal Settings' to allow the user to
manage their Sieve mail rules. Uses the Managesieve protocol. Predefined
rules created for the user to select.

%prep
%setup -n %oname
# use Net_Sieve from pear-Net_Sieve
%__subst "s|lib/Net/Sieve.php|Net/Sieve.php|g" %oname.php
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
* Thu Jan 12 2012 Vitaly Lipatov <lav@altlinux.ru> 1.16-alt1
- new version 1.16 (with rpmrb script)

* Tue Oct 19 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt3
- use Net_Sieve from pear-Net_Sieve

* Tue Oct 19 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt2
- rename to roundcube-plugin-sieverules

* Mon Oct 18 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt1
- initial build for ALT Sisyphus

