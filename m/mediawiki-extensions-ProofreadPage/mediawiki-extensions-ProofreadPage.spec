%define oname ProofreadPage
%define mwversion 1.46
%define commit 7b34246
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: The Proofread Page extension can render scanned images

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
The Proofread Page extension can render a book either as a column
of OCR text beside a column of scanned images, or broken into its
logical organization (such as chapters or poems) using transclusion.
The extension is intended to allow easy comparison of text to the
original and allow rendering of a text in several ways without duplicating
data. Since the pages are not in the main namespace, they are not included
in the statistical count of text units.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json,composer.lock}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- update to REL1_46 snapshot 7b34246 (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- version follows the MediaWiki version (extension.json has no version)
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 1.22-alt1
- new version (1.22) with rpmgs script

* Sat Apr 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1.20-alt1
- new version (1.20 compatible)

* Thu Sep 15 2011 Vitaly Lipatov <lav@altlinux.ru> 1.16.r66814-alt1
- new version (1.16.r66814) with rpmgs script

* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r48711-alt1
- initial build for ALT Linux Sisyphus
