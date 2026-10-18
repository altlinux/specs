%define oname UniversalLanguageSelector
%define mwversion 1.46
%define commit 584a24c
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: MediaWiki extension to select the interface language and the input method

License: GPL-2.0-or-later OR MIT
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:UniversalLanguageSelector

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
The Universal Language Selector (ULS) is a MediaWiki extension which allows
users to select a language and configure its support in an easy way. The
interface language can be chosen from a searchable list (and is guessed from
the browser), and the input methods (jquery.ime) and web fonts are provided
for many languages. It is a required extension for Translate.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json,composer.json,composer.lock,bundlesize.config.json,rollup.config.js,scripts}

%files -f %oname.files

%changelog
* Sat Oct 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for Sisyphus (REL1_46 snapshot 584a24c, MediaWiki 1.46)
