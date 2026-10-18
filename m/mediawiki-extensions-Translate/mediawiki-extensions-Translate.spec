%define oname Translate
%define mwversion 1.46
%define commit db85a40
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: MediaWiki extension to translate pages and messages

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:Translate

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# extension.json requires UniversalLanguageSelector
Requires: mediawiki-extensions-UniversalLanguageSelector >= 1.46

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
Translate is a MediaWiki extension for translating wiki pages (the
<translate> markup, Special:PageTranslation) and the messages of
software and documentation, with a translation interface, translation
memory, message groups, statistics and import/export of many file
formats.

The bundled composer vendor directory (mustangostang/spyc YAML parser and
the composer autoloader) comes with the snapshot.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json,composer.json,composer.lock,Doxyfile,jsdoc.json,sonar-project.properties}

%files -f %oname.files

%changelog
* Sat Oct 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for Sisyphus (REL1_46 snapshot db85a40, MediaWiki 1.46)
