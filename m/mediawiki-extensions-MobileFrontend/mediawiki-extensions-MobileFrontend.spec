%define ShortName MobileFrontend
%define major 1.23
%define revision 85e1f54

Name: mediawiki-extensions-%ShortName
Version: %major.%revision
Release: alt1

Summary: MediaWiki extension providing a mobile front-end to MediaWiki sites

License: GPLv2
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Requires: mediawiki-common >= 1.22


# Source-git: https://git.wikimedia.org/git/mediawiki/extensions/MobileFrontend.git
Source: %name-%version.tar

BuildPreReq: rpm-build-mediawiki >= 0.3

%description
MobileFrontend is a MediaWiki extension providing a mobile front-end to MediaWiki sites.


%prep
%setup

%build

%install
%mediawiki_ext_install 50 %ShortName
rm -rf %buildroot/%_mediawikidir/extensions/%ShortName/tests/

#check
#make tests

%files -f %ShortName.files

%changelog
* Thu Feb 06 2014 Vitaly Lipatov <lav@altlinux.ru> 1.23.85e1f54-alt1
- initial build for ALT Linux Sisyphus
