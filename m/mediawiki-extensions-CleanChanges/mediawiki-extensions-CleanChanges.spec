%define oname CleanChanges
%define mwversion 1.46
%define commit 909a1d6
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: Enhanced grouped view of recent changes

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
CleanChanges is an extension that provides an alternative, grouped
view of Special:RecentChanges (the "enhanced" changes list, usenewrc):
edits are grouped by page and by date, with an optional trailer filter
($wgCCTrailerFilter) and a user filter ($wgCCUserFilter).

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{vendor,Gruntfile.js,package.json,package-lock.json,composer.json,composer.lock}

%files -f %oname.files

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for Sisyphus
