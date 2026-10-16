%define oname Math
%define mwversion 1.46
%define commit 1cbf35f
%define defphp php%php_defver
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 3.0.0.1.46
Release: alt1

Summary: Math extension provides support for rendering mathematical formulas on-wiki

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7
BuildRequires(pre): rpm-build-php

Requires: %defphp-curl

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
Math extension provides support for rendering mathematical formulas
on-wiki via texvc.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,mathoid,modules/ve-math/tools,Gruntfile.js,package.json,package-lock.json,composer.lock}
# disable extra reqs
rm -v %buildroot%mediawiki_ext_dir/maintenance/{buildPHPparser.js,downloadMoreTexVCtests.sh}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.0.1.46-alt1
- update to REL1_46 snapshot 1cbf35f (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- dropped Requires: mediawiki (it pulls apache and mysql)
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Thu Jan 29 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.0.1.40-alt2.4cf19b0
- use php_defver macro instead of hardcoded php8.1

* Sat Aug 12 2023 Vitaly Lipatov <lav@altlinux.ru> 3.0.0.1.40-alt1.4cf19b0
- new version (3.0.0.1.40) with rpmgs script
- change requires to php8.1-curl (ALT bug 46923)

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 3.0.0.1.39-alt1.1e7a549
- new version (3.0.0.1.39) with rpmgs script

* Tue Jul 31 2018 Vitaly Lipatov <lav@altlinux.ru> 3.0.0.1.31-alt1.a1263db
- build new version
- set noarch, drop texvc subpackage (ALT bug #34734)

* Thu Aug 21 2014 Vitaly Lipatov <lav@altlinux.ru> 1.24-alt1
- new build

* Sat Oct 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.r22a09c87d3895-alt2
- fixes for real work (adopted to MW 1.18)

* Sat Oct 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.r22a09c87d3895-alt1
- initial build for ALT Linux Sisyphus
