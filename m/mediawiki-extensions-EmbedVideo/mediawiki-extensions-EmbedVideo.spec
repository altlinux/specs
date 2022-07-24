%define ShortName EmbedVideo

Name: mediawiki-extensions-%ShortName
Version: 3.0.8
Release: alt1

Summary: MediaWiki extension which adds a parser function called #ev for embedding video clips

Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName
License: GPLv2

# Source-url: https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-mediawiki >= 0.2


%description
The EmbedVideo Extension is a MediaWiki extension which adds a parser function
called #ev for embedding video clips from over 22 popular video sharing services
in multiple languages and countries.

%prep
%setup

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files

%changelog
* Sun Jul 24 2022 Vitaly Lipatov <lav@altlinux.ru> 3.0.8-alt1
- new version 3.0.8 (with rpmrb script)

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt1
- new version (2.9.0) with rpmgs script

* Sun Sep 14 2014 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- initial build for ALT Linux Sisyphus
