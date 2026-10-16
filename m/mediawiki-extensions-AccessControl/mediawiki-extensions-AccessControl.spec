%define oname AccessControl
%define mwversion 1.46
%define commit a434f4c
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 6.0
Release: alt1

Summary: Group Based Access Control for MediaWiki

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
Extension to restrict access to specific pages based on groups.

See also description in russian: http://kb.etersoft.ru/%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0:AccessControl_1.1

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,package-lock.json}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 6.0-alt1
- update to REL1_46 snapshot a434f4c (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- dropped Requires: mediawiki-extensions-SpecialNamespaces (6.0 does not use it)
- removed unused patches (not applied since 2.1)
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Sat Apr 27 2013 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- new version 2.1 for 1.20 and above

* Thu Sep 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- add russian translation
- add fixes

* Thu Sep 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Linux Sisyphus
