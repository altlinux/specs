%define ShortName EmbedVideo

Name: mediawiki-extensions-%ShortName
Version: 2.1.3
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName
License: GPL

%define mwversion 1.22
# convert version for Source URL (set before Summary:)
%define REL %(echo "REL%mwversion" | sed -e "s|\\.|_|g")

Summary: MediaWiki extension which adds a parser function called #ev for embedding video clips

Packager: Vitaly Lipatov <lav@altlinux.ru>


BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= %mwversion

# Source-git: https://github.com/Alexia/mediawiki-embedvideo
Source: %name-%version.tar

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
* Sun Sep 14 2014 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- initial build for ALT Linux Sisyphus
