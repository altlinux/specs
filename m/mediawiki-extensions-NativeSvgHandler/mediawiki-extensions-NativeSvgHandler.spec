%define oname NativeSvgHandler
%define mwversion 1.46
%define commit 66cb1d1
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.5.0
Release: alt1

Summary: Allows SVG files to be served directly to clients

License: GPL-3.0-only
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
The NativeSvgHandler extension allows SVG files
to be served directly to clients for client-side rendering.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,package-lock.json,composer.lock}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- update to REL1_46 snapshot 66cb1d1 (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- initial build for ALT Sisyphus
