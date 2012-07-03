%define oname PdfHandler
%define major 1.16
%define revision r61594

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: PdfHandler extension shows uploaded pdf files in a multipage preview layout
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.3
Requires: mediawiki-common >= 1.16

# gs
Requires: ghostscript-classic
# pdfinfo
Requires:  poppler
# convert (FIXME: GraphicsMagick)
Requires: ImageMagick-tools

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://upload.wikimedia.org/ext-dist/%oname-MW%major-%revision.tar.gz
Source: %oname-%version.tar


%description
This is the README file for the PdfHandler extension for MediaWiki
software. The extension is only useful if you've got a MediaWiki
installation; it can only be installed by the administrator of the site.

The extension shows uploaded pdf files in a multipage preview layout. With
enabled WebStore the extension generates automatically Images from the
specified page.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
subst "4i\$wgFileExtensions[] = 'pdf';" %buildroot%_mediawiki_settings_dir/50-%oname.php

%files -f %oname.files

%changelog
* Thu Sep 15 2011 Vitaly Lipatov <lav@altlinux.ru> 1.16.r61594-alt1
- initial build for ALT Linux Sisyphus

