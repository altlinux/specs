%define ShortName HitCounters
%setup_mediawiki_ext 1.46 %ShortName

Name: mediawiki-extensions-%ShortName
Version: 0.4
Release: alt1

Summary: Mediawiki hit counters (removed since Mediawiki 1.25)

License: GPL
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-build-mediawiki >= 0.6

# Source-url: https://github.com/wikimedia/mediawiki-extensions-HitCounters/archive/refs/heads/%MWREL.tar.gz
Source: %ShortName-%version.tar

%description
Mediawiki hit counters (removed since Mediawiki 1.25).

%prep
%setup -n %ShortName-%version

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- new version 0.4 (REL1_46 branch, compatible with MediaWiki 1.46)
- drop patch (fixed upstream)
- require mediawiki-common >= 1.46
- added BuildRequires(pre): rpm-build-mediawiki >= 0.6 (for %setup_mediawiki_ext, replaces BuildPreReq)

* Fri Jun 11 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3.4-alt1
- new version 0.3.4 (with rpmrb script)

* Sat Sep 29 2018 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Linux Sisyphus
