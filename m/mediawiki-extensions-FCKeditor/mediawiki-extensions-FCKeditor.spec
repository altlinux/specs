%define ShortName FCKeditor
%define webappdir %webserver_webappsdir/mediawiki

Name: mediawiki-extensions-%ShortName
Version: 0.r60520
Release: alt3
BuildArch: noarch

Group: Networking/WWW
Summary: WYSIWYG editor for MediaWiki
Summary(ru_RU.UTF-8): Расширение для визуального редактирования страниц на MediaWiki-сайтах.
Url: http://www.mediawiki.org/wiki/Extension:FCKeditor_(Official)
License: GPL
Packager: Michael A. Kangin <prividen@altlinux.org>

BuildRequires(pre): rpm-macros-apache2
Requires: mediawiki-common >= 1.15.1-alt4 fckeditor-php

Source0: %ShortName-%version.tgz

%description
mediawiki-extensions-FCKeditor enables a more intuitive WYSIWYG editor
(based on fckeditor) when editing pages on a MediaWiki-based site

%prep
%setup -n %ShortName-%version

%build

%install

mkdir -p %buildroot%_datadir/mediawiki/extensions/%ShortName
mkdir -p %buildroot%_datadir/mediawiki/config/LocalSettings.d
mkdir -p %buildroot%webappdir/config
install -m 0644 *.php *.html %buildroot%_datadir/mediawiki/extensions/%ShortName/ 
cp -r css plugins %buildroot%_datadir/mediawiki/extensions/%ShortName/
install -m 0644 fckeditor_config.js %buildroot%webappdir/config/
ln -s %_datadir/fckeditor %buildroot%_datadir/mediawiki/extensions/%ShortName/
ln -s %webappdir/config/fckeditor_config.js %buildroot%_datadir/mediawiki/extensions/%ShortName/


cat > %buildroot%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php << EOF
<?php
 
require_once("\$IP/extensions/%ShortName/%ShortName.php");

?>
EOF

%pre
if [ -f %_datadir/mediawiki/extensions/%ShortName/fckeditor_config.js -a \
! -L %_datadir/mediawiki/extensions/%ShortName/fckeditor_config.js ]; then
   mv %_datadir/mediawiki/extensions/%ShortName/fckeditor_config.js \
   	%_datadir/mediawiki/extensions/%ShortName/fckeditor_config.js.rpmsave &&
   echo "%_datadir/mediawiki/extensions/%ShortName/fckeditor_config.js saved as \
%_datadir/mediawiki/extensions/%ShortName/fckeditor_config.js.rpmsave"
fi

%files
%add_findreq_skiplist %_datadir/mediawiki/extensions/%ShortName/fckeditor
%_datadir/mediawiki/extensions/%ShortName/*.php
%_datadir/mediawiki/extensions/%ShortName/*.html
%_datadir/mediawiki/extensions/%ShortName/fckeditor_config.js
%_datadir/mediawiki/extensions/%ShortName/css
%_datadir/mediawiki/extensions/%ShortName/plugins
%config(noreplace) %webappdir/config/fckeditor_config.js
%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php
%_datadir/mediawiki/extensions/%ShortName/fckeditor

%changelog
* Thu Jan 07 2010 Michael A. Kangin <prividen@altlinux.org> 0.r60520-alt3
- Some config defaults improvement
- Config now in webappdir

* Thu Dec 31 2009 Michael A. Kangin <prividen@altlinux.org> 0.r60520-alt2
- Fix requires

* Thu Dec 31 2009 Michael A. Kangin <prividen@altlinux.org> 0.r60520-alt1
- New release

* Sat Jul 25 2009 Michael A. Kangin <prividen@altlinux.org> 0.r3972-alt1
- Initial release


