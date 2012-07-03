%define ShortName MistyLook

Name: mediawiki-skins-%ShortName
Version: 0.1
Release: alt2
BuildArch: noarch

Group: Networking/WWW
Summary: MistyLook skin for MediaWiki
Summary(ru_RU.UTF-8): Симпатичная тема для MediaWiki, имитирующая одноимённую тему WordPress.
Url: http://ninecoldwinters.com/code/mistylook-skin-mediawiki/
License: Unknown
Packager: %packager

Requires: mediawiki-common >= 1.15.1-alt4

Source0: %ShortName-%version.tgz

%description
This can be used as a skin for MediaWiki.

%prep
%setup -n %ShortName-%version

%build

%install
mkdir -p %buildroot%_datadir/mediawiki/skins
cp -r * %buildroot%_datadir/mediawiki/skins/

%files
%_datadir/mediawiki/skins/*

%changelog
* Thu Dec 31 2009 Michael A. Kangin <prividen@altlinux.org> 0.1-alt2
- Release for Sisyphus

* Mon Dec 07 2009 Andrey Bergman <vkni@altlinux.org> 0.1-alt1
- initial build.

