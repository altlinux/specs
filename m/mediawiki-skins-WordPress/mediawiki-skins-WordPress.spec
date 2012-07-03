%define ShortName WordPress

Name: mediawiki-skins-%ShortName
Version: 0.1
Release: alt3
BuildArch: noarch

Group: Networking/WWW
Summary: WordPress skin for MediaWiki
Summary(ru_RU.UTF-8): Тема для MediaWiki, имитирующая WordPress
Url: http://www.redaktionundalltag.de/index.php?id=174
License: Unknown
Packager: Michael A. Kangin <prividen@altlinux.org>

Requires: mediawiki-common >= 1.15.1-alt4

Source0: %ShortName-%version.tgz

%description
This can be used as a skin for MediaWiki (tested in version 1.11)
to model the look and feel of WordPress - as it can be found on the
documentation website of WordPress at: http://codex.wordpress.org/Main_Page
The implementation is not 100%% percent correct, since we tried to
include more of the original MediaWiki functionality in the CSS file.

%prep
%setup -n %ShortName-%version

%build

%install
mkdir -p %buildroot%_datadir/mediawiki/skins
cp -r * %buildroot%_datadir/mediawiki/skins/
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete


%files
%_datadir/mediawiki/skins/*

%changelog
* Thu Jan 07 2010 Michael A. Kangin <prividen@altlinux.org> 0.1-alt3
- Remove some wasted files

* Thu Dec 31 2009 Michael A. Kangin <prividen@altlinux.org> 0.1-alt2
- Fix requires

* Mon Sep 14 2009 Michael A. Kangin <prividen@altlinux.org> 0.1-alt1
- Initial build



