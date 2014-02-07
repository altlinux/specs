%define oname ProofreadPage

Name: mediawiki-extensions-%oname
Version: 1.22
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: The Proofread Page extension can render scanned images
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.22

# Source-url: https://codeload.github.com/wikimedia/mediawiki-extensions-ProofreadPage/legacy.tar.gz/REL1_22
Source: %name-%version.tar

%description
The Proofread Page extension can render a book either as a column
of OCR text beside a column of scanned images, or broken into its
logical organization (such as chapters or poems) using transclusion.
The extension is intended to allow easy comparison of text to the
original and allow rendering of a text in several ways without duplicating
data. Since the pages are not in the main namespace, they are not included
in the statistical count of text units.

%prep
%setup

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 1.22-alt1
- new version (1.22) with rpmgs script

* Sat Apr 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1.20-alt1
- new version (1.20 compatible)

* Thu Sep 15 2011 Vitaly Lipatov <lav@altlinux.ru> 1.16.r66814-alt1
- new version (1.16.r66814) with rpmgs script

* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r48711-alt1
- initial build for ALT Linux Sisyphus
