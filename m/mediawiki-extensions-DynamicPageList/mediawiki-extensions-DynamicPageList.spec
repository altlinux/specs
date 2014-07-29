%define ShortName DynamicPageList

Name: mediawiki-extensions-%ShortName
Version: 1.7.0
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName
License: GPL

%define mwversion 1.22
# convert version for Source URL (set before Summary:)
%define REL %(echo "REL%mwversion" | sed -e "s|\\.|_|g")

Summary: MediaWiki extension for build a list of pages that are listed in a set of categories

Packager: Vitaly Lipatov <lav@altlinux.ru>


BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= %mwversion

# Source-git: https://git.wikimedia.org/git/mediawiki/extensions/intersection.git
Source: %name-%version.tar

%description
DynamicPageList is a MediaWiki extension which allows wiki users to
create a list of pages that are listed in a set of categories.

%prep
%setup

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files

%changelog
* Tue Jul 29 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- initial build for ALT Linux Sisyphus
