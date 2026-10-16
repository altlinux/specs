%define oname SecureHTML
%define mwversion 1.46
%define commit ca352e4
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 3.0
Release: alt3

Summary: This MediaWiki extension provides a secure way to include raw HTML code on a page

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
This extension allows editors to add HTML section(s) or pages on a wiki page.
This extension can only be used on protected pages,
but allows an editor to add a protected template on an unprotected, editable page.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,package-lock.json}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt3
- update to REL1_46 snapshot ca352e4 (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- switched to the extdist snapshot
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Thu Oct 31 2019 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt2
- drop StubManager require 

* Mon May 14 2018 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- new version (3.0) with rpmgs script

* Wed May 26 2010 Vitaly Lipatov <lav@altlinux.ru> 2.3.0.r1223-alt1
- initial build for ALT Linux Sisyphus
