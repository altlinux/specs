%define gimpver 2.0

Name: gimp-script-smartsharpening
Version: 1.00
Release: alt1

Summary: Gimp script for sharpening, which sharpens only the edges in the image
License: GPL
Group: Graphics

Url: http://www.trsqr.net/photokit/ss.html
Source: http://www.trsqr.net/photokit/smart-sharpening.scm

BuildArch: noarch
Requires: gimp >= 2.2

%description
Smart sharpening of image. This script finds the edges of images and only
sharpens those. You can find more about smart sharpening at
http://www.gimpguru.org/Tutorials/SmartSharpening/

%prep
%setup -c -T
cp -a %_sourcedir/smart-sharpening.scm .

%build

%install
install -d %buildroot%_datadir/gimp/%gimpver/scripts/
install -p -m644 smart-sharpening.scm %buildroot%_datadir/gimp/%gimpver/scripts/

%files
%_datadir/gimp/%gimpver/scripts/*

%changelog
* Thu Sep 13 2007 Victor Forsyuk <force@altlinux.org> 1.00-alt1
- Initial build.
