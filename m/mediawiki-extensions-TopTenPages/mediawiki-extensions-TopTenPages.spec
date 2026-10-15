%define ShortName TopTenPages
%setup_mediawiki_ext 1.46 %ShortName

Name: mediawiki-extensions-%ShortName
Version: 0.4.0
Release: alt2

Summary: Shows the most popular Pages within an article

License: GPL
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-build-mediawiki >= 0.6

Requires: mediawiki-extensions-HitCounters >= 0.4

# Source-url: https://github.com/wikimedia/mediawiki-extensions-TopTenPages/archive/refs/heads/%MWREL.tar.gz
Source: %ShortName-%version.tar

%description
Shows the most popular Pages within an article.

%prep
%setup -n %ShortName-%version

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt2
- update to REL1_46 branch (compatible with MediaWiki 1.46)
- require mediawiki-common >= 1.46
- added BuildRequires(pre): rpm-build-mediawiki >= 0.6 (for %setup_mediawiki_ext, replaces BuildPreReq)

* Sat Sep 29 2018 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- new version (0.4.0) with rpmgs script

* Sun Mar 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt1
- update to 0.3.1

* Sun May 27 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
