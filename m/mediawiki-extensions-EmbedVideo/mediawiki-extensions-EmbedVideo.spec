%define oname EmbedVideo
%define mwversion 1.46
%setup_mediawiki_ext %mwversion %oname
%define defphp php%php_defver

Name: mediawiki-extensions-%oname
Version: 4.2.0
Release: alt2

Summary: MediaWiki extension which adds a parser function called #ev for embedding video clips

License: MIT
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:EmbedVideo

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7
BuildRequires(pre): rpm-build-php
# the extension checks the curl PHP extension at load time (not an autodependency)
Requires: %defphp-curl

# Source-url: https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/archive/refs/tags/v%version.tar.gz
Source: %oname-%version.tar

%description
The EmbedVideo Extension is a MediaWiki extension which adds a parser function
called #ev for embedding video clips from over 22 popular video sharing services
in multiple languages and countries.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,package.json,package-lock.json}

%files -f %oname.files

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt2
- fix "EmbedVideo requires curl PHP extension" in update.php: added Requires on the curl PHP extension of the default PHP (as in other mediawiki extensions)
- added BuildRequires: rpm-build-php (php_defver macro)

* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt1
- new version 4.2.0 (StarCitizenWiki fork, requires MediaWiki 1.43+)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Sun Jul 24 2022 Vitaly Lipatov <lav@altlinux.ru> 3.0.8-alt1
- new version 3.0.8 (with rpmrb script)

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt1
- new version (2.9.0) with rpmgs script

* Sun Sep 14 2014 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- initial build for ALT Linux Sisyphus
