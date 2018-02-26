%define ShortName SearchSuggest

Name: mediawiki-extensions-%ShortName
Version: 0.2
Release: alt2
BuildArch: noarch

Group: Networking/WWW
Summary: Ajax-based Search Suggest that places results below search bar.
Summary(ru_RU.UTF-8): Расширение для поиска в mediawiki, по мере ввода показывает найденные результаты.
Url: http://www.mediawiki.org/wiki/Extension:Search_Suggest
License: Public domain
Packager: Michael A. Kangin <prividen@altlinux.org>

Requires: mediawiki-common >= 1.15.1-alt4

Source0: %ShortName-%version.tgz

%description
This extension takes the idea of MediaWiki's built-in Ajax search, and makes it
much more useful. It places the search results directly under the search bar,
and does not take over the content (like the built in feature does). 
The search looks for the word (or whatever you are looking for) within the
article names, and not just at the beginning by default.

%prep
%setup -n %ShortName-%version

%build

%install

mkdir -p %buildroot%_datadir/mediawiki/extensions/%ShortName
mkdir -p %buildroot%_datadir/mediawiki/config/LocalSettings.d
install -m 0644 %ShortName.* %buildroot%_datadir/mediawiki/extensions/%ShortName/ 
cat > %buildroot%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php << EOF
<?php

require_once("\$IP/extensions/%ShortName/%ShortName.php");

?>
EOF

%files
%_datadir/mediawiki/extensions/%ShortName
%_datadir/mediawiki/config/LocalSettings.d/50-%ShortName.php

%changelog
* Wed Dec 30 2009 Michael A. Kangin <prividen@altlinux.org> 0.2-alt2
- Adopt for new Mediawiki config layout
- Link to CSS and JS instead include them into documents
- Fix search in binary-encoded MySQL tables

* Wed Jul 22 2009 Michael A. Kangin <prividen@altlinux.org> 0.2-alt1
- Initial release


