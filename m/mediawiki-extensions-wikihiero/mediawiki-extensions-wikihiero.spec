%define oname wikihiero
%define mwversion 1.46
%define commit 9d316da
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: Hieroglyph rendering extension for MediaWiki

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
The Wikihiero extension renders Egyptian hieroglyphs in MediaWiki pages
using the <hiero> tag.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
rm -rf %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json,composer.lock}

%files -f %oname.files

%changelog
* Wed Oct 28 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for ALT Linux Sisyphus
