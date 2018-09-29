%define ShortName TopTenPages

Name: mediawiki-extensions-%ShortName
Version: 0.4.0
Release: alt1

Summary: Shows the most popular Pages within an article

License: GPL
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.2

Requires: mediawiki-common >= 1.19

Requires: mediawiki-extensions-HitCounters

# http://www.mediawiki.org/wiki/Extension:TopTenPages/Code
# Source-url: https://github.com/wikimedia/mediawiki-extensions-TopTenPages/archive/master.tar.gz
Source: %ShortName-%version.tar

%description
Shows the most popular Pages within an article.

%prep
%setup -n %ShortName-%version

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files


%changelog
* Sat Sep 29 2018 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- new version (0.4.0) with rpmgs script

* Sun Mar 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt1
- update to 0.3.1

* Sun May 27 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
