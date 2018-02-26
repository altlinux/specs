%define ShortName Cite

Name: mediawiki-extensions-%ShortName
Version: 0.r60364
Release: alt1
BuildArch: noarch

Group: Networking/WWW
Summary: Extension for mediawiki that adds citations to pages.
Summary(ru_RU.UTF-8): Расширение mediawiki для создания ссылок
Url: http://www.mediawiki.org/wiki/Extension:Cite/Cite.php
License: Unknown
Packager: Michael A. Kangin <prividen@altlinux.org>

Requires: mediawiki-common >= 1.15.1-alt4

Source0: %ShortName-%version.tgz

%description
Cite.php is a Cite extension that adds two parser hooks to MediaWiki, <ref> and
<references />; these operate together to add citations to pages.

%prep
%setup -n %ShortName-%version

%build

%install

mkdir -p %buildroot%_datadir/mediawiki/extensions/%ShortName
mkdir -p %buildroot%_datadir/mediawiki/config/LocalSettings.d
install -m 0644 *.php cite_text* %buildroot%_datadir/mediawiki/extensions/%ShortName/ 
cat > %buildroot%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php << EOF
<?php

require_once("\$IP/extensions/%ShortName/%ShortName.php");

?>
EOF

%files
%_datadir/mediawiki/extensions/%ShortName
%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php

%changelog
* Fri Dec 25 2009 Michael A. Kangin <prividen@altlinux.org> 0.r60364-alt1
- New release

* Sun Jul 19 2009 Michael A. Kangin <prividen@altlinux.org> 0.r53483-alt1
- Initial release

