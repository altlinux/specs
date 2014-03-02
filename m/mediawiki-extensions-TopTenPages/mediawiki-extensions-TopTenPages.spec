%define ShortName TopTenPages

Name: mediawiki-extensions-%ShortName
Version: 0.3.2
Release: alt1

Summary: Shows the most popular Pages within an article

License: GPL
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.2

Requires: mediawiki-common >= 1.19

# http://www.mediawiki.org/wiki/Extension:TopTenPages/Code
Source: %ShortName-%version.tar

%description
Shows the most popular Pages within an article.

%prep
%setup -n %ShortName-%version

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files


%changelog
* Sun Mar 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt1
- update to 0.3.1

* Sun May 27 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
