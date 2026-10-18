%define oname LanguageSelector
%define mwversion 1.46
%define commit 49bb668
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: MediaWiki extension to select the interface language from a drop-down list

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:LanguageSelector

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
The LanguageSelector extension adds a language selector (a drop-down list
of languages) to the wiki pages, so that users and anonymous visitors
can choose the interface language. The list of languages is configured
with $wgLanguageSelectorLanguages and related settings.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json,composer.json,bundlesize.config.json,CODE_OF_CONDUCT.md}

%files -f %oname.files

%changelog
* Sat Oct 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for Sisyphus
