%define ShortName Dia

Name: mediawiki-extensions-%ShortName
Version: 1.11
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: Allows Dia diagrams to be rendered inside MediaWiki pages
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPLv2

Requires: mediawiki-common >= 1.15.1-alt4

Source: http://tools.wikimedia.de/~daniel/misc/Dia.tar

%description
The Dia extension allows Dia diagrams to be embedded/rendered inside
MediaWiki pages. It can be used to have thumbnails of specified size to
be automatically generated from the uploaded .dia files. (If no size is
given, then the nominal size will be used.)

%prep
%setup -n Dia

%install
mkdir -p %buildroot%_datadir/mediawiki/extensions/%ShortName
mkdir -p %buildroot%_datadir/mediawiki/config/LocalSettings.d
install -m 0644 * %buildroot%_datadir/mediawiki/extensions/%ShortName/
cat > %buildroot%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php << EOF
<?php

require_once("\$IP/extensions/%ShortName/%ShortName.php");

# The nominal width of a Dia file when rendered to png (default: 300px).
# $wgDIANominalSize

# Don't scale a Dia file larger than this (default: 1024px).
# $wgDIAMaxSize

?>
EOF

%files
%_datadir/mediawiki/extensions/%ShortName
%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php

%changelog
* Fri Aug 10 2012 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- initial build for ALT Linux Sisyphus

