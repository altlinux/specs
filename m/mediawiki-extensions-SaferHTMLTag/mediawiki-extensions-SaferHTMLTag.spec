%define oname SaferHTMLTag
%define mwversion 1.46
%define commit b359765e4438c9686eb4f6e03eda66e80d3bc69b
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 0.4
Release: alt1

Summary: MediaWiki extension that restricts editing of pages with the raw html tag

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://github.com/Wikimedica/mediawiki-extensions-SaferHTMLTag/archive/%commit.tar.gz
Source: %oname-%version.tar

%description
SaferHTMLTag prevents unauthorized users from editing pages where the <html>
tag is used when raw html ($wgRawHtml) is enabled. Only users with the
edit-html right (granted to sysop by the package) can save such pages, and
obfuscated ways of producing the tag (parser functions, #tag) are detected too.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,composer.json}
subst "4i\$wgGroupPermissions['sysop']['edit-html'] = true;" %buildroot%_mediawiki_settings_dir/50-%oname.php

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- initial build for Sisyphus
