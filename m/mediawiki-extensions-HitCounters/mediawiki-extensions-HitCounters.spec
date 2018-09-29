%define ShortName HitCounters

Name: mediawiki-extensions-%ShortName
Version: 0.3
Release: alt1

Summary: Mediawiki hit counters (removed since Mediawiki 1.25)

License: GPL
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.2

Requires: mediawiki-common >= 1.19

# Source-url: https://github.com/wikimedia/mediawiki-extensions-HitCounters/archive/master.tar.gz
Source: %ShortName-%version.tar

%description
Mediawiki hit counters (removed since Mediawiki 1.25).

%prep
%setup -n %ShortName-%version

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files


%changelog
* Sat Sep 29 2018 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Linux Sisyphus
