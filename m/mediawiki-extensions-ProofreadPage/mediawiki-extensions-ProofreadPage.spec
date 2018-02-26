%define oname ProofreadPage
%define major 1.16
%define revision r66814

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: The Proofread Page extension can render scanned images
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.16

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://upload.wikimedia.org/ext-dist/%oname-MW%major-%revision.tar.gz
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
* Thu Sep 15 2011 Vitaly Lipatov <lav@altlinux.ru> 1.16.r66814-alt1
- new version (1.16.r66814) with rpmgs script

* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r48711-alt1
- initial build for ALT Linux Sisyphus
