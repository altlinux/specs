%define ShortName Math
%define mwversion 1.31
%setup_mediawiki_ext %mwversion %ShortName
# can we exclude it?
%define commit a1263db

Name: mediawiki-extensions-%ShortName
Version: 3.0.0.%mwversion
Release: alt1.%commit

Summary: Math extension provides support for rendering mathematical formulas on-wiki

License: GPLv2
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:Math

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source-git: https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Math.git
# Source-url: https://extdist.wmflabs.org/dist/extensions/Math-%MWREL-%commit.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-mediawiki >= 0.6

# for default math rendering service
Requires: php7-curl

%description
Math extension provides support for rendering mathematical formulas
on-wiki via texvc. It was a part of the core MediaWiki software until
MediaWiki 1.18, r85706.

%prep
%setup

%build

%install
# remove build files
rm -f $(cat .gitignore | grep -v "^#.*")
%__subst "s|^\$wgTexvc =.*|\$wgTexvc = '%_bindir/texvc';|g" Math.php

%mediawiki_ext_install 50 %ShortName

rm -rfv %buildroot%mediawiki_ext_dir/{texvccheck,math,tests,mathoid,modules/ve-math/tools}

%files -f %ShortName.files

%changelog
* Tue Jul 31 2018 Vitaly Lipatov <lav@altlinux.ru> 3.0.0.1.31-alt1.a1263db
- build new version
- set noarch, drop texvc subpackage (ALT bug #34734)

* Thu Aug 21 2014 Vitaly Lipatov <lav@altlinux.ru> 1.24-alt1
- new build

* Sat Oct 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.r22a09c87d3895-alt2
- fixes for real work (adopted to MW 1.18)

* Sat Oct 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.r22a09c87d3895-alt1
- initial build for ALT Linux Sisyphus

