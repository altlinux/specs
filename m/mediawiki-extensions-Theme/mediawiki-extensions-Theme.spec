%define oname Theme
%define mwversion 1.46
%define commit 94e5bc6
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: MediaWiki extension to load colour themes of skins

# the main PHP code is public domain, monobook/pink.css and stellarbook.css are GPL-2.0-or-later
License: Public domain and GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:Theme

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
Theme is a MediaWiki extension which allows to use themes (colour
variants) of skins. A skin declares its themes in the ThemeModules
attribute of its skin.json, the theme is chosen by $wgDefaultTheme,
by the user preference or by the ?usetheme= URL parameter, and its
stylesheet module is added to the page. The extension itself ships
themes for Monobook and Vector.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,package-lock.json,composer.json,CODE_OF_CONDUCT.md}

%files -f %oname.files

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for Sisyphus (REL1_46 snapshot 94e5bc6, MediaWiki 1.46)
