%define ShortName CharInsert

Name: mediawiki-extensions-%ShortName
Version: 1.21
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: Create JavaScript character insert boxes
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

Requires: mediawiki-common >= 1.15.1-alt4

# Source-url: https://codeload.github.com/wikimedia/mediawiki-extensions-CharInsert/legacy.tar.gz/REL1_21
Source: %ShortName-%version.tar

%description
CharInsert is an extension that creates JavaScript links that when
clicked, insert predefined text into the text box.  These links are
usually used in MediaWiki:Edittools system message (for an example,
see Wikipedia:MediaWiki:Edittools).

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
* Sun Oct 13 2013 Vitaly Lipatov <lav@altlinux.ru> 1.21-alt1
- new version (1.21) with rpmgs script

* Mon Feb 01 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r47913-alt1
- initial build for ALT Linux Sisyphus
