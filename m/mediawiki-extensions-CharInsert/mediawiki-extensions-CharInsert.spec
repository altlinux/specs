%define oname CharInsert
%define mwversion 1.46
%define commit e8c32a5
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: Create JavaScript character insert boxes

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
CharInsert is an extension that creates JavaScript links that when
clicked, insert predefined text into the text box.  These links are
usually used in MediaWiki:Edittools system message (for an example,
see Wikipedia:MediaWiki:Edittools).

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- update to REL1_46 snapshot e8c32a5 (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- version follows the MediaWiki version (extension.json has no version)
- install with %%mediawiki_ext_install (wfLoadExtension)
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Sun Oct 13 2013 Vitaly Lipatov <lav@altlinux.ru> 1.21-alt1
- new version (1.21) with rpmgs script

* Mon Feb 01 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r47913-alt1
- initial build for ALT Linux Sisyphus
