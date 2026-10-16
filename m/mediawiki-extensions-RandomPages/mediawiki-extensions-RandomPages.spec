%define oname RandomPages
%define mwversion 1.46
%define commit 73849b8
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 0.6.0
Release: alt1

Summary: RandomPages adds a new MediaWiki wiki parser for get random pages

License: GPL-3.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar
Patch: %oname-portable-random.patch

%description
RandomPages adds a new MediaWiki wiki parser tag: <randompages />
Available options:
* limit int, to control how many links should be
  fetched randomly from the database, defaults to 150
* namespace bool, true to restrict only to the global namspace, defaults to false
* levels int, levels of CSS applyed to each entry, defaluts to 5

%prep
%setup -n %oname-%version
%patch -p1

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,package-lock.json}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- update to REL1_46 snapshot 73849b8 (MediaWiki 1.46)
- added patch: use random() instead of the MySQL-only rand() (sqlite, PostgreSQL)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- new version (0.6) with rpmgs script - for 1.35

* Fri May 01 2020 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- new version (0.5) with rpmgs script - for 1.34

* Tue Jun 13 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- update version

* Sat Jun 05 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
