%define ShortName CheckUser
%define major 1.15
%define revision r48763

Name: mediawiki-extensions-%ShortName
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary:  CheckUser is an extension that allows to check user IP
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

Requires: mediawiki-common >= 1.15.1-alt4

# what with - in version?
#Source0: http://upload.wikimedia.org/ext-dist/%ShortName-MW%major-%revision.tar
Source0: %ShortName-%version.tar

%description
CheckUser is an extension that allows a user (with the checkuser
permission) to check which IPs are used by a given username and which
usernames are used by a given IP, without having to run queries directly
against the database by hand. The extension is running live on all
Wikimedia wikis.

%prep
%setup -n %ShortName-%version

%install
mkdir -p %buildroot%_datadir/mediawiki/extensions/%ShortName
mkdir -p %buildroot%_datadir/mediawiki/config/LocalSettings.d
rm -rf archives
install -m 0644 * %buildroot%_datadir/mediawiki/extensions/%ShortName/ 
cat > %buildroot%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php << EOF
<?php

require_once("\$IP/extensions/%ShortName/%ShortName.php");

?>
EOF

%files
%_datadir/mediawiki/extensions/%ShortName
%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php

%changelog
* Mon Jan 18 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r48763-alt1
- initial build for ALT Linux Sisyphus
