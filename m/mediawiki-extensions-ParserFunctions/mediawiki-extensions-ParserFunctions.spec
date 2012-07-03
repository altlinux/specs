%define ShortName ParserFunctions
%define major 1.15
%define revision r50579

Name: mediawiki-extensions-%ShortName
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: ParserFunctions extension enhances parser with logical functions
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL2 or Any OSI approved license

Requires: mediawiki-common >= 1.15.1-alt4

# what with - in version?
#Source0: http://upload.wikimedia.org/ext-dist/%ShortName-MW%major-%revision.tar
Source0: %ShortName-%version.tar

%description
The ParserFunctions extension provides ten additional parser functions
to supplement the "magic words", which are already present in MediaWiki.

%prep
%setup -n %ShortName-%version

%install
mkdir -p %buildroot%_datadir/mediawiki/extensions/%ShortName
mkdir -p %buildroot%_datadir/mediawiki/config/LocalSettings.d
install -m 0644 *.php *.txt %buildroot%_datadir/mediawiki/extensions/%ShortName/ 
cat > %buildroot%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php << EOF
<?php

require_once("\$IP/extensions/%ShortName/%ShortName.php");

?>
EOF

%files
%_datadir/mediawiki/extensions/%ShortName
%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php

%changelog
* Mon Jan 18 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r50579-alt1
- initial build for ALT Linux Sisyphus

