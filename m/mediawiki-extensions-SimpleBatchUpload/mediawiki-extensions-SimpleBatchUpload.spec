%define oname SimpleBatchUpload
%define mwversion 1.43
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 4.0.0
Release: alt1

Summary: Special:BatchUpload page for uploading many files at once to MediaWiki

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://github.com/ProfessionalWiki/%oname/archive/refs/tags/%version.tar.gz
Source: %oname-%version.tar

%description
SimpleBatchUpload adds the Special:BatchUpload page, which allows
uploading several files at once with a single comment and with
a progress display. It uses the standard MediaWiki upload API,
so the usual upload permissions and checks apply.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
cd %buildroot%mediawiki_ext_dir
rm -rv tests build docs \
	composer.json package.json package-lock.json phpcs.xml phpstan.neon phpstan-baseline.neon \
	phpunit.xml.dist vitest.config.mjs

%files -f %oname.files

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- initial build for Sisyphus
