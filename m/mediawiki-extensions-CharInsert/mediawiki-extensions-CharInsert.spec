%define ShortName CharInsert
%define major 1.15
%define revision r47913

Name: mediawiki-extensions-%ShortName
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: Create JavaScript character insert boxes
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

Requires: mediawiki-common >= 1.15.1-alt4

# what with - in version?
#Source0: http://upload.wikimedia.org/ext-dist/%ShortName-MW%major-%revision.tar
Source0: %ShortName-%version.tar

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
* Mon Feb 01 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r47913-alt1
- initial build for ALT Linux Sisyphus
