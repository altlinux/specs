%define oname CSS
%define mwversion 1.46
%define commit 19c5af3
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: MediaWiki extension to add CSS to pages with the #css parser function

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:CSS

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
The CSS extension allows adding CSS rules to a wiki page with the {{#css:}}
parser function, either as inline rules or as a reference to a CSS page
in the wiki or to a stylesheet file.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# libraries are provided by mediawiki core (same versions)
rm -rv %buildroot%mediawiki_ext_dir/vendor
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json,composer.json,composer.lock}

%files -f %oname.files

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for Sisyphus (REL1_46 snapshot 19c5af3, MediaWiki 1.46)
