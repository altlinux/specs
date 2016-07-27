Name: crosti
Version: 1.13.2
Release: alt1

Summary: Tool to create cross stitch scheme from custom image
License: GPLv3+
Group: Graphics

Url: https://sites.google.com/site/crostiapp/
Source: http://garr.dl.sourceforge.net/project/crosti/crosti%%20%version/%name-%version-source.zip
Source1: crosti.xml
Source100: crosti.watch

BuildRequires: gcc-c++ qt4-devel unzip

%description
This tool allows you to make your own unique cross stitch scheme
from custom image. You can resize and rotate image, reduce the
number of colors, change image palette, make cross stitch scheme,
preview it, save and print. Cross stitch scheme edition
available: colors and icons changing, new color addition,
color fill, scheme pixel draw, lines and half-stitches.

Features

* Convert custom image to cross stitch scheme.
* Edit cross stitch scheme.
* Save and print the scheme that you created.
* Input images: BMP, GIF, ICO, JPEG, JPG, MNG, PBM, PGM, PNG,
  PPM, SVG, TIF, TIFF, XBM, XPM.
* Output cross stitch scheme: BMP, ICO, JPEG, JPG, PNG, PPM, TIF,
  TIFF, XBM, XPM, PDF, CST (crosti scheme text file).

%prep
%setup -c
sed -i 's/\r\n/\n/g' {readme,changelog}.txt

%build
qmake-qt4
%make

%install
%make_install install INSTALL_ROOT=%buildroot
install -pDm644 %SOURCE1 %buildroot%_datadir/mime/packages/%name.xml

%files
%doc readme.txt changelog.txt
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/*/apps/*
%_iconsdir/hicolor/*/mimetypes/*

%changelog
* Wed Jul 27 2016 Michael Shigorin <mike@altlinux.org> 1.13.2-alt1
- added watch file
- new version (watch file uupdate)

* Mon Nov 24 2014 Michael Shigorin <mike@altlinux.org> 1.13.0-alt1
- built for ALT Linux
- based on rosa contrib package for 1.10.1

* Sun Jan 26 2014 symbianflo <symbianflo@symbianflo> 1.10.1-1
+ Revision: d0d18d3
- Log. fix sources, permits and url

