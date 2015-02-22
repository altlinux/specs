%define ShortName PdfHandler

Name: mediawiki-extensions-%ShortName
Version: 1.23
Release: alt1

BuildArch: noarch

License: GPL
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Summary: PdfHandler extension shows uploaded pdf files in a multipage preview layout

Packager: Vitaly Lipatov <lav@altlinux.ru>


BuildPreReq: rpm-build-mediawiki >= 0.3
Requires: mediawiki-common >= 1.23.8

# gs
Requires: ghostscript-classic
# pdfinfo (former xpf-utils)
Requires:  poppler
# convert
Requires: ImageMagick-tools

# Source-git: https://git.wikimedia.org/git/mediawiki/extensions/%ShortName.git
Source: %name-%version.tar

%description
This is the README file for the PdfHandler extension for MediaWiki
software. The extension is only useful if you've got a MediaWiki
installation; it can only be installed by the administrator of the site.

The extension shows uploaded pdf files in a multipage preview layout. With
enabled WebStore the extension generates automatically Images from the
specified page.

%prep
%setup

%install
%mediawiki_ext_install 50 %ShortName
subst "4i\$wgFileExtensions[] = 'pdf';" %buildroot%_mediawiki_settings_dir/50-%ShortName.php

%files -f %ShortName.files

%changelog
* Sun Feb 22 2015 Vitaly Lipatov <lav@altlinux.ru> 1.23-alt1
- restore package (build from git)

* Thu Sep 15 2011 Vitaly Lipatov <lav@altlinux.ru> 1.16.r61594-alt1
- initial build for ALT Linux Sisyphus
