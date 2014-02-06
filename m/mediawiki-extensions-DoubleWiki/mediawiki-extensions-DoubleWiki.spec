%define ShortName DoubleWiki
%define major 1.23
%define revision wmf22

Name: mediawiki-extensions-%ShortName
Version: %major.%revision
Release: alt1

Summary: Allows you to compare wikis in two separate languages side by side

License: GPLv2
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Requires: mediawiki-common >= 1.23


# Source-git: https://git.wikimedia.org/git/mediawiki/extensions/%ShortName.git
Source: %name-%version.tar

BuildPreReq: rpm-build-mediawiki >= 0.3

%description
Allows you to compare wikis in two separate languages side by side.


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
* Thu Feb 06 2014 Vitaly Lipatov <lav@altlinux.ru> 1.23.wmf22-alt1
- initial build for ALT Linux Sisyphus
