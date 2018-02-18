Name: libpano13
Version: 2.9.19
Release: alt1.qa1

Group: System/Libraries
Summary: %name - library for panorama stitching programs. This is new generation and development version
License: GPL
Url: http://sourceforge.net/projects/panotools
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

Source0: %name-%{version}.tar.gz
Patch0: %name-configure.patch
Patch1: %name.patch

# Automatically added by buildreq on Mon Jan 15 2018
# optimized out: perl python-base zlib-devel
BuildRequires: libjpeg-devel libpng-devel libtiff-devel

%package devel
Group: System/Libraries
Summary: Devel package for %name
Requires: %name = %version
Provides: %name.so

%package programs
Group: Graphics
Summary: Programs built with %name
Requires: %name = %version
Obsoletes: libpano12-programs panotools

%description
This library is required for running any of the panorama stitching applications (hugin, PTStitcher, etc).

%description devel
This package contains files for development.

%description programs
This package contains programs from %name:
PTSticher   - Based on code found in Helmut Dersch's panorama-tools to
	      duplicate the functionality of original program
PTblender   - Implements the colour and brightness correction originally
	      found in PTStitcher.
PTcrop      - This program takes as input a TIFF (cropped or uncropped)
	      and generates an cropped TIFF according to the spec:
		* Specific boounding rectangle
		* Outer bounding rectangle
		* Inner inclusive rectangle
PTinfo      - Displays information about an image created with panotools
PTmasker    - Takes a set of tiffs and computes their stitching masks
PTmender    - This is a rewrite of PTStitcher. It has most of its functionality
	      (see below) and it should be (for most people) a drop in
	      replacement for PTstitcher.
PToptimizer - Clone of PTOptimizer of Helmut Dersch's panorama-tools
PTroller    - Flattens a set of TIFFs into one TIFF
PTtiff2psd  - Converts a set of TIFF files into a Photoshop PSD file
PTtiffdump  - This program compares the contents of 2 different tiff files.
	      If the byte is different it outputs it.
PTuncrop    - This program takes as input a cropped TIFF and generates an
	      uncropped TIFF
panoinfo    - Display info from pano12 dll/library

%prep
%setup -n %name-%version
%patch0 -p1
#Off because MAX_FISHEYE_FOV value is equal 720, not 160
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README README.linux AUTHORS NEWS
%_libdir/*.so.*

%files devel
%dir %_includedir/pano13
%_includedir/pano13/*
%_pkgconfigdir/libpano13.pc
%_libdir/*.so

%files programs
%doc doc/*.txt tools/README.PTmender
%_bindir/*
%_man1dir/*

%changelog
* Mon Jan 15 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.9.19-alt1.qa1
- Rebuilt without gcj.

* Mon Jul 13 2015 Yuri N. Sedunov <aris@altlinux.org> 2.9.19-alt1
- 2.9.19
- removed obsolete libpano13-2.9.18.patch

* Sat Sep 22 2012 Sergei Epiphanov <serpiph@altlinux.ru> 2.9.18-alt2
- Rebuild with new libpng and libtiff

* Thu Jul 21 2011 Sergei Epiphanov <serpiph@altlinux.ru> 2.9.18-alt1
- New version

* Mon Oct 18 2010 Sergei Epiphanov <serpiph@altlinux.ru> 2.9.17-alt1
- Release

* Mon Feb 08 2010 Sergei Epiphanov <serpiph@altlinux.ru> 2.9.17-alt0.beta1
- New version

* Sat Oct 31 2009 Sergei Epiphanov <serpiph@altlinux.ru> 2.9.15-alt0.beta3
- New version

* Sun Feb 08 2009 Sergei Epiphanov <serpiph@altlinux.ru> 2.9.14-alt0.beta1
- New version

* Thu Dec 18 2008 Sergei Epiphanov <serpiph@altlinux.ru> 2.9.12-alt4
- Remove ls.do update

* Sat Jun 23 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.9.12-alt3
- Some fixes in library from upstream

* Mon Feb 19 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.9.12-alt2
- Remove illegal require to libz.so.1
- Add description for set of programs

* Wed Feb 14 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.9.12-alt1
- initial build
