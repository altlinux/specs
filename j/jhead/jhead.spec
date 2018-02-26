Name: jhead
Version: 2.95
Release: alt1

Summary: Tool for handling EXIF data in JPEG image files
License: Public Domain
Group: Graphics

URL: http://www.sentex.net/~mwandel/jhead
Source: %url/jhead-%version.tar.gz

# Without jpegtran from libjpeg-utils rotation feature will not work.
# Exif thumbnail regeneration relies on 'mogrify' program from ImageMagick.
Requires: libjpeg-utils ImageMagick

%description
Jhead is a command line driven utility for extracting digital camera settings
from the Exif format files used by many digital cameras. It is also able to
reduce the size of digital camera JPEGs without loss of information, by
deleting integral thumbnails that digital cameras put into the Exif header.

%prep
%setup

%build
subst 's/-O./%optflags/' makefile
%make_build

%install
install -pD -m755 jhead %buildroot%_bindir/jhead
install -pD -m644 jhead.1 %buildroot%_man1dir/jhead.1

%files
%_bindir/*
%doc changes.txt readme.txt usage.html
%_man1dir/*

%changelog
* Sat Mar 17 2012 Victor Forsiuk <force@altlinux.org> 2.95-alt1
- 2.95

* Sat Dec 10 2011 Victor Forsiuk <force@altlinux.org> 2.93-alt1
- 2.93

* Mon Feb 08 2010 Victor Forsiuk <force@altlinux.org> 2.90-alt1
- 2.90

* Mon Dec 14 2009 Victor Forsyuk <force@altlinux.org> 2.8.8-alt1
- 2.88

* Wed Mar 11 2009 Victor Forsyuk <force@altlinux.org> 2.8.7-alt1
- 2.87

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 2.8.4-alt1
- 2.84

* Tue Jun 24 2008 Victor Forsyuk <force@altlinux.org> 2.8.2-alt1
- Version 2.82 (packaged as 2.8.2 to avoid adding epoch if 2.9 will be
  released by upstream).

* Thu Mar 13 2008 Victor Forsyuk <force@altlinux.org> 2.8-alt1
- 2.8

* Tue Feb 06 2007 Victor Forsyuk <force@altlinux.org> 2.7-alt1
- 2.7

* Mon May 15 2006 Victor Forsyuk <force@altlinux.ru> 2.6-alt1
- 2.6 (this version fixes FTBFS with gcc4).

* Tue Jan 17 2006 Victor Forsyuk <force@altlinux.ru> 2.5-alt1
- 2.5
- Added dependancy on ImageMagick.

* Mon Jun 06 2005 Victor Forsyuk <force@altlinux.ru> 2.4-alt1
- 2.4 (able to display GPS info if included in image!).

* Tue Mar 29 2005 Victor Forsyuk <force@altlinux.ru> 2.3-alt1
- Added dependancy on libjpeg-utils.
- Change rpm group to Graphics.
- Remove portugese tags.
- Build with our optflags.

* Tue Sep 30 2003 Michael Shigorin <mike@altlinux.ru> 2.0-alt1
- built for ALT Linux
  (based on 2.0-2 spec)

* Mon Apr 14 2003 Matthias Wandel
- First jhead 2.0 RPM built by me.
  Finally wrote a nice man page for jhead
  Using jhead 1.9 RPM from connectiva linux as starting point (left in the
  portugese tags)
