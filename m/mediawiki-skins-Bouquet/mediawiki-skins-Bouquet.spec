%define oname Bouquet
%define mwversion 1.46
%define commit 472bab8
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-skins-%oname
Version: 1.46
Release: alt1

Summary: Bouquet skin for MediaWiki

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Skin:Bouquet

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7
# colour themes (tigerlily...) are loaded by Extension:Theme
Requires: mediawiki-extensions-Theme

# Source-url: https://extdist.wmflabs.org/dist/skins/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
Bouquet is a colourful MediaWiki skin based on the Automattic's
Bouquet theme for WordPress. It comes with three colour themes
(forgetmenot, pinkdogwood, tigerlily), which are selected with
Extension:Theme ($wgDefaultTheme, ?usetheme=); it is installed with the skin.

The skin is enabled by %_mediawiki_settings_dir/50-%oname.php,
select it with ?useskin=bouquet or in the user preferences.

%prep
%setup -n %oname-%version

%install
mkdir -p %buildroot%_mediawikidir/skins/%oname/
cp -a * %buildroot%_mediawikidir/skins/%oname/
# remove development files
rm -rv %buildroot%_mediawikidir/skins/%oname/{Gruntfile.js,package.json,package-lock.json,composer.json,CODE_OF_CONDUCT.md,gitinfo.json}

mkdir -p %buildroot%_mediawiki_settings_dir/
cat >%buildroot%_mediawiki_settings_dir/50-%oname.php <<EOF2
<?php

wfLoadSkin( '%oname' );

EOF2

%files
%_mediawikidir/skins/%oname/
%_mediawiki_settings_dir/50-%oname.php

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for Sisyphus (REL1_46 snapshot 472bab8, MediaWiki 1.46)
