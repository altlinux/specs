%define oname Collection
%define major 1.15
#%define dversion MW%major
%define dversion trunk
%define revision r62858

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt2

BuildArch: noarch

Group: Networking/WWW
Summary: Collects a number of pages. Collections can be edited, persisted and optionally retrieved as PDF, ODF or DocBook (XML)
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.15.1-alt4

Requires: php5-curl

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://upload.wikimedia.org/ext-dist/%oname-%dversion-%revision.tar.gz
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

%files -f %oname.files

%changelog
* Tue Jul 13 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r62858-alt2
- add php5-curl requires (ALT bug #23749)

* Sat Feb 27 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r62858-alt1
- new version (1.15.r62858) import in git

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r48763-alt1
- initial build for ALT Linux Sisyphus
