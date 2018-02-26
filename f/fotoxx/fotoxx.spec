Name: fotoxx
Version: 12.04
Release: alt1

Summary: Software for digital image editing, HDR composites, and panoramas
License: GPLv3+
Group: Graphics

Url: http://kornelix.squarespace.com/fotoxx
Source: http://kornelix.squarespace.com/storage/downloads/fotoxx-%version.tar.gz
Source1: fotoxx.desktop
Source2: fotoxx16.png
Source3: fotoxx32.png
Patch1: fotoxx-11.11.1-install.patch
Patch2: fotoxx-12.01-helpdir.patch

# Automatically added by buildreq on Sat Mar 17 2012
BuildRequires: gcc-c++ libgtk+3-devel libtiff-devel perl-Image-ExifTool ufraw xdg-utils

# fotoxx is able to use exiftool and ufraw to extend functionality
Requires: exiftool ufraw

# fotoxx uses exiv2 executable to read EXIF data:
Requires: exiv2
# fotoxx uses xdg-open executable to launch HTML docs viewer:
Requires: xdg-utils

Provides: fotox
Obsoletes: fotox

%description
Fotox is a program for improving digital photos. Navigate through large image
directories using a window of thumbnail images. Create HDR (high dynamic range)
images by combining bright and dark images to improve details visible in both
bright and dark areas. Create panorama (extra wide) images by joining overlapped
images. Adjust brightness and color intensity independently for different
underlying brightness levels. Reduce fog or haze by removing "whiteness" and
intensifying colors. Rotate an image (level a tilted image or turn 90 degrees).
Remove the red-eye effect from electronic flash photos. Resize or crop an image.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
# build with docs (in fact, gui help) in program data directory
subst 's|share/doc|share|' Makefile
# verbose and with our optimization
subst 's/@ g++/g++/g; s/-O. /%optflags /' Makefile

%make_build PREFIX=/usr

%install
install -d %buildroot%_man1dir
%make_install install DESTDIR=%buildroot PREFIX=/usr

install -pD -m644 %SOURCE1 %buildroot%_desktopdir/fotoxx.desktop
install -pD -m644 doc/fotoxx.man %buildroot%_man1dir/fotoxx.1
install -pD -m644 icons/fotoxx.png %buildroot%_liconsdir/fotoxx.png
install -pD %_sourcedir/fotoxx32.png %buildroot%_niconsdir/fotoxx.png
install -pD %_sourcedir/fotoxx16.png %buildroot%_miconsdir/fotoxx.png

%files
%_bindir/*
%_desktopdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_datadir/fotoxx
%_man1dir/*

%changelog
* Sun Apr 01 2012 Victor Forsiuk <force@altlinux.org> 12.04-alt1
- 12.04

* Sat Mar 17 2012 Victor Forsiuk <force@altlinux.org> 12.03.2-alt1
- 12.03.2

* Mon Jan 02 2012 Victor Forsiuk <force@altlinux.org> 12.01-alt1
- 12.01

* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 11.11.1-alt1
- 11.11.1

* Fri Sep 02 2011 Victor Forsiuk <force@altlinux.org> 11.09-alt1
- 11.09

* Sun Jul 31 2011 Victor Forsiuk <force@altlinux.org> 11.08-alt1
- 11.08

* Sun Jun 12 2011 Victor Forsiuk <force@altlinux.org> 11.06.1-alt1
- 11.06.1

* Thu May 05 2011 Victor Forsiuk <force@altlinux.org> 11.05.1-alt1
- 11.05.1

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 11.04-alt1
- 11.04

* Tue Mar 29 2011 Victor Forsiuk <force@altlinux.org> 11.03.1-alt1
- 11.03.1

* Fri Mar 04 2011 Victor Forsiuk <force@altlinux.org> 11.03-alt1
- 11.03

* Wed Feb 02 2011 Victor Forsiuk <force@altlinux.org> 11.02-alt1
- 11.02

* Thu Jan 13 2011 Victor Forsiuk <force@altlinux.org> 11.01.2-alt1
- 11.01.2

* Thu Nov 25 2010 Victor Forsiuk <force@altlinux.org> 10.11.2-alt1
- 10.11.2

* Mon Oct 18 2010 Victor Forsiuk <force@altlinux.org> 10.10.3-alt1
- 10.10.3

* Mon Sep 13 2010 Victor Forsiuk <force@altlinux.org> 10.9.1-alt1
- 10.9.1

* Wed Sep 08 2010 Victor Forsiuk <force@altlinux.org> 10.9-alt1
- 10.9

* Fri Aug 20 2010 Victor Forsiuk <force@altlinux.org> 10.8.4-alt1
- 10.8.4

* Fri Aug 13 2010 Victor Forsiuk <force@altlinux.org> 10.8.3-alt1
- 10.8.3

* Mon Jul 12 2010 Victor Forsiuk <force@altlinux.org> 10.7-alt1
- 10.7

* Fri Jun 18 2010 Victor Forsiuk <force@altlinux.org> 10.6.1-alt1
- 10.6.1

* Mon May 31 2010 Victor Forsiuk <force@altlinux.org> 10.4-alt1
- 10.4

* Tue Apr 06 2010 Victor Forsiuk <force@altlinux.org> 10.0-alt1
- 10.0

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 9.9-alt1
- 9.9

* Thu Mar 25 2010 Victor Forsiuk <force@altlinux.org> 9.8.1-alt1
- 9.8.1

* Mon Mar 22 2010 Victor Forsiuk <force@altlinux.org> 9.8-alt1
- 9.8

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 9.7-alt1
- 9.7

* Thu Feb 25 2010 Victor Forsiuk <force@altlinux.org> 9.6-alt1
- 9.6

* Wed Feb 03 2010 Victor Forsyuk <force@altlinux.org> 9.5-alt1
- 9.5

* Fri Jan 22 2010 Victor Forsyuk <force@altlinux.org> 9.4-alt1
- 9.4

* Thu Jan 14 2010 Victor Forsyuk <force@altlinux.org> 9.3-alt1
- 9.3

* Sat Dec 26 2009 Victor Forsyuk <force@altlinux.org> 9.1-alt1
- 9.1

* Mon Dec 14 2009 Victor Forsyuk <force@altlinux.org> 9.0-alt1
- 9.0

* Wed Oct 21 2009 Victor Forsyuk <force@altlinux.org> 8.6-alt1
- 8.6

* Sun Oct 11 2009 Victor Forsyuk <force@altlinux.org> 8.5.2-alt1
- 8.5.2

* Tue Sep 22 2009 Victor Forsyuk <force@altlinux.org> 8.4.3-alt1
- 8.4.3

* Thu Sep 03 2009 Victor Forsyuk <force@altlinux.org> 8.3-alt1
- 8.3
- Added %%f field code to .desktop's Exec key.

* Tue Aug 04 2009 Victor Forsyuk <force@altlinux.org> 8.0-alt1
- 8.0

* Thu Jul 23 2009 Victor Forsyuk <force@altlinux.org> 7.7-alt1
- 7.7

* Wed Jul 01 2009 Victor Forsyuk <force@altlinux.org> 7.4.1-alt1
- 7.4.1

* Wed Mar 11 2009 Victor Forsyuk <force@altlinux.org> 6.1.1-alt1
- 6.1.1

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 5.6.1-alt1
- 5.6.1

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 5.3.1-alt1
- 5.3.1

* Tue Sep 23 2008 Victor Forsyuk <force@altlinux.org> 5.3-alt1
- 5.3

* Mon Sep 15 2008 Victor Forsyuk <force@altlinux.org> 5.2.4-alt1
- 5.2.4

* Wed May 21 2008 Victor Forsyuk <force@altlinux.org> 42-alt1
- Version 42.

* Thu Mar 27 2008 Victor Forsyuk <force@altlinux.org> 37-alt1
- Version 37.

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 36-alt1
- Version 36.

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 33-alt1
- Initial build.
