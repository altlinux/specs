%define oname LabeledSectionTransclusion
%define mwversion 1.46
%define commit 04d749f
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: Transclude labeled sections of wiki pages

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
Labeled Section Transclusion provides the section tag and parser functions
for transcluding labeled sections from one wiki page into another.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json}
rm -f %buildroot%mediawiki_ext_dir/composer.lock

%files -f %oname.files

%changelog
* Wed Oct 28 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for ALT Linux Sisyphus
