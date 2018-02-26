%define ShortName Cavendish-MW

Name: mediawiki-skins-%ShortName
Version: 0.1
Release: alt1
BuildArch: noarch

Group: Networking/WWW
Summary: Cavendish-MW skin for MediaWiki

Url: http://sourceforge.net/p/cavendishmw/home/
License: Unknown
Packager: Mike Radyuk <torabora@altlinux.org>

Requires: mediawiki-common >= 1.16.0-alt1

Source: %ShortName-%version.tar

%description
Cavendish-MW (previously Cavendish mod) is a MediaWiki skin that
provides the mozilla.org look and feel. It's an enhanced version of the
Cavendish MediaWiki skin.
The original Cavendish MediaWiki skin has some flaws and is not
compatible with the latest versions of MediaWiki. Cavendish-MW fixes
these issues and has other improvements like a full width template
and updated style sheets.

%prep
%setup -n %ShortName-%version

%build
%install
mkdir -p %buildroot%_datadir/mediawiki/skins
cp -r * %buildroot%_datadir/mediawiki/skins/

%files
%_datadir/mediawiki/skins/*

%changelog
* Thu May 19 2011 Mike Radyuk <torabora@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus
