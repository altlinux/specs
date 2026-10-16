%define oname Collection
%define mwversion 1.46
%define commit 7b9996d
%define defphp php%php_defver
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: Collects a number of pages. Collections can be edited, persisted and optionally retrieved as PDF, ODF or DocBook (XML)

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
This extension allows a user to organize personal selections of pages in a collection. Collections can be
* edited and structured using chapters
* persisted, loaded and shared
* rendered as PDF (see Extension:PDF_Writer)
* exported as ODF Text Document (see Extension:OpenDocument_Export)
* exported as DocBook XML (see Extension:XML_Bridge)
* ordered as a printed book at http://pediapress.com/

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json,composer.lock}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- update to REL1_46 snapshot 7b9996d (MediaWiki 1.46) (closes: #60922)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- version follows the MediaWiki version (extension.json says 1.8.0)
- release without the commit (the commit is only in the Source-url and here)
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Thu Jan 29 2026 Vitaly Lipatov <lav@altlinux.ru> 1.40-alt2.d3c0c1b
- use php_defver macro instead of hardcoded php8.1

* Sat Aug 12 2023 Vitaly Lipatov <lav@altlinux.ru> 1.40-alt1.d3c0c1b
- new version (1.40) with rpmgs script
- switch to php8.1 (ALT bug 46922)

* Mon Mar 04 2019 Vitaly Lipatov <lav@altlinux.ru> 1.32-alt1
- new version 1.32

* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 1.22-alt1
- new version 1.22 (with rpmrb script)

* Mon Sep 09 2013 Vitaly Lipatov <lav@altlinux.ru> 1.21.6bbedcf-alt1
- new version 1.21.6bbedcf (with rpmrb script)

* Tue Jul 13 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r62858-alt2
- add php5-curl requires (ALT bug #23749)

* Sat Feb 27 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r62858-alt1
- new version (1.15.r62858) import in git

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r48763-alt1
- initial build for ALT Linux Sisyphus
