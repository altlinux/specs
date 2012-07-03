%define ShortName TopTenPages

Name: mediawiki-extensions-%ShortName
Version: 0.2
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: Shows the most popular Pages within an article
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

Requires: mediawiki-common >= 1.15.1-alt4

# http://www.mediawiki.org/wiki/Extension:TopTenPages/Code
Source: %ShortName-%version.tar

%description
Shows the most popular Pages within an article.

%prep
%setup -n %ShortName-%version

%install
mkdir -p %buildroot%_datadir/mediawiki/extensions/%ShortName
mkdir -p %buildroot%_datadir/mediawiki/config/LocalSettings.d

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
* Sun May 27 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
