%define ShortName ImageMap
%define major 1.15
%define revision r48578

Name: mediawiki-extensions-%ShortName
Version: %major.%revision
Release: alt2

BuildArch: noarch

Group: Networking/WWW
Summary: ImageMap is an extension which allows clickable image maps
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: No license specified

Requires: mediawiki-common >= 1.15.1-alt4
Requires: /usr/bin/convert php5-dom

# what with - in version?
#Source0: http://upload.wikimedia.org/ext-dist/%ShortName-MW%major-%revision.tar
Source0: %ShortName-%version.tar

%description
ImageMap is an extension which allows clickable image maps. An image
map is a list of coordinates in a specific image, which hyperlinks
areas of the image to multiple destinations (in contrast to a normal
image link, in which the entire area of the image links to a single
destination). For example, a map of the world may have each country
hyperlinked to further information about that country. The intention of
an image map is to provide an easy way of linking various parts of an
image without dividing the image into separate image files.

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
* Mon Jan 18 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r48578-alt2
- fix requires

* Mon Jan 18 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r47297-alt1
- initial build for ALT Linux Sisyphus

