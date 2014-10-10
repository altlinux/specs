%define ShortName MwEmbedSupport

Name: mediawiki-extensions-%ShortName
Version: 0.3.0
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: Mediawiki extension for support for mwEmbed modules and extensions
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL2

BuildPreReq: rpm-build-mediawiki >= 0.2
BuildPreReq: rpm-build-intro
Requires: mediawiki-common >= 1.15.1-alt4

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://git.wikimedia.org/zip/?r=mediawiki/extensions/%ShortName&h=REL1_23&format=zip
Source: %name-%version.tar

%description
The MwEmbedSupport extension adds support for mwEmbed modules and extensions.
It was previously known as JS2Support. This extension solely supports other
extensions (such as TimedMediaHandler).

%prep
%setup
%remove_repo_info

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files

%changelog
* Fri Oct 10 2014 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- initial build for ALT Linux Sisyphus
