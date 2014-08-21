%define ShortName Math
%define major 1.24

Name: mediawiki-extensions-%ShortName
Version: %major
Release: alt1

#BuildArch: noarch

Group: Networking/WWW
Summary: Math extension provides support for rendering mathematical formulas on-wiki
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPLv2

Requires: mediawiki-common >= 1.23


#Source: https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Math.git
Source0: %name-%major.tar

BuildPreReq: rpm-build-mediawiki >= 0.3

# Automatically added by buildreq on Sat Oct 06 2012
BuildRequires: ocaml

%description
Math extension provides support for rendering mathematical formulas
on-wiki via texvc. It was a part of the core MediaWiki software until
MediaWiki 1.18, r85706.

%package texvc
Summary: Math extension provides support for rendering mathematical formulas on-wiki via texvc
Requires: %name = %version-%release
Group: Development/Other

Requires: /usr/bin/latex /usr/bin/dvipng
# due cancel.sty
Requires: texlive-latex-recommended

%description texvc
Math extension provides support for rendering mathematical formulas on-wiki via texvc.

%prep
%setup -n %name-%major

%build
cd math
make

%install
mkdir -p %buildroot%_bindir/
cd math
cp texvc texvc_test texvc_tex %buildroot%_bindir/
# remove build files
rm -f $(cat .gitignore | grep -v "^#.*")
cd ..
cd texvccheck
make
cd ..
%__subst "s|^\$wgTexvc =.*|\$wgTexvc = '%_bindir/texvc';|g" Math.php
%mediawiki_ext_install 50 %ShortName

rm -rf %buildroot%_mediawikidir/extensions/Math/texvccheck/
rm -rf %buildroot%_mediawikidir/extensions/Math/math/{*.*,Makefile}
rm -rf %buildroot%_mediawikidir/extensions/Math/tests/

%files -f %ShortName.files

%files texvc
%_bindir/texvc*

%changelog
* Thu Aug 21 2014 Vitaly Lipatov <lav@altlinux.ru> 1.24-alt1
- new build

* Sat Oct 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.r22a09c87d3895-alt2
- fixes for real work (adopted to MW 1.18)

* Sat Oct 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.r22a09c87d3895-alt1
- initial build for ALT Linux Sisyphus

