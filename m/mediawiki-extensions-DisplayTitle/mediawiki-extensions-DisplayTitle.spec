%define oname DisplayTitle
%define mwversion 1.46
%define commit 4e41492
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: MediaWiki extension to override the displayed page title

License: MIT
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:Display_Title

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
Display Title is a MediaWiki extension which allows overriding the
displayed title of a page (in links, category lists and the page heading)
using the {{DISPLAYTITLE:}} magic word or the "displaytitle" page property,
including titles which differ from the page name beyond capitalization.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json,composer.json}

%files -f %oname.files

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for Sisyphus (REL1_46 snapshot 4e41492, MediaWiki 1.46)
