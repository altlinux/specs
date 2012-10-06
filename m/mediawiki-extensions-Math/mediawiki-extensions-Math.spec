%define ShortName Math
%define major 1.0
%define revision r22a09c87d3895

Name: mediawiki-extensions-%ShortName
Version: %major.%revision
Release: alt2

#BuildArch: noarch

Group: Networking/WWW
Summary: Math extension provides support for rendering mathematical formulas on-wiki via texvc
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPLv2

Requires: mediawiki-common >= 1.15.1-alt4

Requires: /usr/bin/latex /usr/bin/dvipng
# due cancel.sty
Requires: texlive-latex-recommended

#Source: https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Math.git
Source0: %name-%major.tar

BuildPreReq: rpm-build-mediawiki >= 0.3

# Automatically added by buildreq on Sat Oct 06 2012
BuildRequires: ocaml

%description
Math extension provides support for rendering mathematical formulas
on-wiki via texvc. It was a part of the core MediaWiki software until
MediaWiki 1.18, r85706. See also the related bug, bug #14202 on Bugzilla.

Uncomment in config for 1.18 follow lines, and comment out config of the package
$wgUseTeX           = true;
$wgTexvc = "/usr/bin/texvc";

See also http://www.mediawiki.org/wiki/Manual:Enable_TeX/problems

For debug:
$wgDebugComments= true;
$wgDebugLogFile = "/tmp/log_info.txt";


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
%__subst "s|^\$wgTexvc =.*|\$wgTexvc = '%_bindir/texvc';|g" Math.php
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files
%_bindir/texvc*

%changelog
* Sat Oct 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.r22a09c87d3895-alt2
- fixes for real work (adopted to MW 1.18)

* Sat Oct 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.r22a09c87d3895-alt1
- initial build for ALT Linux Sisyphus

