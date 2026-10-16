%define oname DynamicPageList
%define mwversion 1.46
%define commit dc16342
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: MediaWiki extension for build a list of pages that are listed in a set of categories

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/intersection-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
DynamicPageList is a MediaWiki extension which allows wiki users to
create a list of pages that are listed in a set of categories.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- update to REL1_46 snapshot dc16342 (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- the source is the intersection repository (DynamicPageList was renamed and archived upstream), extension and directory name stay DynamicPageList
- version follows the MediaWiki version (extension.json says 1.7.0)
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Sun Feb 13 2022 Vitaly Lipatov <lav@altlinux.ru> 1.37-alt1
- new version (1.37) with rpmgs script
- switch to MW version

* Fri May 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1.1
- new version (1.7.0) with rpmgs script

* Tue Jul 29 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- initial build for ALT Linux Sisyphus
