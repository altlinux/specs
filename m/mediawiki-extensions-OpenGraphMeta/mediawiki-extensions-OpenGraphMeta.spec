%define oname OpenGraphMeta
%define mwversion 1.46
%define commit 24159f8
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 0.6
Release: alt1
Serial: 1

Summary: OpenGraphMeta provides OpenGraph protocol metadata for articles on the wiki for 3rd parties like Facebook to extract

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
OpenGraphMeta provides OpenGraph protocol metadata for articles on the wiki
for 3rd parties like Facebook to extract. The primary use for this extension
is for any wiki that provides its users a button to "Like" pages on the wiki,
especially if the wiki uses a custom default skin.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,package-lock.json}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1:0.6-alt1
- update to REL1_46 snapshot 24159f8 (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- Serial: 1 (0.6 is lower than the old 0.2012)
- converted to the extension.json format and the tarball import scheme
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Sat Feb 02 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2012-alt1
- initial build for ALT Linux Sisyphus
