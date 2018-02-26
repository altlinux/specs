%define ShortName SyntaxHighlight_GeSHi

Name: mediawiki-extensions-%ShortName
Version: 0.r60508
Release: alt1
BuildArch: noarch

Group: Networking/WWW
Summary: Extension for mediawiki to highlight source code with GeSHi.
Summary(ru_RU.UTF-8): Расширение mediawiki для раскраски синтаксиса исходников с помощью GeSHi.
Url: http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi
License: GPLv2
Packager: Michael A. Kangin <prividen@altlinux.org>

Requires: geshi mediawiki-common >= 1.15.1-alt4

Source0: %ShortName-%version.tgz

%description
The <source> tags allow the display of preformatted code modules but in addition
they add coloring according to the code language settings. Like the <pre> tags
and the <poem> tags, they preserve white space, that is, they depict the code
module exactly as it was typed.

%prep
%setup -n %ShortName-%version

%build

%install

mkdir -p %buildroot%_datadir/mediawiki/extensions/%ShortName
mkdir -p %buildroot%_datadir/mediawiki/config/LocalSettings.d
install -m 0644 *.php %buildroot%_datadir/mediawiki/extensions/%ShortName/ 
ln -s %_datadir/geshi %buildroot%_datadir/mediawiki/extensions/%ShortName/
cat > %buildroot%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php << EOF
<?php

require_once("\$IP/extensions/%ShortName/%ShortName.php");

?>
EOF

%files
%add_findreq_skiplist %_datadir/mediawiki/extensions/%ShortName/geshi
%_datadir/mediawiki/extensions/%ShortName
%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php
%doc README

%changelog
* Wed Dec 30 2009 Michael A. Kangin <prividen@altlinux.org> 0.r60508-alt1
- New version
- Adopt for new Mediawiki config layout

* Sun Jul 19 2009 Michael A. Kangin <prividen@altlinux.org> 0.r53473-alt1
- Initial release

