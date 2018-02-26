%define ShortName Poem
%define major 1.15
%define revision r47297

Name: mediawiki-extensions-%ShortName
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: The Poem extension allows for easy inclusion of poems and similar material in MediaWiki pages
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: No license specified

Requires: mediawiki-common >= 1.15.1-alt4

# what with - in version?
#Source0: http://upload.wikimedia.org/ext-dist/%ShortName-MW%major-%revision.tar
Source0: %ShortName-%version.tar

%description
The Poem extension allows for easy inclusion of poems and similar material
in MediaWiki pages, by simply putting them between <poem></poem> tags,
instead of adding <br> to the end or : to the beginning of every line,
which is common practice now. Though small, it might be useful, especially
on Wikisource or similar projects (there are poems with thousands of
lines, so obviously current solution isn't practical). The extension
preserves wikilinks, bolding, etc. if they are present in the poem,
as well as indenting lines which start with spaces.

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
* Mon Jan 18 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r47297-alt1
- initial build for ALT Linux Sisyphus

