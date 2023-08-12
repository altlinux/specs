%define ShortName Collection
%define mwversion 1.40
%setup_mediawiki_ext %mwversion %ShortName
%define commit d3c0c1b
%define defphp php8.1

Name: mediawiki-extensions-%ShortName
Version: %mwversion
Release: alt1.%commit

Group: Networking/WWW
Summary: Collects a number of pages. Collections can be edited, persisted and optionally retrieved as PDF, ODF or DocBook (XML)
Url: http://www.mediawiki.org/wiki/Extension:Collection

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPLv2

BuildArch: noarch

BuildRequires(pre): rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.22

Requires: %defphp-curl

# Source-url: https://extdist.wmflabs.org/dist/extensions/%ShortName-%MWREL-%commit.tar.gz
Source: %name-%version.tar

%description
This extension allows a user to organize personal selections of pages in a collection. Collections can be
* edited and structured using chapters
* persisted, loaded and shared
* rendered as PDF (see Extension:PDF_Writer)
* exported as ODF Text Document (see Extension:OpenDocument_Export)
* exported as DocBook XML (see Extension:XML_Bridge)
* ordered as a printed book at http://pediapress.com/

%prep
%setup

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files

%changelog
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
