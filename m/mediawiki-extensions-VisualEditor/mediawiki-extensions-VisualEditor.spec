%define ShortName VisualEditor

Name: mediawiki-extensions-%ShortName
Version: 0.1.0
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName
License: MIT

%define mwversion 1.23
# convert version for Source URL (set before Summary:)
%define REL %(echo "REL%mwversion" | sed -e "s|\\.|_|g")

Summary: Integrates VisualEditor into MediaWiki for editing pages as rich content

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= %mwversion

# Source-git: https://git.wikimedia.org/git/mediawiki/extensions/VisualEditor.git
Source: %name-%version.tar

%description
The VisualEditor project aims to create a reliable rich-text editor for the Web and for MediaWiki.

%prep
%setup

# remove tests on ruby
rm -rf modules/ve-mw/test/

%install
%mediawiki_ext_install 50 %ShortName


%files -f %ShortName.files

%changelog
* Sat Feb 21 2015 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- initial build for ALT Linux Sisyphus
