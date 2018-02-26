%define ShortName OpenID
%define major 1.16
%define revision r66255

Name: mediawiki-extensions-%ShortName
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: Allow users with accounts on other OpenID-enabled sites to log in
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

Requires: mediawiki-common >= 1.16.0-alt1

Requires: php5-openid > 2.0.1-alt1

# what with - in version?
#Source0: http://upload.wikimedia.org/ext-dist/%ShortName-MW%major-%revision.tar
Source0: %ShortName-%version.tar

%description
The extension lets users log in with an OpenID (http://www.openid.net/)
instead of a username and password. An OpenID is a special URL that
people can use to log in to a Web site. The extension also lets users
who have an account on the wiki log in to other OpenID-aware Web sites
with their wiki user page as their OpenID.

%prep
%setup -n %ShortName-%version

%install
mkdir -p %buildroot%_datadir/mediawiki/extensions/%ShortName
mkdir -p %buildroot%_datadir/mediawiki/config/LocalSettings.d
cp -a * %buildroot%_datadir/mediawiki/extensions/%ShortName/ 
cat > %buildroot%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php << EOF
<?php

require_once("\$IP/extensions/%ShortName/%ShortName.php");

?>
EOF

%files
%_datadir/mediawiki/extensions/%ShortName
%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php

%changelog
* Wed Mar 02 2011 Vitaly Lipatov <lav@altlinux.ru> 1.16.r66255-alt1
- A snapshot of version r66255 of the OpenID extension for MediaWiki 1.16.x

* Mon Feb 01 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r48532-alt1
- initial build for ALT Linux Sisyphus
