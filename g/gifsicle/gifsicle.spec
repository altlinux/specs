Name: gifsicle
Version: 1.67
Release: alt1
Summary: command-line program for manipulating GIF images
Group: Graphics
License: GPL
Url: http://www.lcdf.org/gifsicle

Source: %name-%version.tar.gz

# Automatically added by buildreq on Tue Mar 27 2007
BuildRequires: libSM-devel libX11-devel

%description
Gifsicle is a powerful command-line program for manipulating GIF image
files.  It has good support for transparency and colormap manipulation,
simple image transformations (cropping, flipping), and creating,
deconstructing, and editing GIF animations. It can also optimize GIF
animations for space. Also included is a GIF animation viewer and a
program that checks whether two GIFs look the same.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/gifdiff
%_man1dir/gifdiff.1.*
%_bindir/gifsicle
%_man1dir/gifsicle.1.*
%_bindir/gifview
%_man1dir/gifview.1.*
%doc README NEWS

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 1.67-alt1
- Autobuild version bump to 1.67

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1.66-alt1
- Autobuild version bump to 1.66

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 1.64-alt1
- Autobuild version bump to 1.64

* Sat Jul 23 2011 Fr. Br. George <george@altlinux.ru> 1.63-alt1
- Autobuild version bump to 1.63

* Tue Mar 27 2007 Alex V. Myltsev <avm@altlinux.ru> 1.48-alt1
- 1.48: bug fix for --crop-transparency.

* Sun Mar 04 2007 Alex V. Myltsev <avm@altlinux.ru> 1.46-alt1
- 1.46: minor scripting features.

* Sun Sep 18 2005 Alex V. Myltsev <avm@altlinux.ru> 1.43-alt1
- Version 1.43: minor bugfixes.

* Tue Jun 14 2005 Alex V. Myltsev <avm@altlinux.ru> 1.42-alt1
- Version 1.42.

* Fri Apr 08 2005 Alex V. Myltsev <avm@altlinux.ru> 1.37-alt1
- Initial build for ALT Linux.

