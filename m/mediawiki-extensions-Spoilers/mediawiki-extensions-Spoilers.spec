%define oname Spoilers
%define mwversion 1.46
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 2.2.9
Release: alt1

Summary: MediaWiki extension that adds a spoiler tag hiding a block of text

License: MIT
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://github.com/Telshin/Spoilers/archive/refs/tags/%version.tar.gz
Source: %oname-%version.tar

%description
The Spoilers extension adds the <spoiler> tag and the {{#spoiler:}} parser
function that hide a block of text on page load behind a show/hide button.
The button messages can be customized for each spoiler.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,package-lock.json,composer.json}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 2.2.9-alt1
- initial build for Sisyphus
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)
